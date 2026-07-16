from pprint import pprint

from backend.models.team_rating import TeamRating

from backend.intelligence.expected_goals_engine import ExpectedGoalsEngine

engine = ExpectedGoalsEngine()

home = TeamRating(

    attack=2.3,

    defense=1.8,

    form=0.8,

    home_attack=2.6,

    away_attack=2.0,

    home_defense=1.9,

    away_defense=1.7

)

away = TeamRating(

    attack=1.7,

    defense=1.5,

    form=0.6,

    home_attack=1.9,

    away_attack=1.4,

    home_defense=1.8,

    away_defense=1.6

)

pprint(

    engine.calculate(

        home,

        away

    )

)