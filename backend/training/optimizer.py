from copy import deepcopy


class Optimizer:

    def improve(self, weights, name, delta):

        new_weights = deepcopy(weights)

        new_weights[name] += delta

        return new_weights