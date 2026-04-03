# Gemma‑4 Getting Started 🚀

## Introduction
Gemma‑4 is Google’s newest family of open models, delivering advanced reasoning and agentic capabilities in a small footprint. Released under the Apache 2.0 license, Gemma‑4 can run locally or via Google AI Studio with an API key.

This repo helps developers quickly get started with Gemma‑4 — whether you want to run it locally or through the cloud.

---

## Setup Options

### Option A: Cloud Inference (Google AI Studio API Key)
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Generate a free API key.
3. Install the SDK:
   ```bash
   pip install google-generativeai
   ```
4. Save your API key in a `.env` file:
   ```
   GEMMA_API_KEY=your_api_key_here
   ```
5. Quickstart script:
   ```python
   import os
   import google.generativeai as genai
   from dotenv import load_dotenv

   load_dotenv()
   genai.configure(api_key=os.getenv("GEMMA_API_KEY"))

   model = genai.GenerativeModel("gemma-4")
   response = model.generate_content("Explain quantum computing in simple terms")
   print(response.text)
   ```

⚠️ **Note:** Never commit your API key to GitHub. Use `.env` or environment variables.

---

### Option B: Local Inference (Weights from Hugging Face/Kaggle)
1. Install dependencies:
   ```bash
   pip install torch transformers
   ```
2. Download weights from Hugging Face:
   ```bash
   git lfs install
   git clone https://huggingface.co/google/gemma-4-4b
   ```
3. Quickstart script:
   ```python
   from transformers import AutoTokenizer, AutoModelForCausalLM

   model_name = "google/gemma-4-4b"
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForCausalLM.from_pretrained(model_name)

   inputs = tokenizer("Explain quantum computing in simple terms", return_tensors="pt")
   outputs = model.generate(**inputs, max_length=200)
   print(tokenizer.decode(outputs[0], skip_special_tokens=True))
   ```

---

## Examples
- `examples/text_generation.py` → Simple text generation.
- `examples/reasoning_demo.py` → Long‑context reasoning.
- `examples/tool_use_example.py` → Integrating external tools (e.g., calculator).
- `examples/edge_inference.py` → Running Gemma‑4 on constrained devices.

---

## Notebook
Interactive exploration: `notebooks/gemma4_quickstart.ipynb`

---

## Resources
- [Google AI Studio](https://aistudio.google.com/)  
- [Gemma‑4 on Hugging Face](https://huggingface.co/google)  
- [Gemma‑4 Kaggle Challenge](https://www.kaggle.com/)  

---

## Contributing
Pull requests welcome! Add new demos, integrations, or edge deployment guides.

---
