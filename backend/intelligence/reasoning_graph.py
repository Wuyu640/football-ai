class ReasoningGraph:

    def analyse(self, features):

        graph = []

        for feature in features:

            if feature.name == "Attack":

                if feature.value >= 2:

                    graph.append({

                        "effect": "High scoring potential"

                    })

                elif feature.value >= 1.5:

                    graph.append({

                        "effect": "Good attack"

                    })

            if feature.name == "Defense":

                if feature.value < 0.8:

                    graph.append({

                        "effect": "Weak defense"

                    })

                elif feature.value >= 1.2:

                    graph.append({

                        "effect": "Solid defense"

                    })

            if feature.name == "Tempo":

                if feature.value >= 3:

                    graph.append({

                        "effect": "Open match"

                    })

                elif feature.value < 2:

                    graph.append({

                        "effect": "Slow match"

                    })

        return graph