from agents import Agent, Runner, function_tool
from main import config

@function_tool
def usd_to_pkr():
    # """
    # Returns today's USD to PKR rate (fixed).
    # Guardrails:
    # - Only responds if the query is about USD to PKR.
    # - Otherwise gives a safe fallback message.
    # """
    # query_lower = query.lower()

    # # Guardrails
    # if "usd" not in query_lower or "pkr" not in query_lower:
    #     return "❌ This tool only handles USD to PKR conversion requests."

    # # (Fixed response for now, can later be replaced with live API)
    return "✅ Today USD to PKR is 280."

# Create agent with tool
agent = Agent(
    name="An Agent",
    instructions="You are a helpful assistant. Your task is to help the user with their queries.",
    tools=[usd_to_pkr],
)

# Example query
result = Runner.run_sync(
    agent,
    input = input("💬 Enter your query: "),
    run_config=config
)

print("\n🎯 An Agent Output:")
print(result.final_output)
