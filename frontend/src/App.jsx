import SearchPanel from "./components/SearchPanel";
import ResultsPanel from "./components/ResultsPanel";

function App() {
  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#07111f",
        padding: "40px 30px",
        fontFamily:
          "Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      }}
    >
      <div
        style={{
          maxWidth: "1400px",
          margin: "0 auto",
        }}
      >
        <div
          style={{
            textAlign: "center",
            marginBottom: "45px",
          }}
        >
          <h1
            style={{
              color: "white",
              fontSize: "46px",
              margin: 0,
              fontWeight: "800",
              letterSpacing: "-1px",
            }}
          >
            VARGPT
          </h1>

          <p
            style={{
              color: "#94a3b8",
              fontSize: "18px",
              marginTop: "12px",
              marginBottom: 0,
            }}
          >
            El 0-0 no existe.
          </p>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "360px 1fr",
            gap: "30px",
            alignItems: "start",
          }}
        >
          <SearchPanel />

          <ResultsPanel />
        </div>
      </div>
    </div>
  );
}

export default App;
