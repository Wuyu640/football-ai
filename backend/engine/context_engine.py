from __future__ import annotations


class ContextEngine:

    HOME_ADVANTAGE = 0.18
    CROWD_ADVANTAGE = 0.10

    def analyse(
        self,
        home: str,
        away: str,
    ):

        return {

            "home_advantage": self.HOME_ADVANTAGE,

            "travel_penalty": 0.00,

            "motivation": 0.00,

            "rest_advantage": 0.00,

            "weather": 0.00,

            "altitude": 0.00,

            "crowd": self.CROWD_ADVANTAGE,

            "pitch": 0.00,

            "total_context": round(
                self.HOME_ADVANTAGE
                + self.CROWD_ADVANTAGE,
                2,
            ),

        }