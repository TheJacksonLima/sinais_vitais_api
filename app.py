from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


class ZumbiPayload(BaseModel):
    user_id: str
    status: str  # ex: "zumbi"


@app.get("/")
async def root():
    return {"message": "API de sinais vitais ativa!"}


@app.get("/alerta")
async def alerta():
    bpm = random.randint(41, 49)
    spo2 = random.randint(81, 91)

    return {
        "bpm": bpm,
        "spo2": spo2,
        "estado": "alerta"
    }


@app.post("/zumbi")
async def virou_zumbi(payload: ZumbiPayload):
    return {
        "message": "Status de zumbi registrado com sucesso.",
        "user_id": payload.user_id,
        "status": payload.status,
    }
