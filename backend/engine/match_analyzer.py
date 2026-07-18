from __future__ import annotations

from backend.engine.attack_index_engine import AttackIndexEngine
from backend.engine.defense_index_engine import DefenseIndexEngine
from backend.engine.elo_engine import EloEngine
from backend.engine.form_index_engine import FormIndexEngine
from backend.engine.team_profile import TeamProfile


class MatchAnalyzer:

    def __init__(
        self,
        league: str = "PD",
        season: str = "2025",
    ):

        self.profile = TeamProfile(
            league=league,
            season=season,
        )

        self.elo = EloEngine(
            league=league,
            season=season,
        )

        self.attack = AttackIndexEngine(
            league=league,
            season=season,
        )

        self.defense = DefenseIndexEngine(
            league=league,
            season=season,
        )

        self.form = FormIndexEngine(
            league=league,
            season=season,
        )

    def analyse(self, home, away):

        home_name = home.name
        away_name = away.name

        home_profile = self.profile.build(home_name)
        away_profile = self.profile.build(away_name)

        ratings = self.elo.calculate()

        home_elo = ratings.get(home_name, 1500)
        away_elo = ratings.get(away_name, 1500)

        home_attack = self.attack.calculate(home_profile)
        away_attack = self.attack.calculate(away_profile)

        home_defense = self.defense.calculate(home_profile)
        away_defense = self.defense.calculate(away_profile)

        home_form = self.form.calculate(home_profile)
        away_form = self.form.calculate(away_profile)

        home_attack_vs_away_defense = round(
            home_attack - away_defense,
            2,
        )

        away_attack_vs_home_defense = round(
            away_attack - home_defense,
            2,
        )

        offensive_edge = round(
            home_attack_vs_away_defense
            - away_attack_vs_home_defense,
            2,
        )

        defensive_edge = round(
            home_defense - away_defense,
            2,
        )

        momentum = round(
            home_form - away_form,
            2,
        )

        return {

            "home": home,
            "away": away,

            "home_profile": home_profile,
            "away_profile": away_profile,

            "home_elo": home_elo,
            "away_elo": away_elo,
            "elo_difference": round(
                home_elo - away_elo,
                1,
            ),

            "home_attack_index": home_attack,
            "away_attack_index": away_attack,
            "attack_difference": round(
                home_attack - away_attack,
                2,
            ),

            "home_defense_index": home_defense,
            "away_defense_index": away_defense,
            "defense_difference": round(
                home_defense - away_defense,
                2,
            ),

            "home_form_index": home_form,
            "away_form_index": away_form,
            "form_difference": round(
                home_form - away_form,
                2,
            ),

            "home_attack_vs_away_defense": home_attack_vs_away_defense,
            "away_attack_vs_home_defense": away_attack_vs_home_defense,
            "offensive_edge": offensive_edge,
            "defensive_edge": defensive_edge,
            "momentum": momentum,
        }