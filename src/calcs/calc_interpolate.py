from pandas import DataFrame
from scipy.interpolate import interp1d
import pandas as pd


TENORS = {
    "30-year": 30.0, "10-year": 10.0, "5-year": 5.0, "3-year": 3.0,
    "2-year":  2.0,  "1-year":  1.0, "6-month": 0.5,
    "3-month": 0.25, "1-month": 1/12,
}


# ────────────────────────────────────────────────────────────────
# 4. Interpolate to Fed-style tenors
# ────────────────────────────────────────────────────────────────
def calc_interpolate(surface: DataFrame, /) -> DataFrame:
    rows: list[dict] = []
    for obs_date, grp in surface.groupby("obs_date"):
        grp = grp.drop_duplicates(subset="tenor").sort_values("tenor")
        if grp["tenor"].nunique() < 2:
            continue                                         # need ≥2 pts for interp

        x = grp["tenor"].to_numpy()
        y = grp["yield"].to_numpy()

        if len(x) > 1:
            f = interp1d(x, y, kind="linear",
                        bounds_error=False, fill_value="extrapolate",
                        assume_sorted=True)
            interp = lambda t: float(f(t))
        else:                                               # single-point fallback
            interp = lambda t: float(y[0])

        rows.append({"DATE": obs_date.date(),
                    **{k: interp(t) for k, t in TENORS.items()}})

    yc_table = (
        pd.DataFrame(rows)
        .set_index("DATE")
        .sort_index()
        .dropna(how="any")       # guarantees clean for plotting
    )
    rows.clear()
    del rows

    return yc_table


__all__ = [
    # Functions
    "calc_interpolate",
    # Constants
    "TENORS",
]
