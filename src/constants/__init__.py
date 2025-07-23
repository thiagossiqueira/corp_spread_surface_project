from pathlib import Path

# ────────────────────────────────────────────────────────────────
# 2. Locate repo root & data files
# ────────────────────────────────────────────────────────────────
REPO_ROOT = Path.cwd()
while not (REPO_ROOT / ".git").exists() and REPO_ROOT != REPO_ROOT.parent:
    REPO_ROOT = REPO_ROOT.parent

CODE_PATH = REPO_ROOT / "datos_y_modelos"

DATABASE_PATH = CODE_PATH / "db"
DI_PATH = DATABASE_PATH /  "one-day_interbank_deposit_futures_contract_di" / "bsrch.xlsx"
YIELD_PATH = DATABASE_PATH / "one-day_interbank_deposit_futures_contract_di" / "ODA_Comdty.xlsx"


GRAPHS_PATH = CODE_PATH / "graphs"
ODA_COMDTY_GRAPHS_PATH = GRAPHS_PATH / "oda_comdty"

CORP_PATH = CODE_PATH / "Domestic"

AUTHOR_CALCULATION_SOURCE = ("Source:DI B3 "
            "- author calculations")

# NOTE(hspadim): Check if folder exists or not
if not DATABASE_PATH.exists():
    DATABASE_PATH.mkdir(parents=True, exist_ok=True)

# NOTE(hspadim): Check if folder exists or not
if not ODA_COMDTY_GRAPHS_PATH.exists():
    ODA_COMDTY_GRAPHS_PATH.mkdir(parents=True, exist_ok=True)

# NOTE(hspadim): Check if folder exists or not
if not CORP_PATH.exists():
    CORP_PATH.mkdir(parents=True, exist_ok=True)

__all__ = [
    "REPO_ROOT",
    "DI_PATH",
    "YIELD_PATH",
    "ODA_COMDTY_GRAPHS_PATH",
    "AUTHOR_CALCULATION_SOURCE",
    "CORP_PATH",
]
