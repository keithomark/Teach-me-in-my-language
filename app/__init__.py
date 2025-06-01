from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.routes.api import router
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Teach Me In My Language")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(router)

# Get the absolute path to the static directory
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
logger.info(f"Serving static files from: {static_dir}")

# Verify static directory exists
if not os.path.exists(static_dir):
    logger.error(f"Static directory not found at: {static_dir}")
    raise RuntimeError(f"Static directory not found at: {static_dir}")

# Mount static files
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_root():
    index_path = os.path.join(static_dir, "index.html")
    if not os.path.exists(index_path):
        logger.error(f"index.html not found at: {index_path}")
        raise RuntimeError(f"index.html not found at: {index_path}")
    return FileResponse(index_path)

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up...")
    try:
        # Check for HuggingFace API key
        hf_api_key = os.getenv("HF_API_KEY")
        if not hf_api_key:
            logger.warning("HuggingFace API key not found. Please set HF_API_KEY environment variable.")
        else:
            logger.info("HuggingFace API key found. Services should be available.")
            
        # Verify static files
        required_files = ["index.html", "styles.css", "script.js"]
        for file in required_files:
            file_path = os.path.join(static_dir, file)
            if not os.path.exists(file_path):
                logger.error(f"Required static file not found: {file}")
                raise RuntimeError(f"Required static file not found: {file}")
            logger.info(f"Found static file: {file}")
            
    except Exception as e:
        logger.error(f"Error during startup: {str(e)}")
        raise 