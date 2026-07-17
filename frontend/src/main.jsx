import { createRoot } from "react-dom/client";

document.body.style.background = "red";

createRoot(document.getElementById("root")).render(
  <h1 style={{ color: "yellow", fontSize: "80px" }}>
    PRUEBA 123
  </h1>
);
