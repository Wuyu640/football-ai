from pprint import pprint

from backend.pipeline.full_match_pipeline import FullMatchPipeline

engine = FullMatchPipeline()

result = engine.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

pprint(result)