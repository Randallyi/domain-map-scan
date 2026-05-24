# Demo: Blind Spot Scanner — Quantitative Factor Research Agent

> **Project Goal**: Build an AI agent that can perform quantitative factor research workflows like a human quant researcher,敏锐ly identify potential factors, and generate testable hypotheses.
>
> **Date**: 2026-05-24

---

## Phase 1: Domain Deconstruction

### Template Matching

This project spans two known template domains:
- **Trading** (`../resources/templates/trading-dimensions.md`) — quantitative strategy development, backtesting, signal generation
- **Agent Systems** (`../resources/templates/agent-dimensions.md`) — autonomous AI agent architecture, tool use, planning

**Custom dimensions** were created by fusing and specializing from both templates, keeping the count within the recommended 5–8 range.

### Final Dimensions (6)

| # | Dimension | Definition | Key Concepts | Safe-to-Proceed Criterion |
|---|-----------|-----------|--------------|--------------------------|
| 1 | **Factor Economics & Domain Knowledge** | Understanding the sources of factor premia, behavioral finance mechanisms, and why factors decay over time | Risk premium vs mispricing, behavioral biases (momentum/reversal), factor crowding, factor lifecycle | Can explain the economic intuition behind 3+ classical factors (e.g., momentum, value, quality) |
| 2 | **Data Engineering & Factor Computation** | The full pipeline from raw market data to computable factors, including cleaning, alignment, and derived features | Look-ahead bias, survivorship bias, adjustment of prices, point-in-time data, missing value handling | Can identify 5+ data quality issues that invalidate backtests |
| 3 | **Factor Testing & Statistical Methods** | Rigorous statistical validation of factor predictive power, avoiding spurious correlations and multiple testing traps | IC/IR, quantile portfolio tests, Newey-West adjustment, Bonferroni/FDR correction, bootstrap | Can design a complete factor testing workflow including Rank IC and long-short return tests |
| 4 | **AI Agent Architecture & Workflow Orchestration** | Modeling quant research workflows (hypothesis → data → test → conclusion) as dynamic, agent-executable pipelines | ReAct/Plan-and-Solve, DAG orchestration, tool calling, memory management, human-in-the-loop | Can diagram the agent decision flow from "observing market anomaly" to "generating testable hypothesis" |
| 5 | **Hypothesis Generation & Creative Discovery** | How the agent proactively identifies potential factors — the core differentiator of this project | Cross-asset analogy, literature migration, counterfactual reasoning, anomaly detection, narrative-driven discovery | Can describe 3+ mechanisms for "machine-generated factor ideas" and assess their novelty |
| 6 | **Overfitting Control & Robustness Assessment** | Ensuring agent-discovered factors remain valid out-of-sample, across markets, and under regime changes | Out-of-sample decay, parameter stability, regime detection, transaction costs, implementation shortfall | Can explain why a backtested Sharpe=3 factor might only achieve Sharpe=0.5 in live trading |

---

## Phase 2: Diagnostic T/F Questions

### Dimension 1: Factor Economics & Domain Knowledge

**Q1.1** Momentum factor premia primarily stem from investor underreaction to new information, falling under the "mispricing" category in behavioral finance rather than compensation for systematic risk.

**Q1.2** When a factor is heavily crowded (factor crowding), its future returns typically *increase* because more capital inflow strengthens its price discovery function.

**Q1.3** The value factor's persistent underperformance in US equities post-2009 is evidence that "value is dead" — i.e., the factor's underlying economic mechanism has permanently broken down.

**Q1.4** For a factor to be recognized as a "true" anomaly in academic research, it typically needs to satisfy three conditions: significant out-of-sample, present across asset classes, and not explained by existing risk factor models.

**Q1.5** The quality factor and low-volatility factor, while often positively correlated empirically, have fundamentally different economic intuitions: quality relies on firm fundamental robustness, while low volatility relies on market participants' leverage constraints and lottery preferences.

#### User Responses

| Question | User Answer | Correct | Explanation |
|----------|-------------|---------|-------------|
| Q1.1 | **T** | ✅ T | Momentum is mainly explained by underreaction and slow information diffusion — behavioral mispricing, not risk compensation. |
| Q1.2 | **F** | ✅ F | Factor crowding typically *compresses* future returns. When too much capital chases the same signal, arbitrage capacity is exhausted, and unwinding can cause violent reversals. |
| Q1.3 | **F** | ✅ F | Value's underperformance is controversial. Dominant alternative explanations include: changing accounting standards (intangibles not captured), outdated metrics (P/B vs modern measures), and cyclical underperformance — not necessarily permanent failure. |
| Q1.4 | **T** | ✅ T | The "robustness triad" of academic factor research: out-of-sample significance, cross-market presence, and non-absorption by existing risk models. |
| Q1.5 | **T** | ✅ T | Quality = fundamental robustness (high ROE, low leverage, stable earnings). Low vol = lottery preference (investors favor high-vol stocks) + leverage constraints. Different mechanisms, often correlated empirically. |

