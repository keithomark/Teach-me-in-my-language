from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.explain import generate_explanation
from app.services.translate import translate_text

router = APIRouter(prefix="/api")

class TopicRequest(BaseModel):
    topic: str

class TranslationRequest(BaseModel):
    text: str
    target_lang: str

@router.post("/explain")
async def explain_topic(request: TopicRequest):
    try:
        explanation = await generate_explanation(request.topic)
        return {"explanation": explanation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/translate")
async def translate(request: TranslationRequest):
    try:
        translated_text = await translate_text(request.text, request.target_lang)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 