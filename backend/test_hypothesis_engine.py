from pprint import pprint

from backend.engine.identity_detector import IdentityDetector

from backend.intelligence.hypothesis_engine import HypothesisEngine

detector = IdentityDetector()

engine = HypothesisEngine()

home = detector.detect("FC Barcelona")

away = detector.detect("Real Madrid CF")

pprint(

    engine.generate(

        home,

        away,

        {},

        {}

    )

)