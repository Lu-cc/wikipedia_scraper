#installs

import requests
from bs4 import BeautifulSoup
import re
import json


class WikipediaScraper():
    """Class object wich contains variables and methods in order to access the API and scrape the wikipedia pages of world leaders.
    """
    def __init__(self):
        self.root_url = "https://country-leaders.onrender.com"
        self.status_ep = "/status"
        self.cookie_ep = "/cookie/"
        self.country_ep = "/countries"
        self.leaders_ep = "/leaders"
        self.leader_ep = "/leader"
        self.cookies = (requests.get(f"{self.root_url}{self.cookie_ep}")).cookies

        self.leaders_data = []

    def refresh_cookie(self):
        """Method to refresh the cookies

        Returns:
            cookies: A cookie object that can be used to access the APIs.
        """
        cookie_req = requests.get(f"{self.root_url}{self.cookie_ep}")
        self.cookies = cookie_req.cookies
        return self.cookies
        
    def list_countries(self):
        """Method to access the corresponding API and list the countries.

        Returns:
            countries(list): Contains a list of the countries available. 
        """
        country_req=requests.get(f"{self.root_url}{self.country_ep}", cookies=self.cookies)
        if country_req.status_code == 200:
            return country_req.json()
        else:
            self.refresh_cookie()
            print(f"Status code: {country_req.status_code}\nUnknown error during requesting countries.")
            
    def get_leaders(self, country):
        """Method to list all the leaders and their data into a dictionary.

        Args:
            country ('string'): The abbreviation of the country. 
        """
        leaders_req = requests.get(f"{self.root_url}{self.leaders_ep}", cookies=self.cookies, params= {"country":country})
        if leaders_req.status_code == 200:
            self.leaders_data = [*self.leaders_data, *leaders_req.json()]
        elif leaders_req.status_code == 403:
            print(f"Status code: {leaders_req.status_code}\nRefreshing cookie...")
            self.refresh_cookie()
        else:
            print(f"Status code: {leaders_req.status_code}\nUnknown error on requesting leader of =={country}==")
    
    def get_first_paragraph(self, wikipedia_url):
        """Extract and print the first paragraph of each leader

        Args:
            wikipedia_url ('string'): The url for the leader's Wikipedia page

        Returns:
            first parargraph("srting"): The first paragraph of the leader's wikipedia page
        """
        req = requests.get(wikipedia_url)
        soup = BeautifulSoup(req.content, "html.parser")
        paragraphs = soup.find_all('p')
        #print(wikipedia_url) # keep this for the rest of the notebook
        for paragraph in paragraphs:
            if re.search(r"^<p><b>.*</b>", str(paragraph)):  
                first_paragraph = paragraph.text
                return first_paragraph
                break
        
    def to_json_file(self, filepath):
        leaders_with_paragraphs = {}
        for leader_info in self.leaders_data:
            leader_id = leader_info.get("id")
            leader = {"First Name": leader_info.get("first_name"), "Last Name": leader_info.get("last_name"),
                      "Birth Date": leader_info.get("birth_date"), "Death Date": leader_info.get("death_date"),
                      "Wikipedia URL": leader_info.get("wikipedia_url")}
            wikipedia_url = leader_info.get("wikipedia_url")
            leader["First Paragraph"] = self.get_first_paragraph(wikipedia_url)
            print(leader)
            leaders_with_paragraphs[leader_id] = leader
            print(leaders_with_paragraphs)
            
        with open(filepath, "w") as output_file:
            json.dump(leaders_with_paragraphs, output_file, indent=4)



