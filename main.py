from scrape_site_data import SiteScraper
from fill_out_form import fill_form

scrape = SiteScraper()
extracted_data = scrape.page()

fill_form(extracted_data[0], extracted_data[1], extracted_data[2])