import os

import requests
from dotenv import load_dotenv


load_dotenv()


class FootballDataClient:

    BASE_URL = "https://api.football-data.org/v4"

    def __init__(self):

        self.api_key = os.getenv("FOOTBALL_DATA_API_KEY")

        self.headers = {
            "X-Auth-Token": self.api_key
        }

    def get(self, endpoint):

        url = f"{self.BASE_URL}/{endpoint}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=20
        )

        response.raise_for_status()

        return response.json()