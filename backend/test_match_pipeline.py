from pprint import pprint

from backend.engine.match_pipeline import MatchPipeline

pipeline = MatchPipeline()

result = pipeline.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

pprint(result)