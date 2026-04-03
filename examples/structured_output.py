# structured_output_pydantic_demo.py
# This example shows how to validate Gemma‑4's JSON output using Pydantic.
# Real-life use case: ensuring product data is clean and reliable before inserting into a database.

from google import genai
from dotenv import load_dotenv
import json
from pydantic import BaseModel, ValidationError, field_validator
from typing import List
import re

load_dotenv()
client = genai.Client()

# Define a schema for product data with a custom validator for price

class Product(BaseModel):
    product_name: str
    price: float
    features: List[str]
    warranty: str

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        # Handle cases like "249.99 USD" or "$249.99"
        if isinstance(v, str):
            match = re.search(r"[\d\.]+", v)
            if match:
                return float(match.group(0))
        return v


# Unstructured product description
product_text = """
Introducing the UltraClean Vacuum 3000 — a powerful cordless vacuum cleaner.
It features a 60-minute battery life, HEPA filter for allergens, and weighs only 2.5 kg.
Currently priced at $249.99 with a 2-year warranty included.
"""

# Prompt asking for structured JSON output
prompt = f"""
Extract the following details from the product description and return ONLY valid JSON, no extra text:
- product_name
- price (numeric)
- features (list of strings)
- warranty

Text:
{product_text}

"""

response = client.models.generate_content(
    model="models/gemma-4-26b-a4b-it",  # or gemma-4-31b-it
    contents=prompt
)

print("Raw model output:")
raw_output = response.text
print(raw_output)

clean_output = re.sub(r"^```json\s*|\s*```$", "", raw_output.strip(), flags=re.MULTILINE)



# Validate with Pydantic
try:
    structured_data = json.loads(clean_output)
    product = Product(**structured_data)
    print("\nValidated Product object:")
    print(product)
except (json.JSONDecodeError, ValidationError) as e:
    print("\nValidation failed:", e)