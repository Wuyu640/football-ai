from pprint import pprint

from backend.engine.match_intelligence import MatchIntelligence

engine = MatchIntelligence()

result = engine.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

pprint(result)