<h1 align="center">Blind Spot Scanner</h1>

<p align="center">
  <b>Tackling an invisible problem: you don't know what you don't know.</b><br>
  Structured cognitive audit · Quantified knowledge gaps · Risk-calibrated launch decisions
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude%20Code-compatible-blue" alt="Claude Code">
  <img src="https://img.shields.io/badge/Kimi%20Code-compatible-green" alt="Kimi Code">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="License">
</p>

<p align="center">
  <a href="./README.zh-CN.md">🇨🇳 Simplified Chinese</a>
</p>

When you enter a new domain, start a new project, or ask an AI for help but feel like you're "not asking the right questions" — the bottleneck is rarely your execution ability. It's that your **knowledge blind spots are invisible to you**. This Skill turns "don't know what you don't know" into quantified, patchable gaps through structured diagnostics, so you can see the map before you start moving.

---

## Why Do You Need This Skill?

| Common Pain | Root Cause | How Blind Spot Scanner Helps |
|-------------|-----------|---------------------------|
| AI always gives "entry-level" answers; feels inefficient | You can't articulate what you don't know | T/F diagnostic questions expose blind spots so AI can fill them precisely |
| Halfway through a project, you discover a critical concept you never considered | Lack of a full domain map upfront | Deconstruct into 5–8 core dimensions first to build a complete picture |
| After studying for a while, unsure if you're ready to start | No objective "readiness" benchmark | Quantified coverage + risk-calibrated go/no-go threshold |
| You know a bit about every topic, but can't connect them | Knowledge silos; missing cross-dimensional links | Cross-dimension questions designed to test integrated understanding |

**Core Value**: Turn "I feel ready" into "I know exactly what's missing, what to prioritize, and how much is enough to start."

---

## When to Activate

- You're exploring a new technical domain or sub-field
- You feel your questions to AI are "low quality" or repetitive
- You've asked for a "learning path," "roadmap," or "where to start"
- You're about to commit to a project but unsure of prerequisite depth
- You want to re-audit or track progress on a previously scanned domain

---

## Workflow

A complete Blind Spot Scanner consists of four phases:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ 1. Deconstruct  │ →  │ 2. Diagnose     │ →  │ 3. Quantify     │ →  │ 4. Gate         │
│                 │    │                 │    │                 │    │                 │
│ Identify 5–8    │    │ 4–6 T/F         │    │ 0–100% coverage │    │ Risk-calibrated │
│ dimensions      │    │ per dimension   │    │ score per dim   │    │ go/no-go        │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Phase Details

**① Deconstruct the Domain**  
Break the target domain into 5–8 core dimensions. If the domain matches a known template (quantitative trading, AI agent systems, academic publishing, etc.), a preset template is loaded as the baseline; otherwise built from first principles.

**② Diagnose Blind Spots**  
Each dimension has 4–6 True/False questions covering:
- Concept definitions (catch definitional errors)
- Common misconceptions / tacit knowledge (catch hidden foot-guns)
- Cross-dimensional intersections (prevent siloed understanding)

Answers are revealed immediately after each question, with concise explanations. If you can't answer, the system automatically switches to "exploratory mode."

**③ Quantify Coverage**  
Each dimension is scored 0–100%, and the bottleneck dimension (lowest score) is identified.

**④ Gate Decision**  
Set a go/no-go threshold based on the project's risk profile (cost of error × feedback speed):
- High cost + slow feedback (medicine, law, production security): 75–90%
- Medium cost + medium feedback (data science, web dev): 50–65%
- Low cost + fast feedback (prototypes, backtests, personal projects): 25–40%

Output includes: threshold rationale, prioritized dimensions to patch, recommended resources, and a launch checklist.

---

## Re-audit

After your first scan, say **"re-audit"** to run a follow-up scan on the same domain. The agent will:

1. **Find your last report** in `docs/blind-spot-scan/`
2. **Ask for confirmation**: "Re-audit the report `blind-spot-scan-[domain]-YYYY-MM-DD.md`?"
3. **Reuse the same dimensions** but rotate questions to test retention + new depth
4. **Generate a Diff appendix** comparing coverage before vs. after:

```
## Re-audit Diff (vs 2024-05-01)

**Data Pipeline:** 35% → 62% (+27%) 📈
**Risk Management:** 58% → 45% (-13%) 📉
**Backtesting:** 75% → 82% (+7%) ➡️

Coverage legend: <60%=🔴  60–79%=🟡  ≥80%=🟢

**Top improvement:** Data Pipeline — from near-blank to tutorial-ready
**Regression alert:** Risk Management — slipped back on tail-risk concepts
```

The Diff uses a render-safe text format (no markdown tables). Trend arrows: +10% or more → 📈 | −10% or more → 📉 | otherwise → ➡️.

**When to re-audit:**
- After 2–4 weeks of active study
- When project scope changes significantly
- After reaching a milestone and encountering new unknowns

---

