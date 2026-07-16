import json

from pathlib import Path

file = Path(
    "backend/knowledge/ontology/football_ontology.json"
)

with open(
    file,
    encoding="utf8"
) as f:

    ontology = json.load(f)

print()

print(ontology["high_press"])