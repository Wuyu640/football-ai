import json
from pathlib import Path

file = Path(
    "backend/knowledge/database/coaches.json"
)

with open(
    file,
    encoding="utf8"
) as f:

    coaches = json.load(f)

print()

print(coaches["Hansi Flick"])