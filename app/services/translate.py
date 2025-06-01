from transformers import pipeline
import torch
from typing import Dict
import os

# Initialize the translator with error handling
try:
    # Set cache directory to avoid permission issues
    cache_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "model_cache")
    os.makedirs(cache_dir, exist_ok=True)
    
    # Initialize the translator
    translator = pipeline(
        "translation",
        model="ai4bharat/indictrans2-en-indic",
        device=0 if torch.cuda.is_available() else -1,
        cache_dir=cache_dir
    )
except Exception as e:
    print(f"Error loading translation model: {str(e)}")
    translator = None

# Language code mapping
LANGUAGE_CODES = {
    "hindi": "hi",
    "tamil": "ta",
    "telugu": "te",
    "bengali": "bn",
    "marathi": "mr",
    "kannada": "kn",
    "gujarati": "gu",
    "malayalam": "ml"
}

async def translate_text(text: str, target_lang: str) -> str:
    """
    Translate text to the target Indian language using IndicTrans2.
    """
    try:
        if translator is None:
            return "Translation service is not available. Please try again later."
            
        # Get the language code
        lang_code = LANGUAGE_CODES.get(target_lang.lower(), "hi")  # Default to Hindi
        
        # Perform translation
        result = translator(
            text,
            tgt_lang=lang_code,
            max_length=512
        )
        
        return result[0]['translation_text']
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return f"Translation error: {str(e)}" 