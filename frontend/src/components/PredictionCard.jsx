function PredictionCard({ title, children }) {
  return (
    <div
      style={{
        backgroundColor: "#1f2937",
        borderRadius: "12px",
        padding: "20px",
        marginTop: "20px",
      }}
    >
      <h2
        style={{
          marginTop: 0,
          marginBottom: "15px",
        }}
      >
        {title}
      </h2>

      {children}
    </div>
  );
}

export default PredictionCard;