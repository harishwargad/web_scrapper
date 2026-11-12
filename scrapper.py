import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"

def scrape_countries(url: str) -> pd.DataFrame:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    rows = []
    for c in soup.select("div.country"):
        rows.append({
            "Country": c.select_one("h3.country-name").get_text(strip=True),
            "Capital": c.select_one(".country-capital").get_text(strip=True),
            "Population": int(c.select_one(".country-population").get_text(strip=True)),
            "Area": float(c.select_one(".country-area").get_text(strip=True)),
        })
    return pd.DataFrame(rows)

df = scrape_countries(URL)
df.to_csv("CountriesInfo.csv", index=False, encoding="utf-8")
print(len(df))  # expect 250