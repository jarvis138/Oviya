from fastapi import FastAPI
from pydantic import BaseModel
import torch
from csm import CSMModel
import base64, io, soundfile as sf

app = FastAPI()

# Load CSM model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CSMModel.from_pretrained("sesame-ai/csm-small").to(device)

class TTSRequest(BaseModel):
    text: str
    voice: str = "neutral"

@app.post("/tts")
async def generate_tts(req: TTSRequest):
    wav = model.tts(req.text, voice=req.voice).cpu().numpy()

    buf = io.BytesIO()
    sf.write(buf, wav, 22050, format="WAV")
    audio_bytes = buf.getvalue()

    return {
        "audio_base64": base64.b64encode(audio_bytes).decode("utf-8"),
        "sample_rate": 22050
    }
