class TeamComparator:

    def compare(

        self,

        home_features,

        away_features

    ):

        result = {}

        home = {

            feature.name: feature.value

            for feature in home_features

        }

        away = {

            feature.name: feature.value

            for feature in away_features

        }

        keys = set(home.keys()) | set(away.keys())

        for key in keys:

            result[key] = round(

                home.get(key, 0)

                -

                away.get(key, 0),

                2

            )

        return result