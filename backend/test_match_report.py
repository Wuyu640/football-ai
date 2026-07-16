from pprint import pprint

from backend.engine.unified_prediction_engine import UnifiedPredictionEngine

from backend.intelligence.match_report import MatchReport

engine = UnifiedPredictionEngine()

report = MatchReport()

result = engine.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

pprint(

    report.build(

        result

    )

)