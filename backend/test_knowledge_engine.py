from pprint import pprint

from backend.engine.knowledge_engine import KnowledgeEngine

engine = KnowledgeEngine()

print()

print(engine.exists("FC Barcelona"))

print()

pprint(

    engine.get_team(

        "FC Barcelona"

    )

)