import StatCard from "./StatCard";
import ProbabilityRow from "./ProbabilityRow";
import SummaryCard from "./SummaryCard";

function PredictionSection({ prediction }) {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(2, 1fr)",
        gap: "20px",
      }}
    >
      <div style={{ gridColumn: "1 / -1" }}>
        <SummaryCard summary={prediction.summary} />
      </div>

      <StatCard title="Probabilidades (1X2)">
        <ProbabilityRow
          label="1 - Local"
          value={`${prediction.probabilities.home}%`}
        />
        <ProbabilityRow
          label="X - Empate"
          value={`${prediction.probabilities.draw}%`}
        />
        <ProbabilityRow
          label="2 - Visitante"
          value={`${prediction.probabilities.away}%`}
        />
      </StatCard>

      <StatCard title="Expected Goals">
        <ProbabilityRow
          label={prediction.homeTeam}
          value={prediction.xg.home}
        />
        <ProbabilityRow
          label={prediction.awayTeam}
          value={prediction.xg.away}
        />
      </StatCard>

      <StatCard title="Ambos marcan">
        <ProbabilityRow
          label="Sí"
          value={`${prediction.btts.yes}%`}
        />
        <ProbabilityRow
          label="No"
          value={`${prediction.btts.no}%`}
        />
      </StatCard>

      <StatCard title="Marcadores más probables">
        {prediction.scorelines.map((score, index) => (
          <ProbabilityRow
            key={score}
            label={`${index + 1}º`}
            value={score}
          />
        ))}
      </StatCard>
    </div>
  );
}

export default PredictionSection;
