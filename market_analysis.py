"""
Historical Market Data Analysis & Volatility Study
--------------------------------------------------
Beginner-friendly quantitative finance project.

The project:
1. Downloads historical market data
2. Cleans and inspects the dataset
3. Calculates daily returns
4. Calculates rolling and annualized volatility
5. Calculates moving averages
6. Calculates basic risk/performance statistics
7. Visualizes price, returns, volatility, and moving averages
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# -----------------------------
# 1. Download historical data
# -----------------------------
TICKER = "AAPL"
START_DATE = "2023-01-01"
END_DATE = "2025-01-01"

data = yf.download(
    TICKER,
    start=START_DATE,
    end=END_DATE,
    auto_adjust=True
)

# Handle possible MultiIndex columns returned by yfinance
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

data = data.dropna()

print("First five rows:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())


# -----------------------------
# 2. Basic descriptive statistics
# -----------------------------
print("\nDescriptive statistics:")
print(data.describe())


# -----------------------------
# 3. Daily returns
# -----------------------------
data["Daily_Return"] = data["Close"].pct_change()

# Percentage return
data["Daily_Return_Pct"] = data["Daily_Return"] * 100

print("\nDaily returns:")
print(data[["Close", "Daily_Return_Pct"]].head(10))


# -----------------------------
# 4. Moving averages
# -----------------------------
data["MA_20"] = data["Close"].rolling(window=20).mean()
data["MA_50"] = data["Close"].rolling(window=50).mean()


# -----------------------------
# 5. Volatility
# -----------------------------
# 20-day rolling volatility
data["Rolling_Volatility_20D"] = (
    data["Daily_Return"].rolling(window=20).std()
)

# Annualized volatility: daily volatility * sqrt(252)
data["Annualized_Volatility"] = (
    data["Rolling_Volatility_20D"] * np.sqrt(252)
)

print("\nLatest annualized volatility:")
print(data["Annualized_Volatility"].dropna().tail())


# -----------------------------
# 6. Basic performance statistics
# -----------------------------
clean_returns = data["Daily_Return"].dropna()

total_return = (data["Close"].iloc[-1] / data["Close"].iloc[0] - 1) * 100
annualized_return = (
    (data["Close"].iloc[-1] / data["Close"].iloc[0])
    ** (252 / len(data))
    - 1
) * 100

annualized_volatility = clean_returns.std() * np.sqrt(252) * 100

sharpe_ratio = (
    clean_returns.mean() / clean_returns.std()
) * np.sqrt(252)

# Maximum drawdown
cumulative_max = data["Close"].cummax()
drawdown = data["Close"] / cumulative_max - 1
max_drawdown = drawdown.min() * 100

print("\n========== SUMMARY ==========")
print(f"Ticker: {TICKER}")
print(f"Period: {START_DATE} to {END_DATE}")
print(f"Total Return: {total_return:.2f}%")
print(f"Annualized Return: {annualized_return:.2f}%")
print(f"Annualized Volatility: {annualized_volatility:.2f}%")
print(f"Sharpe Ratio (risk-free rate assumed 0%): {sharpe_ratio:.2f}")
print(f"Maximum Drawdown: {max_drawdown:.2f}%")
print("=============================")


# -----------------------------
# 7. Price + moving averages
# -----------------------------
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Close"], label="Close Price")
plt.plot(data.index, data["MA_20"], label="20-Day Moving Average")
plt.plot(data.index, data["MA_50"], label="50-Day Moving Average")

plt.title(f"{TICKER} Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# -----------------------------
# 8. Daily returns
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(data.index, data["Daily_Return_Pct"])
plt.axhline(0, linewidth=1)

plt.title(f"{TICKER} Daily Returns")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# -----------------------------
# 9. Rolling volatility
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(
    data.index,
    data["Annualized_Volatility"] * 100
)

plt.title(f"{TICKER} 20-Day Rolling Annualized Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility (%)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# -----------------------------
# 10. Drawdown
# -----------------------------
plt.figure(figsize=(12, 5))
plt.plot(data.index, drawdown * 100)
plt.axhline(0, linewidth=1)

plt.title(f"{TICKER} Drawdown")
plt.xlabel("Date")
plt.ylabel("Drawdown (%)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# -----------------------------
# 11. Save processed data
# -----------------------------
output_file = "processed_market_data.csv"
data.to_csv(output_file)

print(f"\nProcessed data saved to: {output_file}")
