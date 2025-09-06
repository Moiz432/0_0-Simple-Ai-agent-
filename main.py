import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig

# Load environment
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_BASE = os.getenv("GEMINI_API_BASE", "https://openrouter.ai/api/v1")

if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is not set in the environment variables.")

print("✅ OpenRouter API Key loaded successfully!")
print(f"🔗 Using API Base: {GEMINI_API_BASE}")

# Create an OpenAI-compatible client (OpenRouter endpoint)
provider = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=GEMINI_API_BASE)

# Define the model
model = OpenAIChatCompletionsModel(
    model="google/gemini-2.5-flash-lite",
    openai_client=provider
)

# Setup RunConfig
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)
