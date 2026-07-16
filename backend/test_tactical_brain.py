from pprint import pprint

from backend.intelligence.tactical_brain import TacticalBrain
from backend.models.team_style import TeamStyle

brain = TacticalBrain()

home = TeamStyle(
    attack="High",
    defense="Strong",
    clean_sheet_rate=0.60,
    scoring_rate=0.95
)

away = TeamStyle(
    attack="Medium",
    defense="Weak",
    clean_sheet_rate=0.20,
    scoring_rate=0.70
)

pprint(
    brain.analyse(
        home,
        away
    )
)