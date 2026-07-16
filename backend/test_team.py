from backend.data_engine.team_stats import TeamStats

team = TeamStats()

data = team.get_team(81)

print("Nombre:", data["name"])
print("Fundación:", data["founded"])
print("Estadio:", data["venue"])

print("\nPrimeros jugadores:")

for player in data["squad"][:10]:
    print("-", player["name"], "-", player["position"])