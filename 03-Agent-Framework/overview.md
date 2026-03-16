## 03 - Agent Framework Overview (15%)

This final segment is a glimpse into pro-code orchestration. Keep it light: understand the pattern, run the sample, and identify where it helps your scenario.

### What Is Multi-Agent Orchestration?

Multi-agent orchestration coordinates specialized agents that each do one job well, then combines their outputs into a better final result.

### Why It Matters for AI for Good

- Complex social-impact challenges often require multiple perspectives.
- Specialized agents improve reliability over one overloaded assistant.
- Orchestration helps enforce clear responsibilities and safer decision flow.

### GroupChat Pattern at a Glance

- **Planner Agent**: breaks down user intent into tasks.
- **Research Agent**: gathers grounded facts and context.
- **Coordinator Agent**: merges outputs and crafts the response.

### When to Use This Pattern

Use this when:

- Your use case requires more than one reasoning style.
- You need traceable steps for accountability.
- You want to scale from demo to maintainable architecture.

### Hands-On Link

Run the sample in `samples/multi-agent-demo.py` and observe how each agent contributes to one final response.