**Coverage: 100%** (5/5 correct)

---

### Dimension 2: Data Engineering & Factor Computation

**Q2.1** When building a point-in-time factor database, using the "filing date" is more critical than using the "period end date" because the former effectively prevents look-ahead bias.

**Q2.2** If a quant team uses current S&P 500 constituents' historical data to backtest a 2010–2020 strategy without accounting for constituent changes over time, this bias is called survivorship bias and will significantly inflate strategy returns.

**Q2.3** When computing price-volume factors (e.g., 20-day returns), the difference between adjusted prices and unadjusted prices is only in magnitude and does not materially affect cross-sectional ranking.

**Q2.4** When a factor involves cross-calculation of financial statement data (e.g., net income) and market price data (e.g., market cap) — such as P/E = market cap / net income — with quarterly financials and daily market data, the proper approach is "use the market cap at the time when the financial report was available," not "use the latest market cap with the latest financials."

**Q2.5** When handling suspended stocks, simply forward-filling returns is usually safe because the true return during suspension is zero and will not affect the cross-sectional distribution.

#### User Responses

| Question | User Answer | Correct | Explanation |
|----------|-------------|---------|-------------|
| Q2.1 | **不清楚** | 🔍 T | **Filing date** is the cornerstone of point-in-time data. Using period-end date assumes the market knew the report content on that date — classic look-ahead bias. |
| Q2.2 | **F** | ❌ T | This **is** survivorship bias. Current constituents are the "survivors"; delisted/bankrupt/acquired stocks are silently removed. Backtesting with current constituents systematically overstates returns. |
| Q2.3 | **不清楚** | 🔍 F | The difference is **not just magnitude**. Unadjusted prices drop on ex-dividend dates, creating false losses that distort return calculations and rankings. Adjusted prices are mandatory for any return-based factor. |
| Q2.4 | **T** | ✅ T | This is the **point-in-time alignment principle**: at any point in time, only use data "known at that time." Using today's market cap with last quarter's earnings is looking into the future. |
| Q2.5 | **T** | ❌ F | Returns during suspension are **not zero** — they are **unobserved**. Forward-filling masks post-resumption gap risk and creates false safety in cross-sectional analysis. Proper handling requires special flags, exclusion, or post-resumption window treatment. |

**Coverage: ~30%** (1/5 definitively correct, 2 unclear, 2 wrong)

---

### Dimension 3: Factor Testing & Statistical Methods

**Q3.1** In single-factor testing, Rank IC (Spearman correlation) is preferred over Pearson IC because Rank IC is less sensitive to outliers and better aligns with the "rank-based stock selection" practice in factor investing.

**Q3.2** If a researcher tests 100 factors and finds 5 significant at the 5% level, these 5 factors can be considered "truly effective" because the 5% significance level already controls the false positive rate.

**Q3.3** When computing a factor's Information Ratio (IR = mean(IC) / std(IC)), higher volatility in the IC time series means worse prediction stability, thus a lower Information Ratio.

**Q3.4** In quantile portfolio tests, if a factor is effective, one typically expects a monotonic return distribution: i.e., the top quantile portfolio's return should systematically exceed the 2nd quantile, and so on down to the 10th quantile.

**Q3.5** When a factor's autocorrelation is low (e.g., monthly IC autocorrelation near 0 for a monthly-rebalanced factor), this means the factor's predictive power is completely independent across time periods, so Newey-West adjustment is unnecessary for statistical inference.

#### User Responses

