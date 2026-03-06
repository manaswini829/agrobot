import os
from dotenv import load_dotenv # 1. Import the loader
import google.genai as genai
from google.genai.types import GenerateContentConfig
from PIL import Image

# 2. Load the .env file (Must be before os.getenv)
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
    print("✅ Gemini API configured")
else:
    # This will now tell you if the key is actually missing
    print("⚠️ WARNING: GEMINI_API_KEY not found. Check your .env file.")
    client = None

# 3. Changed default model to 2.0-flash (2.5 does not exist)
def ask_gemini(prompt, model="gemini-2.0-flash"):
    try:
        if not client:
            return "Error: API key not loaded."

        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=GenerateContentConfig(temperature=0.7)
        )

        if response.text:
            return response.text
        return "Gemini returned an empty response."

    except Exception as e:
        # 4. Print the ACTUAL error to your terminal so you can see it
        print(f"🔥 Gemini API error: {e}")
        return f"An error occurred: {e}"

# ... rest of your analyze_with_gemini function