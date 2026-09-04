# Equity Research Automation Tool

Automatisierte Rendite- und Risikoanalyse für frei wählbare börsennotierte Titel — von der Kursbeschaffung über SQL-Auswertung bis zum interaktiven Dashboard.

**Live-Demo:** https://equity-research-toolkit-4cms54huuby8ekvnlj4nyw.streamlit.app

## Funktionen

- Kursimport über yfinance, bereinigt um Splits und Dividenden
- Speicherung in einer lokalen SQLite-Datenbank
- Tagesrendite berechnet direkt in SQL (Window Function)
- Kennzahlen: Volatilität, Sharpe Ratio, Max Drawdown, Beta
- Interaktives Streamlit-Dashboard mit freier Ticker-Eingabe

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

## Lizenz

MIT

