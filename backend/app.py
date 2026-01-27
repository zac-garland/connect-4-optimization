from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

from core.inference import predict_move

app = FastAPI(
    title="Connect4 Backend",
    version="0.1"
)

class PredictRequest(BaseModel):
    board: List[List[int]] = Field(..., description="6x7 board with values -1, 0, 1")
    model_type: Literal["cnn", "transformer"] = "cnn"
    player: Literal[-1, 1] = 1

class PredictResponse(BaseModel):
    move: Optional[int]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        move = predict_move(
            board=req.board,
            model_type=req.model_type,
            player=req.player
        )
        return {"move": move}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
