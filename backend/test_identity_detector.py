from pprint import pprint

from backend.engine.identity_detector import IdentityDetector

detector = IdentityDetector()

pprint(

    detector.detect(

        "FC Barcelona"

    )

)

print()

pprint(

    detector.detect(

        "Real Madrid CF"

    )

)