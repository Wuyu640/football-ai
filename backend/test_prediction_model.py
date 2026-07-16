from backend.models.prediction import Prediction

prediction = Prediction(

    home_team="FC Barcelona",

    away_team="Real Madrid CF",

    home_xg=2.15,

    away_xg=1.38,

    home_probability=0.53,

    draw_probability=0.24,

    away_probability=0.23,

    btts=0.61,

    over25=0.67,

    top_scores=[

        ("2-1", 0.11),

        ("1-1", 0.09),

        ("2-0", 0.08)

    ]

)

print(prediction)