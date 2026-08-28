SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: int, interval: int) -> float:
    """Return the percentage of the service interval that has been used."""
    if interval <= 0:
        return 0.0
    return (km_since_service / interval) * 100


def needs_service(car: dict) -> bool:
    """Return True when a car has reached the service warning threshold."""
    odometer = car.get("odometer")
    last_service = car.get("last_service_km")

    if odometer is None or last_service is None:
        return False

    km_since_service = odometer - last_service
    pct = wear_percent(km_since_service, SERVICE_INTERVAL_KM)

    return pct >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list[dict]:
    """Return the cars that currently need service."""
    return [car for car in fleet if needs_service(car)]