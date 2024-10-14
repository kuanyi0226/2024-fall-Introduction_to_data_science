import scrapy
from hw2_mlb.items import Hw2MlbItem
from bs4 import BeautifulSoup


class MlbSpiderSpider(scrapy.Spider):
    name = "mlb_spider"
    allowed_domains = ["www.mlb.com"]
    start_urls = ["https://www.mlb.com/stats/"]
    page_number = 1

    def parse(self, response):
        #check the page is valid?
        if not self.is_valid_page(response):
            self.logger.info(f"No valid data found on page: {self.page_number}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('tbody', class_="notranslate")
        rows = table.find_all('tr')

        for row in rows:
            item = Hw2MlbItem()
            item['AB'] = row.find('td',attrs={'data-col': '3'}).text
            item['AVG'] = row.find('td',attrs={'data-col': '14'}).text
            item['BB'] = row.find('td',attrs={'data-col': '10'}).text
            item['G'] = row.find('td',attrs={'data-col': '2'}).text
            item['H'] = row.find('td',attrs={'data-col': '5'}).text
            item['HR'] = row.find('td',attrs={'data-col': '8'}).text
            item['OBP'] = row.find('td',attrs={'data-col': '15'}).text
            item['PLAYER'] = row.find('th').text
            item['R'] = row.find('td',attrs={'data-col': '4'}).text
            item['RBI'] = row.find('td',attrs={'data-col': '9'}).text
            item['SB'] = row.find('td',attrs={'data-col': '12'}).text
            item['SLG'] = row.find('td',attrs={'data-col': '16'}).text
            item['SO'] = row.find('td',attrs={'data-col': '11'}).text
            item['TEAM'] = row.find('td',attrs={'data-col': '1'}).text

            yield item
        
        self.page_number = self.page_number + 1
        next_page = self.start_urls[0] + '?page=' + str(self.page_number)
        yield response.follow(next_page, callback=self.parse)

    def is_valid_page(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('tbody', class_="notranslate")
        #check whether find table with rows
        if table and table.find_all('tr'): 
            return True
        return False
