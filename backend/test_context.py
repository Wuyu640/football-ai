from pprint import pprint

from backend.engine.core_engine import CoreEngine

engine = CoreEngine()

result = engine.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

pprint(result["context"])