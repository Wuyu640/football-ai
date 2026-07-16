from pprint import pprint

from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.simulation_engine import SimulationEngine

analysis = MatchAnalyzer().analyse(
    "FC Barcelona",
    "Real Madrid CF"
)

result = SimulationEngine().simulate(analysis)

pprint(result)
