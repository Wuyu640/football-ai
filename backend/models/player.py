from dataclasses import dataclass


@dataclass
class Player:

    name: str

    position: str

    rating: float

    injured: bool

    suspended: bool

    minutes: int

    goals: int

    assists: int

    starter: bool