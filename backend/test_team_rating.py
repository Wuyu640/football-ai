from backend.models.team_rating import TeamRating

rating = TeamRating(

    attack=2.2,

    defense=1.8,

    form=0.75,

    home_attack=2.5,

    away_attack=1.9,

    home_defense=1.6,

    away_defense=2.0

)

print(rating)