import SearchPanel from "./components/SearchPanel";
import ResultsPanel from "./components/ResultsPanel";

function App() {
  return (
    <div
      style={{
        maxWidth: "1200px",
        margin: "40px auto",
        padding: "20px",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          color: "white",
          marginBottom: "40px",
        }}
      >
        ⚽ Football AI
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "360px 1fr",
          gap: "25px",
        }}
      >
        <SearchPanel />

        <ResultsPanel />
      </div>
    </div>
  );
}

export default App;