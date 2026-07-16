class EvaluationReport:

    def build(

        self,

        evaluation

    ):

        report = []

        report.append("=== FOOTBALL AI REPORT ===")

        report.append("")

        report.append(

            f"Accuracy: {evaluation['accuracy']:.1%}"

        )

        report.append(

            f"Matches analysed: {evaluation['matches']}"

        )

        if "correct" in evaluation:

            report.append(

                f"Correct predictions: {evaluation['correct']}"

            )

        if "incorrect" in evaluation:

            report.append(

                f"Incorrect predictions: {evaluation['incorrect']}"

            )

        return report