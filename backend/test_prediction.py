from backend.engine.prediction_engine import PredictionEngine

engine = PredictionEngine()

result = engine.predict(

    "FC Barcelona",

    "Real Madrid CF"

)

print()

for k, v in result.items():

    print(k, ":", v)