# Flipkart TV Price Scraper

A beginner-built Python project for scraping product names and listed prices from Flipkart search results. It also includes a practice scraper for country data from [scrapethissite.com](https://www.scrapethissite.com/pages/simple/).

## What it does

- Prompts for a Flipkart search URL, then prints product names and prices found on the page.
- Optionally reads HTTP and HTTPS proxy settings from a `.env` file.
- Includes a separate practice script that collects country names, capitals, populations, and areas, then writes them to a CSV.

## Project structure

```text
web_scrapper/
├── data/
│   └── Scraped_countriesInfo.csv       # Existing country data
├── notebooks/
│   ├── flipkartScrapper_test.ipynb
│   └── simple_scraper.ipynb
├── src/
│   ├── main.py                         # Currently empty
│   ├── models/
│   │   └── product.py                  # Currently empty
│   ├── scrapers/
│   │   ├── flipkart.py                 # Currently empty
│   │   └── scrapeThisSite.py           # Country-data practice scraper
│   └── services/
│       └── price_tracker.py            # Interactive Flipkart scraper
├── tests/                              # Currently empty
├── .env.example
└── requirements.txt
```

## Setup

Requires Python 3.10 or later.

```bash
git clone https://github.com/harishwargad/web_scrapper.git
cd web_scrapper
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt pandas python-dotenv
```

`pandas` and `python-dotenv` are currently used by the source but are not listed in `requirements.txt`, so they are included explicitly in the install command.

## Run

Run the Flipkart scraper:

```bash
python src/services/price_tracker.py
```

Paste a Flipkart search URL when prompted.

Run the country-data practice scraper:

```bash
python src/scrapers/scrapeThisSite.py
```

It writes `Scrapped_countriesInfo.csv` to the current working directory.

## Optional proxy

To use a proxy, copy `.env.example` to `.env` and add your proxy values:

```bash
cp .env.example .env
```

Then set the values in `.env`:

```env
http_proxy=
https_proxy=
```

`.env` is gitignored. Keep credentials out of source control. Leave the values empty to run without a proxy.

## Limitations

- Flipkart can change its page structure at any time, which may break extraction.
- Search results can vary by location and personalization; only the page returned for the submitted URL is handled.
- The Flipkart scraper prints results and does not yet save price history or send alerts.
- This is a personal educational project, not intended for bulk or commercial scraping. Respect each website's terms of service and `robots.txt`.
