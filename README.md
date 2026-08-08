# Historical Market Data Analysis & Volatility Study

## Project Overview

This project demonstrates core quantitative finance principles by analyzing historical stock market data. It retrieves real-world financial data, performs time-series analysis, and calculates essential risk and performance metrics that are fundamental to quantitative finance and portfolio management.

The analysis applies Python-based data manipulation and statistical techniques to uncover market trends, measure volatility, and evaluate risk-adjusted performance—skills essential for roles in quantitative finance, trading technology, and financial data analysis.

---

## Features

- Download and process historical market data using real financial APIs
- Calculate daily returns and identify price trends using moving averages
- Measure rolling and annualized volatility to quantify market risk
- Compute maximum drawdown to assess downside risk
- Calculate Sharpe ratio for risk-adjusted performance evaluation
- Generate publication-quality visualizations of price action, returns, and volatility
- Export processed market data to CSV for further analysis

---

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and time-series analysis |
| **NumPy** | Numerical computations and statistical calculations |
| **Matplotlib** | Data visualization and charting |
| **yfinance** | Real-time and historical financial market data retrieval |

---

## Key Financial Concepts

### Daily Return
The percentage change in asset price from one trading day to the next. Used to measure short-term performance and analyze price momentum.

### Moving Average
A smoothing technique that calculates the average price over a fixed window (e.g., 20 or 50 days). Helps identify trends and support/resistance levels.

### Volatility (Annualized)
Measures the degree of price fluctuation over time, typically expressed as standard deviation. Higher volatility indicates greater risk. Annualized volatility scales rolling volatility to a yearly basis using ~252 trading days per year.

### Maximum Drawdown
The largest cumulative percentage decline from a historical peak to a subsequent trough. A key metric for understanding worst-case downside scenarios.

### Sharpe Ratio
A risk-adjusted performance metric calculated as (average return - risk-free rate) / volatility. Indicates how much return is earned per unit of risk taken. This project assumes a 0% risk-free rate for simplicity.

---

## Project Structure

```
historical-market-data-analysis/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── market_analysis.py           # Main analysis script
├── data/
│   └── processed_data.csv       # Output: processed market data
└── output/
    └── market_analysis_charts/  # Generated visualizations
        ├── price_chart.png
        ├── returns_chart.png
        ├── volatility_chart.png
        └── drawdown_chart.png
```

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Clone and Install

```bash
# Clone the repository
git clone https://github.com/ankitkharod438-cloud/historical-market-data-analysis.git
cd historical-market-data-analysis

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## How to Run

```bash
python market_analysis.py
```

The script will:
1. Download historical AAPL (Apple Inc.) price data
2. Calculate daily returns, moving averages, volatility, and maximum drawdown
3. Compute the Sharpe ratio for risk-adjusted performance assessment
4. Generate visualizations showing price trends, volatility, and drawdown analysis
5. Export processed market data to `data/processed_data.csv`
6. Save charts to `output/market_analysis_charts/`

---

## Results & Analysis

The project outputs the following key analyses:

**Price Analysis**
- Historical price trends with 20-day and 50-day moving averages
- Identification of support and resistance levels based on moving average crossovers

**Volatility Analysis**
- Rolling 20-day volatility with annualization (252 trading days/year)
- Volatility changes over time to identify periods of market calm and stress

**Drawdown Analysis**
- Cumulative maximum drawdown from historical peaks
- Visualization of underwater plots to assess recovery periods

**Risk-Adjusted Performance**
- Sharpe ratio calculation to evaluate returns relative to risk taken
- Basis for comparing the efficiency of returns across different time periods

All metrics are calculated using standard financial formulas and are suitable for educational purposes and portfolio risk assessment.

---

## Future Improvements

- Multi-asset comparison (compare volatility and returns across multiple stocks)
- Correlation analysis to study relationships between assets
- Index analysis (S&P 500, broader market indices)
- Rolling Sharpe ratio and sortino ratio calculations
- Distribution analysis of returns (skewness, kurtosis)
- Value-at-Risk (VaR) calculations for risk management
- Parameterized moving average windows for sensitivity analysis
- Interactive visualization using Plotly or Dash

---

## What I Learned

**Python & Data Science**
- Data manipulation, cleaning, and transformation using Pandas and NumPy
- Working with time-series data and applying rolling window calculations
- Creating professional visualizations with Matplotlib

**Financial Analysis**
- Understanding volatility as a measure of risk and market uncertainty
- Calculating and interpreting risk-adjusted performance metrics
- Analyzing price trends and identifying patterns in financial time-series data

**Quantitative Concepts**
- Moving averages and their applications in trend analysis
- Annualization of financial metrics for meaningful comparison
- The relationship between risk and return in portfolio management

---

## Getting Help

For questions or issues:
- Check the documentation in the code comments
- Review the financial concepts section above
- Refer to official documentation: [Pandas](https://pandas.pydata.org/), [yfinance](https://github.com/ranaroussi/yfinance)

---

---

**License**: MIT  
**Author**: [Ankit Kumar]  
**Last Updated**: 2026
