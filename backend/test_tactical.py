from backend.engine.tactical_engine import TacticalEngine

engine = TacticalEngine()

barca = engine.profile("FC Barcelona")

madrid = engine.profile("Real Madrid CF")

print(barca)

print()

print(madrid)