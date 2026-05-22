# Scheduled_web_scraper (BBC Health News Scraper 📰)

A command-line web scraper that automatically collects BBC Health headlines every minute and saves them to a CSV file, built with Python.

## Features
- Scrapes BBC Health news headlines and URLs
- Runs automatically every minute using a scheduler
- Saves results to a CSV file with timestamps
- Appends new data without overwriting previous results

## How to Use
Run the script:

python bbc_scraper.py

The script will run continuously and scrape new headlines every minute. Results are saved automatically to bbc_headline.csv.

To stop the script press CTRL + C

## Output
A file called bbc_headline.csv will be created with the following columns:

title, url, scraped_at
Weight loss drugs linked to lower risk of..., https://www.bbc.com/news/..., 14:30
New study reveals benefits of..., https://www.bbc.com/news/..., 14:31

## Requirements
- Python 3.x
- requests
- beautifulsoup4
- schedule

## Installation
pip install requests beautifulsoup4 schedule
