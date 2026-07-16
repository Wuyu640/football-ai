from backend.knowledge.feature_builder import FeatureBuilder

from backend.intelligence.team_comparator import TeamComparator

from backend.intelligence.advantage_engine import AdvantageEngine

from backend.intelligence.explanation_engine import ExplanationEngine


class UnifiedPredictionEngine:

    def __init__(self):

        self.builder = FeatureBuilder()

        self.compare = TeamComparator()

        self.advantage = AdvantageEngine()

        self.explain = ExplanationEngine()

    def analyse(

        self,

        home,

        away

    ):

        home_features = self.builder.build(home)

        away_features = self.builder.build(away)

        comparison = self.compare.compare(

            home_features,

            away_features

        )

        advantage = self.advantage.analyse(

            comparison

        )

        explanation = self.explain.explain(

            advantage

        )

        return {

            "home_features": home_features,

            "away_features": away_features,

            "comparison": comparison,

            "advantage": advantage,

            "explanation": explanation

        }