from dataclasses import dataclass


@dataclass
class Team:

    name: str
    elo: float
    attack: float
    defense: float
    form: float
    possession: float
    pressing: float
    transition: float