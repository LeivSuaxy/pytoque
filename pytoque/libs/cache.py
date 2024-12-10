import time

class Cache:
    def __init__(self, many=False, expire_time=15):
        self.data: dict|None = None
        self.__many__: bool = many
        self.__expire_time__: int = expire_time

    # Implement caching methods here
    def exists(self, date=None) -> bool:
        if not self.data or self.data.get('expire') < time.time():
            return False

        if date:
            if self.data.get('info')['date'] != date:
                return False

        return True

    def set_expire_time(self, expire_time) -> None:
        if not expire_time > 0:
            raise Exception('The expiration time must be greater than 0')
        self.__expire_time__ = expire_time

    def set(self, data) -> None:
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
        if not self.data:
            return None

        if self.data.get('expire') < time.time():
            self.data = None
            return None

        return self.data.get('info')



