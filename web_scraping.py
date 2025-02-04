import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = "https://quotes.toscrape.com/page/{}/"

def scrape_data(url):
    data = requests.get(url)
    if data.status_code == 200:
        soup = BeautifulSoup(data.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        data = []

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            data.append({"text": text, "author": author, "tags": tags})
        return data
    
    else:
        raise Exception("Url is not working or not able to fetch")
    

def scrape_all_data(base_url, pages=5):
    all_quotes = []

    for page_num in range(1, pages + 1):
        url = base_url.format(page_num)
        data = scrape_data(url)
        all_quotes.extend(data)
    return all_quotes

def save_to_csv(quotes_data, filename="quotes.csv"):
    df = pd.DataFrame(quotes_data)
    df.to_csv(filename, index=False)

def write_to_json(quotes_data, filename):
    with open(filename, "w", encoding='utf-8') as json_file:
        json.dump(quotes_data, json_file, indent=4)


try:
    csv = scrape_all_data(url)
    save_to_csv(csv)
    write_to_json(csv, "quotes.json")
    print("Scraping completed")
except Exception as e:
    print(e)
