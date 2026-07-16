from dataclasses import dataclass


@dataclass
class TeamRating:

    attack: float

    defense: float

    form: float

    home_attack: float

    away_attack: float

    home_defense: float

    away_defense: float