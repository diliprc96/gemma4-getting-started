from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

# Define a simple calculator tool
def calculator(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# Prompt that instructs the model to explicitly suggest tool usage
prompt = """You are a helpful assistant with access to a calculator tool.
When solving math problems, output the calculation you want to perform
inside <calc> ... </calc> tags, then explain the result.

Example:
Question: What is 120 / 2?
Answer: <calc>120/2</calc> The average speed is 60 km/h.

Now solve this:
If a car travels 150 km in 3 hours, what is its average speed in km/h?
"""

response = client.models.generate_content(
    model="models/gemma-4-26b-a4b-it",  # or gemma-4-31b-it
    contents=prompt
)

print("Raw model output:")
print(response.text)

# Detect if the model suggested a calculation
import re
match = re.search(r"<calc>(.*?)</calc>", response.text)
if match:
    expression = match.group(1)
    calc_result = calculator(expression)
    print("\nCalculator executed:", expression, "=", calc_result)
    print("Final Answer:", calc_result, "km/h")