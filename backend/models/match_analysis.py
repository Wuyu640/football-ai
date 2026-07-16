from dataclasses import dataclass


@dataclass
class MatchAnalysis:

    home: str
    away: str

    elo_difference: float

    goal_difference: float

    defense_difference: float

    form_difference: float