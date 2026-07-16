from backend.config.tactical_rules import TACTICAL_RULES


class MatchupEngine:

    def analyse(self, home, away):

        score = 0

        reasons = []

        for rule in TACTICAL_RULES:

            condition = rule["if"]

            apply = True

            if "pressing" in condition:

                if home.pressing < condition["pressing"]:

                    apply = False

            if "build_up" in condition:

                if away.build_up != condition["build_up"]:

                    apply = False

            if "transition_speed" in condition:

                if home.transition_speed < condition["transition_speed"]:

                    apply = False

            if "defensive_line" in condition:

                if away.defensive_line < condition["defensive_line"]:

                    apply = False

            if apply:

                score += rule["score"]

                reasons.append(rule["reason"])

        return {

            "score": round(score, 2),

            "reasons": reasons

        }