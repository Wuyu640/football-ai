from pprint import pprint

from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.prediction_engine import PredictionEngine
from backend.engine.simulation_engine import SimulationEngine
from backend.engine.calibration_engine import CalibrationEngine

analysis = MatchAnalyzer().analyse(
    "FC Barcelona",
    "Real Madrid CF"
)

prediction = PredictionEngine().predict(
    "FC Barcelona",
    "Real Madrid CF"
)

simulation = SimulationEngine().simulate(
    analysis
)

result = CalibrationEngine().calibrate(
    prediction,
    simulation
)

pprint(result)