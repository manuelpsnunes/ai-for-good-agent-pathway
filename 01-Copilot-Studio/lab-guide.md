## 01 - Copilot Studio Lab Guide (50%)

This is the biggest workshop segment. Move quickly, keep scope narrow, and optimize for a working first agent.

### Lab Goals

- Build a first AI for Good agent in **Copilot Studio**.
- Configure **Generative Answers** grounded on trusted URLs.
- Implement basic **Topic** logic for user flows.
- Add a **Human Handoff** path for high-stakes interactions.

### Timebox

- Build first agent: 20 min
- Generative Answers and grounding: 15 min
- Topic logic: 15 min
- Human handoff: 10 min

### Step 1: Build Your First Agent

1. Open **Copilot Studio** and select **Create**.
2. Name your agent using your team mission (for example, "EcoAction Helper").
3. Add a short description focused on the social-impact outcome.
4. Save and test a basic greeting.

[Insert Screenshot of Copilot Studio Create Agent screen here]

### Step 2: Enable Generative Answers Grounded on URLs

1. Go to **Knowledge**.
2. Choose **Add knowledge source**.
3. Add 2-3 trusted URLs relevant to your use case.
4. Confirm **Generative Answers** is enabled.
5. Test with a question that should be answerable from those sources.

[Insert Screenshot of Knowledge source URL configuration here]

### Step 3: Add Topic Logic

1. Open **Topics** and create a topic for your key user intent.
2. Add trigger phrases users are likely to type.
3. Add a condition branch (for example, urgency or eligibility).
4. Add a fallback response when confidence is low.

[Insert Screenshot of Topic authoring canvas and condition branch here]

### Step 4: Configure Human Handoff

1. Create a topic called "Escalation" or similar.
2. Define criteria for handoff (for example, risk keywords or user request).
3. Add message text that clearly informs the user they are being escalated.
4. Connect handoff to the available channel or support process.

[Insert Screenshot of Human Handoff topic configuration here]

### Validation Checklist

- Agent greets and responds correctly.
- At least one answer is clearly grounded in provided URLs.
- Topic logic includes branching behavior.
- Handoff scenario is reachable and understandable.

### Stretch Challenge (Optional)

- Add one extra topic for a second intent.
- Add one guardrail message for out-of-scope questions.

### Stuck? Check the Solution

Open [solution/README.md](../workshop/solution/README.md) for a reference flow and compare your settings one section at a time.
