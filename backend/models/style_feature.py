from dataclasses import dataclass


@dataclass
class StyleFeature:

    name: str

    value: float

    confidence: float

    evidence: list[str]