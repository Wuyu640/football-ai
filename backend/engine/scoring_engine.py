from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.style_detector import StyleDetector
from backend.engine.tactical_matchup import TacticalMatchup
from backend.engine.elo_engine import EloEngine


class ScoringEngine:

    def __init__(self):

        self.analysis = MatchAnalyzer()
        self.styles = StyleDetector()
        self.tactical = TacticalMatchup()
        self.elo = EloEngine()

    def calculate(self, home, away):

        analysis = self.analysis.analyse(home, away)

        home_style = self.styles.detect(home)
        away_style = self.styles.detect(away)

        tactical = self.tactical.analyse(
            home_style,
            away_style
        )

        ratings = self.elo.calculate()

        home_elo = ratings.get(home, 1500)
        away_elo = ratings.get(away, 1500)

        score = 50

        score += (home_elo - away_elo) / 25

        score += analysis["goal_difference"] * 8

        score += analysis["defense_difference"] * 6

        score += analysis["form_difference"] * 10

        score += tactical["tactical_score"] * 8

        score = max(0, min(score, 100))

        return {
            "score": round(score, 2),
            "analysis": analysis,
            "styles": {
                "home": home_style,
                "away": away_style
            },
            "tactical": tactical
        }