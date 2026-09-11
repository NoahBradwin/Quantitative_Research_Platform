import pandas as pd
prices = pd.read_csv("SPY_daily.csv")

open_prices = prices["Open"].tolist()
close_prices = prices["Close"].tolist()
dates = prices["Date"].tolist()

cash = 20000
target_exposure = 0
shares = []
portfolio = []
relationship = None

no_strat_cash = 20000
no_strat_shares = no_strat_cash / open_prices[0]

change_log = [[],[],[],[],[],[],[],[],[]]

def EMA(close_prices, num):
    EMA = []
    SMA = 0
    for i in range(num):
        SMA += close_prices[i]
    SMA = SMA / num
    for i in range(len(close_prices)):
        if i < num - 1:
            EMA.append(None)
        elif i == num - 1:
            EMA.append(SMA)
        else:
            EMA.append(close_prices[i]*(2/(1+num)) + EMA[i-1]*(1-2/(1+num)))
    return EMA

EMA_14 = EMA(close_prices, 14)
EMA_50 = EMA(close_prices, 50)
exposure = 0

for i in range(len(open_prices)):
    if relationship == 1 and exposure <= 0.9:
        exposure += 0.1
    elif relationship == 0 and exposure >= 0.1:
        exposure -= 0.1

    if EMA_14[i] == None or EMA_50[i] == None:
        relationship = None
    elif EMA_14[i] > EMA_50[i]:
        relationship = 1
    elif EMA_14[i] == EMA_50[i]:
        relationship = -1
    else:
        relationship = 0
    if shares:
        shares.append(exposure * (cash + shares[i-1]*open_prices[i]) / open_prices[i])
    else:
        shares.append(exposure * cash / open_prices[i])
    cash = cash - (shares[i]-shares[i-1]) * open_prices[i]
    portfolio.append(shares[i]*close_prices[i] + cash)


    change_log[0].append(dates[i])
    if i > 0:
        change_log[1].append(EMA_14[i-1])
        change_log[2].append(EMA_50[i-1])
    else:
        change_log[1].append(None)
        change_log[2].append(None)
    change_log[3].append(exposure)
    change_log[4].append(shares[i]-shares[i-1])
    change_log[5].append(shares[i])
    change_log[6].append(cash)
    change_log[7].append(portfolio[i])
    change_log[8].append(no_strat_shares*close_prices[i])

log = pd.DataFrame(change_log).T
log.columns = [
    "Date",
    "Previous 14 EMA",
    "Previous 50 EMA",
    "Target Exposure",
    "Shares Traded",
    "Shares Held",
    "Cash",
    "Portfolio Value",
    "Portfolio Value No Strategy"
]
log.to_csv("trade_log.csv", index=False)

print(f"Portfolio: {portfolio[-1]}")
print(f"Cash: {cash}")
print(f"Shares: {shares[-1]}")
print(f"Return: {(portfolio[-1]-portfolio[0])/(portfolio[0])*100}%")
print(f"Portfolio No Strategy: {no_strat_shares * close_prices[-1]}")