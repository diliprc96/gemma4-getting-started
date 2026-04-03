# Gemma‑4 Getting Started 🚀

## Introduction
Gemma‑4 is Google’s newest family of open models, delivering advanced reasoning and agentic capabilities in a small footprint. Released under the Apache 2.0 license, Gemma‑4 can run locally or via Google AI Studio with an API key.

This repo helps developers quickly get started with Gemma‑4 — whether you want to run it locally or through the cloud.

---

## Setup Options

### Option A: Cloud Inference (Google AI Studio API Key)
👉 See [QuickStart.py](examples\Quickstart.py) for a runnable script.
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Generate a free API key.
3. Install the SDK:
   ```bash
   pip install -q -U google-genai
   ```
4. Save your API key in a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
5. Quickstart script:
   ```python
    from google import genai
    from dotenv import load_dotenv

    load_dotenv()
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
    )
    print(response.text)
   ```

⚠️ **Note:** Never commit your API key to GitHub. Use `.env` or environment variables.

---

### 📋 Listing Available Models
👉 See [list_models.py](list_models.py) for a runnable script.

After setting up your API key and running the quickstart script, you may want to see which models are available to your account. You can list them like this:

```python
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

# List all models available
models = client.models.list().page
for m in models:
    print(m.display_name, "->", m.name)
```

**Sample Output:**
```
Gemini 2.5 Flash -> models/gemini-2.5-flash
Gemini 2.5 Pro -> models/gemini-2.5-pro
Gemma 4 26B A4B IT -> models/gemma-4-26b-a4b-it
Gemma 4 31B IT -> models/gemma-4-31b-it
...
```

You can then choose the model you want by passing its `name` into your inference call:

```python
response = client.models.generate_content(
    model="models/gemma-4-26b-a4b-it",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

---

### Option B: Local Inference (Weights from Hugging Face/Kaggle)
⚠️ **Note:** This downloads more than 10GB of data, so make sure you have enough disk space and a good internet connection.
👉 See [QuickStart_local.py](examples/QuickStart_local.py) for a runnable script.
1. Install dependencies:
   ```bash
   pip install torch transformers tokenizers huggingface_hub
   ```
2. Save your Hugging face Access token in a `.env` file
   ```bash
   HF_TOKEN=your_access_token_here
   ```
3. Download weights from Hugging Face:
   ```bash
   git lfs install
   git clone https://huggingface.co/google/gemma-4-E2B
   ```
4. Quickstart script:
   ```python
   from transformers import AutoTokenizer, AutoModelForCausalLM
   from dotenv import load_dotenv

   load_dotenv()
   model_name = "google/gemma-4-E2B"
   tokenizer = AutoTokenizer.from_pretrained(model_name)
   model = AutoModelForCausalLM.from_pretrained(model_name)

   inputs = tokenizer("Explain quantum computing in simple terms", return_tensors="pt")
   outputs = model.generate(**inputs, max_length=200)
   print(tokenizer.decode(outputs[0], skip_special_tokens=True))
   ```

---

## Examples
- `examples/reasoning_demo.py` → Long‑context reasoning.
- `examples/tool_use_demo.py` → Integrating external tools (e.g., calculator).

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
