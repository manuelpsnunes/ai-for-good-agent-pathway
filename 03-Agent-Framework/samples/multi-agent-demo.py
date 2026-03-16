"""Minimal multi-agent GroupChat-style demo for workshop participants.

This script is intentionally simple: no external SDK required.
It demonstrates the orchestration concept without setup overhead.
"""

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class Agent:
    name: str
    role: str
    respond: Callable[[str], str]


def run_group_chat(user_goal: str, agents: List[Agent]) -> str:
    """Collect responses from specialist agents and synthesize output."""
    messages = []
    for agent in agents:
        messages.append(f"{agent.name} ({agent.role}): {agent.respond(user_goal)}")

    synthesis = "\n".join(messages)
    return f"USER GOAL: {user_goal}\n\nGROUPCHAT TRANSCRIPT\n{synthesis}\n"


def main() -> None:
    planner = Agent(
        name="PlannerAgent",
        role="Task decomposition",
        respond=lambda goal: (
            f"I split '{goal}' into steps: understand need, identify constraints, "
            "and draft an action plan."
        ),
    )

    researcher = Agent(
        name="ResearchAgent",
        role="Evidence and context",
        respond=lambda goal: (
            f"For '{goal}', I gather trusted sources, summarize key facts, "
            "and highlight confidence limits."
        ),
    )

    coordinator = Agent(
        name="CoordinatorAgent",
        role="Final response assembly",
        respond=lambda goal: (
            f"I combine planner + researcher outputs for '{goal}' into "
            "a concise recommendation with next actions."
        ),
    )

    transcript = run_group_chat(
        user_goal="Design an AI assistant to help local clinics triage common questions",
        agents=[planner, researcher, coordinator],
    )

    print(transcript)


if __name__ == "__main__":
    main()
