Inputs:
One asset and one frozen daily-price dataset.

Strategy:
A moving-average strategy which adjusts exposure between a long position and cash.
Check 50 EMA and 14 EMA. When 14 is above 50, increase portfolio allocation by 10% per period. When 14 is below the 50, decrease portfolio allocation by 10% per period. 
When EMAs are equal, do nothing.
Portfolio allocation will be calculated at open for this increase/decrease. EMA comparison uses closign data from completed day t. The resulting order executes at the opening price on dat t + 1.
Assumes enough history exists.
Fractional shares allowed.

Timing:
Market orders executed at the next eligible opening price.

Portfolio:
Starting at $20000.00 with no fees.

Outputs:
A trade log which tracks the portfolio in holdings, in cash, and the total value.
