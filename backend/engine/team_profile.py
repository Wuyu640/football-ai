from backend.engine.stats_engine import StatsEngine


class TeamProfile:

    def __init__(self):

        self.stats = StatsEngine()

    def build(self, team):

        stats = self.stats.analyse(team)

        profile = {

            # Equipo
            "team": team,

            # Partidos
            "played": stats["played"],
            "wins": stats["wins"],
            "draws": stats["draws"],
            "losses": stats["losses"],

            # Goles
            "gf": stats["gf"],
            "ga": stats["ga"],
            "avg_gf": stats["avg_gf"],
            "avg_ga": stats["avg_ga"],

            # Defensa
            "clean_sheets": stats["clean_sheets"],
            "failed_to_score": stats["failed_to_score"],

            # Forma
            "recent_points": stats["recent_points"],
            "recent_avg_gf": stats["recent_avg_gf"],
            "recent_avg_ga": stats["recent_avg_ga"],

            # Local / Visitante
            "home_avg_gf": stats["home_avg_gf"],
            "away_avg_gf": stats["away_avg_gf"],

            # Mercados
            "over25_rate": stats["over25_rate"],
            "btts_rate": stats["btts_rate"]

        }

        return profile