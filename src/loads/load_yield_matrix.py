from pandas import DataFrame
from pathlib import Path
import pandas as pd



# ────────────────────────────────────────────────────────────────
# 4. Historical YAS yield matrix
# ────────────────────────────────────────────────────────────────
def load_yield_matrix(filepath: Path, /) -> DataFrame:
    ylds = pd.read_excel(filepath, sheet_name="ya_values_only")
    ylds.rename(columns={ylds.columns[0]: "OBS_DATE"}, inplace=True)
    ylds["OBS_DATE"] = pd.to_datetime(ylds["OBS_DATE"])
    ylds = ylds.set_index("OBS_DATE").sort_index()

    return ylds

__all__ = [
    "load_yield_matrix",
]
