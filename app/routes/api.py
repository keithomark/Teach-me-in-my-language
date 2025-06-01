from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.explain import generate_explanation
from app.services.translate import translate_text
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api")

class TopicRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=500, description="The topic to explain")

class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to translate")
    target_lang: str = Field(..., description="The target language code")

@router.post("/explain")
async def explain_topic(request: TopicRequest):
    try:
        logger.info(f"Generating explanation for topic: {request.topic}")
        explanation = await generate_explanation(request.topic)
        if not explanation:
            raise HTTPException(status_code=500, detail="Failed to generate explanation")
        return {"explanation": explanation}
    except Exception as e:
        logger.error(f"Error generating explanation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/translate")
async def translate(request: TranslationRequest):
    try:
        logger.info(f"Translating text to {request.target_lang}")
        translated_text = await translate_text(request.text, request.target_lang)
        if not translated_text:
            raise HTTPException(status_code=500, detail="Failed to translate text")
        return {"translated_text": translated_text}
    except Exception as e:
        logger.error(f"Error translating text: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 