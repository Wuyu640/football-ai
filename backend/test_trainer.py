from pprint import pprint

from backend.training.trainer import Trainer


trainer = Trainer()

print("\nPESOS INICIALES\n")

pprint(
    trainer.train()
)

trainer.update_weight(
    "recent_attack",
    5
)

print("\nPESO MODIFICADO\n")

print(
    trainer.get_weight(
        "recent_attack"
    )
)

trainer.reset()

print("\nTRAS RESET\n")

print(
    trainer.get_weight(
        "recent_attack"
    )
)