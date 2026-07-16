from backend.intelligence.opponent_strength_engine import OpponentStrengthEngine

engine = OpponentStrengthEngine()

for rating in [3, 5, 7, 9]:

    print(

        rating,

        engine.calculate(rating)

    )