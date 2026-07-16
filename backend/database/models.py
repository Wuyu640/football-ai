from dataclasses import dataclass


@dataclass
class Team:
    name: str
    attack: float
    defense: float
    elo: float


@dataclass
class Match:
    home: Team
    away: Team
    