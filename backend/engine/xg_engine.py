from __future__ import annotations


class XGEngine:

    HOME_BASE_XG = 1.35
    AWAY_BASE_XG = 1.05

    MIN_XG = 0.20
    MAX_XG = 4.50

    def calculate(self, analysis):

        home_attack = analysis["home_attack_index"] / 100
        away_attack = analysis["away_attack_index"] / 100

        home_defense = analysis["home_defense_index"] / 100
        away_defense = analysis["away_defense_index"] / 100

        attack_difference = (
            analysis["attack_difference"] / 100
        )

        defense_difference = (
            analysis["defense_difference"] / 100
        )

        form_difference = (
            analysis["form_difference"] / 100
        )

        elo_difference = (
            analysis["elo_difference"] / 400
        )

        home_xg = (

            self.HOME_BASE_XG

            + home_attack * 0.55

            - away_defense * 0.30

            + attack_difference * 0.25

            + defense_difference * 0.15

            + form_difference * 0.20

            + elo_difference * 0.15

        )

        away_xg = (

            self.AWAY_BASE_XG

            + away_attack * 0.55

            - home_defense * 0.30

            - attack_difference * 0.25

            - defense_difference * 0.15

            - form_difference * 0.20

            - elo_difference * 0.15

        )

        home_xg = round(
            min(
                self.MAX_XG,
                max(self.MIN_XG, home_xg)
            ),
            2
        )

        away_xg = round(
            min(
                self.MAX_XG,
                max(self.MIN_XG, away_xg)
            ),
            2
        )

        return {

            "home_xg": home_xg,

            "away_xg": away_xg,

            "total_xg": round(
                home_xg + away_xg,
                2
            )

        }