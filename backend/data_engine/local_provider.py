import json
from pathlib import Path


class LocalProvider:

    def __init__(self):

        self.base = Path(
            "backend/data/seasons"
        )

        self.base.mkdir(
            parents=True,
            exist_ok=True
        )

    def path(self, league, season):

        return self.base / f"{league}_{season}.json"

    def exists(self, league, season):

        return self.path(
            league,
            season
        ).exists()

    def load(self, league, season):

        with open(

            self.path(
                league,
                season
            ),

            "r",

            encoding="utf8"

        ) as f:

            return json.load(f)

    def save(

        self,

        league,

        season,

        matches

    ):

        with open(

            self.path(
                league,
                season
            ),

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                matches,

                f,

                ensure_ascii=False,

                indent=2

            )