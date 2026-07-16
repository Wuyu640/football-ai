from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.reasoning_graph import ReasoningGraph

from backend.intelligence.prediction_factors import PredictionFactors


class PredictionEngineV2:

    def __init__(self):

        self.builder = FeatureBuilder()

        self.graph = ReasoningGraph()

        self.factors = PredictionFactors()

    def analyse(self, team):

        features = self.builder.build(team)

        graph = self.graph.analyse(features)

        prediction = self.factors.analyse(graph)

        return {

            "features": features,

            "graph": graph,

            "prediction": prediction

        }