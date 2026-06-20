import os
from pathlib import Path
from dotenv import load_dotenv

# code/ directory
CODE_DIR = Path(__file__).resolve().parent
# repo root (one level up from code/)
REPO_ROOT = CODE_DIR.parent
# dataset directory
DATASET_DIR = REPO_ROOT / "dataset"

# Load .env from repo root
load_dotenv(REPO_ROOT / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GPT_MODEL = "gpt-4.1-mini"

GROQ_MODEL = "llama-3.3-70b-versatile"

TEMPERATURE = 0