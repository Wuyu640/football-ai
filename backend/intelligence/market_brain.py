class MarketBrain:

    def analyse(self, market):

        score = 0
        reasons = []

        movement = market.get("movement", 0)
        value = market.get("value", 0)

        score += movement * 5
        score += value * 5

        return {

            "score": round(score, 2),

            "reasons": reasons

        }