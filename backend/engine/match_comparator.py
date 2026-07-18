from __future__ import annotations

from backend.engine.attack_engine import AttackEngine
from backend.engine.defense_engine import DefenseEngine
from backend.engine.form_engine import FormEngine
from backend.engine.rating_engine import RatingEngine
from backend.engine.schedule_strength import ScheduleStrength


class MatchComparator:

    def __init__(self):
        self.attack = AttackEngine()
        self.defense = DefenseEngine()
        self.form = FormEngine()
        self.rating = RatingEngine()
        self.schedule = ScheduleStrength()

    def compare(
        self,
        home_team: str,
        away_team: str,
        league: str | None = None,
        season: int | None = None,
    ):

        home_attack = self.attack.analyse(
            home_team,
            league,
            season,
        )

        away_attack = self.attack.analyse(
            away_team,
            league,
            season,
        )

        home_defense = self.defense.analyse(
            home_team,
            league,
            season,
        )

        away_defense = self.defense.analyse(
            away_team,
            league,
            season,
        )

        home_form = self.form.analyse(
            home_team,
            league,
            season,
        )

        away_form = self.form.analyse(
            away_team,
            league,
            season,
        )

        rating = self.rating.calculate(
            home_team,
            away_team,
            league,
            season,
        )

        home_schedule = self.schedule.analyse(
            home_team,
            league,
            season,
        )

        away_schedule = self.schedule.analyse(
            away_team,
            league,
            season,
        )

        return {

            "rating": rating,

            "attack": {
                "home": home_attack,
                "away": away_attack,
            },

            "defense": {
                "home": home_defense,
                "away": away_defense,
            },

            "form": {
                "home": home_form,
                "away": away_form,
            },

            "schedule": {
                "home": home_schedule,
                "away": away_schedule,
            },

        }