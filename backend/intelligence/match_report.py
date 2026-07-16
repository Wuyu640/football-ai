class MatchReport:

    def build(

        self,

        result

    ):

        report = []

        report.append("=== MATCH REPORT ===")

        report.extend(

            result["explanation"]

        )

        report.append("")

        report.append("Feature comparison:")

        for feature, value in result["comparison"].items():

            report.append(

                f"{feature}: {value:+.2f}"

            )

        return report