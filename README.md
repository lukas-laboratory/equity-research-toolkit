# Equity Research Automation Tool

Automatisierte Kennzahlenanalyse für börsennotierte Aktien:
yfinance → SQLite → SQL/pandas-Auswertung → Streamlit-Dashboard.

## Live-Demo
https://equity-research-toolkit-4cms54huuby8ekvnlj4nyw.streamlit.app

## Features
- [x] Kursimport (yfinance)
- [x] SQLite-Datenbank
- [x] SQL-Abfragen inkl. Window Function (LAG)
- [x] Kennzahlen: Return, Volatilität, Sharpe Ratio, Max Drawdown, Beta
- [ ] Train/Test-Split (In-/Out-of-Sample) — geplant für v0.2
- [x] Streamlit-Dashboard


## Setup
    git clone https://github.com/<username>/equity-research-toolkit.git
    cd equity-research-toolkit
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

## Methodik
Returns via SQL Window Function (LAG) berechnet. Kennzahlen annualisiert
über 252 Handelstage. Beta via OLS-Regression gegen den Referenzindex.

