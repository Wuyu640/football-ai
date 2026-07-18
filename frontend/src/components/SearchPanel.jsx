import { useEffect, useState } from "react";
import CompetitionSelect from "./CompetitionSelect";
import TeamSelect from "./TeamSelect";
import teams from "../constants/teams";
import { predictMatch } from "../services/predictionApi";

function SearchPanel({ onPrediction }) {
  const [competition, setCompetition] = useState("LaLiga EA Sports");

  const [homeTeamId, setHomeTeamId] = useState(
    teams["LaLiga EA Sports"][0].id
  );

  const [awayTeamId, setAwayTeamId] = useState(
    teams["LaLiga EA Sports"][1].id
  );

  useEffect(() => {
    const competitionTeams = teams[competition] || [];

    if (competitionTeams.length >= 2) {
      setHomeTeamId(competitionTeams[0].id);
      setAwayTeamId(competitionTeams[1].id);
    } else if (competitionTeams.length === 1) {
      setHomeTeamId(competitionTeams[0].id);
      setAwayTeamId(competitionTeams[0].id);
    } else {
      setHomeTeamId("");
      setAwayTeamId("");
    }
  }, [competition]);

  async function handleAnalyse() {
    try {
      const competitionTeams = teams[competition] || [];

      const homeTeam = competitionTeams.find(
        (team) => team.id === Number(homeTeamId)
      );

      const awayTeam = competitionTeams.find(
        (team) => team.id === Number(awayTeamId)
      );

      if (!homeTeam || !awayTeam) {
        alert("Selecciona dos equipos.");
        return;
      }

      const result = await predictMatch(
        homeTeam.name,
        awayTeam.name
      );

      const prediction = {
        homeTeam: homeTeam.name,

        awayTeam: awayTeam.name,

        probabilities: {
          home: Math.round(result.probabilities.home * 100),
          draw: Math.round(result.probabilities.draw * 100),
          away: Math.round(result.probabilities.away * 100),
        },

        xg: {
          home: Number(result.xg.home_xg).toFixed(2),
          away: Number(result.xg.away_xg).toFixed(2),
        },

        btts: {
          yes: "-",
          no: "-",
        },

        over25: "-",

        scorelines: result.scores.map(
          (score) =>
            `${score.score} (${Math.round(
              score.probability * 100
            )}%)`
        ),

        summary:
          "Predicción generada automáticamente por VARGPT.",
      };

      onPrediction(prediction);
    } catch (error) {
      console.error(error);
      alert("No se pudo obtener la predicción.");
    }
  }

  return (
    <div
      style={{
        background: "#1e293b",
        borderRadius: "16px",
        padding: "25px",
      }}
    >
      <h2
        style={{
          marginBottom: "25px",
        }}
      >
        Analizar partido
      </h2>

      <CompetitionSelect
        value={competition}
        onChange={setCompetition}
      />

      <TeamSelect
        label="Equipo local"
        competition={competition}
        value={homeTeamId}
        onChange={setHomeTeamId}
      />

      <TeamSelect
        label="Equipo visitante"
        competition={competition}
        value={awayTeamId}
        onChange={setAwayTeamId}
      />

      <button
        onClick={handleAnalyse}
        style={{
          width: "100%",
          padding: "15px",
          background: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "10px",
          cursor: "pointer",
          fontSize: "16px",
          marginTop: "10px",
        }}
      >
        Analizar
      </button>
    </div>
  );
}

export default SearchPanel;