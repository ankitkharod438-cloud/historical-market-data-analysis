# Historical Market Data Analysis & Volatility Study

## Project Overview

This project analyzes historical financial market data using Python. It focuses on basic quantitative analysis concepts such as returns, moving averages, volatility, drawdown, and risk-adjusted performance.

The project is designed as a beginner-friendly introduction to quantitative finance and financial market data analysis.

## Objectives

- Obtain historical market data
- Inspect and clean financial time-series data
- Calculate daily returns
- Calculate moving averages
- Measure rolling and annualized volatility
- Calculate maximum drawdown
- Calculate a basic Sharpe ratio
- Visualize market behavior

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance

## Key Concepts

### Daily Return
Measures the percentage change in price from one trading day to the next.

### Moving Average
A moving average smooths price data and helps identify trends.

### Volatility
Measures how much returns fluctuate over time. The project uses rolling standard deviation and annualizes it using approximately 252 trading days per year.

### Maximum Drawdown
Measures the largest decline from a previous peak.

### Sharpe Ratio
A simple risk-adjusted performance measure. This project assumes a 0% risk-free rate for simplicity.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python market_analysis.py
```

The script downloads AAPL data for the selected period and creates several charts.

## Possible Extensions

- Compare multiple stocks
- Add correlation analysis
- Analyze S&P 500 or other indices
- Test a moving-average trading strategy
- Add transaction costs
- Compare different volatility windows
- Perform out-of-sample backtesting

## Resume Description

**Historical Market Data Analysis & Volatility Study**
- Analyzed historical market data using Python, Pandas, and NumPy to calculate daily returns, moving averages, volatility, and drawdowns.
- Visualized price trends and rolling annualized volatility using Matplotlib and evaluated basic risk-adjusted performance using the Sharpe ratio.
