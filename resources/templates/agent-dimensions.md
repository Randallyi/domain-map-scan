# AI Agent Systems Dimensions

Use this template when the domain involves building, deploying, or evaluating 
autonomous AI agents.

## Dimensions

1. **Agent Architecture**
   - Definition: Core structural patterns for autonomous agent design
   - Key concepts: ReAct, Reflexion, Plan-and-Solve, multi-agent orchestration, tool calling, function schemas
   - Safe-to-proceed: Can explain trade-offs between monolithic and multi-agent architectures for a given task

2. **Tool Use & Integration**
   - Definition: Connecting agents to external capabilities and APIs
   - Key concepts: tool definitions, parameter validation, error handling, rate limiting, tool selection strategies
   - Safe-to-proceed: Can design a tool schema with proper typing, descriptions, and fallback behavior

3. **Memory & State Management**
   - Definition: Persisting and retrieving context across agent interactions
   - Key concepts: short-term vs. long-term memory, vector stores, conversation history, state machines, context windows
   - Safe-to-proceed: Can implement a memory system that prevents context window overflow while preserving critical state

4. **Planning & Reasoning**
   - Definition: Decomposing goals into actionable steps and handling uncertainty
   - Key concepts: chain-of-thought, tree-of-thought, hierarchical planning, backtracking, goal decomposition
   - Safe-to-proceed: Can identify when an agent plan is overly optimistic (missing failure branches)

5. **Safety & Alignment**
   - Definition: Ensuring agents behave within acceptable boundaries
   - Key concepts: prompt injection, output filtering, human-in-the-loop, reward hacking, constitutional AI
   - Safe-to-proceed: Can list 3+ attack vectors and corresponding mitigations for an agent handling user data

6. **Evaluation & Monitoring**
   - Definition: Measuring agent performance and detecting degradation
   - Key concepts: task success rate, hallucination detection, latency benchmarking, A/B testing, drift detection
   - Safe-to-proceed: Can design an evaluation suite with at least 2 success metrics and 1 safety metric
