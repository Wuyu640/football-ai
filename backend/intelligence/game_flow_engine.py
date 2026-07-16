class GameFlowEngine:

    def analyse(

        self,

        home,

        away,

        match_tags

    ):

        flow = []

        # Inicio

        if "HIGH_PRESS" in match_tags:

            flow.append({

                "minute": "0-15",

                "description":
                "Inicio muy intenso con presión alta de ambos equipos."

            })

        else:

            flow.append({

                "minute": "0-15",

                "description":
                "Inicio prudente mientras ambos equipos se estudian."

            })

        # Mitad

        if home.possession > away.possession:

            flow.append({

                "minute": "15-45",

                "description":
                "El equipo local tenderá a controlar la posesión."

            })

        else:

            flow.append({

                "minute": "15-45",

                "description":
                "El visitante puede equilibrar o dominar fases del balón."

            })

        # Segunda parte

        if "HIGH_TRANSITIONS" in match_tags:

            flow.append({

                "minute": "45-75",

                "description":
                "Las transiciones ganarán protagonismo."

            })

        else:

            flow.append({

                "minute": "45-75",

                "description":
                "Partido relativamente estable tácticamente."

            })

        # Final

        flow.append({

            "minute": "75-90",

            "description":
            "El contexto del marcador influirá en el ritmo final."

        })

        return flow