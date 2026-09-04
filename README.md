# Equity Research Automation Tool

Automatisierte Kennzahlenanalyse für börsennotierte Aktien:
yfinance → SQLite → SQL/pandas-Auswertung → Streamlit-Dashboard.

## Features
- [ ] Kursimport (yfinance)
- [ ] SQLite-Datenbank
- [ ] SQL-Abfragen inkl. Window Function (LAG)
- [ ] Kennzahlen: Return, Volatilität, Sharpe Ratio, Max Drawdown, Beta
- [ ] Train/Test-Split (In-/Out-of-Sample)
- [ ] Streamlit-Dashboard

## Setup
    git clone https://github.com/<username>/equity-research-toolkit.git
    cd equity-research-toolkit
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
