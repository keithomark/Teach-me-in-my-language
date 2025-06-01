import uvicorn
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT", 8000))
        logger.info(f"Starting server on port {port}")
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=port,
            reload=False,
            log_level="info"
        )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise 