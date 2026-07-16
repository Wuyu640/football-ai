from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.style_detector import StyleDetector
from backend.engine.probability_engine import ProbabilityEngine
from backend.engine.tactical_matchup import TacticalMatchup


class MatchIntelligence:

    def __init__(self):

        self.analysis = MatchAnalyzer()
        self.styles = StyleDetector()
        self.probability = ProbabilityEngine()
        self.tactical = TacticalMatchup()

    def analyse(self, home, away):

        analysis = self.analysis.analyse(home, away)

        home_style = self.styles.detect(home)

        away_style = self.styles.detect(away)

        tactical = self.tactical.analyse(
            home_style,
            away_style
        )

        probability = self.probability.calculate(analysis)

        return {

            "analysis": analysis,

            "home_style": home_style,

            "away_style": away_style,

            "tactical": tactical,

            "probability": probability

        }