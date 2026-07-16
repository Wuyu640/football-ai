from backend.models.team_identity import TeamIdentity


class IdentityDetector:

    def detect(self, team):

        database = {

            "FC Barcelona": TeamIdentity(

                possession=67,

                pressing=9,

                transition_speed=7,

                defensive_line=9,

                width=8,

                build_up="Short",

                attack_focus="Central",

                tempo=8

            ),

            "Real Madrid CF": TeamIdentity(

                possession=58,

                pressing=7,

                transition_speed=10,

                defensive_line=7,

                width=8,

                build_up="Mixed",

                attack_focus="Transitions",

                tempo=9

            )

        }

        return database.get(

            team,

            TeamIdentity(

                possession=50,

                pressing=5,

                transition_speed=5,

                defensive_line=5,

                width=5,

                build_up="Mixed",

                attack_focus="Balanced",

                tempo=5

            )

        )