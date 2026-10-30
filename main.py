from langchain_ollama import ChatOllama

llm = ChatOllama(
    model= "llama3.2:1b",
    temperature=0.7
)

def generate_log():
    prompt = """
        Generate one short, friendly, unique sentence for a company
        that likes green walls.

        Example:
        This line was added by an AI agent for a company that likes green walls.

        Return only the sentence. No explanation.
    """
    response = llm.invoke(prompt)
    return response.content.strip()


if __name__ == "__main__":
    log_line = generate_log()
    with open("agent-log.txt", "a", encoding="utf-8" ) as f:
        f.write(log_line + "\n")

    print(f"Added to agent_log.txt: {log_line}")