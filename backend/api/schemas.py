from pydantic import BaseModel


class PredictRequest(BaseModel):
    home: str
    away: str