function SummaryCard({ summary }) {
  return (
    <div
      style={{
        background: "#1e293b",
        borderRadius: "16px",
        padding: "20px",
        marginBottom: "20px",
      }}
    >
      <h2
        style={{
          marginBottom: "15px",
          fontSize: "20px",
          color: "white",
        }}
      >
        Resumen del partido
      </h2>

      <p
        style={{
          color: "#cbd5e1",
          lineHeight: "1.7",
          margin: 0,
        }}
      >
        {summary}
      </p>
    </div>
  );
}

export default SummaryCard;
