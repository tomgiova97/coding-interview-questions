import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
# This will search for a .env file in the current directory and load it.
load_dotenv()

# --- Accessing the variables ---
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_FREE_API_KEY = os.environ.get("GEMINI_FREE_API_KEY")
CHAT_GPT_API_KEY = os.environ.get("CHAT_GPT_API_KEY")