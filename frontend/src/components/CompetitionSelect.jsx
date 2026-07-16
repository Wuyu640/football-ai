import competitions from "../constants/competitions";

function CompetitionSelect({ value, onChange }) {
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
        Competición
      </label>

      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        style={{
          width: "100%",
          padding: "12px",
          borderRadius: "8px",
          border: "1px solid #334155",
          background: "#0f172a",
          color: "white",
          fontSize: "15px",
        }}
      >
        {competitions.map((competition) => (
          <option key={competition} value={competition}>
            {competition}
          </option>
        ))}
      </select>
    </div>
  );
}

export default CompetitionSelect;