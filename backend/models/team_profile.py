from dataclasses import dataclass


@dataclass
class TeamProfile:

    # Información básica
    team: str

    # Rendimiento
    played: int
    wins: int
    draws: int
    losses: int

    # Goles
    gf: int
    ga: int

    avg_gf: float
    avg_ga: float

    clean_sheets: int
    failed_to_score: int

    # Rating
    elo: float = 1500

    # Forma
    form5: float = 0
    form10: float = 0

    # Local / Visitante
    home_strength: float = 0
    away_strength: float = 0

    # Ataque
    attack_rating: float = 0

    # Defensa
    defense_rating: float = 0

    # Contexto
    injuries: int = 0

    rest_days: int = 0

    coach: str = ""

    formation: str = ""

    tactical_style: str = ""

    pressing: str = ""

    tempo: str = ""

    possession: float = 0