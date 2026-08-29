# Key factors: km_since_service (r=0.40) is the strongest breakdown predictor -- overdue cars
# break down. avg_daily_km (r=0.25) and load_factor (r=0.22) matter too. Odometer and age are
# near zero (r~0.00) -- total mileage and car age do NOT predict breakdowns in this fleet.
#
# Build a 0-100 risk score from the three real predictors, rank cars, fix the riskiest first.

import pandas as pd


def normalize(series: pd.Series) -> pd.Series:
    """Scale a series to 0-1 range using min-max normalization."""
    mn, mx = series.min(), series.max()
    if mx == mn:
        return pd.Series(0.5, index=series.index)
    return (series - mn) / (mx - mn)


def build_risk_scores(df: pd.DataFrame) -> pd.Series:
    """Return a 0-100 risk score for each car, built from the three real predictors."""
    w_service = 0.50
    w_daily = 0.30
    w_load = 0.20
    score = (
        w_service * normalize(df["km_since_service"])
        + w_daily * normalize(df["avg_daily_km"])
        + w_load * normalize(df["load_factor"])
    )
    return (score * 100).clip(0, 100)


def main() -> None:
    df = pd.read_csv("fleet_history.csv")

    cols = ["odometer_km", "km_since_service", "avg_daily_km", "load_factor", "age_years"]

    # --- Step 1: compare the two groups ---
    print("=== Mean values by group (0 = safe, 1 = broke down) ===")
    means = df.groupby("broke_down")[cols].mean()
    print(means.to_string())
    print()

    # --- Step 2: correlation with breakdown ---
    print("=== Correlation with broke_down ===")
    for c in cols:
        r = df[c].corr(df["broke_down"])
        print(f"  {c:20s}  r = {r:+.3f}")
    print()

    # --- Step 3: risk scores ---
    df["risk_score"] = build_risk_scores(df)

    # --- Step 4: ranked output ---
    ranked = df.sort_values("risk_score", ascending=False)
    print("=== All cars ranked by risk (highest first) ===")
    print(
        ranked[["car_id", "km_since_service", "avg_daily_km", "load_factor", "broke_down", "risk_score"]]
        .to_string(index=False)
    )
    print()

    # --- Step 5: top 10 summary ---
    top10 = ranked.head(10)
    flagged = top10["broke_down"].sum()
    print(f"Top 10 riskiest: {flagged} of 10 actually broke down.")
    print(f"Bottom 10 safest: {ranked.tail(10)['broke_down'].sum()} of 10 actually broke down.")


if __name__ == "__main__":
    main()
