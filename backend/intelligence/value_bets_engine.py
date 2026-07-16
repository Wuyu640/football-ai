class ValueBetsEngine:

    def analyse(

        self,

        model,

        bookmaker

    ):

        value = {}

        for market in model:

            if market not in bookmaker:

                continue

            edge = model[market] - bookmaker[market]

            value[market] = {

                "edge": round(edge, 3),

                "value": edge > 0.05

            }

        return value