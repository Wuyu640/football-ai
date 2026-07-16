class TacticalReasoner:

    def analyse(

        self,

        home_identity,

        away_identity

    ):

        conclusions = []

        # Presión alta contra salida corta

        if (

            home_identity.pressing >= 8

            and

            away_identity.build_up == "Short"

        ):

            conclusions.append({

                "importance": 9,

                "title": "Presión alta",

                "description":

                "El equipo local puede provocar pérdidas peligrosas."

            })

        # Transiciones rápidas

        if (

            away_identity.transition_speed >= 8

            and

            home_identity.defensive_line >= 8

        ):

            conclusions.append({

                "importance": 8,

                "title": "Espacios a la espalda",

                "description":

                "El visitante puede aprovechar la espalda de la defensa."

            })

        conclusions.sort(

            key=lambda x: x["importance"],

            reverse=True

        )

        return conclusions