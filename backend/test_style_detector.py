from backend.engine.style_detector import StyleDetector

engine = StyleDetector()

teams = [
    "FC Barcelona",
    "Real Madrid CF",
    "Atlético de Madrid",
    "Athletic Club"
]

for team in teams:

    print("\n", team)

    print(engine.detect(team))