# This example demonstrates Gemma‑4's ability to handle long inputs (large context windows).
# Unlike simple text generation, this shows how developers can feed entire articles or reports
# and get structured analysis back — summaries, key points, recommendations, etc.
# It's useful for document summarization, knowledge extraction, and enterprise workflows.

from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
# models = client.models.list().page
# for m in models:
#     print(m.display_name, "->", m.input_token_limit)

# A long piece of text (could be an article, report, or documentation)
long_text = """
Artificial intelligence (AI) is transforming industries by automating tasks, improving decision-making,
and enabling new products and services. In healthcare, AI assists in diagnostics and personalized medicine.
In finance, it enhances fraud detection and algorithmic trading. In education, AI enables adaptive learning
platforms tailored to individual student needs. However, challenges remain: ethical concerns, bias in data,
and the need for transparency in AI systems. Policymakers and researchers are working to establish guidelines
that ensure AI benefits society while minimizing risks.
"""

# Prompt asking for structured analysis
prompt = f"""
You are a helpful assistant.
Analyze the following text and provide:
1. A concise summary (3-4 sentences).
2. Key domains where AI is applied.
3. Main challenges mentioned.
4. One recommendation for policymakers.

Text:
{long_text}
"""

response = client.models.generate_content(
    model="models/gemma-4-26b-a4b-it",  # or "models/gemma-4-31b-it"
    contents=prompt
)

print("Model output:")
print(response.text)


