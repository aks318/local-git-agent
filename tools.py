from pathlib import Path
from langchain_core.tools import tool

import subprocess
from datetime import datetime


# Always write to agent_log.txt inside this project
LOG_FILE = Path(__file__).parent / "agent_log.txt"


@tool
def append_log(line: str) -> str:
    """Append a new sentence to the agent_log.txt file."""

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(line.strip() + "\n")

    return f"Successfully added to agent_log.txt: {line}"


@tool
def git_commit_and_push() -> str:
    """Commit the updated agent_log.txt file and push it to GitHub."""

    try:
        # Stage only the log file
        subprocess.run(
            ["git", "add", "agent_log.txt"],
            cwd=Path(__file__).parent,
            check=True,
            capture_output=True,
            text=True,
        )

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Commit changes
        subprocess.run(
            ["git", "commit", "-m", f"AI agent update: {timestamp}"],
            cwd=Path(__file__).parent,
            check=True,
            capture_output=True,
            text=True,
        )

        # Push changes
        result = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=Path(__file__).parent,
            check=True,
            capture_output=True,
            text=True,
        )

        return f"Successfully committed and pushed agent_log.txt. {result.stdout}"

    except subprocess.CalledProcessError as error:
        return (
            f"Git operation failed. "
            f"Command: {error.cmd}. "
            f"Error: {error.stderr or error.stdout}"
        )