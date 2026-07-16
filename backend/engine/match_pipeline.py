from backend.engine.identity_detector import IdentityDetector
from backend.engine.matchup_engine import MatchupEngine
from backend.intelligence.match_classifier import MatchClassifier
from backend.intelligence.tactical_reasoner import TacticalReasoner


class MatchPipeline:

    def __init__(self):

        self.identity = IdentityDetector()
        self.classifier = MatchClassifier()
        self.matchup = MatchupEngine()
        self.reasoner = TacticalReasoner()

    def analyse(self, home_team, away_team):

        home = self.identity.detect(home_team)
        away = self.identity.detect(away_team)

        tags = self.classifier.classify(
            home,
            away
        )

        matchup = self.matchup.analyse(
            home,
            away
        )

        reasoning = self.reasoner.analyse(
            home,
            away
        )

        return {

            "home_identity": home,

            "away_identity": away,

            "match_type": tags,

            "matchup": matchup,

            "reasoning": reasoning

        }