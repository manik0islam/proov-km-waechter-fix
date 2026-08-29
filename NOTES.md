# What I checked, and what the agent got wrong

## What the agent got wrong

The km-to-miles conversion was backwards. The constant was named MILES_PER_KM and held the
value 1.609, but it was used to multiply instead of dividing. This made 100 km report as 160.9
miles instead of the correct 62.1. I noticed it when verify.py flagged the mileage conversion
check as FAIL. The agent also used floor division (//) in fleet_summary for the average wear,
which silently truncated 59.67 to 59.0. The verify check happened to pass because its tolerance
was 1.5, but the result was still wrong. A third issue was that needs_service silently treated a
missing last_service_km as 0 and then falsely flagged the car, while car_wear in fleet_report
used direct dict access and crashed with a KeyError. The agent fixed both in one pass.

## What I checked before I accepted its work

I ran python verify.py before and after every change. I confirmed that 100 km converts to
approximately 62.1 miles, that a car with no last_service_km entry does not crash the report,
that the average wear for a two-car fleet comes out to about 59.67 and not 59.0, and that the
15000 km and 80 percent constants are untouched in both km_wachter.py and settings.cfg. I also
ran pytest to make sure the four tests all pass, including the new one for missing readings.

## What the data actually said

The obvious guess that high total mileage or old age predict breakdowns turned out to be
completely wrong. Odometer and age_years both had correlations near zero with the broke_down
column. What actually predicts breakdowns is km_since_service with a correlation of 0.40,
followed by avg_daily_km at 0.25 and load_factor at 0.22. The riskiest cars are not the
oldest or highest-mileage ones. They are the ones that have been driven hard daily and are
long overdue for service.
