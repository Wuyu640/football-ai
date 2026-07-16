from pprint import pprint

from backend.engine.identity_detector import IdentityDetector
from backend.engine.matchup_engine import MatchupEngine

detector = IdentityDetector()

engine = MatchupEngine()

home = detector.detect("FC Barcelona")

away = detector.detect("Real Madrid CF")

result = engine.analyse(home, away)

print()

pprint(result)