"""Dispatcher module for building and running agent commands."""


def build_command(agent: str, prompt: str) -> list[str]:
    """
    Build the gemini command for the given agent and prompt.

    Args:
        agent: The name of the agent to invoke.
        prompt: The prompt to send to the agent.

    Returns:
        A list of command arguments.
    """
    return [
        "gemini",
        "--yolo",
        "-r",
        "--model",
        "gemini-3.1-pro-preview",
        f"--context=.squad/{agent}/.gemini/GEMINI.md",
        prompt,
    ]
