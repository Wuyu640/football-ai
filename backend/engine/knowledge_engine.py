import json
from pathlib import Path


class KnowledgeEngine:

    def __init__(self):

        self.base = Path(
            "backend/knowledge"
        )

        self._teams = None

    def teams(self):

        if self._teams is None:

            with open(

                self.base / "teams.json",

                "r",

                encoding="utf8"

            ) as f:

                self._teams = json.load(f)

        return self._teams

    def get_team(self, name):

        return self.teams().get(name)

    def exists(self, name):

        return name in self.teams()