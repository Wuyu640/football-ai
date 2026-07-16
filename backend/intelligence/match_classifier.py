class MatchClassifier:

    def classify(
        self,
        home,
        away
    ):

        tags = []

        if (
            home.possession >= 60
            and
            away.possession >= 55
        ):

            tags.append(
                "POSSESSION_BATTLE"
            )

        if (
            home.transition_speed >= 8
            or
            away.transition_speed >= 8
        ):

            tags.append(
                "HIGH_TRANSITIONS"
            )

        if (
            home.pressing >= 8
            and
            away.pressing >= 8
        ):

            tags.append(
                "HIGH_PRESS"
            )

        if (
            home.tempo >= 8
            and
            away.tempo >= 8
        ):

            tags.append(
                "HIGH_TEMPO"
            )

        if not tags:

            tags.append(
                "BALANCED_MATCH"
            )

        return tags