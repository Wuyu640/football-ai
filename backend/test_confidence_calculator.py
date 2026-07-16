from backend.engine.unified_prediction_engine import UnifiedPredictionEngine

from backend.intelligence.confidence_calculator import ConfidenceCalculator

engine = UnifiedPredictionEngine()

confidence = ConfidenceCalculator()

result = engine.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

print(

    confidence.calculate(

        result["comparison"]

    )

)