from dataclasses import dataclass


@dataclass
class Prediction:

    home_team: str

    away_team: str

    home_xg: float

    away_xg: float

    home_probability: float

    draw_probability: float

    away_probability: float

    btts: float

    over25: float

    top_scores: list