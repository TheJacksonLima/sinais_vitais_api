import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import time
import random

app = FastAPI()

start_time = time.time()

class ZumbiPayload(BaseModel):
    user_id: str
    status: str

def get_cycle_second():
    elapsed = time.time() - start_time
    return int(elapsed % 30)

@app.get("/")
async def root():
    return {"message": "API de sinais vitais ativa!"}

@app.get("/monitor")
async def monitor():
    sec = get_cycle_second()

    if sec < 15:
        bpm = random.randint(60, 80)
        spo2 = random.randint(95, 100)
        estado = "normal"

    elif sec < 25:
        bpm = random.randint(41, 49)
        spo2 = random.randint(81, 91)
        estado = "alerta"

    else:
        bpm = random.randint(30, 39)
        spo2 = random.randint(70, 79)
        estado = "zumbi"

    return {
        "bpm": bpm,
        "spo2": spo2,
        "estado": estado
    }

@app.post("/zumbi")
async def virou_zumbi(payload: ZumbiPayload):
    return {
        "message": "Status de zumbi registrado com sucesso.",
        "user_id": payload.user_id,
        "status": payload.status,
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
