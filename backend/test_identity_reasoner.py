from pprint import pprint

from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.identity_reasoner import IdentityReasoner

builder = FeatureBuilder()

reasoner = IdentityReasoner()

features = builder.build(

    "FC Barcelona"

)

pprint(

    reasoner.analyse(

        features

    )

)