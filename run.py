import uvicorn
import os
import logging
import sys
from pathlib import Path

# Configure logging
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

def check_environment():
    """Check if all required environment variables and directories are set up."""
    model_cache_dir = os.getenv("MODEL_CACHE_DIR", "model_cache")
    try:
        # Check required directories
        required_dirs = [model_cache_dir, 'static']
        for dir_name in required_dirs:
            dir_path = Path(dir_name)
            if not dir_path.exists():
                logger.warning(f"Creating directory: {dir_name}")
                dir_path.mkdir(parents=True, exist_ok=True)
        
        # Check environment variables
        hf_api_key = os.getenv("HF_API_KEY")
        if not hf_api_key:
            logger.error("HF_API_KEY environment variable is not set")
            return False
        
        logger.info("Environment check passed successfully")
        return True
    except Exception as e:
        logger.error(f"Environment check failed: {str(e)}")
        return False

if __name__ == "__main__":
    try:
        # Check environment before starting
        if not check_environment():
            logger.error("Environment check failed. Exiting...")
            sys.exit(1)

        port = int(os.getenv("PORT", 8000))
        logger.info(f"Starting server on port {port}")
        
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=port,
            reload=False,
            log_level=log_level.lower(),
            workers=1
        )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        sys.exit(1) 