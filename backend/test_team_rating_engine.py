from pprint import pprint

from backend.intelligence.team_rating_engine import TeamRatingEngine

engine = TeamRatingEngine()

pprint(

    engine.analyse(

        "FC Barcelona"

    )

)