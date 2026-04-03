from google import genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = genai.Client()

# A reasoning-style prompt
prompt = """You are a helpful assistant.
Solve this step by step:

If a train travels 60 km in 1.5 hours, what is its average speed in km/h?
"""

# Choose a Gemma-4 model (adjust based on what you listed with client.models.list())
response = client.models.generate_content(
    model="models/gemma-4-26b-a4b-it",  # or "models/gemma-4-31b-it"
    contents=prompt
)

print(response.text)