from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

# List all models
models = client.models.list().page
for m in models:
    print(m.display_name, "->", m.name)