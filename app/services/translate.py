import httpx
import logging
import os
from dotenv import load_dotenv

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# HuggingFace API key
HF_API_KEY = os.getenv("HF_API_KEY")

# Model mapping for different languages
MODEL_MAPPING = {
    "hindi": "Helsinki-NLP/opus-mt-en-hi",
    "tamil": "Helsinki-NLP/opus-mt-en-ta",
    "telugu": "Helsinki-NLP/opus-mt-en-te",
    "bengali": "Helsinki-NLP/opus-mt-en-bn",
    "marathi": "Helsinki-NLP/opus-mt-en-mr",
    "kannada": "Helsinki-NLP/opus-mt-en-kn",
    "gujarati": "Helsinki-NLP/opus-mt-en-gu",
    "malayalam": "Helsinki-NLP/opus-mt-en-ml"
}

async def translate_text(text: str, target_lang: str) -> str:
    """
    Translate text to the target Indian language using HuggingFace's Inference API.
    """
    try:
        if not HF_API_KEY:
            return "Error: HuggingFace API key not found. Please set the HF_API_KEY environment variable."
            
        target_lang = target_lang.lower()
        
        if target_lang not in MODEL_MAPPING:
            return f"Translation service is not available for {target_lang}. Please try another language."
            
        model_id = MODEL_MAPPING[target_lang]
        api_url = f"https://api-inference.huggingface.co/models/{model_id}"
        
        headers = {
            "Authorization": f"Bearer {HF_API_KEY}",
            "Content-Type": "application/json"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                api_url,
                headers=headers,
                json={
                    "inputs": text,
                    "parameters": {
                        "max_length": 512,
                        "return_tensors": "pt"
                    }
                },
                timeout=60.0  # Increased timeout
            )
            
            if response.status_code == 401:
                logger.error("Invalid HuggingFace API key")
                return "Error: Invalid API key. Please check your HuggingFace API key."
            elif response.status_code != 200:
                logger.error(f"HuggingFace API error: {response.text}")
                return f"Error: Failed to translate. Status code: {response.status_code}"
                
            result = response.json()
            if not result or not isinstance(result, list) or not result[0].get("translation_text"):
                logger.error("Empty response from HuggingFace API")
                return "Error: Empty response from API. Please try again."
                
            return result[0]["translation_text"]
            
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return f"Error: {str(e)}" 