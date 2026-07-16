from pprint import pprint

from backend.engine.football_brain import FootballBrain

brain = FootballBrain()

result = brain.analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

pprint(result)