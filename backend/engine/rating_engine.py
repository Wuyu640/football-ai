from __future__ import annotations

from backend.engine.stats_engine import StatsEngine


class RatingEngine:

    def __init__(self):
        self.stats = StatsEngine()

    def calculate(
        self,
        home_team: str,
        away_team: str,
        league: str | None = None,
        season: int | None = None,
    ):

        home = self.stats.analyse(
            team_name=home_team,
            league=league,
            season=season,
        )

        away = self.stats.analyse(
            team_name=away_team,
            league=league,
            season=season,
        )

        home_attack = (
            home["avg_gf"] * 0.45
            + home["recent_avg_gf"] * 0.35
            + home["home_avg_gf"] * 0.20
        )

        away_attack = (
            away["avg_gf"] * 0.45
            + away["recent_avg_gf"] * 0.35
            + away["away_avg_gf"] * 0.20
        )

        home_defense = (
            (100 - home["avg_ga"] * 25) * 0.6
            + home["clean_sheet_rate"] * 100 * 0.4
        )

        away_defense = (
            (100 - away["avg_ga"] * 25) * 0.6
            + away["clean_sheet_rate"] * 100 * 0.4
        )

        home_form = home["recent_points_per_game"] * 33.33
        away_form = away["recent_points_per_game"] * 33.33

        home_rating = (
            home_attack * 0.40
            + home_defense * 0.35
            + home_form * 0.25
        )

        away_rating = (
            away_attack * 0.40
            + away_defense * 0.35
            + away_form * 0.25
        )

        difference = round(
            home_rating - away_rating,
            2
        )

        if difference > 2:
            favourite = home_team
        elif difference < -2:
            favourite = away_team
        else:
            favourite = "Draw"

        return {

            "home": home_team,
            "away": away_team,

            "home_rating": round(home_rating, 2),
            "away_rating": round(away_rating, 2),

            "difference": difference,

            "favorite": favourite,

            "home_stats": home,
            "away_stats": away,

        }