| Question | User Answer | Correct | Explanation |
|----------|-------------|---------|-------------|
| Q3.1 | **不知道** | 🔍 T | **Rank IC** is indeed preferred. Pearson is outlier-sensitive; factor investing is fundamentally about **ranking** (which stocks are top vs bottom), making Rank IC the natural choice. |
| Q3.2 | **T** | ❌ F | This is the classic **multiple testing problem**. With 100 random factors, you'd expect ~5 to appear significant at 5% by chance (100 × 0.05 = 5). Without correction (Bonferroni, FDR), false positives run rampant. |
| Q3.3 | **T** | ✅ T | IR = mean(IC) / IC volatility. Higher denominator → lower IR. IR measures **prediction stability** — a high IR means consistent, stable predictive power. |
| Q3.4 | **T** | ✅ T | Monotonicity is the **signature** of quantile tests. A flat or inverted return curve signals noise or structural breaks. |
| Q3.5 | **T** | ❌ F | Financial time series are **rarely truly independent**. Even with low 1st-order autocorrelation, **volatility clustering** (heteroskedasticity) or higher-order autocorrelation may exist. Newey-West is a conservative robust standard error practice recommended in nearly all factor research. |

**Coverage: ~45%** (3/5 conceptually correct, but weak on multiple testing and robust inference)

---

### Dimension 4: AI Agent Architecture & Workflow Orchestration

**Q4.1** When building a quant factor research agent, a "single agent + rich toolset" architecture is typically easier to debug than a "multi-agent collaboration" architecture, but for complex multi-step research workflows (hypothesis → data acquisition → factor computation → backtest → report), multi-agent architectures better isolate failures and support modular iteration.

**Q4.2** To enable an agent to execute quantitative backtests, best practice is to encapsulate the backtest engine as a "tool" that the agent calls with parameters (factor definition, parameter range, time window), rather than having the agent directly generate executable Python backtest code and run it in the current environment.

**Q4.3** In agent memory design, storing every factor research attempt (hypothesis, data used, test results, failure reasons) into long-term memory provides no substantial help for the agent's "learning ability," because factor return structures are time-varying and historical experience cannot directly transfer to the future.

**Q4.4** ReAct (Reasoning + Acting) mode makes the agent output a thought process (Thought) before deciding on an action (Action). For a quant factor research agent, this explicit chain of thought helps researchers audit the agent's decision logic — e.g., "why does the agent think this factor is worth further testing?"

**Q4.5** Introducing "human-in-the-loop" (HITL) nodes in an agent workflow is typically an unnecessary slowdown, because quantitative research emphasizes automation and speed, and manual review undermines the core value of the agent system.

#### User Responses

| Question | User Answer | Correct | Explanation |
|----------|-------------|---------|-------------|
| Q4.1 | **T** | ✅ T | Classic **modularity vs simplicity tradeoff**. Single-agent has shorter debug paths; multi-agent isolates failure domains and supports independent iteration — critical for complex 5-step research pipelines. |
| Q4.2 | **T** | ✅ T | **Encapsulation as tools is best practice.** Letting agents generate and execute arbitrary Python code opens an ACE (arbitrary code execution) vulnerability with uncontrolled outputs. Tool-based interfaces constrain parameters via schemas and return structured results. |
| Q4.3 | **F** | ✅ F | Historical experience **is valuable**. Agents can learn: which hypothesis types are often falsified, which data sources have reliable lag patterns, which testing pipelines are prone to overfitting. This is the agent's "institutional memory." |
| Q4.4 | **T** | ✅ T | ReAct's explicit **Thought** is the audit lifeline of quant research agents. When an agent decides to "test this factor," researchers need to see its reasoning path (e.g., "this factor is momentum-related but adds volatility adjustment; literature X shows this combination has additional explanatory power in bear markets"). |
| Q4.5 | **T** | ❌ F | In factor research, HITL is **not a slowdown but a guardrail**. Agents can mine statistically significant but economically absurd factors (e.g., "stocks with ticker containing letter A have higher returns"). Human review is irreplaceable at hypothesis generation, economic intuition validation, and overfitting prevention. Fully automated "black-box research" carries extreme risk. |

**Coverage: 80%** (4/5 correct — solid understanding of agent architecture and workflow design)

---

### Dimension 5: Hypothesis Generation & Creative Discovery

**Q5.1** Having an agent read academic literature (e.g., JF, JFE, RFS top journal papers) and automatically extract factor definitions and testing methods is an effective "hypothesis generation" strategy, because these factors may retain predictive power out-of-sample.

**Q5.2** If an agent discovers the pattern "stocks with abnormally low average trading volume over the past 20 days perform better over the next month," this pattern itself already constitutes a tradable factor hypothesis that can be directly put into backtests and live trading without further economic explanation.

**Q5.3** "Cross-market migration" is an effective creative discovery mechanism: e.g., after an agent finds that "earnings momentum" works in US equities, it can attempt to migrate the factor to A-shares or commodity futures and test its applicability.

