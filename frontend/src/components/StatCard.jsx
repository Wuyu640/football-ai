function StatCard({ title, children }) {
  return (
    <div
      style={{
        background: "#1e293b",
        borderRadius: "16px",
        padding: "20px",
        marginTop: "20px",
      }}
    >
      <h2
        style={{
          marginBottom: "20px",
          fontSize: "20px",
          color: "white",
        }}
      >
        {title}
      </h2>

      {children}
    </div>
  );
}

export default StatCard;
