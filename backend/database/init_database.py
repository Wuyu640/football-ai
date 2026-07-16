from backend.database.database import Database

db = Database()

db.execute("""
CREATE TABLE IF NOT EXISTS matches (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    utc_date TEXT,

    competition TEXT,

    home_team TEXT,

    away_team TEXT,

    home_goals INTEGER,

    away_goals INTEGER

)
""")

print("Database creada correctamente.")