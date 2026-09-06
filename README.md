Inputs:
One asset and one frozen daily-price dataset.

Strategy:
A moving average strategy.
Check 50 EMA and 14 EMA. When 14 is above 50, take long trades. When 14 crosses below the 50, make short trades. 
Assumes enough history exists.
Fractional shares allowed.

Timing:
Market orders excexuted at the next eligible opening price.

Portfolio:
Starting at $20000.00 with no fees.

Outputs:
A results chart including a trade log and complete history/tracking.
