class CalibrationEngine:

    def calibrate(self, probabilities):

        home = probabilities["home"]
        draw = probabilities["draw"]
        away = probabilities["away"]

        total = home + draw + away

        return {
            "home": round(home / total, 3),
            "draw": round(draw / total, 3),
            "away": round(away / total, 3)
        }