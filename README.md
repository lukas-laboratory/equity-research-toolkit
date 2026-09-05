# Equity Research Automation Tool

Automated return and risk analysis for any publicly traded stock — from data ingestion through SQL analysis to an interactive dashboard.

**Live demo:** https://equity-research-toolkit-4cms54huuby8ekvnlj4nyw.streamlit.app

## Features

- Price data via yfinance, adjusted for splits and dividends
- Stored in a local SQLite database
- Daily returns calculated directly in SQL (window function)
- Metrics: volatility, Sharpe ratio, max drawdown, beta
- Interactive Streamlit dashboard with free ticker input

## Tech Stack

Python · pandas · numpy · SQLite · SQL · statsmodels · Plotly · Streamlit · Jupyter · Git

## Setup

```bash
git clone https://github.com/<username>/equity-research-toolkit.git
cd equity-research-toolkit

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## License

MIT
