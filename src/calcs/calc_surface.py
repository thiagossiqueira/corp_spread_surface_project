from pandas import DataFrame

# ────────────────────────────────────────────────────────────────
# 3. Build surface: obs_date, tenor (yrs), yield (%)
# ────────────────────────────────────────────────────────────────
def calc_surface(ylds: DataFrame, bonds_static: DataFrame) -> DataFrame:
    long = (
        ylds.reset_index()
            .melt(id_vars="OBS_DATE",
                var_name="Generic ticker",
                value_name="yield")
            .dropna(subset=["yield"])
            .loc[lambda df: df["yield"] > 0]        # keep positives without .query
    )

    # merge with calendar and compute tenor – same as before
    calendar_cols = ["Generic ticker", "Curve date", "End of Month days"]
    bonds_key = bonds_static[calendar_cols].rename(columns={"Curve date": "OBS_DATE"})

    merged = (long.merge(bonds_key, on=["Generic ticker", "OBS_DATE"], how="left").dropna(subset=["End of Month days"]))

    surface = merged.rename(columns={"OBS_DATE": "obs_date", "Generic ticker": "id", "End of Month days": "tenor" })[["obs_date", "id", "yield", "tenor"]].reset_index(drop=True)

    return surface

__all__ = [
    "calc_surface",
]
