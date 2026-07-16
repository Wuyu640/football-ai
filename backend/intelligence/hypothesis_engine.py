class HypothesisEngine:

    def generate(

        self,

        home,

        away,

        matchup,

        context

    ):

        hypotheses = []

        if home.possession > away.possession:

            hypotheses.append({

                "title":
                "Dominio local",

                "confidence": 0.75

            })

        if away.transition_speed > 8:

            hypotheses.append({

                "title":
                "Contraataques visitantes",

                "confidence": 0.68

            })

        if context.get("must_win"):

            hypotheses.append({

                "title":
                "Partido abierto",

                "confidence": 0.60

            })

        return hypotheses