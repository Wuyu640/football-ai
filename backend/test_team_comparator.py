from pprint import pprint

from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.team_comparator import TeamComparator

builder = FeatureBuilder()

engine = TeamComparator()

home = builder.build(

    "FC Barcelona"

)

away = builder.build(

    "Real Madrid CF"

)

pprint(

    engine.compare(

        home,

        away

    )

)