from backend.evaluation.backtester import Backtester


class SeasonValidator:

    def __init__(self):

        self.backtester = Backtester()

    def validate(

        self,

        predictions,

        results

    ):

        return self.backtester.evaluate_1x2(

            predictions,

            results

        )