from backend.engine.team_profile import TeamProfile
from backend.engine.elo_engine import EloEngine
from backend.engine.attack_index_engine import AttackIndexEngine
from backend.engine.defense_index_engine import DefenseIndexEngine
from backend.engine.form_index_engine import FormIndexEngine


class MatchAnalyzer:

    def __init__(self):

        self.profile = TeamProfile()
        self.elo = EloEngine()

        self.attack = AttackIndexEngine()
        self.defense = DefenseIndexEngine()
        self.form = FormIndexEngine()

    def analyse(self, home, away):

        home_profile = self.profile.build(home.name)
        away_profile = self.profile.build(away.name)

        ratings = self.elo.calculate()

        home_elo = ratings.get(home.name, 1500)
        away_elo = ratings.get(away.name, 1500)

        home_attack = self.attack.calculate(home_profile)
        away_attack = self.attack.calculate(away_profile)

        home_defense = self.defense.calculate(home_profile)
        away_defense = self.defense.calculate(away_profile)

        home_form = self.form.calculate(home_profile)
        away_form = self.form.calculate(away_profile)

        # ============================
        # MATCHUPS
        # ============================

        home_attack_vs_away_defense = round(
            home_attack - away_defense,
            2
        )

        away_attack_vs_home_defense = round(
            away_attack - home_defense,
            2
        )

        offensive_edge = round(
            home_attack_vs_away_defense -
            away_attack_vs_home_defense,
            2
        )

        defensive_edge = round(
            home_defense - away_defense,
            2
        )

        momentum = round(
            home_form - away_form,
            2
        )

        analysis = {

            # Equipos
            "home": home,
            "away": away,

            # Profiles
            "home_profile": home_profile,
            "away_profile": away_profile,

            # ============================
            # ELO
            # ============================

            "home_elo": home_elo,
            "away_elo": away_elo,
            "elo_difference": round(
                home_elo - away_elo,
                1
            ),

            # ============================
            # ATTACK
            # ============================

            "home_attack_index": home_attack,
            "away_attack_index": away_attack,

            "attack_difference": round(
                home_attack - away_attack,
                2
            ),

            # ============================
            # DEFENSE
            # ============================

            "home_defense_index": home_defense,
            "away_defense_index": away_defense,

            "defense_difference": round(
                home_defense - away_defense,
                2
            ),

            # ============================
            # FORM
            # ============================

            "home_form_index": home_form,
            "away_form_index": away_form,

            "form_difference": round(
                home_form - away_form,
                2
            ),

            # ============================
            # MATCHUPS
            # ============================

            "home_attack_vs_away_defense":
                home_attack_vs_away_defense,

            "away_attack_vs_home_defense":
                away_attack_vs_home_defense,

            "offensive_edge":
                offensive_edge,

            "defensive_edge":
                defensive_edge,

            "momentum":
                momentum

        }

        return analysis