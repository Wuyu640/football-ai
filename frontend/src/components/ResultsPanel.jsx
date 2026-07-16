import samplePrediction from "../data/samplePrediction";
import PredictionSection from "./PredictionSection";

function ResultsPanel() {
  return (
    <PredictionSection prediction={samplePrediction} />
  );
}

export default ResultsPanel;