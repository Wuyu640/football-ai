from backend.engine.stats_engine import StatsEngine
from backend.models.style_feature import StyleFeature


class FeatureBuilder:

    def __init__(self):

        self.stats = StatsEngine()

    def build(self, team):

        s = self.stats.analyse(team)

        features = []

        features.append(

            StyleFeature(

                name="Attack",

                value=s["avg_gf"],

                confidence=0.90,

                evidence=[

                    "Average goals",

                    "Scoring rate"

                ]

            )

        )

        features.append(

            StyleFeature(

                name="Defense",

                value=2 - s["avg_ga"],

                confidence=0.90,

                evidence=[

                    "Goals conceded",

                    "Clean sheets"

                ]

            )

        )

        features.append(

            StyleFeature(

                name="Tempo",

                value=s["avg_gf"] + s["avg_ga"],

                confidence=0.75,

                evidence=[

                    "Goals",

                    "Open matches"

                ]

            )

        )

        return features