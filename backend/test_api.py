from backend.data_engine.client import FootballDataClient

client = FootballDataClient()

# Equipo 81 = FC Barcelona
team = client.get("teams/81")

print("Nombre:", team["name"])
print("Fundación:", team["founded"])
print("Estadio:", team["venue"])
print("Entrenador:", team["coach"]["name"])

print("\nÚltimos jugadores:")

for player in team["squad"][:10]:
    print("-", player["name"], "-", player["position"])