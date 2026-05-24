---
name: domain-map-scan
description: |
  Trigger: User mentions entering a new field, starting a new project, 
  feeling "stuck" on what to ask, or requests a "knowledge audit" / 
  "domain map" / "T/F assessment".
  
  Outcome: Produces a structured knowledge gap analysis with 
  quantified coverage per sub-domain and a go/no-go launch threshold.
  
  Constraint: Never proceed to deep implementation until user 
  confirms the launch decision.
model: claude-sonnet-4
---

# Domain Map Scan

Audit knowledge gaps before executing. Prevent "don't know what you don't know" 
from bottlenecking AI-assisted work.

## When to Activate

- User is exploring a new technical domain or sub-field
- User feels their questions to AI are "low quality" or repetitive
- User asks for a "learning plan", "roadmap", or "where to start"
- User is about to commit to a project but unsure of prerequisite depth

## Prerequisites

- User must provide: target domain name + project goal (1 sentence)
- Optional but recommended: current familiarity level (beginner / dabbler / practitioner)

## Instructions

### Step 1: Deconstruct the Domain

Identify 5–8 core dimensions. Templates provide a baseline of 6 dimensions; 
adjust by splitting or merging to stay within the 5–8 range based on project scope.
For each dimension, provide:
- Name
- One-sentence definition (accessible to non-experts)
- 3–5 key concepts or technical terms
- A "safe-to-proceed" criterion: what minimum understanding prevents foot-guns

Load dimension templates from `{baseDir}/resources/templates/` if the domain 
matches known patterns (trading, publishing, agent systems). Present the matched 
template(s) to the user and ask them to confirm or request custom dimensions. 
If no match or the user declines, generate from first principles.

### Step 2: Generate Diagnostic T/F Questions

For each dimension, generate 4–6 True/False questions covering:
- 1–2 concept definitions (catch definitional errors)
- 1–2 common misconceptions or tacit knowledge (catch hidden foot-guns)
- 1–2 cross-dimensional intersections (prevent siloed understanding)

Present questions one at a time within each dimension. After the user answers 
(True, False, or "I don't know"), reveal the correct answer with a concise 
explanation before proceeding to the next question. Complete one full dimension 
before moving to the next.

### Step 3: Quantify Coverage

After all answers are collected, score each dimension 0–100%:
- 80–100%: Can teach others
- 60–79%: Can execute with reference docs
- 40–59%: Can follow tutorials, likely to get stuck
- 20–39%: Concepts fuzzy, systemic errors likely
- 0–19%: Near blank

Identify the bottleneck dimension: the dimension with the lowest coverage score.

### Step 4: Gate Decision

Determine the go/no-go threshold by analyzing the domain's risk profile:
- **Domain risk**: cost of error (irreversible harm → high; recoverable bugs → low)
- **Iteration cost**: time/resources to test and pivot (clinical trials → high; 
  coding prototypes → low)
- **Feedback loop speed**: how quickly the user learns from mistakes 
  (trading backtests → minutes; academic publishing → months)

Higher risk × slower feedback → higher threshold. Lower risk × faster feedback → lower threshold.

Reference points (agent adapts based on specific project context):
- High-stakes + slow feedback (medicine, law, production security): 75–90%
- Medium-stakes + medium feedback (data science, web dev, hardware): 50–65%
- Low-stakes + fast feedback (coding prototypes, trading backtests, hobby projects): 25–40%

Deliver:
1. The rationale for the chosen threshold
2. Which 1–2 dimensions to prioritize for patching (bottleneck + next lowest score)
3. Specific resources (docs, repos, papers) to reach threshold
4. A "launch checklist" with observable signals

## Output Format

Return a markdown report with this exact structure:

```markdown
# Domain Map: [Domain Name]
Date: [YYYY-MM-DD]
Goal: [User's project goal]

## Dimensions
| Dimension | Coverage | Threshold | Status |
|-----------|----------|-----------|--------|
| ...       | ...%     | ...%      | 🔴🟡🟢 |

Status rules: 🟢 if Coverage ≥ Threshold; 🟡 if Coverage ≥ Threshold × 0.7; 🔴 otherwise.

## Critical Blind Spots (Top 3)
1. **[Dimension]**: [Blind spot] → [Action]
2. ...
3. ...

## Launch Decision
- [ ] GO — Start project. Parallel track: patch [Dimension] to [X]%
- [ ] NO-GO — First patch [Dimension] to [X]%. Estimated time: [Y]

## Re-audit Triggers
- When [signal], revisit [dimension]
```

## Error Handling

- If user cannot answer questions in a dimension: Switch to "exploratory mode" 
  — provide all correct answers immediately and ask the user to self-rate 
  confidence (high / medium / low) on each instead. Trigger exploratory mode 
  when either (a) the user fails or skips 3+ consecutive questions in a dimension, 
  or (b) the user explicitly asks to skip the dimension.
- If domain is too broad: Ask user to narrow to a specific project or 
  deliverable before proceeding.
- If user disputes a "correct" answer: Flag it as "contested / paradigm-dependent" 
  and note the dominant vs. alternative view.

## Examples

### Example Invocation

User: "I want to build a momentum strategy on QQQ constituents but I don't 
know where to start."

Agent response: "I'll run a domain map scan for quantitative momentum trading. 
First, the 6 core dimensions..."

### Example Output Snippet

See `{baseDir}/resources/examples/sample-output.md` for a full rendered example.

### End-to-End Demo Walkthrough

See `{baseDir}/demo/quant-factor-research-agent.md` for a complete, annotated walkthrough covering:
- Domain deconstruction across two templates (trading + agent systems)
- 6 dimensions with 30 T/F questions and answer rationales
- Coverage scoring and contested-question handling
- Final launch decision with risk-calibrated threshold

## Guardrails

- T/F answers reflect mainstream consensus, not absolute truth. Flag contested 
  topics explicitly without fabricating consensus percentages.
- Thresholds are advisory. User overrides only after the agent restates the risk 
  and the user responds with an explicit go-ahead (e.g., "确认继续", 
  "是的，继续", "I accept the risk and want to proceed").
- Re-audit is user-initiated. Suggest the user re-run a domain map scan when: 
  (a) project scope changes significantly, (b) a milestone is reached and new 
  unknowns surface, or (c) after 2–4 weeks of active work as a routine check-in. 
  Each re-audit should be scoped to the project's current state and open questions, 
  not a full reset.
- Never embed credentials, API keys, or absolute file paths in skill output.
- During the scan phase, do not write executable code, configure production 
  environments, submit real orders, send submission emails, deploy services to 
  public networks, or use live API credentials. The scan phase is limited to 
  concept explanation, resource recommendation, pseudocode, environment prep 
  checklists, and dependency installation guides.
