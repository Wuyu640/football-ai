from dataclasses import dataclass


@dataclass
class TeamIdentity:

    possession: float

    pressing: float

    transition_speed: float

    defensive_line: float

    width: float

    build_up: str

    attack_focus: str

    tempo: float