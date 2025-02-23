import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self):
        self.url = 'https://www.eltoque.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def __parse__(self) -> dict:
        currencies, prices = self.__scrap__()
        data: dict = {}

        for c, p in zip(currencies, prices):
            data[c.text[1:].replace(' ', '')] = float(p.text.replace(' CUP', ''))

        return data

    def __scrap__(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        currency = soup.find_all('span', class_='currency')
        prices = soup.find_all('span', class_='price-text')

        return currency, prices

    def get(self) -> dict:
        return self.__parse__()