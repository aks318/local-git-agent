from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import tool


@tool
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello {name}! Tool executed successfully."


llm = ChatOllama(
    model="qwen3.8:latest",
    temperature=0,
)

agent = create_agent(
    model=llm,
    tools=[greet],
    system_prompt="""
    You are a helpful AI agent.
    Use the available tools whenever appropriate.
    After executing a tool, explain its result briefly.
    """,
)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Use the greet tool to greet Aakash."
        }
    ]
})

print(response["messages"][-1].content)