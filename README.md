# Teach Me In My Language

A web application that simplifies complex topics and translates them into Indian languages using Google's Gemini API and IndicTrans2.

## Features

- **Simplified Explanations**: Uses Google's Gemini API to generate easy-to-understand explanations of complex topics
- **Multi-language Support**: Translates content into 8 Indian languages:
  - Hindi
  - Tamil
  - Telugu
  - Bengali
  - Marathi
  - Kannada
  - Gujarati
  - Malayalam
- **Modern UI**: Clean and responsive interface built with HTML, CSS, and JavaScript
- **FastAPI Backend**: Efficient and scalable API endpoints

## Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (recommended for faster translation)
- Google Cloud API key for Gemini

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd teach-me-in-my-language
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

2. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
teach-me-in-my-language/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── routes/
│   │   └── api.py          # API route definitions
│   └── services/
│       ├── explain.py      # Gemini API integration
│       └── translate.py    # IndicTrans2 translation service
├── static/
│   ├── index.html          # Main application page
│   ├── styles.css          # Styling
│   └── script.js           # Frontend logic
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## API Endpoints

- `POST /api/explain`: Generate simplified explanation
  - Request body: `{"topic": "your topic here"}`
  - Response: Simplified explanation in English

- `POST /api/translate`: Translate text to Indian languages
  - Request body: `{"text": "text to translate", "target_lang": "language name"}`
  - Response: Translated text in the target language

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 