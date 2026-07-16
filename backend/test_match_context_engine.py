from pprint import pprint

from backend.intelligence.match_context_engine import MatchContextEngine

engine = MatchContextEngine()

context = {

    "must_win": True,

    "knockout": False,

    "second_leg": False,

    "derby": True,

    "bad_weather": False

}

pprint(

    engine.analyse(

        context

    )

)