from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/twilio/voice")
async def twilio_voice(request: Request):
    vr = VoiceResponse()
    vr.say("Hello. This is Athena voice patient tester. Your setup is working.", voice="alice")
    return Response(content=str(vr), media_type="application/xml")
