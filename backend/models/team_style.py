from dataclasses import dataclass


@dataclass
class TeamStyle:

    # Nivel ofensivo
    attack: str

    # Nivel defensivo
    defense: str

    # Frecuencia de porterías a cero
    clean_sheet_rate: float

    # Frecuencia marcando goles
    scoring_rate: float

    # Promedio de goles
    avg_goals_for: float
    avg_goals_against: float

    # Resultados
    win_rate: float
    draw_rate: float
    loss_rate: float

    # Nuevas métricas
    over25_rate: float

    btts_rate: float

    recent_points: int

    recent_avg_gf: float

    recent_avg_ga: float

    home_avg_gf: float

    away_avg_gf: float