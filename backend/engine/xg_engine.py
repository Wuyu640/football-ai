class XGEngine:

    def calculate(self, analysis):

        home_xg = (
            1.20
            + analysis["goal_difference"] * 0.45
            + analysis["form_difference"] * 0.30
            + analysis["elo_difference"] / 300
        )

        away_xg = (
            1.10
            - analysis["goal_difference"] * 0.45
            - analysis["form_difference"] * 0.30
            - analysis["elo_difference"] / 300
        )

        home_xg = max(0.2, round(home_xg, 2))
        away_xg = max(0.2, round(away_xg, 2))

        return {
            "home_xg": home_xg,
            "away_xg": away_xg
        }