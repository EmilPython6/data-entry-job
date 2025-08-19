#SCRAPE WEBSITE DATA & CLEAN IT UP:

#BEAUTIFUL SOUP DOCS: https://realpython.com/beautiful-soup-web-scraper-python/#step-1-inspect-your-data-source

from bs4 import BeautifulSoup
import requests as r

class SiteScraper:
    def __init__(self):
        self.URL = 'https://appbrewery.github.io/Zillow-Clone/'
        self.list_of_addresses = []
        self.list_of_prices = []
        self.list_of_links = []

    def page(self):
        page_content = r.get(self.URL)
        page = BeautifulSoup(page_content.content, 'html.parser')
        listing_address_list = page.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

        for element in listing_address_list:
            for address in element.find("address", {"data-test": "property-card-addr"}):
                extracted_address = address.text
                formatted_address = extracted_address.strip()
                self.list_of_addresses.append(formatted_address)

            for price in element.find("span", {"data-test": "property-card-price"}):
                extracted_price = price.text
                formatted_price = extracted_price[:6]
                self.list_of_prices.append(formatted_price)

            for link in element.select('a.property-card-link[data-test="property-card-link"]'):
                self.list_of_links.append(link["href"])

        #print(self.list_of_addresses)
        #print(self.list_of_prices)
        #print(self.list_of_links)
        generated_tupple = (self.list_of_addresses, self.list_of_prices, self.list_of_links)
        return generated_tupple