**Q5.4** To avoid data mining bias, when generating factor hypotheses, an agent should prioritize starting from economic theory or behavioral finance mechanisms, then seek data validation; rather than first scanning patterns in data and then reverse-engineering post-hoc economic stories.

**Q5.5** An agent can discover emerging factors by monitoring narrative changes in social media, news, and analyst reports. For example, when the "AI computing power" narrative emerges, the agent automatically constructs an "AI supply chain exposure" factor and tests its pricing power. This is a reasonable factor discovery path.

#### User Responses

| Question | User Answer | Correct | Explanation |
|----------|-------------|---------|-------------|
| Q5.1 | **T** | ✅ T | Academic literature migration is a **classic hypothesis generation path**. Top-journal factors have survived peer review with relatively clear economic mechanisms. Agents can automatically parse factor definitions, construction methods, and test samples, then run out-of-sample validation in new markets/time periods. |
| Q5.2 | **T** | ❌ F | **Statistical pattern ≠ tradable factor.** Without economic explanation, a pattern is likely overfitting, survivorship bias, or random noise. The iron law of quant research: rationale first (economic/behavioral mechanism), data second. Running backtests just because "a pattern exists" is the breeding ground for data mining. |
| Q5.3 | **T** | ✅ T | **Cross-market migration** is common in quant research. The same economic mechanism (e.g., earnings momentum reflecting slow information diffusion) may exist with different intensities across markets. Systematic migration testing by agents can reveal globally effective vs market-specific factors. |
| Q5.4 | **F** | ❌ T | This is the core of the **"theory-driven vs data-driven"** debate. While pure data mining (e.g., deep learning discovering nonlinear patterns) has value, if the goal is **avoiding data mining bias**, theory-first is the gold standard. Start with a testable mechanism hypothesis, then validate with data — far more reliable than "scan data first, construct story later." |
| Q5.5 | **T** | ✅ T | **Narrative-based factors** are a frontier direction. Agents can use NLP to monitor thematic evolution in news, research reports, and social media (e.g., "AI computing power," "carbon neutrality"), construct exposure metrics, and test their pricing power. This complements traditional factors by capturing structural changes. |

**Coverage: ~60%** (3/5 correct — strong intuition on cross-market migration and narrative-driven discovery, but weak on the "pattern vs rationale" boundary)

---

### Dimension 6: Overfitting Control & Robustness Assessment

**Q6.1** If a factor performs well in an in-sample backtest (Sharpe = 2.5) from 2010–2020 but shows near-zero returns in an out-of-sample test from 2020–2024, this is more likely due to the factor having no genuine predictive power rather than temporary failure caused by market regime changes.

**Q6.2** When assessing a factor's parameter robustness, if the factor performs well at parameter A (e.g., 20-day formation) and parameter B (e.g., 25-day formation) but fails at parameter C (e.g., 100-day formation), this still suggests the factor has some robustness because performance did not collapse within a reasonable parameter range.

**Q6.3** "Implementation shortfall" refers to the gap between a factor's paper backtest returns and the actually achievable returns after accounting for transaction costs, slippage, and market impact. For high-turnover factors, implementation shortfall is typically larger.

**Q6.4** When conducting regime detection, if an agent finds a factor works in bull markets but fails in bear markets, the best approach is to label the factor as "bull-market only" and completely disable it in bear markets, rather than trying to find complementary factors that work when this factor fails.

**Q6.5** Even if a factor has been stable over a long period (10+ years), this does not guarantee future effectiveness, because market structure changes (declining retail participation, algorithmic trading proliferation, regulatory changes) can permanently destroy the underlying mechanisms of certain factors.

#### User Responses

| Question | User Answer | Correct | Explanation |
|----------|-------------|---------|-------------|
| Q6.1 | **F** | ⚠️ Contested | The **dominant interpretation** of out-of-sample failure is overfitting (the factor lacks genuine power), but **regime change** is a valid alternative hypothesis. In mainstream quant practice, the inference priority is: first rule out overfitting/data mining, then consider regime change. The statement leans **T** in a statistical inference framework, but your regime perspective is a reasonable alternative view. |
| Q6.2 | **T** | ✅ T | Robustness within a reasonable range (20→25 days) means the factor is not "dancing on a knife's edge." Failure at 100 days actually validates that the factor has a specific **time scale** — this strengthens rather than weakens credibility. |
| Q6.3 | **T** | ✅ T | **Implementation shortfall** = paper returns − actually achievable returns. High-turnover factors trade frequently, accumulating higher friction costs. This is the critical threshold separating "academic factors" from "tradable factors." |
| Q6.4 | **F** | ✅ F | **Simple regime switching is dangerous.** Accurately predicting bull/bear transitions is itself hard; "complete disablement" leads to frequent wrong-way switching. Better strategies: find **complementary factors** (e.g., momentum + quality) to build regime-robust portfolios, or use dynamic weighting. |
| Q6.5 | **T** | ✅ T | Factor **half-lives** are real. Market structure changes (retail→institutional, human→algorithmic, regulatory tightening) can permanently destroy a factor's underlying mechanism. Agents need built-in "factor decay detection," not an assumption that history repeats. |

