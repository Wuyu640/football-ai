import requests


class FootballDataClient:

    def __init__(self):
        self.base_url = ""

    def get_team(self, team_name):
        return {
            "name": team_name
        }