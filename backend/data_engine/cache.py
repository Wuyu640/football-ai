import time


class Cache:

    _instance = None
    _data = {}

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def get(self, key):

        if key not in self._data:
            return None

        value, timestamp = self._data[key]

        # Caduca después de 1 hora
        if time.time() - timestamp > 3600:
            del self._data[key]
            return None

        return value

    def set(self, key, value):

        self._data[key] = (
            value,
            time.time()
        )

    def has(self, key):

        return self.get(key) is not None

    def delete(self, key):

        if key in self._data:
            del self._data[key]

    def clear(self):

        self._data.clear()