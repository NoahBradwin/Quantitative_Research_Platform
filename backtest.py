open = [100.5, 101.25, 102.5, 102.75, 101.5, 99.5, 98.75, 100, 101.5, 102.5, 101, 99.5]
close = [100, 101, 102, 103, 102, 100, 98, 99, 101, 103, 102, 100]
cash = 20000
target_exposure = 0
shares = []
portfolio = []
relationship = None

def EMA(close, num):
    EMA = []
    SMA = 0
    for i in range(num):
        SMA += close[i]
    SMA = SMA / num
    for i in range(len(close)):
        if i < num - 1:
            EMA.append(None)
        elif i == num - 1:
            EMA.append(SMA)
        else:
            EMA.append(close[i]*(2/(1+num)) + EMA[i-1]*(1-2/(1+num)))
    return EMA

EMA_3 = EMA(close, 3)
EMA_5 = EMA(close, 5)
exposure = 0

for i in range(len(open)):
    if relationship == 1 and exposure <= 0.9:
        exposure += 0.1
    elif relationship == 0 and exposure >= 0.1:
        exposure -= 0.1

    if EMA_3[i] == None or EMA_5[i] == None:
        relationship = None
    elif EMA_3[i] > EMA_5[i]:
        relationship = 1
    elif EMA_3[i] == EMA_5[i]:
        relationship = -1
    else:
        relationship = 0
    if shares:
        shares.append(exposure * (cash + shares[i-1]*open[i]) / open[i])
    else:
        shares.append(exposure * cash / open[i])
    cash = cash - (shares[i]-shares[i-1]) * open[i]
    portfolio.append(shares[i]*close[i] + cash)
    print(portfolio[i])


