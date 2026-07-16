from backend.engine.core_engine import CoreEngine
from backend.engine.schedule_strength import ScheduleStrength
from backend.engine.simulation_engine import SimulationEngine


class FootballBrain:

    def __init__(self):

        self.core = CoreEngine()
        self.schedule = ScheduleStrength()
        self.simulation = SimulationEngine()

    def analyse(self, home, away):

        core = self.core.analyse(home, away)

        home_schedule = self.schedule.analyse(home)
        away_schedule = self.schedule.analyse(away)

        simulation = self.simulation.simulate(
            core["prediction"]["xg"]
        )

        return {

            "match": core["match"],

            "prediction": core["prediction"],

            "context": core["context"],

            "injuries": core["injuries"],

            "intelligence": core["intelligence"],

            "schedule": {

                "home": home_schedule,

                "away": away_schedule

            },

            "simulation": simulation

        }