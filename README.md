Inputs:
One asset and one frozen daily-price dataset.

Strategy:
A moving average strategy which alternates between holding a long position and cash.
Check 50 EMA and 14 EMA. When 14 is above 50, increase exposure by 10% per period. When 14 is below the 50, decrease exposure by 10% per period. 
When EMA's are equal, do nothing.
Exposure will be calculated at open for this increase/decrease.
Assumes enough history exists.
Fractional shares allowed.

Timing:
Market orders executed at the next eligible opening price.

Portfolio:
Starting at $20000.00 with no fees.

Outputs:
A trade log which tracks the portfolio in holdings, in cash, and the total value.
