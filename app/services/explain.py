import httpx
import logging
import os
from dotenv import load_dotenv

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# HuggingFace API endpoint
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HF_API_KEY = os.getenv("HF_API_KEY")

async def generate_explanation(topic: str) -> str:
    """
    Generate a simplified explanation for the given topic using HuggingFace's Inference API.
    """
    try:
        if not HF_API_KEY:
            return "Error: HuggingFace API key not found. Please set the HF_API_KEY environment variable."
            
        logger.info(f"Generating explanation for topic: {topic}")
        
        prompt = f"""<s>[INST] Please explain the following topic in simple terms that a high school student can understand. 
        Break it down into key points and use examples where possible. 
        Keep the explanation concise but comprehensive.
        
        Topic: {topic} [/INST]</s>"""
        
        headers = {
            "Authorization": f"Bearer {HF_API_KEY}",
            "Content-Type": "application/json"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                HF_API_URL,
                headers=headers,
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 512,
                        "temperature": 0.7,
                        "top_p": 0.95,
                        "return_full_text": False
                    }
                },
                timeout=60.0  # Increased timeout
            )
            
            if response.status_code == 401:
                logger.error("Invalid HuggingFace API key")
                return "Error: Invalid API key. Please check your HuggingFace API key."
            elif response.status_code != 200:
                logger.error(f"HuggingFace API error: {response.text}")
                return f"Error: Failed to generate explanation. Status code: {response.status_code}"
                
            result = response.json()
            if not result or not isinstance(result, list) or not result[0].get("generated_text"):
                logger.error("Empty response from HuggingFace API")
                return "Error: Empty response from API. Please try again."
                
            logger.info("Successfully generated explanation")
            return result[0]["generated_text"].strip()
            
    except Exception as e:
        logger.error(f"Error generating explanation: {str(e)}")
        return f"Error: {str(e)}" 