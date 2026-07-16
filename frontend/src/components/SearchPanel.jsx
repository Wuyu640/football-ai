import { useEffect, useState } from "react";
import CompetitionSelect from "./CompetitionSelect";
import TeamSelect from "./TeamSelect";
import MatchRequest from "../models/MatchRequest";
import teams from "../constants/teams";

function SearchPanel() {
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

  function handleAnalyse() {
    const request = new MatchRequest(
      homeTeamId,
      awayTeamId
    );

    request.competition = competition;

    console.log(request);
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
