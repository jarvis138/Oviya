# Oviya CSM TTS on RunPod

This repo wraps [Sesame CSM](https://github.com/SesameAILabs/csm) with FastAPI
so it can run as a TTS service on RunPod.

## Usage
POST /tts
```json
{ "text": "Hello Oviya", "voice": "neutral" }
