# fleet_utils.py
# Sammelbecken fuer Helfer seit 2013. Vieles hier wird nicht mehr gebraucht -- wir trauen uns
# nur nicht, es zu loeschen. (Catch-all helpers since 2013. Much of this is unused -- we just
# never dared to delete anything.)

KM_PER_MILE = 1.60934


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles (1 mile = 1.60934 km)."""
    return km / KM_PER_MILE


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a number as a percentage string."""
    return f"{value:.0f}%"


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list of values."""
    if not values:
        return 0
    return sum(values) / len(values)
