from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

# Create Gemini client
client = genai.Client()

# List available models
for model in client.models.list():
    print(model.name)