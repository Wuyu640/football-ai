from backend.engine.attack_engine import AttackEngine
from backend.engine.xg_engine import XGEngine
from backend.engine.xa_engine import XAEngine


class OffensiveQuality:

    def __init__(self):

        self.attack = AttackEngine()
        self.xg = XGEngine()
        self.xa = XAEngine()

    def analyse(self, team, analysis):

        attack = self.attack.analyse(team)

        xg = self.xg.calculate(analysis)

        xa = self.xa.calculate(attack)

        return {

            "attack": attack,

            "xg": xg,

            "xa": xa,

            "quality": round(

                attack["score"] * 0.45 +

                xa * 15 +

                xg["home_xg"] * 20,

                2

            )

        }