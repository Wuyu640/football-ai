from backend.models.tactical_profile import TacticalProfile


class TacticalEngine:

    def profile(self, team):

        defaults = TacticalProfile(

            formation="4-3-3",

            style="Balanced",

            pressing="Medium",

            tempo="Medium",

            possession=50,

            defensive_line="Medium",

            width="Medium",

            transitions="Medium",

            crossing="Medium",

            long_balls=False,

            counter_attack=False,

            set_pieces=5

        )

        database = {

            "FC Barcelona": TacticalProfile(

                formation="4-3-3",

                style="Possession",

                pressing="High",

                tempo="High",

                possession=66,

                defensive_line="High",

                width="Wide",

                transitions="Medium",

                crossing="Low",

                long_balls=False,

                counter_attack=False,

                set_pieces=8

            ),

            "Real Madrid CF": TacticalProfile(

                formation="4-4-2",

                style="Transition",

                pressing="Medium",

                tempo="High",

                possession=57,

                defensive_line="Medium",

                width="Wide",

                transitions="Very High",

                crossing="Medium",

                long_balls=False,

                counter_attack=True,

                set_pieces=8

            )

        }

        return database.get(team, defaults)