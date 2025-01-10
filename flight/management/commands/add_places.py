from django.core.management.base import BaseCommand
from flight.models import Airport
from bs4 import BeautifulSoup as bs
from urllib import request
import logging

class Command(BaseCommand):
    help = 'Fetches airport data and saves it to the database'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)

        self.logger.info("Fetching Data of Different Airports...")

        top_100_url = "https://gettocenter.com/airports/top-100-airports-in-world"
        soup = self.fetch_airport_data(top_100_url)
        if soup:
            tr = soup.body.find_all('tr')
            self.save_airports(tr, "Unknown") 

        india_airports_url = "https://www.worlddata.info/asia/india/airports.php"
        soup = self.fetch_airport_data(india_airports_url)
        if soup:
            tr = soup.body.find_all('table')[0].find_all('tr')
            self.save_airports(tr[1:], "India")

        self.logger.info("DONE")

    def fetch_airport_data(self, url):
        try:
            page = request.urlopen(url)
            soup = bs(page, features="html.parser")
            return soup
        except Exception as e:
            self.logger.error(f"Error fetching data from {url}: {e}")
            return None

    def save_airports(self, tr, country):
        airports_to_save = []
        for r in tr:
            d = r.find_all('td')
            if len(d) < 5: 
                continue
            
            airport_name = d[1].text.strip()
            airport_code = d[2].text.strip().upper()
            city = d[3].text.strip()
            
            if not Airport.objects.filter(code=airport_code).exists():
                airports_to_save.append(Airport(city=city, airport=airport_name, code=airport_code, country=country))
        
        if airports_to_save:
            Airport.objects.bulk_create(airports_to_save)
            self.logger.info(f"Saved {len(airports_to_save)} airports.")
