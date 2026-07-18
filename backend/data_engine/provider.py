import os
import requests
from abc import ABC, abstractmethod

API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")


class DataProvider(ABC):

    @abstractmethod
    def get_match(self, home, away):
        pass


class MatchProvider(DataProvider):

    BASE_URL = "https://api.football-data.org/v4"

    def get_match(self, home, away):

        headers = {
            "X-Auth-Token": API_KEY
        }

        response = requests.get(
            f"{self.BASE_URL}/matches",
            headers=headers
        )

        return response.json()