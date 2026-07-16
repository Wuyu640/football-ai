class MatchNarrative:

    def build(

        self,

        graph

    ):

        text = []

        for node in graph:

            text.append(

                f"{node['cause']} -> {node['effect']}"

            )

        return text