# Flipkart TV Price Scraper

A beginner-built web scraper in Python that pulls TV names and prices from Flipkart search results. Built from scratch using the docs, Google and trial and error.

> **Status:** v1 works. It scrapes and prints. Price history, alerts and automation are planned for v2.

## Why I built this

My family needed a new TV, and finding the right one became my job. So I built something around it.

I started with [scrapethissite.com](https://www.scrapethissite.com), a site made for scraping practice, to learn `requests` and Beautiful Soup. Then I moved to Flipkart.

## What it does (v1)

- Takes a Flipkart search URL as input
- Fetches the page with `requests` (custom headers, optional proxy)
- Finds each product card by its `data-id` attribute
- Extracts the product name and the listed price
- Prints `name --> price` for every TV on the page

## Project structure

```
web_scrapper/
├── price_tracker.py                 # Flipkart scraper (main script)
├── scrapper_for_ScrapeThisSite.py   # Practice scraper (scrapethissite.com)
├── Scraped_countriesInfo.csv        # Output of the practice scraper
├── simple_scraper.ipynb             # Notebook: practice scraper experiments
├── flipkartScrapper_test.ipynb      # Notebook: Flipkart experiments
├── requirements.txt
└── .env.example                     # Template for optional proxy settings
```

## Setup

Requires Python 3.10+ (developed on 3.14).

```bash
git clone https://github.com/harishwargad/web_scrapper.git
cd web_scrapper

# with uv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# or with pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Optional: proxy

If requests get blocked on your network, you can route them through a proxy. Copy the template and fill in your own values:

```bash
cp .env.example .env
```

```
http_proxy=
https_proxy=
```

`.env` is gitignored. Never commit real credentials. Leave the values empty to run without a proxy.

## Usage

```bash
python price_tracker.py
```

Paste a Flipkart search URL when prompted.

## What I learned

- How HTTP requests work, and why headers like `User-Agent` matter
- Reading page structure with browser DevTools, and the difference between view-source and Inspect
- Parsing HTML with Beautiful Soup selectors
- Flipkart's CSS class names are auto-generated and change often, so I find product cards by the stable `data-id` attribute instead
- Search result pages are personalized and reordered, so they're not ideal for tracking one product over time
- Keeping secrets out of code and Git with environment variables

## Roadmap

- [x] Practice scraper on scrapethissite.com
- [x] Flipkart scraper: names and prices
- [ ] Full product titles (search results truncate names)
- [ ] Convert prices like `₹44,990` into numbers
- [ ] Track a single chosen TV by its `data-id` or product page
- [ ] Save price history (CSV or SQLite)
- [ ] Desktop or email alert when the price drops below a target
- [ ] Run daily with cron
- [ ] Error handling: timeouts, blocked requests, missing elements

## Limitations

- Flipkart can change its page structure at any time, which will break the scraper
- Results can differ from what you see in your browser (location, personalization, sponsored listings)
- Only the first page of results is handled

## Disclaimer

This is a personal, educational project. It makes a single request per run and is not meant for bulk or commercial scraping. Respect each website's terms of service and `robots.txt`.