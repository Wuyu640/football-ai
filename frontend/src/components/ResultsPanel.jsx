import samplePrediction from "../data/samplePrediction";
import PredictionSection from "./PredictionSection";

function ResultsPanel({ prediction }) {
  const data = prediction || samplePrediction;

  return (
    <PredictionSection prediction={data} />
  );
}

export default ResultsPanel;