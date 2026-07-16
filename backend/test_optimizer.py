from pprint import pprint

from backend.config.tactical_weights import TACTICAL_WEIGHTS
from backend.training.optimizer import Optimizer

optimizer = Optimizer()

new_weights = optimizer.improve(
    TACTICAL_WEIGHTS,
    "recent_attack",
    0.5
)

print("Original")

pprint(TACTICAL_WEIGHTS)

print()

print("Nuevo")

pprint(new_weights)