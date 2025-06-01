import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

async def generate_explanation(topic: str) -> str:
    """
    Generate a simplified explanation for the given topic using Gemini API.
    """
    try:
        logger.info(f"Generating explanation for topic: {topic}")
        
        prompt = f"""Please explain the following topic in simple terms that a high school student can understand. 
        Break it down into key points and use examples where possible. 
        Keep the explanation concise but comprehensive.
        
        Topic: {topic}"""
        
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            logger.error("Empty response from Gemini API")
            raise Exception("Failed to generate explanation: Empty response from API")
            
        logger.info("Successfully generated explanation")
        return response.text
        
    except Exception as e:
        logger.error(f"Error generating explanation: {str(e)}")
        raise Exception(f"Failed to generate explanation: {str(e)}") 