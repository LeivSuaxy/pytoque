import requests
import datetime
from pytoque.utils.utils import get_url, filter_data
from pytoque.validators.validators import validate_date, validate_filters
from pytoque.libs.cache import Cache

class PyToque:
    def __init__(self, api_key: str):
        if not api_key:
            raise Exception('Please provide an api_key')

        if type(api_key) != str:
            raise TypeError('Please provide a correct api_key')

        self.__cache__: Cache = Cache()

        self.headers = {
            'Authorization': f'Bearer {api_key}'
        }

    def get_today(self, filters: list = None, force: bool = True) -> dict:
        """
        Get the data from the API for today
        :param filters: List of filters to apply to the data, check README for more info.
        :param force: Boolean to force the request to the API, default TRUE, use cache if FALSE
        :return: Dict with the data obtained from the API. Format = { 'CURRENCY': VALUE }
        """

        if filters:
            if not validate_filters(filters):
                raise Exception('Incorrect filters')

        date = datetime.date.today()

        # If force is False and Cache exists return cache
        if force is False:
            if self.__cache__.exists():
                return self.__cache__.get()
            data = self.__do_request__(filters=filters, date=date)
            data['date'] = date.strftime('%Y-%m-%d')
            self.__cache__.set(data)
            return data
        else:
            return self.__do_request__(filters=filters, date=date)

    def get_date(self, date: str, filters: list = None, force: bool = True) -> dict:
        """
        Get the data from the API for a specific date
        :param date: Date in format "YYYY-MM-DD"
        :param filters: List of filters to apply to the data, check README for more info.
        :param force: Boolean to force the request to the API, default TRUE, use cache if FALSE
        :return: Dict with the data obtained from the API. Format = { 'CURRENCY': VALUE }
        """

        if filters:
            if not validate_filters(filters):
                raise Exception('Incorrect filters')

        if not validate_date(date):
            raise Exception('Please provide a date in format "YYYY-MM-DD"')

        if force is False:
            if self.__cache__.exists(date=date):
                return self.__cache__.get()
            data = self.__do_request__(filters=filters, date=date)
            data['date'] = date
            self.__cache__.set(data)
            return data
        else:
            return self.__do_request__(filters=filters, date=date)

    def __do_request__(self, filters: list, date):
        url = get_url(date)

        try:
            response = requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise e

        if response.status_code != 200:
            raise Exception(f'The response was not satisfactory, HTTP STATUS: {response.status_code}')

        data: dict = response.json()

        if not filters:
            return data.get('tasas')

        return filter_data(data.get('tasas'), filters)

