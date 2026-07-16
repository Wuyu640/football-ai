from pprint import pprint

from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.reasoning_graph import ReasoningGraph

builder = FeatureBuilder()

graph = ReasoningGraph()

features = builder.build("FC Barcelona")

pprint(

    graph.analyse(

        features

    )

)