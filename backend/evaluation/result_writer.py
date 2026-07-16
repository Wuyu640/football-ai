import json
from pathlib import Path


class ResultWriter:

    def __init__(self):

        self.folder = Path(

            "backend/evaluation/results"

        )

        self.folder.mkdir(

            parents=True,

            exist_ok=True

        )

    def save(

        self,

        name,

        result

    ):

        file = self.folder / f"{name}.json"

        with open(

            file,

            "w",

            encoding="utf8"

        ) as f:

            json.dump(

                result,

                f,

                indent=4,

                ensure_ascii=False

            )

        return file