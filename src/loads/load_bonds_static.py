from pandas import DataFrame
from pathlib import Path
import pandas as pd


# ────────────────────────────────────────────────────────────────
# 3. Static bond characteristics
# ────────────────────────────────────────────────────────────────
def load_bonds_static(filepath: Path, /) -> DataFrame:
    bonds_static = pd.read_excel(filepath, sheet_name="periods_values_only")
    bonds_static["End of Month date"] = pd.to_datetime(bonds_static["End of Month date"])
    bonds_static["Settlement date"] = pd.to_datetime(bonds_static["Settlement date"])

    return bonds_static

__all__ = [
    "load_bonds_static",
]
