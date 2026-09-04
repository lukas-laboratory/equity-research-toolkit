import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import statsmodels.api as sm
import plotly.express as px

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

    st.subheader("Kennzahlen")
    st.table(pd.DataFrame({
        "Wert": [f"{sharpe:.2f}", f"{max_dd:.2%}", f"{beta:.2f}"]
    }, index=["Sharpe Ratio", "Max Drawdown", "Beta"]))

    cum_bench = (1 + returns[benchmark]).cumprod()
    combined = pd.DataFrame({ticker: cumulative, benchmark: cum_bench})

    fig = px.line(combined, title="Kumulierte Rendite")
    fig.update_layout(yaxis_title="Wachstum (Start = 1.0)")
    st.plotly_chart(fig, use_container_width=True)

    dd = cumulative / cumulative.cummax() - 1
    fig2 = px.area(dd, title="Drawdown")
    fig2.update_layout(yaxis_tickformat=".0%", showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

