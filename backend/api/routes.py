from fastapi import APIRouter

from backend.api.schemas import PredictRequest
from backend.data_engine.mock_provider import MockProvider
from backend.engine.prediction_engine import PredictionEngine

router = APIRouter()

provider = MockProvider()
engine = PredictionEngine()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "project": "Football AI"
    }


@router.get("/version")
def version():
    return {
        "version": "1.0.0"
    }


@router.post("/predict")
def predict(data: PredictRequest):

    match = provider.get_match(
        data.home,
        data.away
    )

    return engine.predict(match)