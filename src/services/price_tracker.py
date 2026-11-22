import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
httpProxy_url = os.getenv("http_proxy")
httpsProxy_url = os.getenv("https_proxy")

proxies = {"http": httpProxy_url, "https": httpsProxy_url}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7",
    "Referer": "https://www.flipkart.com/",
}


def fetch_data(url):
    r = requests.get(url, proxies = proxies, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    cards = soup.find_all("div", attrs={"data-id": True})

    for card in cards:
        img = card.find("img", alt=True)
        name = img["alt"] if img else "No Name"
        
        price = "No Price"
        for text in card.stripped_strings:
            if text.startswith("₹"):
                price = text
                break
        print(name, "-->", price)        


    
url = input("Paste the url: ")
   
fetch_data(url)