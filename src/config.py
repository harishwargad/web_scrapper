from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
COUNTRIES_CSV = DATA_DIR / "Scraped_countriesInfo.csv"