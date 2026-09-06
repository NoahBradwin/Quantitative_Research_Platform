Inputs:
One asset and one frozen daily-price dataset.

Strategy:
A moving average strategy which altrenates between holding a position and cash.
Check 50 EMA and 14 EMA. When 14 is above 50, buy with 10% of portfolio per period. When 14 is below the 50, sell 10% of holdings per period. 
Assumes enough history exists.
Fractional shares allowed.

Timing:
Market orders excexuted at the next eligible opening price.

Portfolio:
Starting at $20000.00 with no fees.

Outputs:
A trade log which tracks the portfolio in holdings, in cash, and the total value.
