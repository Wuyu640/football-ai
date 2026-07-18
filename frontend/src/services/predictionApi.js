const API_URL =
  "https://studious-space-xylophone-vpprqwjxjx9x366j7-8000.app.github.dev";

export async function predictMatch(home, away) {
  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      home,
      away,
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(error);
  }

  return await response.json();
}