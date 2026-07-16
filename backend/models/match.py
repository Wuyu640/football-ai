from dataclasses import dataclass

from backend.models.team import Team


@dataclass
class Match:

    home: Team
    away: Team