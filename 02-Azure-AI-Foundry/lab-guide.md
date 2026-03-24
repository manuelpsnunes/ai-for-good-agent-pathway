## 02 - Azure AI Foundry Lab Guide

Now shift from low-code configuration to model and prompt engineering decisions that improve outcome quality.

### Technology intro: Microsoft Foundry

**Microsoft Foundry** is a middle option between quick, fully managed Copilot experiences and fully custom infrastructure. It gives your team more control over orchestration, model choice, prompt testing, and development workflow (VS Code + GitHub + Foundry portal), while still providing a managed platform experience.

<img src="../supportdocs/foundry-agent-service.png" alt="Microsoft Foundry Agent Service architecture overview" width="75%" />

Planning reference: [Technology solutions and strategy for AI agents](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/technology-solutions-plan-strategy)


### Scope in this lab

- Evaluate and compare model behavior in Azure AI Foundry.
- Iterate on system prompts for safer and more actionable responses.
- Define how Foundry outcomes connect back into the Copilot Studio experience.

For shared workshop context (ecosystem overview, global goals, and architecture), see [README.md](../README.md).

## 🔬 Build in Azure AI Foundry

These sections are repeated in each phase so teams can follow a consistent loop: set context, execute, compare outcomes, document decisions, and validate before moving on.

<details open>
<summary><strong>Phase 1 — 🔎 Model Catalog Exploration</strong></summary>

#### Initial Setup

Before you begin this phase, complete **Step-by-Step: Azure $200 Free Account (30 Days) ☁️** in the [Setup Guide](../00-Setup/setup-guide.md).

1. Open **Azure AI Foundry** ( https://ai.azure.com/ ) and Sign In with your assigned sandbox **work or school account**.

2. Go to the **Model Catalog** and check the available models. Notice you have a Model Leaderboard where you can see the different models and a comparison of their capabilities and performance on different benchmarks (Quality, Safety, Cost, Throughput).

    <img src="../supportdocs/modelleaderboard.png" alt="Microsoft Foundry Agent Model Leadersboard" width="100%" />

3. Filter the catalog for **inference task** equal to **image to text** to check the best models to perform the object detection and count .
#### Execution

2. Find a Phi-4 model and review core capabilities.
3. Find a Llama model and review core capabilities.

#### Comparison

4. Capture a quick decision note: which model suits your use case and why.

#### Validation

[Insert Screenshot of Model Catalog filtered for Phi-4 and Llama here]

> ✅ Checkpoint: Catalog Selection Ready
> - Two model families reviewed.
> - One candidate model selected with rationale.

</details>

<details open>
<summary><strong>Phase 2 — 🧪 Playground Prompt Experimentation</strong></summary>

#### Initial Setup

5. Open **Playground**.

#### Execution

6. Write a short system prompt with role, constraints, and expected tone.
7. Test the same user prompt against two different models.

#### Comparison

8. Evaluate output quality on relevance, safety, and actionability.
9. Refine your system prompt and run one final test.

#### Validation

[Insert Screenshot of Playground with system prompt and output comparison here]

> ✅ Checkpoint: Prompt Iteration Ready
> - At least one prompt revision improved outcomes.
> - Comparison notes captured for both models.

</details>

<details open>
<summary><strong>Phase 3 — 🔗 Connect Back to Copilot Studio</strong></summary>

#### Initial Setup

10. Open your Copilot Studio architecture notes from Lab 01.

#### Execution

11. Document your selected model and final system prompt pattern.
12. Map where this model/prompt logic fits your Copilot Studio agent experience.

#### Integration Notes

13. Identify one high-value topic where richer model behavior improves outcomes.
14. Note integration constraints (latency, cost, approvals).

#### Validation

[Insert Screenshot of architecture notes linking Foundry to Copilot Studio here]

> ✅ Checkpoint: Integration Plan Ready
> - Foundry decision translated into Copilot Studio impact.
> - Constraints documented for implementation planning.

</details>

### ✅ Validation Checklist

- Two model families were reviewed.
- At least one prompt iteration improved output quality.
- Team produced a clear integration note for Copilot Studio.

### 📓 Notebooks Folder

Use the notebooks folder to capture quick experiments, comparisons, and reusable prompt tests.

### 🆘 Stuck? Check the Solution

Open [solution/README.md](../workshop/solution/README.md) to compare your model selection and prompt structure with a sample baseline.
