from pprint import pprint

from backend.engine.identity_detector import IdentityDetector

from backend.intelligence.tactical_reasoner import TacticalReasoner

detector = IdentityDetector()

reasoner = TacticalReasoner()

home = detector.detect("FC Barcelona")

away = detector.detect("Real Madrid CF")

pprint(

    reasoner.analyse(

        home,

        away

    )

)