## AI for Good Hackathon: Low-Code to Pro-Code Agents

Build meaningful, agentic solutions in 2 hours. This workshop helps hackathon teams move from **Copilot Studio** foundations to **Azure AI Foundry** experimentation and finally into **pro-code multi-agent orchestration** patterns.

## 🧭 FoodLink AI Ecosystem Overview

This workshop uses the FoodLink scenario to demonstrate end-to-end agentic orchestration for social impact.

- **FoodLink Agentic AI (Copilot Studio)**: Parent orchestrator that delegates execution to specialist agents.
- **Donor Assistant (Copilot Studio)**: Handles donation intake and donor context.
- **Volunteer Dispatcher (Copilot Studio)**: Matches donations to hub capacity and available volunteers.
- **Meal Organizer (Copilot Studio)**: Transforms available food into balanced distribution plans.
- **Vision Guard (Azure AI Foundry)**: Adds model-driven intelligence for connected scenarios.

## 🧪 Workshop Goals

- Learn how to set up multiple agents in **Microsoft Copilot Studio** and orchestrate them as one end-to-end process.
- Learn how to design robust **Instructions** for predictable handoffs between parent and child agents.
- Learn how to use **Tools** for deterministic operations (lookups, matching, routing, approvals).
- Learn how to use **Knowledge** with grounded responses.
- Learn how to implement **human-in-the-loop** paths for high-impact decisions.
- Learn how to validate complex multi-agent flows quickly, including success and fallback paths.

## 🏗️ Agent Architecture

We build an agentic system composed of:

- 1 orchestrator (FoodLink Agentic AI)
- 3 child agents (Donor Assistant, Volunteer Dispatcher, Meal Organizer)
- 1 connected agent (Vision Guard)

The orchestration pattern is **handoff orchestration**, where execution is passed to a specialist agent when specific conditions are met.

For more patterns, see [AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns).

<img src="./supportdocs/agenticarchitecture.png" alt="Agent architecture" width="75%" />

## 2-Hour Roadmap

| Segment | Focus | Time | Workshop Share |
|---|---|---:|---:|
| 01-Copilot-Studio | First agent, **Generative Answers**, **Topic** logic, **Human Handoff** | 60 min | **50%** |
| 02-Azure-AI-Foundry | Model Catalog (Phi-4, Llama), Playground system prompts, Copilot Studio connection | 42 min | **35%** |
| 03-Agent-Framework | Multi-agent orchestration overview and GroupChat code glimpse | 18 min | **15%** |
| Total | Time-to-Impact sprint | 120 min | **100%** |

## 350-Character Description

A fast-paced, 2-hour AI for Good hackathon workshop that guides builders from low-code Copilot Studio agents to pro-code Azure AI Foundry and multi-agent orchestration. Teams prototype real social-impact solutions, learn practical patterns, and leave with reusable assets to keep shipping responsible, mission-driven AI beyond the event at scale now.

## Why Agents for Social Good?

### Faster Response to Real Needs
Agents help teams translate community challenges into working solutions quickly, so ideas become usable prototypes during the event instead of staying on slides.

### Better Human + AI Collaboration
With **handoff**, **guardrails**, and **grounded responses**, teams design systems where people stay in control while AI accelerates impact.

### Reusable Architecture Beyond the Hackathon
Participants leave with a progression path from low-code to pro-code, making it easier to productionize responsible solutions after the workshop.

## Repository Map

- `00-Setup/`: Tenant, licensing, and readiness checklist.
- `01-Copilot-Studio/`: Core low-code build lab (50% of workshop).
- `02-Azure-AI-Foundry/`: Model and prompt experimentation lab (35% of workshop).
- `03-Agent-Framework/`: Pro-code architecture glimpse with Python sample (15% of workshop).
- `use-cases/`: AI for Good idea bank to kick-start team concepts.

## Suggested Lab Order

1. [00-Setup/setup-guide.md](00-Setup/setup-guide.md)
2. [01-Copilot-Studio/lab-guide.md](01-Copilot-Studio/lab-guide.md)
3. [02-Azure-AI-Foundry/lab-guide.md](02-Azure-AI-Foundry/lab-guide.md)
4. [03-Agent-Framework/overview.md](03-Agent-Framework/overview.md)

## Workshop Outcome

By the end, each team has:

- A functioning first agent.
- A tested model/prompt strategy in Foundry.
- A clear next step toward multi-agent pro-code architecture.
