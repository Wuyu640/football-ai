from backend.engine.match_intelligence import MatchIntelligence
from backend.engine.prediction_engine import PredictionEngine
from backend.engine.context_engine import ContextEngine
from backend.engine.injuries_engine import InjuriesEngine
from backend.engine.calibration_engine import CalibrationEngine
from backend.engine.confidence_engine import ConfidenceEngine

from backend.intelligence.tactical_brain import TacticalBrain
from backend.intelligence.context_brain import ContextBrain
from backend.intelligence.player_brain import PlayerBrain
from backend.intelligence.coach_brain import CoachBrain
from backend.intelligence.market_brain import MarketBrain
from backend.intelligence.decision_brain import DecisionBrain


class CoreEngine:

    def __init__(self):

        self.intelligence = MatchIntelligence()
        self.prediction = PredictionEngine()
        self.context = ContextEngine()
        self.injuries = InjuriesEngine()
        self.calibration = CalibrationEngine()
        self.confidence = ConfidenceEngine()

        self.tactical_brain = TacticalBrain()
        self.context_brain = ContextBrain()
        self.player_brain = PlayerBrain()
        self.coach_brain = CoachBrain()
        self.market_brain = MarketBrain()
        self.decision_brain = DecisionBrain()

    def analyse(self, home, away):

        intelligence = self.intelligence.analyse(home, away)

        prediction = self.prediction.predict(home, away)

        calibrated = self.calibration.calibrate(
            prediction["probabilities"]
        )

        confidence = self.confidence.analyse(
            prediction
        )

        context = self.context.analyse(home, away)

        injuries = self.injuries.analyse(home, away)

        tactical = self.tactical_brain.analyse(
            intelligence["home_style"],
            intelligence["away_style"]
        )

        context_analysis = self.context_brain.analyse(
            context
        )

        player_analysis = self.player_brain.analyse(
            injuries
        )

        coach_analysis = self.coach_brain.analyse({})

        market_analysis = self.market_brain.analyse({})

        brains = {

            "tactical": tactical,

            "context": context_analysis,

            "player": player_analysis,

            "coach": coach_analysis,

            "market": market_analysis

        }

        decision = self.decision_brain.analyse(
            brains
        )

        return {

            "match": {
                "home": home,
                "away": away
            },

            "context": context,

            "injuries": injuries,

            "intelligence": intelligence,

            "prediction": prediction,

            "calibrated": calibrated,

            "confidence": confidence,

            "brains": brains,

            "decision": decision

        }