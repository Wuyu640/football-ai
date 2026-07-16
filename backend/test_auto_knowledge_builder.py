from pprint import pprint

from backend.knowledge.auto_knowledge_builder import AutoKnowledgeBuilder

builder = AutoKnowledgeBuilder()

identity = builder.build("FC Barcelona")

print()

pprint(identity)