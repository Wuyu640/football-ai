from pprint import pprint

from backend.models.team_rating import TeamRating

from backend.intelligence.match_adjustment_engine import MatchAdjustmentEngine

engine = MatchAdjustmentEngine()

home = TeamRating(

    attack=2.3,

    defense=1.8,

    form=0.8,

    home_attack=2.6,

    away_attack=2.0,

    home_defense=1.8,

    away_defense=1.7

)

away = TeamRating(

    attack=1.7,

    defense=1.6,

    form=0.7,

    home_attack=1.8,

    away_attack=1.5,

    home_defense=1.9,

    away_defense=1.7

)

pprint(

    engine.adjust(

        2.10,

        1.35,

        home,

        away

    )

)