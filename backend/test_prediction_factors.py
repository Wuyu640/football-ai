from pprint import pprint

from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.reasoning_graph import ReasoningGraph

from backend.intelligence.prediction_factors import PredictionFactors

builder = FeatureBuilder()

graph = ReasoningGraph()

engine = PredictionFactors()

features = builder.build(

    "FC Barcelona"

)

nodes = graph.analyse(

    features

)

pprint(

    engine.analyse(

        nodes

    )

)