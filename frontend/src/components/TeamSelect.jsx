import teams from "../constants/teams";

function TeamSelect({
  label,
  competition,
  value,
  onChange,
}) {
  const competitionTeams = teams[competition] || [];

  return (
    <div
      style={{
        marginBottom: "20px",
      }}
    >
      <label
        style={{
          display: "block",
          marginBottom: "8px",
        }}
      >
        {label}
      </label>

      <select
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        style={{
          width: "100%",
          padding: "12px",
          borderRadius: "8px",
          border: "1px solid #334155",
          background: "#0f172a",
          color: "white",
          fontSize: "15px",
          outline: "none",
        }}
      >
        {competitionTeams.map((team) => (
          <option
            key={team.id}
            value={team.id}
          >
            {team.name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default TeamSelect;