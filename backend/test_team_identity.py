from backend.models.team_identity import TeamIdentity

identity = TeamIdentity(

    possession=65,

    pressing=8,

    transition_speed=7,

    defensive_line=8,

    width=7,

    build_up="Short",

    attack_focus="Central",

    tempo=8

)

print(identity)