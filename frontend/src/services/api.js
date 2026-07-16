const API_URL =
  "https://studious-space-xylophone-vpprqwjxjx9x366j7-5000.app.github.dev";

export async function checkApi() {
  const response = await fetch(API_URL);

  if (!response.ok) {
    throw new Error("No se pudo conectar con la API");
  }

  return await response.json();
}