function ProbabilityRow({ label, value }) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "12px 0",
        borderBottom: "1px solid #334155",
      }}
    >
      <span
        style={{
          color: "white",
        }}
      >
        {label}
      </span>

      <strong
        style={{
          color: "#38bdf8",
          fontSize: "18px",
        }}
      >
        {value}
      </strong>
    </div>
  );
}

export default ProbabilityRow;
