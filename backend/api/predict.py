from backend.pipeline.full_match_pipeline import FullMatchPipeline


class Predictor:

    def __init__(self):

        self.pipeline = FullMatchPipeline()

    def predict(

        self,

        home,

        away

    ):

        result = self.pipeline.analyse(

            home,

            away

        )

        return {

            "home_team": home,

            "away_team": away,

            "prediction": result["markets"],

            "xg": result["xg"]

        }