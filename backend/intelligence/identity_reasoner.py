class IdentityReasoner:

    def analyse(

        self,

        features

    ):

        identity = {}

        for feature in features:

            if feature.name == "Attack":

                if feature.value >= 2:

                    identity["attack"] = "Elite"

                elif feature.value >= 1.5:

                    identity["attack"] = "Strong"

                else:

                    identity["attack"] = "Average"

            if feature.name == "Defense":

                if feature.value >= 1.2:

                    identity["defense"] = "Elite"

                elif feature.value >= 0.8:

                    identity["defense"] = "Strong"

                else:

                    identity["defense"] = "Weak"

            if feature.name == "Tempo":

                if feature.value >= 3:

                    identity["tempo"] = "High"

                elif feature.value >= 2:

                    identity["tempo"] = "Medium"

                else:

                    identity["tempo"] = "Low"

        return identity