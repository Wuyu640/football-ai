from pprint import pprint

from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.reasoning_graph import ReasoningGraph

from backend.intelligence.match_narrative import MatchNarrative

builder = FeatureBuilder()

graph = ReasoningGraph()

story = MatchNarrative()

features = builder.build(

    "FC Barcelona"

)

nodes = graph.analyse(

    features

)

pprint(

    story.build(

        nodes

    )

)