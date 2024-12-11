import time

class Cache:
    def __init__(self, many=False, expire_time=15):
        """
        Initialize the Cache object.

        :param many: Boolean indicating if multiple cache entries are allowed.
        :param expire_time: Time in minutes before the cache expires.
        """

        self.data: dict|None = None
        self.__many__: bool = many
        self.__expire_time__: int = expire_time

    # Implement caching methods here
    def exists(self, date=None) -> bool:
        """
        Check if the cache exists and is valid.

        :param date: Optional date to check if the cache is for a specific date.
        :return: Boolean indicating if the cache exists and is valid.
        """

        if not self.data or self.data.get('expire') < time.time():
            return False

        if date:
            if self.data.get('info')['date'] != date:
                return False

        return True

    def set_expire_time(self, expire_time) -> None:
        """
        Set the expiration time for the cache.

        :param expire_time: Time in minutes before the cache expires.
        :raises Exception: If the expiration time is not greater than 0.
        """

        if not expire_time > 0:
            raise Exception('The expiration time must be greater than 0')
        self.__expire_time__ = expire_time

    def set(self, data) -> None:
        """
        Set the cache data and expiration time.

        :param data: Data to be cached.
        :raises Exception: If the data is None.
        """

        if not data:
            raise Exception('data cannot be none')

        __expire_at__ = time.time() + (self.__expire_time__ * 60)

        if self.data:
            if self.data.get('info') == data:
                self.data['expire'] = __expire_at__
            else:
                self.data.update({'info': data, 'expire': __expire_at__})
        else:
            self.data = {'info': data, 'expire': __expire_at__}

    def get(self) -> None|dict :
        """
        Get the cached data if it exists and is valid.

        :return: Cached data or None if the cache is invalid or expired.
        """

        if not self.data:
            return None

        if self.data.get('expire') < time.time():
            self.data = None
            return None

        return self.data.get('info')



