from pprint import pprint

from backend.engine.identity_detector import IdentityDetector

from backend.intelligence.match_classifier import MatchClassifier

from backend.intelligence.game_flow_engine import GameFlowEngine

detector = IdentityDetector()

classifier = MatchClassifier()

flow = GameFlowEngine()

home = detector.detect("FC Barcelona")

away = detector.detect("Real Madrid CF")

tags = classifier.classify(home, away)

pprint(

    flow.analyse(

        home,

        away,

        tags

    )

)