from pprint import pprint

from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.team_comparator import TeamComparator

from backend.intelligence.advantage_engine import AdvantageEngine

builder = FeatureBuilder()

compare = TeamComparator()

engine = AdvantageEngine()

home = builder.build(

    "FC Barcelona"

)

away = builder.build(

    "Real Madrid CF"

)

comparison = compare.compare(

    home,

    away

)

pprint(

    engine.analyse(

        comparison

    )

)