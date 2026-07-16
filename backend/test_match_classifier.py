from pprint import pprint

from backend.engine.identity_detector import IdentityDetector
from backend.intelligence.match_classifier import MatchClassifier

detector = IdentityDetector()

classifier = MatchClassifier()

home = detector.detect(
    "FC Barcelona"
)

away = detector.detect(
    "Real Madrid CF"
)

pprint(

    classifier.classify(
        home,
        away
    )

)