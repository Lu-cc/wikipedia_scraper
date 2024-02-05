#imports
import requests
from bs4 import BeautifulSoup
import re
from scripts.scraper import WikipediaScraper as ws
import json



from scripts.scraper import WikipediaScraper as ws


def main():
    # run the program from here
    scraper = ws()

    countries = scraper.list_countries()
    for country in countries:
        scraper.refresh_cookie()
        scraper.get_leaders(country)

    scraper.to_json_file("./leaders_data.json")
    


if __name__ == "__main__":
    main()
