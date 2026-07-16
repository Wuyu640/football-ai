from pprint import pprint

from backend.intelligence.match_simulator import MatchSimulator

engine = MatchSimulator()

for _ in range(10):

    pprint(

        engine.simulate_match(

            2.1,

            1.6

        )

    )