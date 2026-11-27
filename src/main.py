from config import COUNTRIES_CSV
from scrapers.scrapeThisSite import scrape_countries


def main():
    
    countries_df = scrape_countries()
    COUNTRIES_CSV.parent.mkdir(parents=True, exist_ok=True)
    countries_df.to_csv(COUNTRIES_CSV, index=False, encoding="utf-8")
    print(f"CSV Created at {COUNTRIES_CSV}!")
    

if __name__ == "__main__":
    main()