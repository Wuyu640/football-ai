from backend.engine.match_analyzer import MatchAnalyzer
from backend.data_engine.league_provider import LeagueProvider


class DatasetBuilder:

    def __init__(self):

        self.analyzer = MatchAnalyzer()
        self.provider = LeagueProvider()

    def build_match(self, home, away, result):

        analysis = self.analyzer.analyse(
            home,
            away
        )

        return {

            **analysis,

            "result": result

        }

    def build_season(
        self,
        league="PD",
        season=2025
    ):

        dataset = []

        matches = self.provider.matches(
            league,
            season
        )

        for match in matches:

            if match["status"] != "FINISHED":
                continue

            home = match["homeTeam"]["name"]
            away = match["awayTeam"]["name"]

            hg = match["score"]["fullTime"]["home"]
            ag = match["score"]["fullTime"]["away"]

            if hg > ag:
                result = "home"

            elif hg < ag:
                result = "away"

            else:
                result = "draw"

            dataset.append(

                self.build_match(

                    home,

                    away,

                    result

                )

            )

        return dataset