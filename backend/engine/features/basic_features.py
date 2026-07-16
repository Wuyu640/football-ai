class BasicFeatures:

    def calculate(
        self,
        played,
        wins,
        draws,
        losses
    ):

        if played == 0:

            return {

                "points_per_game": 0,

                "win_rate": 0,

                "draw_rate": 0,

                "loss_rate": 0

            }

        return {

            "points_per_game":
                round(
                    (wins * 3 + draws) / played,
                    2
                ),

            "win_rate":
                round(
                    wins / played,
                    2
                ),

            "draw_rate":
                round(
                    draws / played,
                    2
                ),

            "loss_rate":
                round(
                    losses / played,
                    2
                )

        }