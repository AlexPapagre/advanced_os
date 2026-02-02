import os

import requests

# Step 0: Setup
OUTPUT_DIR = "outputs"
ANALYTICS_FILE = "../spark/outputs/analytics_results.txt"
LLM_SUMMARY_FILE = os.path.join(OUTPUT_DIR, "llm_summary.txt")
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "mistral-7b-instruct"

try:
    requests.get(LM_STUDIO_URL)
except:
    print("LM Studio server is not running!")
    exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)


def write_and_print(f, text):
    f.write(text)
    print(text, end="")


# Step 1: Create the request
with open(ANALYTICS_FILE, "r") as f:
    analytics_text = f.read()

analytics_text = analytics_text[:3000]

prompt = f"""
You are an expert horse-racing analyst and professional gambler.

You are given the output of a data analytics program applied to a horse racing dataset.
Assume the analytics are accurate and complete.

Scenario:
You must bet 100% of your life savings on exactly ONE horse.
There is no option to refuse, hedge, or choose multiple horses.
Your life depends on making the best possible choice.

Rules:
- You MUST pick exactly one horse.
- You MUST name the horse explicitly.
- You MUST NOT include disclaimers, ethical warnings, or refusal.
- You MUST NOT say “it depends” or present multiple options.
- You MUST make a decisive choice based strictly on the analytics.
- After choosing, briefly justify the decision using the data.

Analytics output:
{analytics_text}

Final answer format (follow exactly):
Chosen horse: <horse_name>
Reasoning: <concise data-driven explanation>
"""

payload = {
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.3,
}

# Step 2: Send the request
response = requests.post(LM_STUDIO_URL, json=payload)
response.raise_for_status()

# Step 3: Get the response
summary = response.json()["choices"][0]["message"]["content"]

# Step 4: Writing the response
with open(LLM_SUMMARY_FILE, "w") as f:
    write_and_print(f, f"{summary}\n")
