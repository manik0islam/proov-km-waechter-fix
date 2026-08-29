# What I checked, and what the agent got wrong

## What the agent got wrong

The miles conversion was backwards 100 km turned into 160 miles I noticed
immediately when verify.py failed. It also used wholenumber division for the average, so
59.67 became 59. That one passed verify only because the tolerance was too wide. Third
thing: if a car had no service history, the agent's code would either crash or wrongly flag
it. I caught that when I looked at the fleet_sample.json data.

## What I checked

Ran verify.py before and after every single change. Checked the miles conversion by hand
. Ran pytest to make sure all four tests pass, including the new
one. Made sure the 15000 and 80 constants didn't move.

## What the data said

I assumed old high-mileage cars would break down more. Odometer and age had basically
zero correlation. What actually matters is how far past service the car is and how hard it's
driven daily.