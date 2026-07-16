from backend.engine.match_analyzer import MatchAnalyzer

engine = MatchAnalyzer()

result = engine.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

print()

for key, value in result.items():

    print(f"{key:20} {value}")