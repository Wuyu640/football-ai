class ContextEngine:

    HOME_ADVANTAGE = 0.18

    def analyse(self, home, away):

        return {

            "home_advantage": self.HOME_ADVANTAGE,

            # Se implementará con calendario
            "travel_penalty": 0.00,

            # Se implementará con competiciones
            "motivation": 0.00,

            # Se implementará con calendario
            "rest_advantage": 0.00,

            # Se implementará con API meteorológica
            "weather": 0.00,

            # Nuevos campos
            "altitude": 0.00,

            "crowd": 0.10,

            "pitch": 0.00

        }