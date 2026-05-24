<h1 align="center">Blind Spot Scanner</h1>

<p align="center">
  <b>解决一个隐形问题：你不知道自己不知道什么。</b><br>
  结构化认知审计 · 量化知识缺口 · 风险校准启动决策
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude%20Code-compatible-blue" alt="Claude Code">
  <img src="https://img.shields.io/badge/Kimi%20Code-compatible-green" alt="Kimi Code">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="License">
</p>

当你进入一个新领域、启动一个新项目，或者向 AI 求助却总觉得"问不到点子上"时——瓶颈往往不是你的执行力，而是你的**知识盲区本身不可见**。这个 Skill 通过结构化诊断，把"不知道自己不知道"转化为可量化、可修补的具体缺口，帮助你在动手之前先看清地图。

---

## 为什么需要这个 Skill？

| 常见困境 | 根本原因 | Blind Spot Scanner 的解法 |
|---------|---------|----------------------|
| 向 AI 提问总是得到"入门级"回答，感觉低效 | 你无法表达你不知道什么 | 用 T/F 诊断题暴露盲区，让 AI 精准补位 |
| 项目做到一半才发现关键概念完全没考虑 | 前期缺乏领域全貌 | 先拆解 5–8 个核心维度，建立完整地图 |
| 学了半天，不确定自己够不够格开始动手 | 缺乏客观的"就绪度"标尺 | 量化覆盖率 + 风险校准的 go/no-go 门槛 |
| 每个知识点都懂一点，但串不起来 | 知识孤岛，缺少跨维度连接 | 专门设计交叉维度问题，检测融会贯通程度 |

**核心价值**：把"感觉准备好了"变成"知道哪里没准备好、优先补哪里、补到什么程度可以启动"。

---

## 什么时候激活

- 你要进入一个新的技术领域或子方向
- 你觉得问 AI 的问题"质量很低"或总是重复
- 你要了一份"学习路线"或"入门指南"
- 你准备立项，但不确定前置知识深度够不够

---

## 工作流程

一次完整的 Blind Spot Scanner 包含四个阶段：

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  1. 拆解领域     │ → │  2. 诊断盲区     │ → │  3. 量化覆盖     │ → │  4. 启动决策     │
│                 │    │                 │    │                 │    │                 │
│ 识别5-8个核心    │    │ 每维度4-6道     │    │ 各维度0-100%    │    │ 风险校准的       │
│ 维度+关键概念    │    │ T/F诊断题       │    │ 覆盖率评分      │    │ go/no-go门槛    │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 阶段详解

**① 拆解领域**  
将目标领域分解为 5–8 个核心维度。如果领域匹配已知模板（量化交易、AI Agent 系统、学术出版等），会加载预设模板作为基线；否则从零构建。

**② 诊断盲区**  
每个维度 4–6 道 True/False 题，覆盖：
- 概念定义（抓定义性错误）
- 常见误区/隐性知识（抓隐藏的坑）
- 跨维度交叉点（防止知识孤岛）

逐题作答后立即揭示答案与解释，答不上来会自动切换为"探索模式"。

**③ 量化覆盖**  
每个维度 0–100% 评分，并定位瓶颈维度（得分最低项）。

**④ 启动决策**  
根据项目风险画像（错误成本 × 反馈速度）设定 go/no-go 门槛：
- 高代价 + 慢反馈（医疗、法律、生产安全）：75–90%
- 中代价 + 中反馈（数据科学、Web 开发）：50–65%
- 低代价 + 快反馈（原型、回测、个人项目）：25–40%

输出包含：门槛 rationale、优先修补维度、推荐资源、启动检查清单。

---

## 项目结构

```
blind-spot-scanner/
├── SKILL.md                          # Skill 核心定义（触发条件、指令、输出格式）
├── demo/
│   ├── README.md                     # Demo 目录说明
│   └── quant-factor-research-agent.md  # 完整走查示例：量化因子研究 Agent
├── resources/
│   ├── templates/                    # 领域维度模板
│   │   ├── trading-dimensions.md     # 量化交易
│   │   ├── agent-dimensions.md       # AI Agent 系统
│   │   └── publishing-dimensions.md  # 学术出版
│   └── examples/
│       └── sample-output.md          # 报告输出格式示例
└── scripts/
    └── generate-report.py            # 报告生成辅助脚本
```

---

## 安装

