import random


class MatchSimulator:

    def simulate_goal_count(

        self,

        attack,

        defense

    ):

        mean = (

            attack

            +

            defense

        ) / 2

        goals = round(

            random.gauss(

                mean,

                0.8

            )

        )

        return max(

            goals,

            0

        )

    def simulate_match(

        self,

        home_attack,

        away_attack

    ):

        home = self.simulate_goal_count(

            home_attack,

            away_attack

        )

        away = self.simulate_goal_count(

            away_attack,

            home_attack

        )

        return {

            "home": home,

            "away": away

        }