## Project Structure

```
blind-spot-scanner/
├── SKILL.md                          # Core skill definition (triggers, instructions, output format)
├── demo/
│   ├── README.md                     # Demo directory guide
│   └── quant-factor-research-agent.md  # End-to-end walkthrough: quant factor research agent
└── resources/
    ├── templates/                    # Domain dimension templates
    │   ├── trading-dimensions.md     # Quantitative trading
    │   ├── agent-dimensions.md       # AI agent systems
    │   └── publishing-dimensions.md  # Academic publishing
    └── examples/
        └── sample-output.md          # Sample report output
```

---

## Installation

### Claude Code
```bash
# In your project root or global skills directory
mkdir -p .claude/skills/blind-spot-scanner
# Copy SKILL.md and the resources/ directory to this path
```

### Kimi Code
```bash
mkdir -p .kimi/skills/blind-spot-scanner
# Copy SKILL.md and the resources/ directory to this path
```

### Manual Use (Any AI Assistant)
Simply copy the Instructions section from `SKILL.md` into your system prompt or at the start of a conversation. Works on any platform.

## Quick Start

### Method 1: Auto-Trigger (Claude / Kimi Code)

After installing the Skill to `.claude/skills/` or `.kimi/skills/`, say any of the following keywords in a conversation to auto-activate:

| Trigger Keywords | Example |
|------------------|---------|
| domain map / knowledge audit | "Give me a knowledge audit, I want to learn AI agents" |
| don't know where to start / how to begin | "I want to build a quant strategy but have no idea where to start" |
| learning path / roadmap | "I want to publish an ML paper, help me see what's missing" |
| blind spot / gap / bottleneck | "I feel like my questions to AI are low quality" |

The AI will automatically execute the four-phase scan.

### Method 2: Learn from Demo

[`demo/quant-factor-research-agent.md`](./demo/quant-factor-research-agent.md) is a complete end-to-end example covering:
- Domain deconstruction across two templates (trading + agent systems)
- 6 dimensions, 30 T/F questions with answer rationales
- Coverage scoring and contested-question handling
- Final risk-calibrated launch decision

You can use it as a template — replace the dimensions, questions, and project goal for your own domain.

---

## Sample Output

After the scan, you'll receive a structured Markdown report:

```markdown
# Domain Map: [Domain Name]
Date: YYYY-MM-DD
Goal: [Your project goal]

## Dimensions
| Dimension | Coverage | Threshold | Status |
|-----------|----------|-----------|--------|
| ...       | ...%     | ...%      | 🔴🟡🟢 |

## Critical Blind Spots (Top 3)
1. **[Dimension]**: [Blind spot description] → [Action]

## Launch Decision
- [ ] GO — Start project. Parallel track: patch [Dimension] to [X]%
- [ ] NO-GO — First patch [Dimension] to [X]%. Estimated time: [Y]
```

See [`resources/examples/sample-output.md`](./resources/examples/sample-output.md) for a full rendered example.

---

## Design Principles

1. **Make Blind Spots Visible**  
   What you don't know, if missed, is extremely costly. T/F diagnostic questions are designed to "surface" the things you think you understand but actually have wrong.

2. **Dynamic Thresholds**  
   There is no universal "passing grade." A hobby prototype and a clinical decision system have completely different knowledge-depth requirements. The threshold is determined by project risk, not one-size-fits-all.

3. **Scanning Is Not Learning**  
   Blind Spot Scanner tells you **where** the gaps are and **how much** is enough to start, but it does not write code, train models, or replace execution. It is the "surveying" phase before breaking ground.

4. **Re-Auditable with Diff**  
   Re-running a scan after 2–4 weeks is not a reset — it's a delta. The Diff appendix shows exactly which dimensions improved, which regressed, and why, turning "I think I learned something" into "Data Pipeline +27%, but Risk Management slipped −13%." Re-audit is user-initiated; the agent never runs it automatically.

---

## Built-in Domain Templates

Currently available templates, with more to come:

| Domain | Template | Scenarios |
|--------|----------|-----------|
| Quantitative Trading | `trading-dimensions.md` | Strategy development, backtesting |
| AI Agent | `agent-dimensions.md` | Architecture design, tool orchestration |
| Academic Publishing | `publishing-dimensions.md` | Conference submission, journal review |

If your domain isn't listed, the Skill will generate dimensions from first principles. You're also welcome to contribute new templates.

---

## Contributing

1. **Fork** this repository
2. Add a new template in `resources/templates/` or a walkthrough in `demo/`
3. Ensure the template covers 5–8 dimensions, each with definition, key concepts, and safe-to-proceed criterion
4. Submit a **Pull Request** describing the domain and use case

New domain templates, demo walkthroughs, and improvement suggestions are all welcome. Please make sure:
- Demo walkthroughs include complete question sets, answer explanations, and scoring logic
- You follow the existing directory structure and format conventions

---

## License

MIT
