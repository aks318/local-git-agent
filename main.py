from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools import append_log, git_commit_and_push
import time


# Initialize local Ollama model
llm = ChatOllama(
    model="qwen3.8:latest",
    temperature=0.7,
)


# Create the AI agent
agent = create_agent(
    model=llm,
    tools=[
        append_log,
        git_commit_and_push,
    ],
    system_prompt="""
    You are an autonomous GitHub automation agent.

    Your task is to:

    1. Generate one unique, friendly sentence for a company
       that likes green walls.
    2. The sentence should mention that it was added by an AI agent.
    3. Use append_log to save the sentence to agent_log.txt.
    4. After successfully saving the sentence, use
       git_commit_and_push to commit and push the change.
    5. Report the results of both operations.

    Important:
    - Always call append_log before git_commit_and_push.
    - Do not claim an operation succeeded unless its tool confirms it.
    - Do not invent tool results.
    """,
)

def run_agent():
    print("\nStarting AI agent...")

    try:
        response = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": "Execute your GitHub automation task now."
                }
            ]
        })

        print("\nAgent response:")
        print(response["messages"][-1].content)

    except Exception as error:
        print(f"Agent execution failed: {error}")


if __name__ == "__main__":
    while True:
        run_agent()

        print("\nNext execution in 2 hours...")

        try:
            time.sleep(2 * 60 * 60)

        except KeyboardInterrupt:
            print("\nAI agent stopped.")
            break