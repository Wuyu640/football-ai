from pprint import pprint

from backend.engine.match_analyzer import MatchAnalyzer
from backend.engine.offensive_quality import OffensiveQuality

analysis = MatchAnalyzer().analyse(

    "FC Barcelona",

    "Real Madrid CF"

)

engine = OffensiveQuality()

pprint(

    engine.analyse(

        "FC Barcelona",

        analysis

    )

)