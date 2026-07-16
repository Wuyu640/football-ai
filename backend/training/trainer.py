from copy import deepcopy

from backend.config.tactical_weights import TACTICAL_WEIGHTS


class Trainer:

    def __init__(self):

        self.weights = deepcopy(TACTICAL_WEIGHTS)

    def train(self):

        return self.weights

    def update_weight(self, name, value):

        if name not in self.weights:
            raise ValueError(
                f"Peso desconocido: {name}"
            )

        self.weights[name] = value

    def reset(self):

        self.weights = deepcopy(
            TACTICAL_WEIGHTS
        )

    def get_weight(self, name):

        return self.weights.get(name)