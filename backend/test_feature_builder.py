from pprint import pprint

from backend.knowledge.feature_builder import FeatureBuilder

builder = FeatureBuilder()

features = builder.build("FC Barcelona")

print()

pprint(features)