import csv
from pathlib import Path


class CSVExporter:

    def export(self, dataset, filename):

        output = Path(filename)

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not dataset:
            return

        with open(
            output,
            "w",
            newline="",
            encoding="utf8"
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=dataset[0].keys()
            )

            writer.writeheader()

            writer.writerows(dataset)