**Coverage: ~90%** (strong understanding of overfitting, implementation shortfall, and market structure evolution)

---

## Phase 3: Coverage Quantification

| Dimension | Coverage | Level Description |
|-----------|----------|-------------------|
| 1. Factor Economics | 100% | Can teach others |
| 2. Data Engineering | ~30% | Concepts fuzzy, systemic errors likely |
| 3. Statistical Methods | ~45% | Can follow tutorials, likely to get stuck |
| 4. Agent Architecture | 80% | Can execute with reference docs |
| 5. Hypothesis Generation | ~60% | Can execute with reference docs |
| 6. Overfitting Control | ~90% | Can teach others |

**Bottleneck dimension**: Dimension 2 (Data Engineering & Factor Computation)

---

## Phase 4: Launch Decision

### Risk Profile Analysis

| Factor | Assessment | Rationale |
|--------|-----------|-----------|
| Domain Risk | Medium | Factor research errors can lead to live trading losses, but are not irreversible (unlike medical or legal applications) |
| Iteration Cost | Medium | Backtests run in minutes, but full factor research-to-validation cycles take days/weeks |
| Feedback Loop Speed | Medium-Fast | Backtests provide rapid feedback; sample-out validation requires real time to pass |

**Threshold**: 55% (Medium-stakes + medium feedback speed range: 50–65%)

### Final Report

```markdown
# Domain Map: 量化交易因子研究 Agent
Date: 2026-05-24
Goal: Build an AI agent that performs quant factor research workflows and generates testable hypotheses

## Dimensions
| Dimension | Coverage | Threshold | Status |
|-----------|----------|-----------|--------|
| 1. Factor Economics | 100% | 55% | 🟢 |
| 2. Data Engineering | ~30% | 55% | 🔴 |
| 3. Statistical Methods | ~45% | 55% | 🟡 |
| 4. Agent Architecture | 80% | 55% | 🟢 |
| 5. Hypothesis Generation | ~60% | 55% | 🟢 |
| 6. Overfitting Control | ~90% | 55% | 🟢 |

## Critical Blind Spots (Top 3)
1. **Data Engineering (30%)**: Weak grasp of point-in-time alignment, survivorship bias, and price adjustment
   → Action: Build a point-in-time P/E factor pipeline using filing dates; compare adjusted vs unadjusted price rankings
2. **Statistical Methods (45%)**: Insufficient awareness of multiple testing correction and robust standard errors
   → Action: Read Harvey, Liu & Zhu (2016); implement FDR-corrected backtesting framework
3. **Hypothesis Generation (60%)**: Unclear boundary between "data mining" and "theory-driven" discovery
   → Action: Design an "economic plausibility check" layer requiring agents to output economic intuition before backtesting

## Launch Decision
- [ ] GO — Start project. Parallel track: patch Data Engineering to 55%+
- [x] NO-GO — First patch Data Engineering and Statistical Methods to threshold. Estimated time: 2–3 weeks

## Re-audit Triggers
- When agent runs first end-to-end pipeline, revisit Dimensions 2 & 3
- When agent produces first "significant" factor (Sharpe > 2.0), revisit Dimension 6
- When preparing for paper/live trading, revisit all dimensions
- Routine re-audit: 2–4 weeks
```

---

## Key Takeaways for Skill Users

1. **Template fusion**: When a project spans multiple domains (here: trading + agent systems), fuse templates rather than choosing one. Maintain 5–8 dimensions.
2. **Contested questions are OK**: Q6.1 was flagged as contested because quant inference involves paradigm-dependent priors. Always note dominant vs alternative views.
3. **Bottleneck drives the decision**: Even with 3 dimensions at 🟢, one 🔴 dimension (Data Engineering) can block launch because it introduces systemic, hard-to-detect errors.
4. **Parallel patching**: For medium-risk domains, conditional GO with parallel patching is acceptable if the user explicitly accepts risk. NO-GO is the safer default.
