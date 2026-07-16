function Navbar() {
  return (
    <header
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "20px 30px",
        background: "#111827",
        borderRadius: "12px",
        marginBottom: "30px",
      }}
    >
      <h1
        style={{
          margin: 0,
          color: "white",
        }}
      >
        ⚽ Football AI
      </h1>

      <span
        style={{
          color: "#9ca3af",
          fontSize: "14px",
        }}
      >
        AI Match Prediction
      </span>
    </header>
  );
}

export default Navbar;