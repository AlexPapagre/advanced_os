import os

import requests

OUTPUT_DIR = "outputs"
ANALYTICS_FILE = "../spark/outputs/analytics_results.txt"
LLM_SUMMARY_FILE = os.path.join(OUTPUT_DIR, "llm_summary.txt")
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "mistral-7b-instruct"

try:
    requests.get(LM_STUDIO_URL)
except:
    print("LM Studio server is cloned!")
    exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(ANALYTICS_FILE, "r") as f:
    analytics_text = f.read()

analytics_text = analytics_text[:3000]

prompt = f"""
You are given the output of a data analytics program applied to a horse racing dataset.

Explain the results in a short, clear, and friendly way, using simple language.
Assume the reader has no technical background.
Do not mention code, algorithms, or statistics.
Focus only on what the data shows and what we can learn from it.

Analytics output:
{analytics_text}
"""

prompt = f"""
You are given the output of a data analytics program applied to a horse racing dataset.

You are a gambler and you have to put all your life savings in one horse. Which horse would you pick?
You have to make a choice, your life depends on it!

Analytics output:
{analytics_text}
"""

payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.3,
}

response = requests.post(LM_STUDIO_URL, json=payload)
response.raise_for_status()

summary = response.json()["choices"][0]["message"]["content"]

with open(LLM_SUMMARY_FILE, "w") as f:
    f.write(summary)

print("\n=== LLM Summary ===\n")
print(summary)
