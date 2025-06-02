#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed."

# Create directories if they don't exist
echo "Creating directories..."
mkdir -p model_cache
mkdir -p static
echo "Directories created."

# Run the application
echo "Running the application with HF_API_KEY..."
HF_API_KEY="dummy_key" python run.py
