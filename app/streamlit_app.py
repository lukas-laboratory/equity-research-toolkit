import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_white"

st.set_page_config(page_title="Equity Research Dashboard", layout="wide")
st.title("Equity Research Dashboard")

TRADING_DAYS = 252
RISK_FREE_ANNUAL = 0.04

col1, col2 = st.columns(2)
ticker = col1.text_input("Ticker", value="AAPL")
benchmark = col2.text_input("Benchmark", value="^GSPC")
start = st.date_input("Start", value=pd.to_datetime("2015-01-01"))

if st.button("Analyse starten"):
    with st.spinner("Lade Daten..."):
        raw = yf.download([ticker, benchmark], start=start, auto_adjust=True, progress=False)
        close = raw["Close"].dropna()

    if close.empty or ticker not in close.columns:
        st.error("Keine Daten gefunden. Ticker prüfen.")
        st.stop()

    returns = close.pct_change().dropna()

    daily_rf = RISK_FREE_ANNUAL / TRADING_DAYS
    excess = returns[ticker] - daily_rf
    sharpe = (excess.mean() / excess.std()) * np.sqrt(TRADING_DAYS)

    cumulative = (1 + returns[ticker]).cumprod()
    max_dd = (cumulative / cumulative.cummax() - 1).min()

    X = sm.add_constant(returns[benchmark])
    beta = sm.OLS(returns[ticker], X).fit().params[benchmark]

    # Benchmark-Kennzahlen für den Vergleich
    daily_rf = RISK_FREE_ANNUAL / TRADING_DAYS
    excess_bench = returns[benchmark] - daily_rf
    sharpe_bench = (excess_bench.mean() / excess_bench.std()) * np.sqrt(TRADING_DAYS)

    cum_bench_tmp = (1 + returns[benchmark]).cumprod()
    max_dd_bench = (cum_bench_tmp / cum_bench_tmp.cummax() - 1).min()

    total_return = (1 + returns[ticker]).prod() - 1
    total_bench = (1 + returns[benchmark]).prod() - 1

    st.subheader("Kennzahlen")
    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Gesamtrendite", f"{total_return:.1%}",
              delta=f"{total_return - total_bench:+.1%} vs. Index")

    m2.metric("Sharpe Ratio", f"{sharpe:.2f}",
              delta=f"{sharpe - sharpe_bench:+.2f} vs. Index")

    m3.metric("Max Drawdown", f"{max_dd:.1%}",
              delta=f"{max_dd - max_dd_bench:+.1%} vs. Index",
              delta_color="inverse")

    m4.metric("Beta", f"{beta:.2f}",
              delta="schwankungsfreudiger" if beta > 1 else "defensiver",
              delta_color="off")

    cum_bench = (1 + returns[benchmark]).cumprod()
    combined = pd.DataFrame({ticker: cumulative, benchmark: cum_bench})

    fig = px.line(combined, title="Kumulierte Rendite",
                  color_discrete_sequence=["#1f6f6b", "#8a93a0"])
    fig.update_layout(
        yaxis_title="Wachstum eines investierten Euro",
        xaxis_title=None,
        legend_title=None,
        hovermode="x unified",
        height=430,
        margin=dict(t=50, r=10, b=10, l=10),
    )
    st.plotly_chart(fig, use_container_width=True)

    dd = cumulative / cumulative.cummax() - 1
    fig2 = px.area(dd, title="Drawdown", color_discrete_sequence=["#b3402f"])
    fig2.update_traces(opacity=0.55)
    fig2.update_layout(
        yaxis_tickformat=".0%",
        yaxis_title="Abstand zum bisherigen Höchststand",
        xaxis_title=None,
        showlegend=False,
        height=430,
        margin=dict(t=50, r=10, b=10, l=10),
    )
    st.plotly_chart(fig2, use_container_width=True)

