class GoalFeatures:

    def calculate(

        self,

        played,

        goals_for,

        goals_against

    ):

        if played == 0:

            return {

                "goal_difference": 0,

                "goals_total": 0

            }

        return {

            "goal_difference":

                goals_for
                -
                goals_against,

            "goals_total":

                goals_for
                +
                goals_against

        }