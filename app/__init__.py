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

# Mount static files
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(static_dir, "index.html"))

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
    except Exception as e:
        logger.error(f"Error during startup: {str(e)}") 