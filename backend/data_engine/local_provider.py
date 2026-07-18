from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class LocalProvider:
    def __init__(self, base_path: str = "backend/data/seasons"):
        self.base = Path(base_path)
        self.base.mkdir(parents=True, exist_ok=True)

    def _path(self, league: str, season: int) -> Path:
        return self.base / f"{league}_{season}.json"

    def exists(self, league: str, season: int) -> bool:
        return self._path(league, season).exists()

    def load(self, league: str, season: int) -> list[dict[str, Any]]:
        path = self._path(league, season)

        if not path.exists():
            return []

        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def save(
        self,
        league: str,
        season: int,
        matches: list[dict[str, Any]],
    ) -> None:
        with self._path(league, season).open("w", encoding="utf-8") as f:
            json.dump(matches, f, ensure_ascii=False, indent=2)