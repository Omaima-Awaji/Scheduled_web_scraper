import csv
import time
import schedule
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_bbc():
    base_url = "https://www.bbc.com/health"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text,"html.parser")
    headlines = soup.find_all("h2", attrs={"data-testid": "card-headline"})
    data = []
    for headline in headlines:
        a_tag = headline.find_parent("a")
        href = a_tag["href"]
        if href.startswith("http"):
            full_url = href
        else:
            full_url = "http://www.bbc.com" + href
        data.append({
            "title": headline.text,
            "scraped_at": datetime.now().strftime("%H:%M"),
            "url": full_url})
    save_to_csv(data)


def save_to_csv(data):
    with open("bbc_headline.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "url", "scraped_at"])
        writer.writerows(data)



schedule.every().minute.do(scrape_bbc)

while True:
    schedule.run_pending()
    time.sleep(60)