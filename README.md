# Teach Me In My Language 🇮🇳

A web application that helps you understand complex topics in your preferred Indian language. The app uses AI to generate simplified explanations and translates them into various Indian languages.

## Features

- 🤖 AI-powered explanations in simple terms
- 🌐 Support for 8 Indian languages:
  - Hindi 🇮🇳
  - Tamil 🐅
  - Telugu 🌾
  - Bengali 🪔
  - Marathi 🎭
  - Kannada 🏹
  - Gujarati 🌺
  - Malayalam 🐘
- 🎯 Easy-to-understand explanations
- 💫 Modern and responsive UI

## Live Demo

Visit the deployed application at: [https://teach-me-in-my-language.onrender.com](https://teach-me-in-my-language.onrender.com)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/keithomark/Teach-me-in-my-language.git
cd Teach-me-in-my-language
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

4. Create a `.env` file in the root directory:
```
HF_API_KEY=your_huggingface_token_here
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

6. Open your browser and visit: `http://localhost:8000`

## Deployment

The application is configured for deployment on Render.com. To deploy:

1. Fork this repository
2. Create a Render.com account
3. Create a new Web Service
4. Connect your GitHub repository
5. Add your HuggingFace API key as an environment variable
6. Deploy!

## Technology Stack

- Backend:
  - FastAPI
  - HuggingFace Inference API
  - Python 3.11+

- Frontend:
  - HTML5
  - CSS3
  - JavaScript (Vanilla)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- HuggingFace for providing the AI models
- FastAPI for the excellent web framework
- The open-source community for their invaluable tools and libraries 