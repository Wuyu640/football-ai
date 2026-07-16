from backend.engine.stats_engine import StatsEngine
from backend.models.team_identity import TeamIdentity


class AutoKnowledgeBuilder:

    def __init__(self):

        self.stats = StatsEngine()

    def build(self, team):

        s = self.stats.analyse(team)

        # Posesión (estimación inicial)
        possession = min(
            10,
            round(s["avg_gf"] * 3, 1)
        )

        # Presión (estimación inicial)
        pressing = min(
            10,
            round(
                s["clean_sheets"] /
                max(s["played"], 1) * 10,
                1
            )
        )

        # Ritmo
        tempo = min(
            10,
            round(
                (s["avg_gf"] + s["avg_ga"]) * 2,
                1
            )
        )

        # Velocidad de transición
        transition_speed = min(
            10,
            round(
                s["over25_rate"] * 10,
                1
            )
        )

        # Línea defensiva (estimación)
        defensive_line = min(
            10,
            round(
                (2 - s["avg_ga"]) * 5,
                1
            )
        )

        width = 5

        build_up = "Mixed"

        attack_focus = "Balanced"

        return TeamIdentity(

            possession=possession,

            pressing=pressing,

            transition_speed=transition_speed,

            defensive_line=defensive_line,

            width=width,

            build_up=build_up,

            attack_focus=attack_focus,

            tempo=tempo

        )