### Claude Code
```bash
# 在你的项目根目录或全局 skills 目录
mkdir -p .claude/skills/blind-spot-scanner
# 将 SKILL.md 和 resources/ 目录复制到该路径
```

### Kimi Code
```bash
mkdir -p .kimi/skills/blind-spot-scanner
# 将 SKILL.md 和 resources/ 目录复制到该路径
```

### 手动使用（任意 AI 助手）
直接复制 `SKILL.md` 中的 Instructions 部分到系统提示词（system prompt）或对话开头即可生效，不依赖特定平台。

## 快速开始

### 方式一：自动触发（Claude / Kimi Code）

确保 Skill 已安装到 `.claude/skills/` 或 `.kimi/skills/` 目录后，在对话中说出以下任意关键词即可自动激活：

| 触发语 | 示例 |
|--------|------|
| 领域扫描 / Domain Map / 知识审计 | "给我做个知识审计，我要入门 AI Agent" |
| 不知道从哪里开始 / 怎么入手 | "我想做量化策略，但完全不知道从哪里开始" |
| 学习路线 / 入门指南 / roadmap | "我要发 ML 顶会，帮我看看缺什么" |
| 盲区 / 缺口 / 瓶颈 | "我感觉自己问 AI 的问题质量很低" |

AI 会自动执行四阶段扫描流程。

### 方式二：阅读 Demo 自学

[`demo/quant-factor-research-agent.md`](./demo/quant-factor-research-agent.md) 是一个完整的端到端示例，覆盖：
- 跨两个模板（交易 + Agent 系统）的领域拆解
- 6 个维度、30 道 T/F 题及答案解析
- 覆盖率评分与争议题处理
- 最终风险校准启动决策

你可以把它当作"模板"，替换其中的维度、题目和项目目标，用于自己的领域。

---

## 输出样例

扫描完成后，你会得到一份结构化的 Markdown 报告：

```markdown
# Domain Map: [领域名称]
Date: 2026-05-24
Goal: [你的项目目标]

## Dimensions
| Dimension | Coverage | Threshold | Status |
|-----------|----------|-----------|--------|
| ...       | ...%     | ...%      | 🔴🟡🟢 |

## Critical Blind Spots (Top 3)
1. **[维度]**: [盲区描述] → [行动建议]

## Launch Decision
- [ ] GO — 可以启动，并行修补 [维度] 至 [X]%
- [ ] NO-GO — 先修补 [维度] 至 [X]%，预计耗时 [Y]
```

完整样例见 [`resources/examples/sample-output.md`](./resources/examples/sample-output.md)。

---

## 设计原则

1. **盲区显性化**  
   你不知道的东西如果被遗漏，成本极高。T/F 诊断题的设计目标就是"逼出"那些你以为自己懂、其实理解有偏差的点。

2. **门槛动态化**  
   没有统一的"及格线"。一个 hobby 原型和一个临床决策系统的知识深度要求完全不同。门槛由项目风险决定，不是一刀切。

3. **扫描不等于学习**  
   Blind Spot Scanner 告诉你**哪里**有缺口、**补到什么程度**可以启动，但它本身不产生代码、不训练模型、不替代执行。它是动手之前的"勘测"阶段。

4. **可重复审计**  
   建议项目范围变更、到达里程碑、或持续工作 2–4 周后重新扫描，追踪知识覆盖率的变化。

---

## 适用领域模板

当前内置模板覆盖以下领域，持续扩展中：

| 领域 | 模板 | 场景 |
|------|------|------|
| 量化交易 | `trading-dimensions.md` | 策略开发、回测 |
| AI Agent | `agent-dimensions.md` | 架构设计、工具编排 |
| 学术出版 | `publishing-dimensions.md` | 顶会投稿、期刊评审 |

如果你的领域不在列表中，Skill 会从第一性原理生成维度，你也可以贡献新模板。

---

## 贡献

1. **Fork** 本仓库
2. 在 `resources/templates/` 添加新模板，或在 `demo/` 添加走查案例
3. 确保新模板覆盖 5–8 个维度，每个维度含定义、关键概念、safe-to-proceed 标准
4. 提交 **Pull Request**，描述你覆盖的领域和使用场景

欢迎提交新的领域模板、Demo 走查或改进建议。请确保：
- Demo 走查包含完整的问题集、答案解释和评分逻辑
- 遵循现有目录结构和格式规范

---

## License

MIT
