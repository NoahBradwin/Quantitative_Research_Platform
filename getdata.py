import yfinance as yf

prices = yf.download(
  "SPY",
  start="2020-01-01",
  end="2025-01-01",
  interval="1d",
  auto_adjust=True,
  multi_level_index=False,
)

prices.to_csv("SPY_daily.csv")