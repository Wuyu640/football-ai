function ResultCard({ label, value }) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "8px 0",
        borderBottom: "1px solid #374151",
      }}
    >
      <span>{label}</span>

      <strong>{value}</strong>
    </div>
  );
}

export default ResultCard;