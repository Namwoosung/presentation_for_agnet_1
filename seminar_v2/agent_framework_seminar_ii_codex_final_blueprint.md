# Agent Framework Seminar II — Final Production Blueprint for Codex

> **Document language:** Korean for the presenter and audience; English identifiers and technical terms are retained where precision requires them.  
> **Target:** Codex coding agent. **Artifact:** independently usable production brief for an HTML presentation, two real-agent Trace demos, verification suite, and migration guide.  
> **Authoring baseline:** 2026-11-03. **Research status:** design/research blueprint; no claim that an HTML deck, Hermes/PydanticAI run, local relay, target vLLM compatibility, or real Trace has already passed.  
> **Absolute priority:** complete/accurate understanding > readable screens > execution transparency > visual consistency > implementation convenience > slide count/time.  
> **Port ownership:** **Codex builds/uses port 10000**. Port **10001 is reserved for the separate Antigravity implementation**, not a fallback or second server for this document.

## 0. Codex: execute this contract, not a generic slide-generation prompt

**Objective:** Implement a Korean, technically rigorous follow-up seminar that explains how seven Agent technologies *actually* implement, execute, guard, record, and recover Agent behavior. In particular, reveal the difference between **the model requesting an action** and **the runtime/tool process actually executing it**. Demonstrate the actual execution of **Hermes Agent** and **PydanticAI Core** with inspectable, provenance-preserving traces. Be accurate about uncertainty: official documentation, source-code analysis, observed runtime evidence and speculative presentation designs are distinct categories.

**Do not** deliver only a beautiful table of product names. Do not convert this into a generic AI Agent tutorial; the audience already attended part I. Do not predeclare the best product, make up API names, pretend to have executed a command, simulate a live Trace without marking it, or compress away critical technical branches to save slides.

**Execution sequence (follow without asking to reconfirm settled preferences):**

1. Scan the project root `C:\Users\namws\OneDrive\Desktop\study_for_agent_framework` (or repository working directory provided to Codex). Read `AGENTS.md`, original part-I presentation/design, `2차_세미나_발표_흐름.md`, all existing agent framework research files, local notes, and this blueprint. Preserve existing work. If some files are absent, this file is the authoritative self-contained fallback; record what's missing rather than invent it.
2. Create an implementation plan + source/version audit; identify any conflicts between pre-existing sources and this authoritative requirement. The user has already fixed intent, presentation sequence, demo priority, design priorities and port. Implement without scheduling follow-up or asking for nonblocking choices.
3. Investigate the authoritative official docs / installed version source for **every factual claim to be shown onscreen**, especially behavior-dependent claims. Maintain a claim ledger with version, exact official URL or source path, test status, and affected slide IDs. Use the **research baselines** below as baselines, not as an assertion about the latest release or installed environment.
4. Define master diagrams (all seven), common slide data model, 16:9 tokens, Space-only keyboard state machine, and real Trace schema **before** filling slides. Implement in small testable sections. Favor native HTML/CSS/SVG + TypeScript/React/Vite or similarly maintainable stack already present in the repo; do not rewrite an existing working application needlessly.
5. Produce **all slides in Section 8**, with same order and content; additional splitting is mandatory when required for legibility. A slide definition must contain every field in the contract. No filler slides. The 46 legacy identifiers are source anchors, not a 46-slide limit.
6. Build **two separate web demo viewers** from actual framework runs, with isolated setup, real capture, source provenance, and deterministic Space-by-Space REPLAY for presentation. Complete the basic read-only Core paths first; experiment-specific branches may remain marked TEST-PENDING until verified. The live model is not required for every click during the presentation.
7. Implement **Codex-only local 127.0.0.1:10000 OpenAI-compatible relay** to actual OpenAI API with `OPENAI_API_KEY` on the relay process, never the browser. The demo clients address `http://127.0.0.1:10000/v1`. Separately provide a port-preserving, capability-probed deployment recipe for another PC where port 10000 belongs to an existing vLLM proxy. Do not modify that proxy.
8. Run Playwright navigation/visual/semantic tests and Python unit/integration tests; record evidence. Iterate until pass. Produce exact installation, startup, trace-recording, presentation, shutdown, rollback and migration instructions. Identify environmental blockers explicitly rather than claiming success.

**Expected delivery:** Complete `seminar_2/` project plus `README.md`, source ledger, all speaker scripts, slide mapping, screenshots, tests/results, two demo viewers + recorders, local relay, `.env.example`, target-machine migration handbook and a human-readable `QA_REPORT.md`. Slide HTML must work without external network once built; live demos may require the configured model service.

### 0.1 Instruction priority and safety

Priority: explicit user requirements in this document > audited official behavior / evidence for factual correctness > existing presentation design system > nonconflicting project `AGENTS.md` > third-party Skills default aesthetics. If documentation proves a sentence factually false, **correct the sentence** and record it in `claim-ledger.md`, rather than following a false statement for visual consistency. When the old 46-slide plan conflicts with this document's unlimited splits/Space-only rules, this document wins. Never overwrite the user's local research, original diagrams, personal Hermes profile or real database.

**Codex development checkpoints:** before large edits, inspect repo status and create a change plan. After each section, run automatic checks and review actual browser screenshots. If a dependency/API is missing or incompatible, keep other independent deliverables moving. No direct uploads of internal/company datasets to external LLMs. Do not put secrets in commands, commits, screenshots, web responses, local logs or Trace JSON. Never log hidden private reasoning/chain of thought.

## 1. Presentation purpose, scope, narrative, audience

**Presentation title:** `Agent Framework 세미나 2차 — Architecture, Execution & Framework Comparison`.

**Audience:** colleagues who already know the first session's basics: Agent concept, core Loop, Tool Calling, the general ideas of Orchestration/Memory/Skills/MCP. Keep brief contextual reminders (one sentence or mini-icon) only when necessary for a new implementation detail. This session is a practical explanation of actual runtimes, including enough background for someone without source-code experience to follow a complex architecture drawing.

**Fixed presentation order (do not rearrange):**

1. Hermes Agent — deep execution anatomy + independent actual demo 1.
2. Claude Code — other complete Harness, permissions, instructions and collaboration; differences against Hermes.
3. PydanticAI — Pydantic vs Core vs optional Harness; internal graph, tools, output, EndStrategy, approval + independent actual demo 2.
4. OpenAI Agents SDK — Runner, handoff vs agent-as-tool, guardrails, RunState.
5. Claude Agent SDK — Host SDK↔Claude Code CLI runtime, MCP callbacks, permission/session boundary.
6. Google ADK — Runner/Flow/Event/Session and distinct parallel/workflow semantics.
7. Microsoft Agent Framework — Agent Pipeline/Middleware vs Harness vs Superstep Workflow.
8. Cross-framework synthesis, semi-conductor-domain implementation responsibility, central/local deployment decision, next-stage validation agenda.

**Deepest coverage:** Hermes and PydanticAI. In those two sections, don't stop at listing components; show *how a request travels into a runtime, which exact actor makes each decision, when history/session/memory changes, when a tool actually executes, what blocks it, how return/output/error/retry happens, and what the final model sees*. Explain the benefits and tradeoffs grounded in these mechanics. For other technologies emphasize **distinctive control contracts** and the differences from the two central subjects, not re-implementing the full depth of all seven.

**Out of scope:** LangChain/LangGraph as separate framework lecture, Mistral AI Studio, vLLM/SGLang serving internals, speculative market/performance league tables, generic Agent definition lecture, real semiconductor production actions, user-specific manufacturing data. Mention vLLM only to explain endpoint compatibility and deployment responsibility; distinguish the **Hermes Agent** codebase from **Hermes language models**.

**Core conclusions audience must be able to state:**

- Harness-provided Loop/Session/Tools simplify assembly, not data authorization, consistency, audit or deployment.
- PydanticAI Core provides an actual run/Graph/tool/output contract; `Pydantic` schema validation alone is not an Agent runtime, and a separate Harness must not be conflated with Core.
- A Tool call is the model's requested action. Invocation, validation, approval, OS/DB authorization, side effects, retry and result persistence are **runtime/application** operations.
- Tool parallelism, subagent delegation, agent-as-tool, handoff, and graph workflows differ in **Loop, context, ownership and return topology**.
- Memory file, transcript, prompt snapshot, session store, artifact and checkpoint are not interchangeable; persistence doesn't imply complete recovery or exactly-once external side effects.
- Model location and Agent-runtime location are independently selectable. The final selection is an architecture and responsibility decision, not a popularity contest.

**Domain through-line:** The same **synthetic** BIN-X / Lot analysis across all appropriate pages and both demos. Show data snapshot, numerator/denominator, observation cutoff, SOP version, Tool Call ID, evaluation split, prediction model/version, approval and reproducibility. Correlation or a plausible explanation is not proof of physical causality; a validated JSON schema is not evidence that an analysis is true.

## 2. Fixed visual design system (must override Skill defaults)

### 2.1 Screen and type

- **Audience presentation:** single browser-based **16:9, nominal 1920×1080 coordinate stage**, responsive scale to window while keeping entire slide within viewport; no page-level scrolling, no overflow, no endless vertical website, no slide thumbnails, slide selection UI, tabs, click navigation, hover-only disclosure, route transitions requiring mouse or input. This is a projected conference deck, not a dashboard.
- Design language: dark, elegant technical systems lecture; **flat 2D, editable SVG/CSS diagrams** with restrained line/shape motion. No ornamental 3D, glassmorphism, neon overload, gratuitous stock photos or pointless image generation. Use technical structure as visual interest.
- Background `#0B1020`; main text `#EFF4FF`; secondary `#9EACC8`; divider `#33415D`.
- Semantic colors: **Model/Reasoning blue `#60A5FA`**; **Runtime/Harness purple `#B794F4`**; **Tool/External action green `#34D399`**; **Context/Memory orange `#FDBA74`**; **Risk/Failure red `#FB7185`**; **Success teal `#5EEAD4`**.
- At nominal 1920×1080: title 38–54px, main 22–30px, labels 18–24px, code 18–22px; small source ID may be 16–18px if visible. Use Korean-appropriate system fonts (`Pretendard` if legally locally available; otherwise `Noto Sans KR` or accessible sans); NEVER redistribute commercial font files. Approx 7% horizontal and 6% vertical safe margins; no text or arrows clipped at 1920×1080, 1366×768, 1280×720.
- Make **the headline an actual conclusion** (“모델이 Tool을 실행하지 않는다”), not a generic title (“Tool”). One slide = one central question/conclusion. Prefer **diagram > 2–3 short statements**, not essay-sized text. Presentation notes are intentionally rich and separate.
- Diagram conventions: rectangles = actors/components, lanes = distinct thread/process/Agent/participant, solid arrows = actual message/execution, dashed arrows = conditional/possible design, red dashed boundary = trust/approval. Label every important arrow **request, response, Tool Call, return, history write, approval, resume** so arrows aren't decorative. Use `App-owned / Runtime-owned / SDK-owned / Provider-owned` boundary labels and line styles in addition to color.
- For the seven subjects, display one **complete master architecture before** component zooms; use **the same exact master SVG node IDs and coordinates throughout that subject**. Subsequent slides highlight/dim the active subsystem. Changing components arbitrarily between slides harms learning.
- Prefer native SVG for clear architecture/sequence/trace diagrams; CSS and monospaced blocks for code. Avoid giant markdown tables on screen; if two independent claims or a code sample+diagram+result cannot fit at readable size, split into more slides. **There is no slide count or presentation time limit.**
- Motion: 0.25–0.45s ease-out reveal; past steps remain visible but 30–50% dimmer; current step high-contrast outline and label. Preserve all information in a paused frame. Respect `prefers-reduced-motion` by removing animation, not by hiding steps.
- Footer on every slide: section, `slideId`, `build k/n`, succinct source IDs and **provenance of any non-static demo figure**. The audience never needs a click/hover to read a necessary label.

### 2.2 Mandatory single-key audience progression: Space only

A **single Space keypress yields exactly one semantic progression**, first within the current slide then to the next slide. None of the content may depend on `Enter`, arrows, mouse click, toggle, radio, select, tabs, wheel or hover. No automatic progression or auto-loop at the end. Build steps have no timer-based advance; animation is cosmetic only.

**State contract:** `slideId`, `slideIndex`, `stepIndex` (0-based internal), `stepCount`, `sourceRefs`, optionally `traceEventId`. At each page enter show **the first meaningful state** (step 0) and subsequently expose one additional node/edge/state per Space; after its final build, one more Space opens the next slide's first state. Protect against `KeyboardEvent.repeat`, keydown/keyup auto-repeat, default browser scrolling and accidental multiple changes during transitions. Choose a consistent rule for Space pressed while animation runs (discard or queue at most one), test it. Ignore Space if focus somehow resides in a forbidden form element; presentation should not contain forms. At final page, no wrap.

A build is atomic by **meaning**, not necessarily exactly one SVG DOM element. It may reveal `[one actor + its immediately explanatory arrow]`; it may **not** reveal “Guardrail, 3 Tool outputs and 4 conclusions” together. To teach multi-branch decisions, split into further slides or multiple discrete builds. Don't randomly wipe the master diagram between adjacent zoom pages.

**Notes and operator controls:** Presenter notes (`speaker-notes.json`/MD) and operator recording actions live separately from audience routes. Any external link inside notes is for preparation, not a required live-click presentation step. Demo viewers use the same Space contract to step through *previously captured* events; pressing Space **does not pause the live model mid-inference**. No Prev/Play/Stop/Replay/Mode buttons in audience viewers; a separate operator preparation interface or CLI may provide those controls. Fullscreen may be configured before the talk, never required mid-talk.

### 2.3 Template families and architecture reuse

`T-ARCH`: 12% headline, 70% readable full master architecture, 18% legend/takeaway.  
`T-ZOOM`: master minimap top-left, large 55% component/sequence panel, 30% state/invariants/right context; do not squeeze code+diagram+log together.  
`T-SEQ`: actor lanes left-to-right, time top-to-bottom, separate causal arrows from concurrent start/end times.  
`T-COMP`: two equivalent-scale designs with same axes, rather than a wall of small text.  
`T-DECISION`: one conclusion + 3–5 grounded conditions.  
`T-DEMO`: architecture return + actual-observation/capture-scope checklist; no embedded demo server.

## 3. Authoritative evidence, correctness and release discipline

Use **four separate assertion types**: `DOC_CONFIRMED` (official documentation checked), `SOURCE_CONFIRMED` (fixed release file/symbol/line checked), `RUNTIME_OBSERVED` (saved real run and timestamp/capture), `DESIGN_OR_ILLUSTRATIVE` (presentation/architecture proposal). Use `UNVERIFIED` and `NOT_OBSERVED` rather than guessing. A `source_id` maps to an actual URL/release/file/hash; not every official *latest* page describes an older tagged release.

**Existing analysis baseline, not guaranteed current/installed:** Hermes v0.22.5; Claude Code CLI v2.1.314; PydanticAI Core v2.61.0; OpenAI Agents SDK Python v0.24.0; Claude Agent SDK Python v0.2.176 and bundled CLI v2.1.316; Google ADK Python v2.13.0; Microsoft AF Python `python-1.24.0` as recorded in the local research. Verify **whether each exact version/tag and symbol exists** before putting it on a slide, and record the installed version separately. Version labels are research context and must never be described as latest simply because they were used in the prior analysis.

**Source and code discipline:**

- Every content slide must carry at least one authoritative evidence ID where it makes an implementation claim. UI footer may abbreviate IDs; `source-map.json` and notes must expose actual URLs, claim, checked date, target version/commit and any caveat. Source links should be from the actual release tag when naming internal files/methods.
- Official docs may change. Audit in a fresh checkout or source browser; when the current main branch disagrees with fixed local study notes, do not silently adopt a brand-new feature as an old-version behavior.
- **Hermes Agent source**: architecture and Loop implementation are publicly accessible; prefer actual loop/tool/prompt/state source inspection. Don't claim `tool intent is durable before execution` without matching the actual tag; current developer docs describe tool hooks, registry and session persistence, and are not by themselves proof of every proposed fail-closed persistence rule.
- **Claude Code**: document publicly exposed CLI, instructions, permission, hooks, subagents and Teams; do not invent private Agent Loop source files or assert a specific internal runtime implementation was read. The Python Claude SDK transport is also not the same thing as the CLI's private internal source.
- **PydanticAI**: the five main run methods, internal Graph, `RunContext.deps`, tool argument validation and output modes belong to Core; do not bundle optional Harness/Capabilities into Core without installed-version evidence. Import paths and `sequential`/deferred API semantics must be checked at the selected tag.
- **PydanticAI EndStrategy**: the official output documentation describes `'graceful'` as the default, `'early'` and `'exhaustive'` as distinct paths for mixed final output and other tool calls. If the model emits only regular plain-text output alongside a Tool Call, plain text does **not automatically** preempt that Tool the same way as a valid final output tool. `run_stream()` commits the first matching output earlier; do not claim its semantics equal nonstreaming `run()`.
- **OpenAI Agents SDK**: a code-first runtime in the app, not an OpenAI-hosted Agents API service. Agent-as-Tool retains parent response ownership; handoff transfers active Agent. First Agent input guardrail, final Agent output guardrail, attached Tool guardrails are not one universal filter; blocking/parallel timing affects side effects.
- **Claude Agent SDK**: Python SDK→Transport→Claude Code CLI; SDK-hosted MCP Tool calls cross to Host Python; permission callback/rules and session/workspace recovery have distinct contracts.
- **Google ADK**: Runner/Flow/Event/SessionService/state delta are separate roles; Agent `final` may not mean overall Workflow completion. Parallel Tool/Parallel Agent/Graph Workflow contracts depend on the installed release and should not be equated.
- **Microsoft AF**: core Agent/function invocation, middleware, optional Harness, Graph/Functional workflow are distinct layers. Superstep/checkpoint supports framework-state resume, not exactly-once database operations; Python checkpoint behavior changes across releases.
- **Memory/state**: persisted Memory file ≠ frozen prompt snapshot ≠ transcript/FTS index ≠ RAG/vector store ≠ checkpoint. SQLite FTS5 is lexical matching. Prefix KV caching ≠ context compaction. Tool concurrency ≠ process isolation or global DB serializability.
- **Demo:** current 2026 documentation may describe server capabilities not present at target PC. A working external OpenAI API path does **not** prove vLLM proxy tool choice, parser/template, streaming, output mode, token accounting, cancellation, or checkpoint behavior.

### 3.1 Official primary source index (actual URLs)

| ID | Technology | Canonical URL and fact scope |
|---|---|---|
| OFFICIAL-H-ARCH | Hermes | https://hermes-agent.nousresearch.com/docs/developer-guide/architecture — AIAgent, entry points, prompt/tool/session/provider/gateway |
| OFFICIAL-H-LOOP | Hermes | https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop — model→tool dispatch, threading, turn lifecycle, persistence |
| OFFICIAL-H-PROMPT | Hermes | https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly — prompt tiers/snapshot |
| OFFICIAL-H-TOOLS | Hermes | https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime — registry, execution, hooks |
| OFFICIAL-H-DELEGATE | Hermes | https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns — child agents/context |
| OFFICIAL-H-SRC | Hermes | https://github.com/NousResearch/hermes-agent — pin a real tag/commit and verify paths |
| OFFICIAL-C-MEMORY | Claude Code | https://code.claude.com/docs/en/memory — CLAUDE.md, automatic memory |
| OFFICIAL-C-HOOKS | Claude Code | https://code.claude.com/docs/en/hooks — Hook events and outcomes |
| OFFICIAL-C-SUBAGENTS | Claude Code | https://code.claude.com/docs/en/sub-agents — child Agent behavior |
| OFFICIAL-C-TEAMS | Claude Code | https://code.claude.com/docs/en/agent-teams — team setup, collaboration limits |
| OFFICIAL-P-AGENT | PydanticAI | https://pydantic.dev/docs/ai/core-concepts/agent/ — five run methods, Agent semantics |
| OFFICIAL-P-OUTPUT | PydanticAI | https://pydantic.dev/docs/ai/core-concepts/output/ — output modes and EndStrategy |
| OFFICIAL-P-TOOLS | PydanticAI | https://github.com/pydantic/pydantic-ai/blob/main/docs/tools-advanced.md — Tool handling |
| OFFICIAL-P-HARNESS | PydanticAI | https://pydantic.dev/docs/ai/capabilities/overview/ — optional Capabilities, check actual release |
| OFFICIAL-P-SRC | PydanticAI | https://github.com/pydantic/pydantic-ai — pin release; inspect `_agent_graph`, tool manager, output paths |
| OFFICIAL-O-RUN | OpenAI | https://developers.openai.com/api/docs/guides/agents/running-agents — Runner loop/state |
| OFFICIAL-O-ORCH | OpenAI | https://developers.openai.com/api/docs/guides/agents/orchestration — Handoff vs as-tool |
| OFFICIAL-O-GUARD | OpenAI | https://developers.openai.com/api/docs/guides/agents/guardrails-approvals — guards/approval |
| OFFICIAL-O-SRC | OpenAI | https://github.com/openai/openai-agents-python — pin release |
| OFFICIAL-S | Claude Agent SDK | https://code.claude.com/docs/en/agent-sdk/overview — SDK/CLI architecture |
| OFFICIAL-S-PY | Claude Agent SDK | https://github.com/anthropics/claude-agent-sdk-python — Host-side source |
| OFFICIAL-G | Google ADK | https://adk.dev/runtime/ — runtime/event/session flow; verify links & version |
| OFFICIAL-G-SRC | Google ADK | https://github.com/google/adk-python — pin release |
| OFFICIAL-M-OVERVIEW | Microsoft | https://learn.microsoft.com/en-us/agent-framework/overview/ — core concepts |
| OFFICIAL-M-WORKFLOW | Microsoft | https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/builder-and-execution — superstep/edge semantics |
| OFFICIAL-M-CHECKPOINT | Microsoft | https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/checkpoints — checkpoint scope; check Python version |
| OFFICIAL-M-SRC | Microsoft | https://github.com/microsoft/agent-framework — pin release |
| OFFICIAL-V | vLLM | https://docs.vllm.ai/en/latest/features/tool_calling/ — auto tool choice/parser/chat template conditional support |

Also inspect the current project research inventory: `agent_framework_seminar_2_planning_handoff.md`, `Agent_Framework_7종_최종_종합_비교_분석.md`, Hermes/Claude_Code/PydanticAI/OpenAI_Agents_SDK/Claude_Agent_SDK/Google_ADK/Microsoft_Agent_Framework nested deep-dive and comments, and the original slide flow MD. These are valuable **secondary research inputs**, not a replacement for official documentation; missing files must not block creation because this document contains the required essential content.

**Fact-review priority P0:** EndStrategy exact conditions + streaming; Hermes prompt snapshot/update and Hook/Intent recording; Pydantic Graph/tool sequence and separate Harness; official SDK guardrail range; ADK workflow version; MS checkpoint/superstep; OpenAI-compatible local port flow. Record a `fact_review.csv` with each claim and `PASS / CORRECTED / CONDITIONAL / NOT_VERIFIED`.

## 4. Seven reusable master architectures (fixed semantic objects)

Define each diagram as immutable node/edge data with stable IDs. The first slide in each technology **must** instantiate the complete graph; all subsequent diagrams reference/highlight those same object IDs, optionally zoomed into an associated detail graph. Do not use a separate inconsistent drawing for each slide. Preserve the owner's boundaries; a diagram must show **what the model sees**, **who executes tools**, and **where state persists**.

### H-ARCH — Hermes Agent (entry→loop→provider/tool/state)

- `H-ENTRY`: CLI/TUI, Gateway adapters, ACP, Cron scheduler as **distinct entry triggers**; `H-CORE`: `AIAgent` with conversation loop and per-turn phases; `H-PROVIDER`: runtime provider resolver/adapter; `H-MODEL`: external LLM or OpenAI-compatible vLLM endpoint; `H-TOOLS`: tool definitions + dispatch registry, builtins, MCP Client↔MCP Server, Plugin Manager and hooks; `H-PROMPT`: Stable/Context/Volatile builder, frozen session snapshot, skill references; `H-STATE`: SQLite session history, FTS5 lexical search, memory files (`MEMORY.md`, `USER.md`), compression/session lineage; `H-POLICY`: Runtime policy/approval + OS/DB ACL. `H-DELEGATE`: optional independent child Agent Loop. `H-CRON`: Cron job starts *new run*, not the existing Loop iteration.
- Directed path: `H-ENTRY→H-CORE→H-PROVIDER↔H-MODEL`; `H-MODEL→tool_calls→H-CORE→H-POLICY→H-TOOLS→tool_result→H-STATE→H-CORE`; `H-PROMPT→H-CORE` snapshot; `H-CORE↔H-STATE`; `H-CORE→H-DELEGATE→summary→H-CORE`. Use different arrow labels for request, tool dispatch, DB write and delegation.
- Do not imply `Agent Loop` is inside the model, Plugin source code is sent to LLM, Cron shares all session History, every MCP Tool is locally executed, or observed Tool call guarantees a persisted pre-execution intent.

### C-ARCH — Claude Code (public contract vs internal unknown)

- `C-ENTRY`: Terminal/IDE/Desktop; `C-RUNTIME`: Claude Code CLI/coding Harness, explicitly mark **inner implementation not fully open source**; `C-MODEL`: Claude model; `C-TOOLS`: Read/Edit/Bash/MCP; `C-INSTR`: CLAUDE.md/project rules; `C-MEM`: auto memory/Skill/session; `C-POLICY`: permissions/hooks/sandbox; `C-DELEGATE`: subagents and optional teams. External SDK→CLI bridge is a later highlight only.
- `C-ENTRY→C-RUNTIME↔C-MODEL`, `C-RUNTIME↔C-TOOLS`, `C-INSTR/C-MEM→C-RUNTIME`, `C-POLICY` gates actual Tool dispatch; delegated Agents have own contexts but file/system isolation requires a separate policy.
- Do not invent internal class names; distinguish skills, CLAUDE.md, memories and session commands.

### P-ARCH — PydanticAI Core (code-owned vs core-owned)

- `P-APP`: app-created Agent config, model, instructions, function tools/toolsets, deps, output_type, message_history. `P-GRAPH`: Core's internal `UserPromptNode→ModelRequestNode↔CallToolsNode→End`, with actual observed branches; `P-MODEL`: provider adapter/LLM; `P-TOOLS`: ToolManager, argument validation and tool execution; `P-OUTPUT`: output types, validators, `end_strategy`, retry; `P-STATE`: RunContext/history/messages/deferred; `P-APP-STATE`: external DB, policies, artifacts, long-term persistence. `P-HARNESS`: **optional separate** higher-level capability/Harness package, not present by default.
- `P-APP→P-GRAPH↔P-MODEL`; `P-GRAPH→P-TOOLS→P-STATE→P-GRAPH`; `P-OUTPUT` chooses End/Retry; Tool handler uses `P-APP-STATE` for Authorization. `Deps` stays runtime-side unless its data is explicitly used in returned text/tool payload.
- Differentiate internal graph implementation from separately authored `pydantic_graph` workflows, and distinguish final output validity from data truth.

### O-ARCH — OpenAI Agents SDK

- `O-APP`: Agent declarations/tools/handoffs/SDK options; `O-RUNNER`: Runner/model requests/NextStep Loop; `O-MODEL`: provider; `O-TOOLS`: function tools/MCP; `O-SPECIALIST`: child agent as tool or handoff destination; `O-GUARD`: input/output/tool guards and HITL; `O-STATE`: run result, RunState/interruption/session strategy. As-tool flows back to parent, handoff changes active agent. SDK is **app-owned deployment**, distinct from hosted APIs.

### S-ARCH — Claude Agent SDK

- `S-APP`: Host Python query()/ClaudeSDKClient/options; `S-TRANSPORT`: Python SDK/client transport/control; thick process boundary; `S-CLI`: Claude Code CLI runtime; `S-MODEL`: model; `S-TOOLS`: built-in tools/MCP; `S-HOST-MCP`: SDK-hosted MCP callbacks in Host Python; `S-POLICY`: permission rules/hooks/callback/modes; `S-STATE`: transcripts and externally saved sessions, workspace side effects separate. `S-CLI→S-TRANSPORT→S-HOST-MCP→S-CLI` for SDK-hosted tool roundtrip; do not draw as an independent Python SDK Loop replacing CLI.

### G-ARCH — Google ADK

- `G-CALLER→G-RUNNER→G-FLOW` (LlmAgent/BaseLlmFlow, per installed version) `↔G-MODEL`; `G-FLOW↔G-TOOLS` (Tool callback/execution); `G-FLOW→G-EVENT→G-SESSION` (SessionService + state delta); `G-MEMORY` / `G-ARTIFACT` are not the same as Session; `G-WORKFLOW`: optional sequential/parallel/graph orchestration; final Event scopes marked. Display Event producers/consumers and a graph completion state separately.

### M-ARCH — Microsoft Agent Framework

- `M-APP→M-AGENT→M-CHATCLIENT→M-MODEL`, with function invocation/tool pipeline and `M-MIDDLEWARE` at agent/chat/function boundaries. `M-HARNESS`: optional higher-level agent behavior, **not** every individual Agent tool Loop. `M-WORKFLOW`: executor graph/edges/supersteps/joins/checkpoints. Checkpoint is workflow state, not DB transaction. Illustrate normal Tool Error vs policy-driven interruption as separate branches.

**All master diagrams:** export SVG as accessible DOM with meaningful text elements and stable ids; no rasterized text. Use fixed frame map coordinates and theme tokens. Test every highlight reference exists. The same synthetic Lot/Tool names should mean the same thing across frameworks; framework-specific SDK function names are permitted when verified.

## 5. Common synthetic semiconductor scenario and correctness contract

This is **educational data, never internal or actual fab data**. Keep the dataset and task constant between the two demos, vary only runtime/Framework. Use a seed and immutable snapshot ID so students can reproduce results. Do not claim physical causation from synthetic correlations.

**Scenario:** A user asks (T1) “합성 LOT-A의 지정 기간 BIN-X 비율과 기준값을 조회해줘”, (T2) “같은 기간 측정값·SOP 문서 버전을 함께 확인하고 상승 이유에 대한 가능성과 반례를 설명해줘”, (T3) “시간누수 없는 과거 자료로 다음 기간 BIN-X 비율의 단순 Baseline을 예측하고 평가 결과를 보여줘.” T1–T3 are **read-only**. T4 (“이 분석 리포트를 게시하라”) is a **separate mock-only approval/restart controlled test** and must not mutate fab systems or user source directories.

Canonical synthetic schema:

```sql
lots(lot_id, wafer_id, observed_at_utc, bin_code, numerator, denominator, snapshot_id);
measurements(lot_id, wafer_id, observed_at_utc, metric, value, unit, equipment_alias, revision);
sops(sop_id, revision, valid_from_utc, valid_to_utc, document_ref);
reference_rates(bin_code, period_start_utc, period_end_utc, numerator, denominator, snapshot_id);
```

Tool contracts (the Python code may use specific verified SDK APIs): `get_bin_rates(lot_id, start_utc, end_utc)`, `get_reference_rates(bin_code, start_utc, end_utc)`, `get_measurements(lot_id, start_utc, end_utc)`, `read_sop(sop_id, as_of_utc)`, `compare_segments(...)`, `fit_baseline(training_cutoff_utc)`, `predict_bins(target_period_utc)`, `evaluate_model(holdout_start_utc, holdout_end_utc)`, optionally `mock_publish_report(report_id, approved_request_id)`. The user-visible Tool names should be matched in both implementations unless a Framework forces different registration naming; preserve **semantic equivalence**.

**Data dictionary required before numeric charts:** `BIN-X rate = numerator / denominator` only after the denominator's count unit (wafer/test item/measurement), duplicate handling, tested vs total counts, time-zone boundary and the period selection are defined. `denominator > 0`, numerator in [0,denominator]. All summaries need `snapshot_id`, `as_of_utc`, reference period, `sop_revision`. Prediction: explicit target and unit; train/holdout separated temporally; future measurement must never be fed as historical input; use simple honest baseline and report MAE or comparable metric **only after computed on the synthetic fixture**. If insufficient data, state “not enough synthetic evidence” rather than inventing benchmark accuracy or a causal root cause.

For the demos, provide one concrete generated fixture: `seed=20261103`, `snapshot_id=SYN-BIN-20261103-v1`, synthetic `SYN-LOT-A/SYN-LOT-B`, UTC timestamp, annotated units, and deterministic `expected-results.json` computed from real fixture. In presentation text use placeholders `<실제 합성 계산값>` until tests establish exact figures, then label displayed values `SYNTHETIC / 계산 검증됨` with dataset provenance. Never show guessed percentages as measured results.

**Business authenticity:** diagram labels `BIN 오류율`, `Lot`, `SOP` are explanatory domain terms and **may not exactly match the organization's actual metric definitions**; label the example synthetic and remain agnostic to private manufacturing processes. Source data, truth tables, model output and runtime trace must be independent objects.

## 6. Slide data / source / presenter notes contract

Each final slide is a standalone, machine-readable definition. For **every slide below**, populate this schema in `slides-data.ts` or JSON and its note in `speaker-notes.json`. Any additional split slide follows the same schema and stable IDs. The user expects detailed speaker notes sufficient to learn from and to deliver naturally—not generic one-liners. Separate onscreen content from preparation commentary.

```yaml
slideId: F001  # never duplicate; re-number in fixed sequence
section: Hermes
sourceBlockId: S04  # original research slide anchor; repeated when split
status: required
purpose: '이 장이 설명할 단 하나의 질문'
headline: '한글 결론 문장'
onScreen: ['실제 표시할 문구 1','실제 표시할 문구 2']
visual:
  template: T-ZOOM
  master: H-ARCH
  highlightedNodes: [H-CORE, H-TOOLS]
  actors: [{id: agent, label: 'Hermes Agent', owner: 'runtime'}]
  arrows: [{from: agent, to: tool, label: 'Validated call'}]
  geometry: '실제 배치/선/축/레이아웃 지시'
buildSteps:
  - {id: F001-B01, changes: ['첫 상태'], narrationCue: '한 가지 변화에 집중'}
  - {id: F001-B02, changes: ['다음 관계'], narrationCue: '이전 단계의 원인·결과'}
speakerNotes:
  setup: '이 화면 전에 청중이 알아야 할 전제'
  explanation: '정확한 개념 정의, 데이터 경계, 실제 분기와 반례'
  script: '발표자가 자연스럽게 그대로 말할 수 있는 한국어 문단'
  qa: [{q: '혼동하기 쉬운 질문', a: '검증 가능한 대답'}]
  limitations: ['버전·환경 의존 또는 아직 관측하지 않은 사실']
sourceIds: ['OFFICIAL-H-LOOP']
certainty: DOC_CONFIRMED  # per-claim records may be stricter
traceEventMapping: []  # actual recorded Event IDs only, otherwise empty
nextBridge: '다음 화면으로 이동하는 자연스러운 문장'
```

**Implementation rule:** source material uses numbered phases `① ②` in its older “전개”; treat these as ideas, not an excuse to expose many concepts per Space. For each one, split further until one step can be narrated in one sentence, and preserve a stable printed `build k/n`. At least two substantive builds per slide, unless the slide's single static conclusion truly warrants one. If a diagram shows more than ~7 primary actors, use complete master first + an enlarged local view in the next slide. Speaker notes must include: short setup, per-build what to say, full technically correct explanation, BIN example when relevant, caveat/why it's not something else, likely Q&A, official sources, and bridge. Avoid long technical paragraphs on audience screen.

**Source-map rule:** `Fxxx -> legacy Sxx -> claim IDs -> URLs/tags -> associated actual demo trace event IDs`. A real Event reference is assigned only **after** a captured trace exists and its manifest hash passes; any blank demo view is labeled `실행 전 / 실제 Trace 없음`. Do not manufacture placeholders that look like real event IDs.

## 7. Diagram / slide QA acceptance tests

- First slide of each product shows **all master nodes** and ownership; every later highlight uses the **same** IDs/coordinates. When the master is complex, first whole map may reveal semantically grouped nodes one at a time, then an immediate zoom page for detail. Each technical claim has a source ID.
- At 1920×1080, 1366×768 and 1280×720, no clipped arrow, overlapping label, horizontal scrollbar, microscopically shrunk text or hidden notes; when layout overflows **split the slide**, don't apply tiny font or arbitrary `transform: scale(.65)` inside content.
- Using Space from F001 first state eventually traverses **every build of every slide** exactly once and stops after the final build. Key auto-repeat cannot skip builds. No interaction required other than Space. Navigation tests assert actual `slideId`, `stepIndex` and changes to visible nodes—not just screenshot count.
- Every source tag resolves, every highlight refers to defined master, every slide mapping has exactly one legacy `Sxx` or clearly labeled `NEW`, and every note has a nonempty detailed script and caution.
- Code/diagram examples must use **matching actual method names, model/provider setup and installed-version syntax**. If uncertain, use a visibly `[PSEUDO]`-labeled conceptual code block, never misleading runnable code.
- Screens and scripts shall never state external model performance, internal/real manufacturing metrics, exactly-once Tool side effects or global policy enforcement absent evidence.


## 8. Complete production slide script: 94 initial screen units

**This is the authoritative sequential deck.** `F001` onward is the presenter-visible order. These are **94 independently planned teaching units** (46 legacy-centered plus 48 intentionally split detail units), *not* a maximum slide count. Codex **must split further** if any unit cannot be delivered with readable text and one causal concept per build. Never merge to meet a timeline. Each block specifies actual Korean on-screen wording, diagram construction, ordered Space steps, detailed presenter talking points and provenance. The summary, source, and demo sections following these page definitions remain binding.

### F001 | S01 · 이번 질문은 'Agent란?'이 아니라 '누가 실행을 소유하나?'

**Section/master:** 도입 / `NONE`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “이번 질문은 'Agent란?'이 아니라 '누가 실행을 소유하나?'”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Agent Framework 2차 세미나` / `구현을 읽고, 책임을 비교하다` / `완성형 Harness ↔ 직접 조립하는 SDK/Framework`.

**Diagram/layout specification:** 가운데 두 기둥: 왼쪽 `Harness: 실행 루프·세션·도구 통합`, 오른쪽 `SDK: 런타임 제공 + 앱 정책/서빙은 개발자`. 모델 서버는 양쪽 아래 공통 기반으로 분리. 청중이 이미 아는 Agent 구성요소는 푸터에 작은 아이콘으로만.

**Space-only semantic builds:**

- `F001-B01`: 큰 질문만.
- `F001-B02`: 두 선택지.
- `F001-B03`: 마지막 `통제권·운영 책임` 강조.

**Speaker script / detailed explanation:** 이번 발표는 기초 강의 후속이다. 동일한 Tool과 Memory도 어느 코드에서 실행되고 어디에 저장되는지 다르다. 제품들을 기능 수로 순위 매기지 않는다. 마지막에는 어떤 실행 계약이 도메인 데이터에 적합한지 결정한다.

**Likely Q&A:** Q. 2차 발표가 1차와 다른 점은 무엇인가요? A. Agent의 정의 대신 모델 입력, Tool 실행, 상태·권한·복구를 누가 책임지는지 실구현으로 비교합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `LOCAL-HANDOFF`; legacy `S01` reference: [LOCAL-CMP] §§1–3. `[DESIGN]` 구성.. **Trace:** No fake actual trace.

**Bridge:** “일곱 기술을 같은 서열이 아닌 아키텍처 층위에 놓고 시작하자.”

### F002 | S01 deep dive · 기초 강의에서 런타임 분석으로

**Section/master/template:** 도입 / `NONE` / `T-DECISION`. **Question/purpose:** 2차는 기능 목록이 아니라 실행 책임의 지도다.

**Exact audience headline:** “2차는 기능 목록이 아니라 실행 책임의 지도다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 1차: Agent·Tool·Orchestration의 공통 개념
- 2차: 누가 모델을 호출하고, Tool을 실행하고, 상태를 보존하는가?
- 다음: 검증 가능한 최소 도메인 Agent

**Geometry and labeled visual (explicit construction):** 좌측 1차의 단일 일반 루프 실루엣 → 가운데 2차의 6개 실행 책임 마크 → 우측 단계별 구현; 좌→우 한 방향.

**Space-only semantic builds:**

- `F002-B01`: 1차에서 배운 공통 루프 실루엣.
- `F002-B02`: 소유권·실행·상태·정책·복구의 질문.
- `F002-B03`: 이번 발표가 구현 검증으로 이어짐.

**Speaker script (readable Korean):** “기본적인 Agent 구성요소를 다시 가르치지 않겠습니다. 같은 Tool이라는 이름 뒤에 모델이 요청하는 순간과 실제 운영체제가 실행하는 순간이 다릅니다. 그 틈을 비교합니다.”

**Technical explanation / caution / counterexample:** 기본 개념 복습에 슬라이드 시간을 쓰지 말 것. 1차 내용을 이미 학습했다고 전제. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `LOCAL-HANDOFF §1–2` and same legacy `S01`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F003 | S02 · 일곱 기술의 자리와 고정 진행 순서

**Section/master:** 도입 / `NONE`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “일곱 기술의 자리와 고정 진행 순서”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Hermes → Claude Code | PydanticAI → OpenAI SDK → Claude SDK → Google ADK → Microsoft AF` / `두 축을 깊이 분석하고, 나머지는 차이만 본다`.

**Diagram/layout specification:** 위쪽 완성형 Harness 두 카드(Hermes, Claude Code), 아래쪽 Core/SDK/Framework 다섯 카드. **Claude Agent SDK는 Claude Code CLI에 연결된 브리지**로 그려 같은 레벨 독립 엔진으로 오해하지 않게. PydanticAI Core 바깥에 선택 Harness를 점선으로 그림.

**Space-only semantic builds:**

- `F003-B01`: 전체 지도.
- `F003-B02`: Hermes/PydanticAI 강조.
- `F003-B03`: 데모 두 개 위치 표시.

**Speaker script / detailed explanation:** SDK, Library, Framework, Harness는 배타적 인증 분류가 아니라 이번 발표에서 실행 책임을 설명하는 묶음이다. 같은 개발자가 둘 이상 결합해서 쓸 수도 있다.

**Likely Q&A:** Q. Claude Agent SDK를 OpenAI SDK와 같은 독립 Python Loop로 봐도 되나요? A. 아닙니다. SDK와 Claude Code CLI 런타임 사이 프로세스·제어 경계를 구분해야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `LOCAL-HANDOFF`; legacy `S02` reference: [LOCAL-CMP] §§1–2, [OFFICIAL-H], [OFFICIAL-P-HARNESS], [OFFICIAL-S].. **Trace:** No fake actual trace.

**Bridge:** “먼저 완성된 Harness를 열어 보자.”

### F004 | S02 deep dive · 완성형과 코드형은 절대적 양분이 아니다

**Section/master/template:** 도입 / `NONE` / `T-ARCH`. **Question/purpose:** 제품 계층을 섞어 같은 순위로 세우지 않는다.

**Exact audience headline:** “제품 계층을 섞어 같은 순위로 세우지 않는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Harness: Hermes · Claude Code
- Core/SDK: PydanticAI · OpenAI SDK · Claude Agent SDK · Google ADK · Microsoft AF
- 특수 관계: Claude Agent SDK ↔ Claude Code CLI / PydanticAI Core ↔ 선택 Harness

**Geometry and labeled visual (explicit construction):** 상하 레인과 가운데 연결 가교; 각 제품 카드는 고정 발표 순서대로 배열, ‘하나의 절대 분류’라고 표시하지 않는다.

**Space-only semantic builds:**

- `F004-B01`: Harness 두 곳 강조.
- `F004-B02`: PydanticAI 중심 확대.
- `F004-B03`: Claude SDK→CLI 브리지.
- `F004-B04`: 나머지 비교 대상의 위치 확정.

**Speaker script (readable Korean):** “SDK라는 이름이 붙었다고 반드시 독립 실행 루프를 Python에서 소유하는 것은 아닙니다. Claude Agent SDK는 Claude Code 런타임과 연결됩니다.”

**Technical explanation / caution / counterexample:** LangChain/LangGraph, Mistral AI Studio, vLLM/SGLang 엔진 내부는 다른 발표 범위. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `LOCAL-HANDOFF §1.2; OFFICIAL-O; OFFICIAL-S` and same legacy `S02`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F005 | S03 · 같은 질문을 일곱 기술에 적용할 비교 렌즈

**Section/master:** 도입 / `NONE`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “같은 질문을 일곱 기술에 적용할 비교 렌즈”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `① Loop 소유자 ② 모델 입력 ③ Tool 실행 ④ 정책·승인 ⑤ 상태·복구 ⑥ 위임·운영`.

**Diagram/layout specification:** 타원형 루프 중심으로 6개 탐침만. 일반 Agent 흐름을 길게 재설명하지 않는다. 각각 앞으로의 구조 그림에서 동일 아이콘 사용.

**Space-only semantic builds:**

- `F005-B01`: 현재 화면의 비교 축과 출발 주체를 한 가지씩 표시.
- `F005-B02`: 아이콘을 한 번에 켠 뒤 Hermes 사례로 줌.
- `F005-B03`: 해당 실행 경계의 확인 가능한 결과와 개발자 책임을 구분해 표시.

**Speaker script / detailed explanation:** “Guardrail이 있다” 대신 모델 호출 전에/도구 실행 직전에/결과 반환 후 중 어디에 적용되는지 묻고, “Memory가 있다” 대신 언제 읽고 언제 다시 Prompt에 반영되는지 묻는다.

**Likely Q&A:** Q. 프레임워크가 둘 다 Memory를 지원하면 같다고 볼 수 있나요? A. 저장 위치·로드 시점·검색 방식·다음 모델 입력 반영 시점을 확인해야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `LOCAL-HANDOFF`; legacy `S03` reference: [LOCAL-CMP] §§4–22.. **Trace:** No fake actual trace.

**Bridge:** “첫 번째로 Hermes의 전체 조직도를 보자.”

### F006 | S04 · Hermes 전체 아키텍처 — 코어 외에도 실행 환경이 있다

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ARCH`.

**Exact audience headline:** “Hermes 전체 아키텍처 — 코어 외에도 실행 환경이 있다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Hermes는 Tool 호출 래퍼가 아니라 자체 Agent Loop·저장소·채널을 갖춘 Harness`.

**Diagram/layout specification:** 가로 3단, 세로 2층. 좌측 `CLI/TUI · Gateway · ACP · Cron`(H-ENTRY). 중앙 큰 `AIAgent / conversation loop`(H-CORE). 상단 `Provider Resolver → vLLM/외부 모델`(H-MODEL). 우측 `Tool Registry → 내장 Tool / Plugin / MCP`(H-TOOLS). 아래 `System Prompt Stable/Context/Volatile, Skills`(H-PROMPT), `Session SQLite/FTS5, MEMORY/USER.md`(H-STATE), `Policies/Approvals`(H-POLICY). **Gateway와 Cron은 코어 외부 진입·스케줄링 역할임을 분리**.

**Space-only semantic builds:**

- `F006-B01`: 입구.
- `F006-B02`: 핵심 반복.
- `F006-B03`: 모델/Tool.
- `F006-B04`: 저장·정책; 이후 Hermes 슬라이드에서 동일 H 다이어그램 재사용.

**Speaker script / detailed explanation:** Channel마다 Agent가 다른 것이 아니라 같은 코어에 서로 다른 진입 방식과 세션 관리 정책을 붙인다. MCP와 Plugin은 Tool 등록의 동일한 이름이 아니라 다른 확장 경로다. 함수명은 노트에 `run_agent.py`, `agent/conversation_loop.py`, `tools/registry.py`, `hermes_state.py` 정도만 둔다.

**Likely Q&A:** Q. Hermes Agent와 Hermes LLM은 같은 제품인가요? A. Agent는 실행 Harness이고 Hermes라는 모델 계열은 별개의 LLM입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S04` reference: [LOCAL-H2] §§2–3; [OFFICIAL-H-ARCH], [OFFICIAL-H-TOOLS]. 버전 경로 검증 R02.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “이 가운데 Loop 하나가 실제 Tool을 어떻게 실행할까?”

### F007 | S04 deep dive · Hermes 실행 주체는 어디에 있나

**Section/master/template:** Hermes / `H-ARCH` / `T-ARCH`. **Question/purpose:** 사용자 인터페이스·Loop·모델·Tool은 서로 다른 위치에 있다.

**Exact audience headline:** “사용자 인터페이스·Loop·모델·Tool은 서로 다른 위치에 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 입구: CLI / Gateway / Cron / ACP
- 실행 소유: AIAgent + Conversation Loop
- 외부 경계: Model Provider / Tool Runtime

**Geometry and labeled visual (explicit construction):** H-ARCH 고정 좌표 사용. 입구에서 AIAgent로 실선 Request, 모델 왕복 파랑, Registry 실행 초록; Cron은 Loop 외부에서 새 Run 트리거.

**Space-only semantic builds:**

- `F007-B01`: H-ENTRY만 보이기.
- `F007-B02`: H-CORE와 단방향 진입 연결.
- `F007-B03`: H-MODEL 요청·응답.
- `F007-B04`: H-TOOLS 왕복.
- `F007-B05`: H-STATE/정책은 별도 추가.

**Speaker script (readable Korean):** “Hermes는 프로토콜 어댑터에만 붙은 함수 호출기가 아닙니다. CLI든 Gateway든 실행 중심은 AIAgent의 대화 Loop입니다.”

**Technical explanation / caution / counterexample:** Hermes Agent 프레임워크와 Hermes LLM 모델 패밀리를 동일시하지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-ARCH` and same legacy `S04`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F008 | S05 · Hermes 한 번의 요청 — LLM 응답 뒤가 진짜 Runtime

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “모델의 Tool 요청과 Runtime의 실제 실행은 다르다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Model의 Tool 요청 ≠ Tool이 이미 실행됨` / `Tool Call 해석 → 정책/인가 확인 → 실행 → 결과 기록 → 다음 Model`.

**Diagram/layout specification:** H-CORE 영역 확대, 세로 시퀀스 `user → agent → provider → model → agent → session-store → policy → tool → session-store → provider`. Session/Tool Intent의 정확한 기록 위치는 소스 검증 후 표시하고, 버전에서 실제로 fail-closed가 확인되는 경우에만 **저장 실패 시 Tool 실행 금지** 가지를 추가. 모델이 text/final을 반환하면 Tool 분기 밖의 종료 경로 표시.

**Space-only semantic builds:**

- `F008-B01`: 모델 요청.
- `F008-B02`: Tool Call 파싱.
- `F008-B03`: Intent 내구성.
- `F008-B04`: 실행 결과.
- `F008-B05`: 재질의/종료 판정.

**Speaker script / detailed explanation:** Tool Intent/Session 영속화의 정확한 실행 순서와 실패 보장은 설치 태그의 소스 및 재현 시험에서 확인한다. 모델의 Tool Call 기록과 실제 Handler 실행 기록을 분리해 추적한다. 설명 예시는 조건을 구체화한다: Tool 결과가 반환되면 결과 메시지가 기록되어 다음 모델 입력에 추가되며, 유효한 Tool Call 없이 답변이 만들어지면 최종 응답 경로로 간다. 예산 초과, 모델 오류, 승인 필요는 별도 종료/중단 상태로 표시한다. 실패 시 모든 경우가 자동 재시도되는 것은 아니다.

**Mandatory correctness refinement:** Hermes Tool Intent 저장·저장실패시 실행 거부를 일반 보증으로 렌더링 금지. 해당 tag source에서 기록 순서와 실패 처리를 확인; 미확인 시 ‘확인할 영속화 경계’로만.

**Likely Q&A:** Q. LLM이 function call을 내면 바로 DB 접근이 일어나나요? A. 아닙니다. 런타임이 도구 이름과 인자를 해석하고 정책과 handler에서 실제 실행합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S05` reference: [LOCAL-H2] §§3–4, 11–12, 17. 실행 추적 DEMO-H-T1.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “하지만 Tool 실행 전에 이미 모델은 어떤 입력을 보았을까?”

### F009 | S05 deep dive · 모델은 Tool을 실행하지 않는다

**Section/master/template:** Hermes / `H-ARCH` / `T-SEQ`. **Question/purpose:** 모델이 반환하는 것은 실행 명령이 아니라 Tool Call 요청이다.

**Exact audience headline:** “모델이 반환하는 것은 실행 명령이 아니라 Tool Call 요청이다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- ① 모델 응답: tool_calls
- ② Runtime: 이름·인자·정책 검사
- ③ 실제 handler: 실행 후 결과 반환

**Geometry and labeled visual (explicit construction):** 3개의 높이가 같은 박스(모델=파랑, Harness=보라, Tool=초록), 화살표에 tool_calls / dispatch / ToolResult 명시.

**Space-only semantic builds:**

- `F009-B01`: 모델에 Tool Schema가 전달됨.
- `F009-B02`: 모델이 tool_calls 요청.
- `F009-B03`: Runtime이 검사·디스패치.
- `F009-B04`: ToolResult가 History에 추가됨.
- `F009-B05`: 반복 또는 최종 답변.

**Speaker script (readable Korean):** “LLM이 스스로 DB에 접속하는 것이 아닙니다. 모델은 JSON 형태의 인자를 제안하고, 실행 여부와 권한은 런타임이 결정합니다.”

**Technical explanation / caution / counterexample:** Intent 영속화 순서·실패 시 강제 중단은 버전별 실제 소스로 검증하기 전 확정적으로 그리지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-LOOP; OFFICIAL-H-TOOLS` and same legacy `S05`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F010 | S05 deep dive · 실패·중단·재시도는 한 경로가 아니다

**Section/master/template:** Hermes / `H-ARCH` / `T-SEQ`. **Question/purpose:** Tool Error, Approval Pending, Model Error, Final은 별도 상태다.

**Exact audience headline:** “Tool Error, Approval Pending, Model Error, Final은 별도 상태다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 성공: ToolResult → 다음 모델 요청
- 실행 전: 승인 대기/거부
- 오류: Tool Error / Provider Error / 예산 종료

**Geometry and labeled visual (explicit construction):** H-CORE를 중심으로 분기 4개의 작은 상태 기계; 실패를 자동으로 모두 Retry하는 단일 화살표를 금지.

**Space-only semantic builds:**

- `F010-B01`: 정상 Tool 경로.
- `F010-B02`: Approval Pending 분기.
- `F010-B03`: Tool Error 피드백.
- `F010-B04`: Model Provider 실패·Fallback.
- `F010-B05`: Final/Cancelled 종료.

**Speaker script (readable Korean):** “같은 실패라도 어디에서 오류가 나고 어떤 상태가 저장되었는지가 복구 전략을 결정합니다.”

**Technical explanation / caution / counterexample:** 실제 실패 처리·재시도 여부·Tool Intent 선행 기록은 해당 태그와 재현 시험 결과를 따를 것. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-LOOP` and same legacy `S05`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F011 | S06 · Hermes 모델 입력은 '저장한 것 전부'가 아니다

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Hermes 모델 입력은 '저장한 것 전부'가 아니다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `System Prompt Snapshot + 현재 대화 History + Tool Schema + 이번 호출의 임시 레이어`.

**Diagram/layout specification:** H-PROMPT 확대. 위에서 아래로 세 레이어 `Stable / Context / Volatile` 옆에 `Session Frozen Snapshot`. 아래 `history/messages`와 `available tool schemas`; 오른쪽 별도의 `ephemeral call-time additions` → Provider payload 변환. **절대 Deps/Skill 파일 전체/과거 세션 전체가 무조건 전송되는 그림을 금지**.

**Space-only semantic builds:**

- `F011-B01`: Stable.
- `F011-B02`: 프로젝트 Context.
- `F011-B03`: Memory/Skills 같은 Volatile.
- `F011-B04`: History/Tool Schema.
- `F011-B05`: Provider-side request. 각 요소가 실제 모델에 포함되는지 `capture origin` 표식.

**Speaker script / detailed explanation:** 파일이 디스크에서 바뀐다고 기존 세션의 System Prompt Snapshot이 즉시 갱신되지는 않는다. 새로운 Tool 결과로 최신 파일을 읽으면 모델에게 별도 대화 메시지로 제공할 수 있다. `Volatile`은 매 호출마다 자동 변경된다는 뜻이 아니라 세션 간 재구성 가능성이 상대적으로 높은 영역이라는 뜻. **Skill 인덱스의 정확한 위치는 버전 고정 출력으로 검증**.

**Likely Q&A:** Q. Memory 파일을 수정하면 진행 중인 모든 요청에 바로 반영되나요? A. 세션 Prompt Snapshot과 Tool을 통한 명시적 읽기·새 세션 구성 조건을 구분해야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S06` reference: [LOCAL-H2] §§5–6, 8; [OFFICIAL-H-PROMPT]. 실행 추적 DEMO-H-T2.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “왜 이런 안정성을 일부러 강제할까?”

### F012 | S06 deep dive · System Prompt의 스냅샷

**Section/master/template:** Hermes / `H-ARCH` / `T-ZOOM`. **Question/purpose:** 파일 변경과 현재 모델 입력 변경은 같은 사건이 아니다.

**Exact audience headline:** “파일 변경과 현재 모델 입력 변경은 같은 사건이 아니다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Stable → Context → Volatile 조립
- 세션 중 재사용되는 Prompt Snapshot
- 명시적 갱신/새 세션 시 재구성 조건

**Geometry and labeled visual (explicit construction):** H-PROMPT의 3단 레이어를 수직 스택으로, 우측 Snapshot 해시와 새 세션 생성 경로를 분리.

**Space-only semantic builds:**

- `F012-B01`: Stable 레이어.
- `F012-B02`: Context 레이어.
- `F012-B03`: Volatile 레이어.
- `F012-B04`: 세션 Snapshot 고정.
- `F012-B05`: 새로 고치는 경로를 점선으로.

**Speaker script (readable Korean):** “디스크 파일을 수정했다고 해서 이미 생성된 세션 프롬프트가 즉시 달라지는 것은 아닙니다. 다만 별도 Tool 읽기로 최신 파일 내용이 대화에 들어올 수 있습니다.”

**Technical explanation / caution / counterexample:** Stable/Context/Volatile 정확한 순서와 갱신 조건은 고정 소스 검증; Provider payload와 별도 표시. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-PROMPT; OFFICIAL-H-ARCH` and same legacy `S06`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F013 | S06 deep dive · 모델 입력 vs 실행기 내부 상태

**Section/master/template:** Hermes / `H-ARCH` / `T-COMP`. **Question/purpose:** 저장된 모든 정보가 매 모델 호출에 전송되는 것은 아니다.

**Exact audience headline:** “저장된 모든 정보가 매 모델 호출에 전송되는 것은 아니다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 모델에 직렬화: messages / exposed tool schemas / output constraints
- 실행기 내부: credentials / DB handles / memory file paths
- Tool이 반환하면 선택 데이터가 모델에 노출될 수 있음

**Geometry and labeled visual (explicit construction):** 좌측 ‘Runtime Only’, 우측 ‘Provider Request’; 통과하는 항목만 파란 실선, 미전송은 회색 자물쇠.

**Space-only semantic builds:**

- `F013-B01`: 런타임 내부 정보.
- `F013-B02`: 직렬화 후보만 오른쪽으로.
- `F013-B03`: Provider Adapter에서 형식 변환.
- `F013-B04`: Tool 결과가 History로 유입되는 조건.

**Speaker script (readable Korean):** “모델 컨텍스트와 실행기의 디스크/프로세스 메모리는 동일한 공간이 아닙니다.”

**Technical explanation / caution / counterexample:** SDK 객체·Adapter 인수·전송 페이로드를 각각 출처 캡처 레벨로 구분. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-PROMPT; DEMO-TRACE` and same legacy `S06`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F014 | S07 · Prefix Cache와 Compaction은 완전히 다른 최적화

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Prefix Cache와 Compaction은 완전히 다른 최적화”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Cache = 같은 Prefix의 연산 재사용` / `Compaction = 다음 요청에 보낼 History를 줄이기`.

**Diagram/layout specification:** 동일 10칸 토큰 바 비교 ① 앞 8칸 같음: Prefix KV 재사용 가능, ② 첫 칸 변경: 뒤가 같아도 Prefix 적중 불리. 아래 Tool 결과가 길어져 압축 전/후 History 바 표시. `Saved Token Count`가 아닌 `reused computation` 레이블. 숫자는 전부 **설명용**.

**Space-only semantic builds:**

- `F014-B01`: 입력 총 길이 동일.
- `F014-B02`: KV Cache 적중.
- `F014-B03`: 뒤쪽 volatile 변화.
- `F014-B04`: 압축으로 사용되는 토큰 자체 감소, 단 캐시 Prefix 변경 가능.

**Speaker script / detailed explanation:** 캐시는 Python 문자열 조립 시간을 줄이는 것이 아니라 모델 서빙의 Prefill 연산 재사용이다. 사용 중인 Provider·vLLM이 실제 APC를 지원·활성화하고 캐시가 살아 있어야 한다. Compaction 시 어떤 Tool Call/Result 쌍을 보존하는지는 안전성 검토의 대상이다. 빠르게 처리되었다고 과거 데이터가 최신이라는 뜻은 아니다.

**Mandatory correctness refinement:** Prefix cache는 Provider의 Prefill 연산 재사용이며 Compaction은 메시지/History 변화. 특정 모델/서버의 cache hit은 실측 전 불명.

**Likely Q&A:** Q. Prefix Cache가 활성화되면 입력 token 수가 줄어드나요? A. 일반적으로 캐시가 Prefill 연산을 재사용하는 것이지 요청에 담긴 메시지를 삭제하는 것은 아닙니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S07` reference: [LOCAL-H2] §§6–8, [OFFICIAL-H-PROMPT]; R08, 캐시 실측 P2.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “그렇다면 Memory는 실제 어디에 저장되고 언제 반영될까?”

### F015 | S07 deep dive · Prefix Cache는 연산 재사용

**Section/master/template:** Hermes / `H-ARCH` / `T-COMP`. **Question/purpose:** Prefill KV 재사용과 프롬프트 길이 감소를 혼동하지 않는다.

**Exact audience headline:** “Prefill KV 재사용과 프롬프트 길이 감소를 혼동하지 않는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 동일한 Prefix → 캐시 적중 가능
- 첫 토큰 차이 → 이후 Prefix 재사용 경계 변화
- 캐시 여부는 Provider/vLLM 설정과 실제 계측에 의존

**Geometry and labeled visual (explicit construction):** 위아래 동일 길이 10칸 토큰 바; 일치 Prefix를 파란 외곽선, 변경 지점 빨간 세로선; 캐시 적중 실측 숫자 쓰지 말 것.

**Space-only semantic builds:**

- `F015-B01`: 두 요청의 공통 Prefix.
- `F015-B02`: 변경 토큰을 표시.
- `F015-B03`: 서빙 측 KV Cache 재사용 가능 구간.
- `F015-B04`: 가능성≠확인 강조.

**Speaker script (readable Korean):** “캐싱은 이전 요청에 있던 정보를 삭제하지 않습니다. 같은 Prefix 계산을 서버가 재사용할 수 있다는 것입니다.”

**Technical explanation / caution / counterexample:** Anthropic prompt caching과 vLLM APC의 구현·표시 지표를 같은 제품 기능으로 섞지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-PROMPT; OFFICIAL-V` and same legacy `S07`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F016 | S07 deep dive · Compaction은 History의 표현을 바꾼다

**Section/master/template:** Hermes / `H-ARCH` / `T-SEQ`. **Question/purpose:** 압축은 모델 입력을 줄이지만 정보 손실과 재현성 이슈가 있다.

**Exact audience headline:** “압축은 모델 입력을 줄이지만 정보 손실과 재현성 이슈가 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 이전 긴 중간 턴 → 요약본
- 최근 N개 메시지 및 Tool Call/Result 쌍은 정책에 따라 보존
- 요약 후 다음 요청 입력이 달라질 수 있다

**Geometry and labeled visual (explicit construction):** 시간 축 상단 원본 대화 8 블록, 하단 Summary+최근 메시지 3블록; 삭제된 영역에는 loss 경고.

**Space-only semantic builds:**

- `F016-B01`: 기존 History.
- `F016-B02`: 압축 트리거.
- `F016-B03`: 압축된 새 History.
- `F016-B04`: 원본 Session lineage·보존 조건.

**Speaker script (readable Korean):** “Compaction은 단순한 캐시가 아니라 앞으로의 모델 입력 근거를 재작성할 수 있는 작업입니다.”

**Technical explanation / caution / counterexample:** 구체 임계값·최근 N개 보호 정책은 설치 태그 확인. 압축을 실제로 실행하지 않았으면 REPLAY에서 미관측. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-LOOP` and same legacy `S07`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F017 | S08 · Hermes Memory / SQLite FTS5 / Skills는 같은 메모리가 아니다

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Hermes Memory / SQLite FTS5 / Skills는 같은 메모리가 아니다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Memory = 선별된 지속 정보` / `Session+FTS5 = 대화 기록·검색` / `Skill = 재사용 절차`.

**Diagram/layout specification:** 세 수평 레인. `MEMORY.md / USER.md ↔ memory Tool`(파일 기록), `Session SQLite → FTS5 lexical search`(이력), `Skill index → 선택적 SKILL.md 본문 로딩`(절차). 레인마다 `저장한 사람 / 읽기 시점 / Prompt 재반영 시점 / 검색 수단` 작은 표. FTS5는 벡터 검색이 아니라 어휘 기반, 검색 내용을 생성에 제공하면 넓은 RAG 패턴 가능.

**Space-only semantic builds:**

- `F017-B01`: 대화 중 메모리 Tool로 저장.
- `F017-B02`: System Prompt는 보통 frozen.
- `F017-B03`: 새 세션/명시 갱신 시 새로운 Snapshot.
- `F017-B04`: FTS 검색과 Skill 본문 읽기는 별도 동작.

**Speaker script / detailed explanation:** Memory 파일의 최신 내용과 이미 구성된 Prompt Snapshot을 동일시하지 않는다. 도메인 지식의 정답원은 현재 SOP Revision·수집 시점이 확인된 조회 데이터여야 한다. Skill 자동 생성은 절차 파일을 작성하는 편의이지 품질 보증이 아니다.

**Mandatory correctness refinement:** SQLite FTS5는 기본적으로 lexical full-text search. Vector RAG 내장 구현이라고 오인시키지 말 것.

**Likely Q&A:** Q. SQLite FTS5는 벡터 RAG와 같은 기술인가요? A. 아니요. FTS5는 어휘 기반 검색이고 RAG는 검색 결과를 생성 단계에 쓰는 더 넓은 패턴입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S08` reference: [LOCAL-H2] §§8–10, [OFFICIAL-H-ARCH]. R02.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “이 절차와 도구가 실행 엔진에 어떻게 들어올까?”

### F018 | S08 deep dive · Memory·Session 검색·Skill의 네 가지 질문

**Section/master/template:** Hermes / `H-ARCH` / `T-COMP`. **Question/purpose:** 저장 위치, 갱신 주체, 검색 방식, 모델 반영 시점이 다르다.

**Exact audience headline:** “저장 위치, 갱신 주체, 검색 방식, 모델 반영 시점이 다르다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Memory 파일: 선택된 지속 정보
- SQLite/FTS5: 대화 이력과 어휘 검색
- Skills: 실행 절차의 선택적 로딩

**Geometry and labeled visual (explicit construction):** 3 레인 각각 저장·검색·모델 재반영 타이밍을 같은 축에 올려 비교; FTS5는 lexical 아이콘.

**Space-only semantic builds:**

- `F018-B01`: Memory 파일 읽고 쓰기.
- `F018-B02`: SQLite/FTS5 조회.
- `F018-B03`: Skill Index/본문 로드.
- `F018-B04`: Prompt Snapshot에 반영되는 시점 비교.

**Speaker script (readable Korean):** “같은 Memory라고 해도 사용자가 기록한 사실, 과거 대화를 찾는 인덱스, 일을 수행하는 절차 파일은 다릅니다.”

**Technical explanation / caution / counterexample:** FTS5 자체를 벡터 검색이라고 부르지 않는다; RAG는 검색 결과를 생성 입력에 붙이는 더 넓은 패턴. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-ARCH; LOCAL-H2 §8–10` and same legacy `S08`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F019 | S09 · Hermes Tool / MCP / Plugin — 확장 경계의 차이

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Hermes Tool / MCP / Plugin — 확장 경계의 차이”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Tool = 실행 기능` / `MCP = 외부 도구 프로토콜` / `Plugin = Hermes 자체 확장 인터페이스`.

**Diagram/layout specification:** H-TOOLS 영역 3갈래. ① `Built-in/Registry Tool` ② `MCP Client → MCP Server Tool` ③ `Plugin manager → ctx.register_tool / hook / command / provider` → 모두 적절한 경로로 Tool 목록에 접속. `LLM에 노출되는 것은 Schema, Hook 코드는 Runtime에서 실행` 문구. Plugin이 Tool 등록 외 Memory/Context Provider도 다룰 수 있음을 작은 가지.

**Space-only semantic builds:**

- `F019-B01`: 현재 화면의 비교 축과 출발 주체를 한 가지씩 표시.
- `F019-B02`: 각 경로에서 `모델에 보이는 이름·Schema → 모델 호출 → Hermes dispatch → 실행 위치` 색다른 화살표.
- `F019-B03`: 해당 실행 경계의 확인 가능한 결과와 개발자 책임을 구분해 표시.

**Speaker script / detailed explanation:** Custom Tool을 추가하는 경로가 Plugin 하나뿐인 것은 아니다. Registry에 직접 등록하거나 MCP 서버에서 Tool을 제공할 수도 있다. Hook은 등록된 Tool의 코드가 모델에 주입된다는 뜻이 아니다. 서비스 제약은 실행 백엔드 권한에서 다시 강제해야 한다.

**Likely Q&A:** Q. Plugin을 등록하면 Plugin 코드 전체가 모델에 보이나요? A. 아닙니다. 노출 가능한 Tool Schema와 실제 Runtime에서 실행되는 Handler/Hook을 구분합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S09` reference: [LOCAL-H2] §§11–12; [OFFICIAL-H-TOOLS], [OFFICIAL-H-HOOKS]. R02.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “실행권한이 없다면 Hook에서 어디를 막아야 할까?”

### F020 | S09 deep dive · Tool Registry와 MCP의 왕복

**Section/master/template:** Hermes / `H-ARCH` / `T-SEQ`. **Question/purpose:** MCP 서버 코드는 Tool Schema처럼 모델에게 전송되지 않는다.

**Exact audience headline:** “MCP 서버 코드는 Tool Schema처럼 모델에게 전송되지 않는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- MCP Client가 서버의 제공 도구를 조회
- 모델에는 선택된 Tool Schema를 노출
- 실행 호출은 Runtime→MCP Server로 전달

**Geometry and labeled visual (explicit construction):** 왼쪽 LLM(파랑), 가운데 Registry(보라), 오른쪽 MCP Server(초록) 사이 Schema/Call/Result 3종 라벨 화살표.

**Space-only semantic builds:**

- `F020-B01`: 도구 발견과 등록.
- `F020-B02`: 모델에 Schema 노출.
- `F020-B03`: LLM 호출 요청.
- `F020-B04`: MCP Client→Server 실행.
- `F020-B05`: 결과를 모델에 반환.

**Speaker script (readable Korean):** “MCP는 에이전트가 외부 Tool을 이용하기 위한 연결 규약입니다. 모델이 MCP 서버에 직접 로그인한다고 그리면 잘못입니다.”

**Technical explanation / caution / counterexample:** Hermes Plugin은 자체 실행 확장 인터페이스로 따로 다룰 것. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-TOOLS` and same legacy `S09`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F021 | S09 deep dive · Plugin과 Hook은 Tool 이상의 확장이다

**Section/master/template:** Hermes / `H-ARCH` / `T-ZOOM`. **Question/purpose:** Plugin 등록 코드는 Runtime에서 실행되며 모델에 통째로 들어가지 않는다.

**Exact audience headline:** “Plugin 등록 코드는 Runtime에서 실행되며 모델에 통째로 들어가지 않는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Plugin discovery → lifecycle load
- register_tool / hook / command / provider 같은 확장 포인트
- Hook의 관찰 기능과 정책 차단 기능은 다름

**Geometry and labeled visual (explicit construction):** H-TOOLS 아래 Plugin Manager 박스를 별도 배치하고 Plugin에서 Tool/Hook/Command로 퍼지는 가지; 실제 지원 API는 릴리스 검사.

**Space-only semantic builds:**

- `F021-B01`: Plugin 발견·로드.
- `F021-B02`: 등록 가능한 확장 분기.
- `F021-B03`: Tool Registry로 연결.
- `F021-B04`: Hook 실행 시점.
- `F021-B05`: Plugin 정책의 한계.

**Speaker script (readable Korean):** “Tool이라는 실행 기능과, 그 기능을 어디서 확장해서 끼워 넣는가 하는 Plugin은 다른 개념입니다.”

**Technical explanation / caution / counterexample:** 사용하지 않는 Plugin 기능을 가짜 Demo Event로 만들지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-ARCH; OFFICIAL-H-TOOLS` and same legacy `S09`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F022 | S10 · Hermes Guardrail은 하나의 '검사 함수'가 아니다

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Hermes Guardrail은 하나의 '검사 함수'가 아니다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `지침 → Tool 노출 → 인자/정책 검사 → 사용자 승인 → 실제 실행 환경 제한`.

**Diagram/layout specification:** 도구 호출 전 4개의 Checkpoint를 배치하고 `pre_tool_call` 같은 Plugin Hook이 위치할 수 있는 곳, terminal approval, OS 파일/네트워크 권한을 각각 다른 위치에 표기. 실패 유형별 `Block` vs `Ask` vs `Error` 경로.

**Space-only semantic builds:**

- `F022-B01`: Prompt 상의 금지 지시만으로 막을 수 없음.
- `F022-B02`: Runtime 정책.
- `F022-B03`: 승인된 최종 인자.
- `F022-B04`: OS/DB 계층이 최종 강제. Hook 예외가 항상 Fail-closed인지 별도 검증 표시.

**Speaker script / detailed explanation:** 프롬프트는 모델의 선택을 유도할 뿐 Tool 실행 자체를 막는 권한 시스템이 아니다. 관찰 Hook과 차단 Hook을 구분한다. 관리자 승인도 승인 후 실제 실행 인자가 달라지면 무의미해질 수 있으므로 최종 인자·사용자·데이터 버전 바인딩을 권장한다.

**Likely Q&A:** Q. Prompt 지침만으로 Tool의 보안 통제가 끝나나요? A. 불가능합니다. 실제 인가는 Runtime·Tool Handler·DB/OS 계층에서도 강제되어야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S10` reference: [LOCAL-H2] §§12–14; [OFFICIAL-H-HOOKS]. R02·R09.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “여러 Tool이나 여러 Agent를 동시에 실행하면 이 정책은 어떻게 적용될까?”

### F023 | S10 deep dive · Guardrail은 마지막 벽이 아니다

**Section/master/template:** Hermes / `H-ARCH` / `T-SEQ`. **Question/purpose:** Prompt 안내와 Tool 실제 접근 통제는 다른 보안 계층이다.

**Exact audience headline:** “Prompt 안내와 Tool 실제 접근 통제는 다른 보안 계층이다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 모델 지침: 행동 유도
- Runtime 승인/Hook: 실행 판단
- OS/DB 인가: 최종 데이터 접근 제약

**Geometry and labeled visual (explicit construction):** H-POLICY 안에 층 3개로 방어 경계; 요청은 끝에서 DB 권한 확인을 거쳐야만 green success.

**Space-only semantic builds:**

- `F023-B01`: 지침만 있을 때의 취약 경로.
- `F023-B02`: Runtime Gate.
- `F023-B03`: Handler/DB 권한.
- `F023-B04`: 허용/거부 로그.
- `F023-B05`: Approval-argument 바인딩.

**Speaker script (readable Korean):** “모델 프롬프트에 ‘허용되지 않은 Lot은 읽지 마’라고 적는 것은 실제 DB의 권한 검사와 동등하지 않습니다.”

**Technical explanation / caution / counterexample:** 특정 Hook이 모든 경로를 전부 막는다고 주장하지 않는다; Hook 예외 처리와 fail-open/closed는 태그 검증. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-TOOLS; LOCAL-H2 §12–14` and same legacy `S10`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F024 | S11 · 병렬 Tool과 병렬 Subagent는 '동시에 실행'의 다른 의미

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “병렬 Tool과 병렬 Subagent는 '동시에 실행'의 다른 의미”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `병렬 Tool: 한 Loop 안에서 함수 여러 개` / `병렬 Subagent: 독립 Loop·History를 여러 개`.

**Diagram/layout specification:** 좌측 Main Agent 한 개 → ThreadPool Worker 3개 Tool → 결과 합치기; 우측 Main Agent → 3개의 `AIAgent` 인스턴스와 각각 Loop·Tool 호출 → 부모로 최종 결과. 아래 `스레드·프로세스·Agent 인스턴스`를 구분하는 3행 레전드.

**Space-only semantic builds:**

- `F024-B01`: 모델이 3개 Tool Call을 제안.
- `F024-B02`: 실제 Pool에 분배.
- `F024-B03`: 충돌·상호작용 도구는 장벽/순차 처리.
- `F024-B04`: Subagent는 각자 모델 재호출 가능.
- `F024-B05`: OS 프로세스 격리는 별도 문제.

**Speaker script / detailed explanation:** Tool 병렬이라고 모든 도구가 무조건 스레드에서 동시에 도는 것은 아니다. 경로 충돌·interactive 도구는 다른 정책을 따른다. 여러 Subagent를 생성해도 반드시 여러 Python 프로세스는 아니다. 별도 컨텍스트와 실제 파일/DB/네트워크 격리는 다른 문제다. Subagent 비용은 여러 모델 Loop 사용으로 증가할 수 있다.

**Likely Q&A:** Q. Subagent 3개면 항상 프로세스도 3개인가요? A. 아닙니다. 독립 Context/Loop와 OS 프로세스 격리 여부는 별개의 속성입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S11` reference: [LOCAL-H2] §§13–15. 재현 로그 DEMO-H-T6.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “동시에 접속하는 사용자가 많아지면 누가 세션을 소유할까?”

### F025 | S11 deep dive · Tool 병렬의 실제 실행 단위

**Section/master/template:** Hermes / `H-ARCH` / `T-SEQ`. **Question/purpose:** 동시 Tool Calls는 하나의 Agent 안에서 분산 처리될 수 있다.

**Exact audience headline:** “동시 Tool Calls는 하나의 Agent 안에서 분산 처리될 수 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 한 모델 응답에 A/B/C Tool Calls
- 조건부 ThreadPool/Sequential 경로
- 결과는 원래 Tool Call ID로 매칭

**Geometry and labeled visual (explicit construction):** 하나의 Agent Loop 위에 3개 thread lane; 각 start/end timestamp 다르게, 결과 통합은 id와 call order 기준.

**Space-only semantic builds:**

- `F025-B01`: 모델이 세 호출을 제안.
- `F025-B02`: 각 Worker 실행.
- `F025-B03`: interactive Tool은 순차 처리 조건.
- `F025-B04`: 완료 시간과 History 삽입 순서 구분.

**Speaker script (readable Korean):** “Tool을 세 번 호출한다는 것이 Agent 세 개를 만든다는 뜻은 아닙니다.”

**Technical explanation / caution / counterexample:** 스레드 처리 정책은 Hermes 고정 버전 확인; 결과 표시 순서를 실제 완료 순서와 혼동 금지. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-LOOP` and same legacy `S11`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F026 | S11 deep dive · Subagent는 다른 대화 수명을 만든다

**Section/master/template:** Hermes / `H-ARCH` / `T-COMP`. **Question/purpose:** Child Agent는 별도의 Context/Loop를 갖지만 OS 격리와 동일하지 않다.

**Exact audience headline:** “Child Agent는 별도의 Context/Loop를 갖지만 OS 격리와 동일하지 않다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Parent가 delegate_task 발행
- Child A/B 독립 Run·History
- Parent는 요약/결과를 받음

**Geometry and labeled visual (explicit construction):** Parent 큰 박스에 Child 두 개 별도 미니 Loop. 점선으로 OS 프로세스 경계를 선택 사항 표시.

**Space-only semantic builds:**

- `F026-B01`: Parent 분업 요청.
- `F026-B02`: Child의 독립 모델 재호출.
- `F026-B03`: Child Tool 실행.
- `F026-B04`: Parent로 결과만 환류.
- `F026-B05`: 보안·비용 이슈.

**Speaker script (readable Korean):** “각 Child가 모델을 다시 부를 수 있어 토큰 사용량과 실수 가능성도 달라집니다. 새 Python 프로세스라는 뜻은 아닙니다.”

**Technical explanation / caution / counterexample:** 컨텍스트 격리와 파일/네트워크 권한 격리를 혼동하지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-DELEGATE; OFFICIAL-H-LOOP` and same legacy `S11`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F027 | S12 · Hermes Gateway·Cron·Session 소유권

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Hermes Gateway·Cron·Session 소유권”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `사용자 수 ≠ Agent 프로세스 수 ≠ LLM 요청 수` / `Cron은 현재 Loop 반복이 아니라 새 작업 트리거`.

**Diagram/layout specification:** `Client A/B/C → Gateway session router → AIAgent runs → remote/localhost model` + 아래 `Cron scheduler → new task/run → delivery`. 한 사용자 세션의 write serialization, 다른 세션의 동시성, Tool Worker, LLM 서버 GPU 병목을 다른 박스로 표현.

**Space-only semantic builds:**

- `F027-B01`: 동기 응답.
- `F027-B02`: 스트리밍.
- `F027-B03`: background job.
- `F027-B04`: Cron.
- `F027-B05`: 재시작/중복 작업 지점 표시.

**Speaker script / detailed explanation:** Hermes의 Gateway가 여러 채널·세션을 관리한다고 해서 외부 Tool/DB 변경이 exactly-once로 보장되는 것은 아니다. Cron 작업 결과를 어떤 채널로 전달하는지, Job의 상태·재시도·중복 방지 경로를 살펴야 한다. `hermes` slash/CLI 명령은 해당 버전의 실제 지원여부 확인 후 예시로 제시한다.

**Likely Q&A:** Q. Cron은 현재 대화를 한 번 더 돌리는 것인가요? A. 스케줄러가 새로운 작업을 트리거할 수 있습니다. 실제 세션·History 정책은 구현에 의존합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S12` reference: [LOCAL-H2] §§15–16; [OFFICIAL-H-ARCH].. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “지금까지의 부품이 한 BIN 분석 실행에서는 어떻게 보일까?”

### F028 | S12 deep dive · Gateway와 Cron의 실행 수명

**Section/master/template:** Hermes / `H-ARCH` / `T-SEQ`. **Question/purpose:** 주기적 트리거는 현재 모델 Loop의 다음 토큰이 아니다.

**Exact audience headline:** “주기적 트리거는 현재 모델 Loop의 다음 토큰이 아니다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Gateway: 채널 이벤트 → 사용자·세션 라우팅
- Cron: 스케줄러 → 별도 Agent Task
- LLM 서버: 여러 Run의 추론 요청을 처리

**Geometry and labeled visual (explicit construction):** 두 시작점 Gateway/Cron → AIAgent Run → Model Gateway; 현재 Run 재귀와 Scheduler 트리거를 서로 다른 라인으로.

**Space-only semantic builds:**

- `F028-B01`: Gateway 채널 이벤트.
- `F028-B02`: 세션/인가 검사.
- `F028-B03`: Cron tick 별도 Run.
- `F028-B04`: 결과 전달·저장.
- `F028-B05`: 중복 작업 방지 문제.

**Speaker script (readable Korean):** “사용자가 100명이라고 Agent 프로세스가 반드시 100개인 것도 아니고, Cron 스케줄이 Tool Loop 한 번을 뜻하지도 않습니다.”

**Technical explanation / caution / counterexample:** Cron job 새 history 여부는 해당 문서/버전 기준. 동시 사용자/세션 별 격리는 구축 방식 의존. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-H-ARCH` and same legacy `S12`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F029 | S13 · Hermes 대표 실행 — 세 가지 질문을 하나의 Trace로

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-DEMO`.

**Exact audience headline:** “Hermes 대표 실행 — 세 가지 질문을 하나의 Trace로”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `BIN 오류율 조회 → 근거 분석 → 예측` / `매 단계: 실제 요청·Tool·History·종료 판단을 확인`.

**Diagram/layout specification:** 고정된 H 마스터 위에 3개의 턴 스티커: `T1 조회`, `T2 근거`, `T3 예측`. 아래 *실제 기록에서만* 채워질 `run ID`, `model ID`, `tool_calls`, `context chars/tokens`, `result` 빈 슬롯. **아직 값 없음** 표시.

**Space-only semantic builds:**

- `F029-B01`: 모델 입력 보이기.
- `F029-B02`: 실행된 Tool.
- `F029-B03`: 추가 모델 호출.
- `F029-B04`: State/Memory 변화.
- `F029-B05`: 분기와 종료. 외부 화면 진입 위치 설명.

**Speaker script / detailed explanation:** 데모는 실제 Hermes 소스/패키지를 설치하고 최소 침습 관측한다. 데모 브라우저에서 Space는 **이미 기록된 이벤트**를 순서대로 읽는 기능이지 모델을 강제로 단일 스텝 실행시키는 기능이 아니다. 캐시·압축·Subagent가 실제 발생하지 않으면 미발생으로 표시한다.

**Likely Q&A:** Q. Demo 화면에서 Space를 누르면 LLM이 실제로 한 단계 실행하나요? A. 아니요. 검증된 실제 Run의 이벤트 기록을 한 단계씩 표시합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S13` reference: 인계 §7.2. 시연 경로 DEMO-H-T1–T7.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “별도 Demo 1 탭으로 이동한다.”

### F030 | S14 · Demo 1 복귀 — Hermes에서 개발자가 얻는 것과 남는 책임

**Section/master:** Hermes / `H-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-DEMO`.

**Exact audience headline:** “Demo 1 복귀 — Hermes에서 개발자가 얻는 것과 남는 책임”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `이미 갖춘 것: Harness·Tool·Memory·Sessions·Gateway` / `남는 것: 도메인 데이터의 정확성·권한·신선도·운영 검증`.

**Diagram/layout specification:** S04 마스터의 실제 Demo에서 관측된 영역만 채색; 미발생/미관측 구역은 회색 점선. 가운데 `Tool schema가 존재한다 ≠ 권한이 보장된다`.

**Space-only semantic builds:**

- `F030-B01`: 확인된 경로.
- `F030-B02`: 확인 불가 영역.
- `F030-B03`: 개발자 책임.

**Speaker script / detailed explanation:** 실제 실행 전이라면 관측 사실이 아닌 발표 목표로만 기재. BIN 결과의 참값은 DB·평가 자료가, 안전성은 애플리케이션과 실행 계층이 책임진다. Hermes가 잘하는 것은 통합 실행 Harness를 빠르게 활용할 수 있다는 것.

**Likely Q&A:** Q. Hermes로 실행 성공했다면 결과의 업무 정확성까지 증명되나요? A. 아닙니다. 소스 데이터, 기간·분모, 보안 인가 및 평가를 별도로 검증합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-H-ARCH, OFFICIAL-H-LOOP`; legacy `S14` reference: [LOCAL-H2], [LOCAL-CMP] §§23, 32.. **Trace:** Demo 1, actual event IDs only after record and hash verification.

**Bridge:** “같은 Harness 성격의 Claude Code는 무엇을 다르게 선택했을까?”

### F031 | S15 · Claude Code 전체 아키텍처 — CLI Harness와 코딩 작업 환경

**Section/master:** Claude Code / `C-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ARCH`.

**Exact audience headline:** “Claude Code 전체 아키텍처 — CLI Harness와 코딩 작업 환경”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Claude Code = 파일·Shell·프로젝트 지침·세션·권한을 통합한 코딩 Agent Harness`.

**Diagram/layout specification:** `Terminal/IDE/Desktop`(C-ENTRY) → `Claude Code runtime (internal implementation not fully public)`(C-RUNTIME) ↔ `Claude model`(C-MODEL). 아래 `Tools: Read/Edit/Bash/MCP`, `Instructions: CLAUDE.md, rules`, `Memory/Skills/Session`, `Hooks/Permissions/Sandbox`, 오른쪽 `Subagents/Teams`. SDK로 접근하는 얇은 통로는 나중에 S35에서만 확대.

**Space-only semantic builds:**

- `F031-B01`: 입력 채널.
- `F031-B02`: Harness와 모델 경계.
- `F031-B03`: 작업 도구·정책.
- `F031-B04`: 세션·협업.

**Speaker script / detailed explanation:** Hermes와 같은 큰 범주의 완성형 Agent를 비교하되, Claude Code 내부 바이너리의 소스 함수 경로를 임의로 만들지 않는다. 공개된 것은 사용 계약·CLI·Hook·SDK 등이며 핵심 내부 Loop 모두가 공개 소스인 것은 아니다.

**Mandatory correctness refinement:** Claude Code 내부 핵심 runtime 구현 소스가 공개된 것처럼 파이썬 함수명 발명 금지.

**Likely Q&A:** Q. Claude Code의 모든 내부 Loop 코드가 공개돼 있나요? A. 아닙니다. 문서화된 CLI·Hook·SDK 계약과 비공개 내부 경계를 분리합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-C-MEMORY`; legacy `S15` reference: [LOCAL-C2], [OFFICIAL-C-MEMORY], [OFFICIAL-S].. **Trace:** No fake actual trace.

**Bridge:** “프로젝트 지침과 기억은 Hermes와 동일하게 고정될까?”

### F032 | S15 deep dive · Claude Code의 공개 범위

**Section/master/template:** Claude Code / `C-ARCH` / `T-ARCH`. **Question/purpose:** 비공개 코어를 소스 분석했다고 표현하지 않는다.

**Exact audience headline:** “비공개 코어를 소스 분석했다고 표현하지 않는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 공개: CLI 동작 계약 · Hooks · Skills · Permissions · SDK
- 비공개 경계: 내부 스케줄러/Agent Loop 구현 상세
- 비교 기준: 관찰 가능한 계약·제어권

**Geometry and labeled visual (explicit construction):** C-ARCH의 Runtime은 반투명 박스, 공개 Hook/Tool 계약은 선명한 외부 테두리; “source-confirmed”와 “docs-confirmed” 구분.

**Space-only semantic builds:**

- `F032-B01`: 사용자가 볼 수 있는 입출력.
- `F032-B02`: 공개 설정과 Hook.
- `F032-B03`: 내부 코어 검은 박스.
- `F032-B04`: Hermes 공개 Python 소스와 대비.

**Speaker script (readable Korean):** “Claude Code는 문서와 지원되는 확장점으로 충분히 분석할 수 있지만, 공개되지 않은 내부 함수 이름을 임의로 만들 수는 없습니다.”

**Technical explanation / caution / counterexample:** CLI 내부 로그나 SDK 메시지로 전체 내부 모델 입력을 자동 복원했다고 주장 금지. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-C; OFFICIAL-S` and same legacy `S15`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F033 | S16 · Claude Code의 Instruction·Memory·Skill과 실제 명령

**Section/master:** Claude Code / `C-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Claude Code의 Instruction·Memory·Skill과 실제 명령”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `프로젝트 지침 / 자동 메모리 / 필요한 시점의 Skill` / `관찰·압축·재개 명령을 '작동 원리'와 연결`.

**Diagram/layout specification:** C-RUNTIME 확대, 지침 파일 읽기 → 세션 프롬프트, Auto Memory 파일 → 필요 시 조회, Skills 메타데이터 → 선택적 본문 로딩. 오른쪽 명령 후보: `/context`(컨텍스트 보기), `/compact`(압축), `/resume`(세션 선택), `claude -c`(최근 대화 이어가기), 버전 검증 마크. `CLAUDE.md / AGENTS.md`는 fallback/import 조건을 두 갈래로 표현하고 둘 다 항상 자동 로딩된다고 그리지 않는다.

**Space-only semantic builds:**

- `F033-B01`: 세션 시작.
- `F033-B02`: 추가 파일 참조.
- `F033-B03`: 압축.
- `F033-B04`: 재개. 명령의 효과를 이벤트와 연결.

**Speaker script / detailed explanation:** `/context`가 모든 실제 Provider wire payload를 보여 준다는 뜻이 아니다. Memory와 프로젝트 파일은 용도가 다르며 재개는 로컬 파일 변경을 자동 복원해 준다는 뜻이 아니다. 명령 구문은 해당 릴리스에서 공식 문서/CLI `--help`로 확인 후 출력한다.

**Mandatory correctness refinement:** CLAUDE.md와 AGENTS.md가 무조건 같은 자동 로딩 규칙이라고 주장 금지.

**Likely Q&A:** Q. CLAUDE.md와 Skill은 같은 시점에 같은 방식으로 로드되나요? A. 다릅니다. 지침과 절차는 탐색·로딩·수명의 규칙이 달라 릴리스별로 확인합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-C-MEMORY`; legacy `S16` reference: [LOCAL-C2], [OFFICIAL-C-MEMORY], [OFFICIAL-C-HOOKS]. R07.. **Trace:** No fake actual trace.

**Bridge:** “이 Harness는 Tool 권한을 어디에서 강제할까?”

### F034 | S16 deep dive · Instruction과 Auto Memory는 역할이 다르다

**Section/master/template:** Claude Code / `C-ARCH` / `T-COMP`. **Question/purpose:** CLAUDE.md·자동 메모리·Skill은 다른 수명과 로딩 규칙을 가진다.

**Exact audience headline:** “CLAUDE.md·자동 메모리·Skill은 다른 수명과 로딩 규칙을 가진다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- CLAUDE.md: 프로젝트/사용자 지침
- Auto Memory: 작업 중 축적된 유용 정보
- Skill: 필요할 때 로드하는 재사용 절차

**Geometry and labeled visual (explicit construction):** 세 개의 서로 다른 파일 스택에서 현재 세션으로 들어오는 화살표; 로딩 보장 범위는 명시된 docs만.

**Space-only semantic builds:**

- `F034-B01`: 프로젝트 지침 경로.
- `F034-B02`: 자동 메모리 경로.
- `F034-B03`: Skill 발견·로드.
- `F034-B04`: 현재 Context에 무엇이 보이는지.
- `F034-B05`: /compact·/resume과 구분.

**Speaker script (readable Korean):** “기억과 지침, Skill은 모두 파일일 수 있지만, 시스템이 파일을 발견하고 모델에 넣는 규칙은 서로 다릅니다.”

**Technical explanation / caution / counterexample:** AGENTS.md를 CLAUDE.md와 무조건 동일하게 자동 로딩한다고 쓰지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-C-MEMORY` and same legacy `S16`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F035 | S17 · Claude Code Permission·Hook·Sandbox: 모델에게 지시하는 것과 강제하는 것

**Section/master:** Claude Code / `C-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Claude Code Permission·Hook·Sandbox: 모델에게 지시하는 것과 강제하는 것”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Tool 선택은 모델, 실행 허가는 Runtime, 실제 접근은 OS/서버`.

**Diagram/layout specification:** `모델의 Bash/Edit/MCP call` → `permission rules + PreToolUse hooks` → `sandbox / filesystem / credentials` → Tool. **보호 주체를 3개**로 분리하고 `Read Hook만 보호`처럼 특정 경로에만 적용된 정책이 다른 읽기 경로까지 통제하지 못하는 예시 표시.

**Space-only semantic builds:**

- `F035-B01`: 모델이 실행 시도.
- `F035-B02`: 승인/Hook.
- `F035-B03`: OS 경계.
- `F035-B04`: PostToolUse/결과 흐름. Hooks 실패가 항상 차단인지 이벤트별로 다르므로 `설정/이벤트에 따라 다름` 주석.

**Speaker script / detailed explanation:** `allowed_tools`나 Permission Mode는 하나의 모든 실행을 강제하는 만능 Whitelist가 아니다. 더 안전한 Agent는 실제 DB·파일 권한을 Runtime 외부에서 중복 검사해야 한다.

**Likely Q&A:** Q. Permission 설정만 있으면 외부 DB도 보호되나요? A. 아닙니다. 외부 DB가 사용자·Lot 권한을 직접 검증해야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-C-MEMORY`; legacy `S17` reference: [OFFICIAL-C-HOOKS], [LOCAL-C2].. **Trace:** No fake actual trace.

**Bridge:** “부모·자식만 있으면 모든 Multi-Agent를 설명할 수 있을까?”

### F036 | S17 deep dive · Hook·Permission·Sandbox의 세 단계

**Section/master/template:** Claude Code / `C-ARCH` / `T-SEQ`. **Question/purpose:** 실행 전 정책이 통과해도 OS/DB 접근 권한은 따로 결정된다.

**Exact audience headline:** “실행 전 정책이 통과해도 OS/DB 접근 권한은 따로 결정된다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 모델이 Read/Edit/Bash 요청
- Permission Rules와 PreToolUse Hook 평가
- Sandbox/OS/External API의 최종 강제

**Geometry and labeled visual (explicit construction):** 모델→승인/Hook→Shell/DB 3개 경계; 실패 화살표는 발생한 계층에만 위치.

**Space-only semantic builds:**

- `F036-B01`: Tool 호출.
- `F036-B02`: Permission 평가.
- `F036-B03`: Hook 조건부 실행.
- `F036-B04`: OS·서버 차단.
- `F036-B05`: PostToolUse 기록.

**Speaker script (readable Korean):** “Permission 모드만 설정하면 모든 외부 서버가 보호된다는 의미가 아닙니다. 리소스를 소유한 서비스가 인가를 수행해야 합니다.”

**Technical explanation / caution / counterexample:** Hook event별 제어 결과 코드 차이를 확인할 것. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-C-HOOKS` and same legacy `S17`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F037 | S18 · Claude Code Subagent vs Agent Teams — 협업 구조 자체가 다르다

**Section/master:** Claude Code / `C-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Claude Code Subagent vs Agent Teams — 협업 구조 자체가 다르다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Subagent = 부모가 맡기고 결과를 받음` / `Teams = 독립 세션들이 메시지·업무를 공유`.

**Diagram/layout specification:** 왼쪽 `Lead → Child A/B → Lead` 단방향 결과 반환; 오른쪽 `Lead + teammate A/B/C` 각각 자기 세션에서 직접 메시지, 공유 작업 상태(작업 단위). 오른쪽에 `experimental / enablement conditional` 각주. `서로 다른 세션`과 `별도 OS 보안 경계`를 동일시하지 말 것.

**Space-only semantic builds:**

- `F037-B01`: 부모 위임.
- `F037-B02`: 결과만 부모 전달.
- `F037-B03`: 팀 간 메시지.
- `F037-B04`: 상태·토큰·충돌 부담.

**Speaker script / detailed explanation:** 독립적인 참가자가 여러 결과를 서로 검증해야 한다면 Teams의 장점이 있을 수 있지만, 공유 파일 충돌·정책 일관성·비용이 증가한다. 실제 Agent Teams 활성화 방식·제약은 배포 버전에 따라 확인한다. 성능 우위를 수치 없이 주장하지 않는다.

**Likely Q&A:** Q. Agent Teams는 단순 Subagent 호출을 여러 번 한 것인가요? A. 팀원 간 직접 의사소통과 작업 공유가 가능하다는 점에서 부모 결과 반환 패턴과 다릅니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-C-MEMORY`; legacy `S18` reference: [OFFICIAL-C-TEAMS], [OFFICIAL-C-SUBAGENTS].. **Trace:** No fake actual trace.

**Bridge:** “같은 Harness라도 선택한 제어권이 다르다.”

### F038 | S18 deep dive · Teams가 Subagent와 다른 이유

**Section/master/template:** Claude Code / `C-ARCH` / `T-COMP`. **Question/purpose:** 팀원 간 직접 메시지·공유 작업은 단순 부모 호출과 다르다.

**Exact audience headline:** “팀원 간 직접 메시지·공유 작업은 단순 부모 호출과 다르다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Subagent: 부모→위임→결과 반환
- Agent Teams: 팀원 간 메시지·독립 작업
- 대가: 설정·동시성·충돌·비용

**Geometry and labeled visual (explicit construction):** 좌측 단방향 트리, 우측 mesh+공유 Task 목록; 두 그림 크기는 동일하고 “실험/설정 의존” 각주.

**Space-only semantic builds:**

- `F038-B01`: Subagent 트리.
- `F038-B02`: 독립 팀원 노드.
- `F038-B03`: 직접 메시지 흐름.
- `F038-B04`: 공유 Task/충돌.
- `F038-B05`: 선택 기준.

**Speaker script (readable Korean):** “프로젝트 파일을 공유한다는 것과 서로 동일한 모델 Context를 가진다는 것도 다른 이야기입니다.”

**Technical explanation / caution / counterexample:** 기본 활성 여부, 팀원 통신·지원 범위는 설치 버전 공식 확인. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-C-TEAMS; OFFICIAL-C-SUBAGENTS` and same legacy `S18`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F039 | S19 · Hermes ↔ Claude Code — 비교의 결론

**Section/master:** Claude Code / `C-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-COMP`.

**Exact audience headline:** “Hermes ↔ Claude Code — 비교의 결론”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `같은 Harness 계층, 다른 확장·관찰·권한 계약`.

**Diagram/layout specification:** 비교 열 `코어 공개성`, `메모리/지침`, `Tool 등록`, `Hooks/권한`, `Subagent/Teams`, `Gateway/배포`. 단정적 우열 표기 금지. 예: Hermes의 공개 Python Agent Loop와 SQLite/FTS5, Claude Code의 공개 CLI/SDK/Hook 계약과 비공개 코어 경계.

**Space-only semantic builds:**

- `F039-B01`: 현재 화면의 비교 축과 출발 주체를 한 가지씩 표시.
- `F039-B02`: Hermes에서 봤던 구조 그림 왼쪽과 Claude 오른쪽, 항목별 단 한 줄 차이.
- `F039-B03`: 해당 실행 경계의 확인 가능한 결과와 개발자 책임을 구분해 표시.

**Speaker script / detailed explanation:** Hermes를 소스 수준으로 수정·관찰하는 연구는 상대적으로 직접적이다. Claude Code는 통합 코딩 경험을 재사용할 수 있지만 내부 세밀한 알고리즘 변경은 공개 API 경계에 제한된다. 선택은 통제·운영·모델 경로에 따라 달라진다.

**Likely Q&A:** Q. Hermes와 Claude Code 중 하나가 언제나 우월한가요? A. 공개 수정 범위와 통합형 코딩 경험, 운영 제약을 무엇에 우선하느냐에 따라 달라집니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-C-MEMORY`; legacy `S19` reference: [LOCAL-H2], [LOCAL-C2], [LOCAL-CMP] §§23,28.. **Trace:** No fake actual trace.

**Bridge:** “이제 완성된 Harness에서 직접 Agent 애플리케이션을 개발하는 Core로 이동한다.”

### F040 | S20 · Pydantic → PydanticAI Core → 별도 Harness, 무엇이 달라지는가

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Pydantic → PydanticAI Core → 별도 Harness, 무엇이 달라지는가”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Pydantic = 데이터 검증 기반` / `PydanticAI Core = Agent 실행·도구·출력 계약` / `Harness = 여러 Capability를 묶은 선택적 Agent Stack`.

**Diagram/layout specification:** 3개의 크기가 다른 레이어가 아닌 **상호 의존 지도**. 아래 `Pydantic: BaseModel/validation`, 중앙 `PydanticAI: Agent/Graph/Toolsets/Model/Output`, 오른쪽에 붙는 `pydantic-ai-harness (별도 패키지): Memory/Skills/Compaction/Guardrails/...`, 바깥 `Logfire / Evals / 외부 DB·API`. `pydantic_graph`는 별도 Graph 라이브러리, Core 내부 실행 Graph와 연결되지만 동일한 사용 API로 오인 금지.

**Space-only semantic builds:**

- `F040-B01`: Pydantic 기본 역할 10초.
- `F040-B02`: AI Core.
- `F040-B03`: Harness는 추가/선택.
- `F040-B04`: 애플리케이션 책임 표시.

**Speaker script / detailed explanation:** 프레임워크의 핵심 가치는 Pydantic으로 JSON만 검사한다는 것이 아니다. 모델 호출·도구 검증·Graph 노드 전이·재시도/출력 완료 정책을 제공한다. 하지만 DB 권한, 데이터 신선도, 승인자 정보, 상태 저장소는 설계 대상이다. Harness의 지원 항목·버전은 Core v2.61.0과 각각 따로 고정한다.

**Mandatory correctness refinement:** PydanticAI Core / Pydantic(pydantic) / 별도 Harness package를 각각 독립 판별.

**Likely Q&A:** Q. PydanticAI는 Pydantic BaseModel 검증 래퍼에 불과한가요? A. 아닙니다. Agent Run, 내부 Graph, Tool 호출과 최종 출력 정책을 Core가 수행합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S20` reference: [LOCAL-P2] §§2,4,15–20; [OFFICIAL-P-HARNESS]. R01/R05.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “실제로 개발자는 코드 어느 부분을 쓰고 Core는 어디부터 실행할까?”

### F041 | S20 deep dive · Pydantic, Core, Harness를 분리

**Section/master/template:** PydanticAI / `P-ARCH` / `T-ARCH`. **Question/purpose:** Pydantic으로 타입을 검사하는 것만이 PydanticAI의 본질은 아니다.

**Exact audience headline:** “Pydantic으로 타입을 검사하는 것만이 PydanticAI의 본질은 아니다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Pydantic: Schema/Validation
- PydanticAI Core: Agent/Model/Tool/Graph/Output
- 추가 Harness: 선택적 Capability를 묶는 별도 계층

**Geometry and labeled visual (explicit construction):** 3개 박스를 위로 쌓지 말고 왼쪽 Foundation, 가운데 Core, 오른쪽 선택 Harness + 바깥 App 저장소. 제품·패키지 경계 선.

**Space-only semantic builds:**

- `F041-B01`: Pydantic validation.
- `F041-B02`: AI Core 실제 Loop.
- `F041-B03`: 별도 Harness 옵션.
- `F041-B04`: 앱의 DB/Policy는 외부.

**Speaker script (readable Korean):** “Core는 검증뿐 아니라 Tool 호출과 내부 실행 Graph, 결과 종료 조건까지 수행합니다. 단 PydanticAI를 설치했다고 상위 Harness 기능을 모두 얻는 것은 아닙니다.”

**Technical explanation / caution / counterexample:** 별도 Harness 실제 패키지·지원 Capability는 고정 릴리스 확인 후 확정. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-AGENT; OFFICIAL-P-HARNESS` and same legacy `S20`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F042 | S21 · PydanticAI 전체 아키텍처 — 개발자 정의와 Runtime 경계

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ARCH`.

**Exact audience headline:** “PydanticAI 전체 아키텍처 — 개발자 정의와 Runtime 경계”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `개발자가 계약을 선언하면, Core가 이를 실행 Graph로 해석한다`.

**Diagram/layout specification:** 좌측 `App: Agent config / model / instructions / tools / deps / output_type / history`(P-APP). 중앙 `Agent Run → UserPromptNode → ModelRequestNode ↔ CallToolsNode → End`(P-GRAPH). 위 `Model+Provider`(P-MODEL), 우측 `ToolManager / Toolsets / OutputValidator`(P-TOOLS), 아래 `RunContext / Messages / Deferred`(P-STATE). 외부 점선 `Harness/Logfire/Evals`, `Session storage`, `App policy`.

**Space-only semantic builds:**

- `F042-B01`: App 코드 작성.
- `F042-B02`: 실행 Graph 진입.
- `F042-B03`: 모델·도구 ↔ 반복.
- `F042-B04`: 검증 완료/대기.
- `F042-B05`: 애플리케이션 저장·응답.

**Speaker script / detailed explanation:** 그래프는 사용자가 LangGraph를 붙여야 동작한다는 뜻이 아니다. `pydantic_graph`를 사용한 사용자 정의 워크플로와 내부 Graph는 구분한다. Deps는 Python 실행 자원, History는 LLM 메시지, Output Type은 결과 계약이다.

**Likely Q&A:** Q. PydanticAI Core를 쓰려면 개발자가 Loop while을 직접 구현해야 하나요? A. 기본 Run Loop는 Core가 제공하지만 업무 Tool·권한·상태 저장은 개발 책임입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S21` reference: [LOCAL-P2] §§4–6; [OFFICIAL-P-AGENT].. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “같은 Agent를 돌려도 API에 따라 관찰하는 수명은 다르다.”

### F043 | S21 deep dive · 개발자 코드와 Core 경계

**Section/master/template:** PydanticAI / `P-ARCH` / `T-ARCH`. **Question/purpose:** 개발자가 Agent를 정의하고 Core가 실행한다.

**Exact audience headline:** “개발자가 Agent를 정의하고 Core가 실행한다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- App: Agent/Tools/Deps/OutputType 선언
- Core: Graph/ToolManager/ModelRequest/Validation
- App: 데이터 인가·저장·운영

**Geometry and labeled visual (explicit construction):** P-ARCH 프레임 두 영역 App-owned/Framework-owned; Developer code→Graph 파란 화살표, Core→Tool handler 녹색.

**Space-only semantic builds:**

- `F043-B01`: 개발자 정의 객체.
- `F043-B02`: 내부 Graph 진입.
- `F043-B03`: 모델/도구를 반복.
- `F043-B04`: 결과와 RunResult.
- `F043-B05`: 남은 앱 책임.

**Speaker script (readable Korean):** “개발자가 별도의 while True 루프를 반드시 작성할 필요는 없지만, 업무 규칙과 데이터의 진위를 검증하는 코드는 여전히 작성해야 합니다.”

**Technical explanation / caution / counterexample:** 내부 Graph와 사용자 정의 pydantic_graph Workflow 혼동 금지. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-AGENT` and same legacy `S21`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F044 | S22 · 다섯 실행 API — 사용자 코드에서 보이는 실행 수명의 차이

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “다섯 실행 API — 사용자 코드에서 보이는 실행 수명의 차이”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `run_sync / run / run_stream / run_stream_events / iter는 동일한 출력 포맷의 변형이 아니다`.

**Diagram/layout specification:** 행 5개 표: `run_sync` 동기 완료 `RunResult`; `run` 비동기 완료 `RunResult`; `run_stream` 출력 중심 스트림과 수명 관리; `run_stream_events` 전체 Event 스트림과 최종 결과 Event; `iter` Graph 노드 단계 탐색. 오른쪽 세로 3색 `완료값 / 이벤트 / 노드 제어`. 문서상 세부 반환 객체·ContextManager 구현은 고정판 검증 표시.

**Space-only semantic builds:**

- `F044-B01`: 쉬운 완결 실행.
- `F044-B02`: 스트리밍의 차이.
- `F044-B03`: 관찰 데모에는 `run_stream_events`/`iter` 검토.

**Speaker script / detailed explanation:** `run_stream()`은 사용자가 예상한 최종 출력이 먼저 나타나면 추가 Tool과의 관계가 비스트리밍 `run()`과 달라질 수 있다. 일부 Tool이 끝나기 전 화면에 문자가 나왔다고 애플리케이션 전체 작업이 완료된 것은 아니다. 데모는 Graph 수명 관찰이 목적이므로 전체 이벤트 스트림 우선 설계.

**Mandatory correctness refinement:** 공식 문서의 5가지 중심 Run API와 보조 sync streaming API를 분리. run_stream_events는 전체 이벤트 기반.

**Likely Q&A:** Q. run_stream()은 run()에서 결과를 스트리밍하기만 하나요? A. 첫 유효 출력 확정과 후속 Tool 처리 등 수명 차이가 있어 공식 계약을 확인해야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S22` reference: [OFFICIAL-P-AGENT] 실행 API 설명; [LOCAL-P2] §5. R01/R03.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “그 이벤트가 내부 어떤 Node에서 만들어지는지 보자.”

### F045 | S22 deep dive · 다섯 Run 방식의 의미

**Section/master/template:** PydanticAI / `P-ARCH` / `T-COMP`. **Question/purpose:** 완료값, 출력 스트림, 전체 이벤트, Graph 노드 관찰은 다르다.

**Exact audience headline:** “완료값, 출력 스트림, 전체 이벤트, Graph 노드 관찰은 다르다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- run_sync/run: 완료된 RunResult
- run_stream: 출력이 먼저 확정될 수 있는 수명
- run_stream_events: 전체 이벤트 / iter: Graph node

**Geometry and labeled visual (explicit construction):** 5행 스윔레인; 같은 초기 입력에서 관찰 가능한 층만 강조. 각 메서드별 실제 반환 객체 이름을 노트.

**Space-only semantic builds:**

- `F045-B01`: run()/run_sync().
- `F045-B02`: run_stream().
- `F045-B03`: run_stream_events().
- `F045-B04`: iter().
- `F045-B05`: 데모는 원인 파악용 경로 선택.

**Speaker script (readable Korean):** “스트리밍이 단순히 텍스트를 조금씩 받는 옵션만은 아닙니다. 어떤 API는 출력으로 인식한 순간에 실행이 확정될 수 있습니다.”

**Technical explanation / caution / counterexample:** run_stream_sync 보조형을 별도 6번째 주요 방식으로 중복 집계하지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-AGENT; OFFICIAL-P-OUTPUT` and same legacy `S22`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F046 | S23 · PydanticAI Graph의 핵심: 모델 응답을 받아 어떤 Node로 이동하는가

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “PydanticAI Graph의 핵심: 모델 응답을 받아 어떤 Node로 이동하는가”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `UserPromptNode → ModelRequestNode → CallToolsNode ↔ ModelRequestNode → End`.

**Diagram/layout specification:** 중앙 State Machine에 3개 Node와 `End`, `Deferred` 분기. `ModelRequestNode`에서 모델 응답을 받아 `Function Tool / Output Candidate / Retry Needed`로 나눔. RunContext와 History는 Node 옆의 공유 상태로 표현.

**Space-only semantic builds:**

- `F046-B01`: 입력 메시지 생성.
- `F046-B02`: Provider 요청.
- `F046-B03`: Tool Call 이벤트.
- `F046-B04`: 인자 검증·출력 검증.
- `F046-B05`: 재모델/종료/Deferred. 실패 유형별 분기를 다른 라벨로.

**Speaker script / detailed explanation:** “언제 종료하나?”의 답은 요청이 끝났기 때문이 아니라 **유효한 최종 출력 후보를 채택했고 해당 EndStrategy/Run 계약상 남은 실행이 더 이상 필요하지 않을 때**다. 도구 실패·Schema 실패는 여러 Retry 경로 중 어디로 반영되는지 구분한다.

**Likely Q&A:** Q. 왜 ModelRequestNode 뒤에 바로 End가 아닌가요? A. 모델 출력의 Tool Call·검증·Retry·Deferred 여부를 평가하고 다음 노드나 종료가 결정됩니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S23` reference: [LOCAL-P2] §§4–7,10–13; [OFFICIAL-P-AGENT], [OFFICIAL-P-OUTPUT].. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “모델에는 Python에 있는 정보를 전부 보내는가?”

### F047 | S23 deep dive · Graph Node의 시간축

**Section/master/template:** PydanticAI / `P-ARCH` / `T-SEQ`. **Question/purpose:** 모델 응답 후 CallToolsNode의 결과에 따라 종료 또는 재호출.

**Exact audience headline:** “모델 응답 후 CallToolsNode의 결과에 따라 종료 또는 재호출”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- UserPromptNode → ModelRequestNode
- CallToolsNode: Tool·Output·Validation의 실제 분기
- 반복·End·Deferred 결과를 분리

**Geometry and labeled visual (explicit construction):** P-GRAPH 동일 미니맵 위에 4개 상태 변환 큰 확대도; 빨간 Retry, 주황 Deferred, 민트 End.

**Space-only semantic builds:**

- `F047-B01`: UserPromptNode.
- `F047-B02`: ModelRequestNode.
- `F047-B03`: Tool Call 도착.
- `F047-B04`: CallToolsNode 분기.
- `F047-B05`: ModelRequest 반복 또는 End.

**Speaker script (readable Korean):** “마지막 노드는 단순히 모델이 문장을 출력해서가 아니라 최종 Output 유효성과 Tool/EndStrategy 조건이 만족된 결과입니다.”

**Technical explanation / caution / counterexample:** 정확한 내부 클래스·Node 수는 고정 버전 링크에서 확인. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-AGENT; OFFICIAL-P-OUTPUT` and same legacy `S23`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F048 | S24 · Instructions·Deps·History·Tool Schema: 모델에 '보이는 것'의 경계

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Instructions·Deps·History·Tool Schema: 모델에 '보이는 것'의 경계”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Deps는 App 실행 문맥; Instructions·History·Tool Schema는 모델 요청 재료`.

**Diagram/layout specification:** 좌측 App Layer에 `RunContext.deps` 안의 DB connection·권한 식별자(마스킹), 우측 Provider payload에 `system/instructions, messages, tools, output mode` 패널. 가운데 `runtime only` vs `serialized to model` 열 비교. Deps 속 데이터를 Tool가 결과로 반환하면 모델에 보일 수 있다는 조건부 화살표.

**Space-only semantic builds:**

- `F048-B01`: 요청 입력.
- `F048-B02`: dynamic instructions 평가.
- `F048-B03`: History와 Tool Schema 준비.
- `F048-B04`: Provider adapter.
- `F048-B05`: 실제 요청 직전 관찰 시점.

**Speaker script / detailed explanation:** 사용자별 허용 Lot을 프롬프트에 명시하는 것과 DB Tool이 실제 사용자를 인증해 해당 Lot만 읽도록 강제하는 것은 다르다. 완성 화면에는 Provider 변환 전 내부 객체를 `실제 HTTP payload`라고 라벨링하지 않는다.

**Likely Q&A:** Q. deps에 넣은 DB 연결이 LLM에게 그대로 보내지나요? A. 아닙니다. Python 실행 문맥이고 Tool이 반환한 허용 데이터만 모델 메시지로 전달될 수 있습니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S24` reference: [LOCAL-P2] §§7–10,14. R03/R09.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “그 Tool의 Python 함수는 정확히 어떻게 호출될까?”

### F049 | S24 deep dive · Deps는 모델 메시지가 아니다

**Section/master/template:** PydanticAI / `P-ARCH` / `T-COMP`. **Question/purpose:** Python RunContext.deps에는 실행 자원이 있지만 ModelRequest에 자동 직렬화되지 않는다.

**Exact audience headline:** “Python RunContext.deps에는 실행 자원이 있지만 ModelRequest에 자동 직렬화되지 않는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Runtime: DB handle / principal / evaluator
- Model Input: instructions / message history / tool schemas
- Tool Output을 거쳐 선택된 데이터만 모델에 전달

**Geometry and labeled visual (explicit construction):** P-APP와 Provider Payload를 두 열로, Deps에서 Payload 직행 화살표에는 금지선; Tool handler를 통과한 반환만 파랑.

**Space-only semantic builds:**

- `F049-B01`: Deps 생성.
- `F049-B02`: Tool 함수에서 ctx.deps 사용.
- `F049-B03`: DB 인가 후 ToolResult.
- `F049-B04`: 모델 Request에서 반환 데이터 확인.

**Speaker script (readable Korean):** “‘DB 객체를 dependencies로 넘겼다’는 것은 DB 비밀번호를 LLM에 전송했다는 뜻이 아닙니다.”

**Technical explanation / caution / counterexample:** 데모 캡처는 SDK_OBJECT/PROVIDER_REQUEST/WIRE_PAYLOAD 구분. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-AGENT; DEMO-TRACE` and same legacy `S24`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F050 | S25 · ToolManager: Schema를 전달한 뒤에도 검증·실행이 남는다

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “ToolManager: Schema를 전달한 뒤에도 검증·실행이 남는다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Function Tool = Schema 생성 → 모델 선택 → 인자 검증 → 정책/Hook → Handler 실행 → 결과 메시지`.

**Diagram/layout specification:** P-TOOLS 확대. 왼쪽 간략 예시 **[PSEUDO]** `@agent.tool; def query_bin(ctx, lot_id, start, end): ...` 4줄; 우측 실제 경로: `ToolDefinition → Model ToolCall(JSON) → ToolManager / Pydantic validation → function → ToolReturn`. 실패 시 `Validation error → retry feedback` 루프.

**Space-only semantic builds:**

- `F050-B01`: 등록.
- `F050-B02`: 모델에서 인자를 생성.
- `F050-B03`: 타입 검증.
- `F050-B04`: 권한 검증.
- `F050-B05`: 실제 조회.
- `F050-B06`: 실패 피드백.

**Speaker script / detailed explanation:** Tool의 입력 타입이 맞아도 `lot_id`의 접근 가능 여부, 데이터 일치 여부는 자동 보장되지 않는다. `@agent.tool`과 context가 없는 plain tool의 차이는 실제 데모 소스와 함께 보여준다. Toolset 필터는 노출 가능한 목록을 제한하지만 DB 인가 대체는 아니다.

**Likely Q&A:** Q. 정상 타입의 lot_id라면 조회해도 되나요? A. 형식 검증 성공과 그 사용자에게 허용된 Lot인지는 별도의 인가 판단입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S25` reference: [LOCAL-P2] §§9–11; [OFFICIAL-P-TOOLS].. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “모델이 Tool 3개를 동시에 요청하면 모두 실행할까?”

### F051 | S25 deep dive · Schema, Validation, Authorization 세 구분

**Section/master/template:** PydanticAI / `P-ARCH` / `T-SEQ`. **Question/purpose:** 타입 검증에 성공해도 허용된 Lot이라는 보장은 없다.

**Exact audience headline:** “타입 검증에 성공해도 허용된 Lot이라는 보장은 없다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Schema 생성: 함수를 모델에 설명
- Validation: arguments 타입·구조 확인
- Authorization: 실행 주체·Lot·시점/버전 제약 확인

**Geometry and labeled visual (explicit construction):** 좌측 ‘lot_id: string’ 체크 → 우측 Tool Handler에서 ‘allowed_lots includes lot_id?’ 검사; 서로 다른 색과 단계.

**Space-only semantic builds:**

- `F051-B01`: Tool Definition.
- `F051-B02`: LLM CallArgs.
- `F051-B03`: Pydantic 검증.
- `F051-B04`: 앱 정책·DB 인가.
- `F051-B05`: 결과 및 오류 재전달.

**Speaker script (readable Korean):** “문자열 Lot ID가 올바르게 생겼다는 것과 그 사용자가 그 Lot을 읽을 권한이 있다는 것은 다릅니다.”

**Technical explanation / caution / counterexample:** Retry가 항상 성공하거나 무한 반복된다고 표시 금지. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-TOOLS` and same legacy `S25`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F052 | S26 · 병렬 Tool과 `sequential` 장벽 — 동시에 실행하는 것과 안전한 순서

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “병렬 Tool과 `sequential` 장벽 — 동시에 실행하는 것과 안전한 순서”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `모델의 동시 호출 요청 ≠ 모든 Tool이 무조건 병렬 실행`.

**Diagram/layout specification:** `Tool A read`, `Tool B read`는 두 parallel lane; `Tool C side-effect`는 `sequential=True` 장벽 뒤 별도 레인. Event 타임라인에서 시작 순서/완료 순서/모델에 재투입한 결과 순서를 다르게 표현.

**Space-only semantic builds:**

- `F052-B01`: Tool Calls 리스트 수신.
- `F052-B02`: Barrier로 구간 분할.
- `F052-B03`: 비동기 Task/필요한 경우 동기 함수 실행 방식 구분.
- `F052-B04`: 결과·오류 수집.
- `F052-B05`: 모델 재질의.

**Speaker script / detailed explanation:** `asyncio` 기반 병렬 실행은 반드시 OS 스레드가 여러 개라는 뜻이 아니다. `sequential=True`도 DB 트랜잭션·모든 사용자 사이의 동시성을 자동 통제하지 않는다. 외부 부작용 호출은 승인·멱등성·읽기/쓰기 권한 분리가 더 중요하다.

**Mandatory correctness refinement:** sequential tool 실행은 전역 DB lock이나 다른 사용자 사이 serialization을 제공하지 않음.

**Likely Q&A:** Q. sequential=True로 Tool을 만들면 전 사용자 DB 쓰기가 직렬화되나요? A. 아닙니다. 특정 실행의 Tool 스케줄링 제약일 뿐 전역 DB lock/transaction을 대신하지 않습니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S26` reference: [LOCAL-P2] §11; [OFFICIAL-P-TOOLS]. R03.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “도구와 최종 Output이 같은 모델 응답에 섞이면?”

### F053 | S26 deep dive · 동시성의 정확한 표현

**Section/master/template:** PydanticAI / `P-ARCH` / `T-SEQ`. **Question/purpose:** async 동시 실행은 OS 스레드 3개 실행과 다르다.

**Exact audience headline:** “async 동시 실행은 OS 스레드 3개 실행과 다르다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 동시 Tool 요청 → async 실행 가능
- sequential=True 조건과 Barrier
- 시작/완료/History 병합은 다른 순서

**Geometry and labeled visual (explicit construction):** 3개 Tool lane(TA/TB/TC)과 Barrier 레인; 호출 순서 숫자와 실제 완료 timestamp 개별 표시.

**Space-only semantic builds:**

- `F053-B01`: 여러 Tool Call 도착.
- `F053-B02`: 동시 수행 가능 집합.
- `F053-B03`: sequential barrier.
- `F053-B04`: 결과 결합.
- `F053-B05`: 충돌/멱등성 점검.

**Speaker script (readable Korean):** “sequential은 특정 Run의 Tool 실행 순서 제약이지 다른 모든 사용자의 DB 쓰기를 직렬화하는 잠금이 아닙니다.”

**Technical explanation / caution / counterexample:** 해당 버전에서 sequential 옵션 지원 여부와 적용 정확한 경계를 확인. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-TOOLS` and same legacy `S26`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F054 | S27 · PydanticAI 출력은 단순 JSON 포맷의 문제가 아니다

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “PydanticAI 출력은 단순 JSON 포맷의 문제가 아니다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Output Type = 최종 Run의 결과 계약` / `Validated Schema ≠ 사실적으로 맞는 분석`.

**Diagram/layout specification:** 4개 열 `ToolOutput / NativeOutput / PromptedOutput / TextOutput`을 각각 `최종값을 얻는 경로`, `Provider 지원 의존성`, `검증·실패 피드백`의 축으로 정리. 오른쪽 `BIN 오류율 Schema 통과` vs `실제 분모·기간 틀림` 빨간 대비.

**Space-only semantic builds:**

- `F054-B01`: `output_type` 선언.
- `F054-B02`: 출력 생성 경로.
- `F054-B03`: Pydantic Validation.
- `F054-B04`: 실패 시 Retry/Feedback.
- `F054-B05`: 도메인 정합성 검사는 앱에서 추가.

**Speaker script / detailed explanation:** ToolOutput은 `최종 출력용 도구` 경로이지 일반 텍스트를 자동으로 Tool로 바꾸는 기능이 아니다. Native/Prompted는 모델·Provider 지원 및 파싱 경계가 다르다. 정확한 API import는 고정 릴리스 확인 후 코드 블록을 완성한다.

**Likely Q&A:** Q. 출력 JSON이 Pydantic 검증에 통과하면 맞는 예측인가요? A. 아닙니다. 데이터 분모·시간 누수·평가 지표·근거 확인이 별개입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S27` reference: [LOCAL-P2] §§12–13; [OFFICIAL-P-OUTPUT]. R01.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “출력이 유효한 상태에서 다른 Tool도 호출되었다면?”

### F055 | S27 deep dive · 출력 방식 네 가지

**Section/master/template:** PydanticAI / `P-ARCH` / `T-COMP`. **Question/purpose:** Output Mode는 모델/Provider와 종료 정책을 함께 바꾼다.

**Exact audience headline:** “Output Mode는 모델/Provider와 종료 정책을 함께 바꾼다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- ToolOutput: 출력 도구 호출
- NativeOutput: Provider-native structured output
- PromptedOutput/TextOutput: 다른 검증·파싱 경로

**Geometry and labeled visual (explicit construction):** 4개 카드 하나씩 등장, 오른쪽 하나의 공통 Pydantic Output Validation에 모임. Provider 조건은 회색 표식.

**Space-only semantic builds:**

- `F055-B01`: ToolOutput 경로.
- `F055-B02`: NativeOutput 경로.
- `F055-B03`: PromptedOutput/Text 경로.
- `F055-B04`: 검증 실패 피드백.
- `F055-B05`: 분석 사실성 검증은 별도.

**Speaker script (readable Korean):** “형식 검증을 통과해도 분모·기간·근거가 틀린 예측은 틀린 결과입니다.”

**Technical explanation / caution / counterexample:** 모델별 native/structured output 지원은 API 호환성 체크 필수. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-OUTPUT` and same legacy `S27`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F056 | S28 · EndStrategy — 같은 모델 응답에도 실제 실행한 Tool이 달라질 수 있다

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “EndStrategy — 같은 모델 응답에도 실제 실행한 Tool이 달라질 수 있다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `early: 유효 출력 우선 종료` / `graceful(기본): 함께 요청한 Function Tool 실행` / `exhaustive: 추가 Output Tool까지 실행`.

**Diagram/layout specification:** **대표 사례 [설명용/통제 시험 계획]**: 하나의 모델 응답에 `valid output tool A + function tool B + another output tool C`. 세 전략을 가로로 비교하는 세 개의 흐름 레인. 각 `실행 여부 / 버려진 결과 / 부작용 위험`을 표시. **Streaming은 결과 확정 규칙이 다를 수 있음을 별도 주석**.

**Space-only semantic builds:**

- `F056-B01`: 유효 출력 도착.
- `F056-B02`: `early`는 B/C를 건너뛸 수 있음.
- `F056-B03`: `graceful`은 B 실행, 나중 Output Tool 생략.
- `F056-B04`: `exhaustive`는 모든 Output Tool도 실행할 수 있음.
- `F056-B05`: Output 실패 시 다시 Tool·Retry 경로 검토.

**Speaker script / detailed explanation:** 공식 docs 기준으로 설명하되 `str` 등 Plain Text Output과 함수 도구 동시 호출, Provider Native/Prompted, streaming에서 예외 동작이 있어 모든 경우에 동일 규칙으로 일반화하면 안 된다. 데모는 **실제 모델 자연 응답 / MockModel로 통제한 단위 시험**을 반드시 분리한다.

**Mandatory correctness refinement:** 2026-11-03 공식 docs의 기본 EndStrategy는 'graceful'; early/graceful/exhaustive와 스트리밍 최초 유효 출력 동작을 구분.

**Likely Q&A:** Q. 최종 출력이 나왔는데 옆의 Function Tool이 실행될 수도 있나요? A. 네. 출력 방식·end_strategy·streaming 경로에 따라 실행 여부가 달라질 수 있습니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S28` reference: [OFFICIAL-P-OUTPUT]의 EndStrategy 표; [LOCAL-P2] §12; R04.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “출력과 실행이 끝난 뒤 무엇을 다음 요청까지 보존할까?”

### F057 | S28 deep dive · EndStrategy의 정확한 비교

**Section/master/template:** PydanticAI / `P-ARCH` / `T-COMP`. **Question/purpose:** 같은 응답에 출력·함수 Tool이 같이 있으면 실제 부작용이 달라질 수 있다.

**Exact audience headline:** “같은 응답에 출력·함수 Tool이 같이 있으면 실제 부작용이 달라질 수 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- early: 성공 Output이면 함께 요청된 Function Tools 생략
- graceful(기본): 함께 요청된 Function Tools 처리, 나중 Output Tool 후보 생략
- exhaustive: 다른 Output Tool 호출까지 처리

**Geometry and labeled visual (explicit construction):** 한 입력 모델 응답 [OutputA, FunctionB, OutputC]에서 3개 레인. 각 실행 여부를 체크·X로, 행위 위험 빨강.

**Space-only semantic builds:**

- `F057-B01`: OutputA 유효성 검증.
- `F057-B02`: early 실행 집합.
- `F057-B03`: graceful 실행 집합.
- `F057-B04`: exhaustive 실행 집합.
- `F057-B05`: Streaming의 예외를 별도 경고.

**Speaker script (readable Korean):** “하나의 출력만 채택하더라도 그 호출과 같은 배치에 있던 함수들이 실행될 수 있습니다. 실행 여부는 결과 내용뿐 아니라 end_strategy의 계약에 달려 있습니다.”

**Technical explanation / caution / counterexample:** 같은 Output 실패 시 다른 전략의 처리도 공식 문서 표대로; run_stream은 첫 출력 조기확정 규칙. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-OUTPUT` and same legacy `S28`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F058 | S28 deep dive · Streaming 조기 확정과 side effect

**Section/master/template:** PydanticAI / `P-ARCH` / `T-SEQ`. **Question/purpose:** run_stream의 출력 시점은 run과 같지 않을 수 있다.

**Exact audience headline:** “run_stream의 출력 시점은 run과 같지 않을 수 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- run: Graph 전체 실행 후 최종 RunResult
- run_stream: 처음 일치한 출력에서 먼저 확정할 수 있음
- 후속 Tool을 중간에 생략한 것으로 관측될 수 있음

**Geometry and labeled visual (explicit construction):** 위/아래 시간축: Graph complete vs Early output commit. 각각 ToolB/Deferred 이벤트 실행 여부 표기.

**Space-only semantic builds:**

- `F058-B01`: 비스트리밍 실행.
- `F058-B02`: Streaming 첫 유효 출력.
- `F058-B03`: 후속 Tool의 처리 차이.
- `F058-B04`: 안전한 사용 조건.

**Speaker script (readable Korean):** “스트리밍을 UI 구현 편의로만 바꾸면 예상한 외부 부작용 순서가 달라질 수 있으므로 Run API 선택 자체를 검토해야 합니다.”

**Technical explanation / caution / counterexample:** 정확한 버전의 stream 종료 조건을 고정 릴리스 테스트. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-OUTPUT; OFFICIAL-P-AGENT` and same legacy `S28`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F059 | S29 · Hook·Capability·History·Memory와 별도 Harness의 책임 구분

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Hook·Capability·History·Memory와 별도 Harness의 책임 구분”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Core는 실행·개입 지점을 제공하고, 상태 지속·Skill/Memory 정책은 구성에 따라 달라진다`.

**Diagram/layout specification:** 마스터 P에 3개 레이어 오버레이: `Core: Hooks / Toolset / Deferred / Context`, `Harness(별도): Memory, Skills, Compaction, Guardrails, Planning 등`, `App: persistence, authorization, data freshness, approval UI`. 아래 `History on next run` 화살표를 App storage에서 Run input으로.

**Space-only semantic builds:**

- `F059-B01`: Core Hooks와 Capabilities.
- `F059-B02`: History 전달 또는 저장.
- `F059-B03`: Harness 패키지의 선택 항목.
- `F059-B04`: App 정책/저장소.

**Speaker script / detailed explanation:** `message_history`를 직접 전달하는 방식과 어떤 Session API가 자동 지속하는지는 실제 버전·사용 방식별로 구분한다. Hook/Capability는 LLM Prompt 앞뒤에 어떤 정보를 추가하거나 Tool 실행을 감싸는 확장 지점이며, 모든 정책을 강제할 마법 같은 하나의 Gate가 아니다. `Memory/Skills가 전부 없다`와 `Core가 기본으로 다 갖고 있다` 모두 과장이다.

**Likely Q&A:** Q. RunResult가 존재하면 자동으로 영구 Memory가 만들어지나요? A. 반드시 그렇지 않습니다. 다음 Run History 전달과 저장소/선택 Harness 책임을 구분합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S29` reference: [LOCAL-P2] §§14–20; [OFFICIAL-P-HARNESS]. R03/R05.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “승인이 필요하거나 분석을 다른 Agent에 위임하면?”

### F060 | S29 deep dive · History·Memory·Harness는 같은 기능이 아니다

**Section/master/template:** PydanticAI / `P-ARCH` / `T-COMP`. **Question/purpose:** Core History 전달과 장기 메모리 저장소의 책임을 구분한다.

**Exact audience headline:** “Core History 전달과 장기 메모리 저장소의 책임을 구분한다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- History = 전달하는 모델 메시지
- Memory = 저장/검색 정책을 앱 또는 선택 Component가 제공
- Harness = 선택적 여러 기능 조합

**Geometry and labeled visual (explicit construction):** P-STATE 옆 session storage와 separate optional Harness 점선 연결; ‘Core가 알아서 DB에 영구 저장’ 잘못된 화살표 삭제.

**Space-only semantic builds:**

- `F060-B01`: Run1의 메시지.
- `F060-B02`: App이 History 보존.
- `F060-B03`: Run2 입력으로 전달.
- `F060-B04`: 추가 Memory 조회·선별.
- `F060-B05`: Harness의 선택적 역할.

**Speaker script (readable Korean):** “RunResult가 돌아온 것과 이를 파일이나 DB에 영구 기록했다는 사실은 다릅니다.”

**Technical explanation / caution / counterexample:** 선택 Harness 패키지의 실제 제공 기능은 개별 공식 API로 확인. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-AGENT; OFFICIAL-P-HARNESS` and same legacy `S29`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F061 | S30 · Deferred 승인과 Orchestration — 제어권이 어디로 돌아오는가

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Deferred 승인과 Orchestration — 제어권이 어디로 돌아오는가”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Approval: 요청 기록 → 사람이 최종 인자 승인 → 같은 작업 맥락 재개` / `위임: 부모 복귀 vs 라우팅 vs 명시적 Graph`.

**Diagram/layout specification:** 상단 `[DeferredToolRequests → App review → DeferredToolResults → resume]` 승인 상태도. 하단 세 가지 작은 흐름: `Parent → Tool(inner Agent) → Parent`, `Program Router → Specialist`, `Graph Node A → Node B`. 모두 `Context·상태 공유·사용자 최종 응답 주체` 라벨.

**Space-only semantic builds:**

- `F061-B01`: 승인 필요 Tool.
- `F061-B02`: Request ID/args snapshot.
- `F061-B03`: 승인/거절.
- `F061-B04`: Resume; 이후 위임 모드 3개 비교.

**Speaker script / detailed explanation:** 승인 요청 대기는 Python 작업이 멈춰 있거나 서버 자원이 무제한 점유된다는 뜻이 아니다. 앱이 요청과 상태를 저장하고 재개할 계약이 필요하다. `Tool로 Agent를 감싸기`와 OpenAI native Handoff는 이름이 비슷해도 제어권이 다를 수 있다. `출력 타입 검증`과 `실제 승인`도 별개다.

**Likely Q&A:** Q. 승인만 받으면 재개 시 다른 인자로 Tool을 실행해도 되나요? A. 안 됩니다. 승인자를 실제 최종 인자·사용자·자료 버전과 묶고 재개 시 재검증해야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S30` reference: [LOCAL-P2] §§16,20,21; [OFFICIAL-P-AGENT], [OFFICIAL-P-HARNESS]. R04.. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “이 모든 것을 실제 개발자가 만든 PydanticAI Run에서 살펴보자.”

### F062 | S30 deep dive · Deferred Tool을 승인 흐름으로

**Section/master/template:** PydanticAI / `P-ARCH` / `T-SEQ`. **Question/purpose:** 승인 필요는 바로 Tool을 실행한다는 의미가 아니다.

**Exact audience headline:** “승인 필요는 바로 Tool을 실행한다는 의미가 아니다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 요청 인자·principal·revision 고정
- Pending approval → approve / reject
- Resume 뒤 다시 검증하고 mock 실행

**Geometry and labeled visual (explicit construction):** P-Graph에서 Pending 상태를 별도 노드로, App approval store와 읽기 전용 데모 Tool 분리.

**Space-only semantic builds:**

- `F062-B01`: 호출 요청.
- `F062-B02`: Pending/상태 직렬화.
- `F062-B03`: 승인자 판단.
- `F062-B04`: Resume와 최종 인자 검증.
- `F062-B05`: Mock side effect 1회.

**Speaker script (readable Korean):** “승인은 승인 당시의 구체적 실행 인자에 대한 것이어야 하고, 재개될 때 바뀐 다른 인자에 그대로 적용되면 안 됩니다.”

**Technical explanation / caution / counterexample:** Deferred API 세부 타입과 승인 흐름은 해당 릴리스 코드·통제시험으로 확정. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-P-AGENT; LOCAL-P2 §14` and same legacy `S30`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F063 | S31 · Demo 2 진입·복귀: Core가 처리한 부분과 개발자가 구현한 부분

**Section/master:** PydanticAI / `P-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-DEMO`.

**Exact audience headline:** “Demo 2 진입·복귀: Core가 처리한 부분과 개발자가 구현한 부분”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Python 개발 코드 → PydanticAI Graph/ToolManager → 모델·도구 → Validated Output` / `같은 BIN 시나리오, 다른 실행 계약`.

**Diagram/layout specification:** 좌측 개발자가 작성한 설정·Tool/Deps 코드 화면(4–8줄 축약), 우측 P 아키텍처 주요 노드, 아래 별도 Demo 2 브라우저 링크 아이콘. 시연 후 같은 화면으로 돌아와 **모델 입력·Tool 검증·출력 채택·History**가 어느 층에서 생겼는지 체크.

**Space-only semantic builds:**

- `F063-B01`: 코드.
- `F063-B02`: 입력 계약.
- `F063-B03`: Run Event.
- `F063-B04`: 세 전략/승인 테스트.
- `F063-B05`: 저장·복구 책임. 실제 로그가 없으면 카운터·성능 수치를 넣지 않는다.

**Speaker script / detailed explanation:** 먼저 Core 최소 실행, 그다음 필요한 범위에서 Harness를 붙인다. EndStrategy·Retry·승인 등 모든 기능을 한 자연 모델 응답에 억지로 발생시키지 않는다. 이번 핵심은 “개발자가 무엇을 구현했는가”를 명확히 보여주는 것.

**Likely Q&A:** Q. Core가 제공한 동작과 우리 코드가 수행한 동작은 어떻게 구분하나요? A. Graph·ToolManager·Output은 SDK Core로, 도메인 Tool·인가·저장·Trace Viewer는 앱 소유로 표시합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-P-AGENT, OFFICIAL-P-OUTPUT`; legacy `S31` reference: 인계 §7.3; [LOCAL-P2].. **Trace:** Demo 2, actual event IDs only after record and hash verification.

**Bridge:** “다른 SDK들은 같은 책임을 어떻게 나누었는가?”

### F064 | S32 · OpenAI Agents SDK 전체 구조 — 명시적 Runner가 다음 실행을 결정

**Section/master:** OpenAI Agents SDK / `O-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ARCH`.

**Exact audience headline:** “OpenAI Agents SDK 전체 구조 — 명시적 Runner가 다음 실행을 결정”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Agent 정의 → Runner → Model 응답 처리 → NextStep`.

**Diagram/layout specification:** `App: Agent(instructions, tools, handoffs, model)` → `Runner + Turn resolution` ↔ `Model`; 오른쪽 `function tools / agent as tool / handoff target`; 아래 `Sessions / RunState / Tracing / Guardrails`. `NextStep: Final | RunAgain | Handoff | Interruption`을 Runner의 실행 결과 분기로 표시.

**Space-only semantic builds:**

- `F064-B01`: Agent 설정.
- `F064-B02`: Runner 반복.
- `F064-B03`: 모델 응답 분류.
- `F064-B04`: 각 다음 단계 이동.
- `F064-B05`: 앱에 결과 반환.

**Speaker script / detailed explanation:** PydanticAI처럼 내부 Graph Node를 명시하는 방식과 달리 Runner의 Turn 분기와 다음 단계 객체가 주요 분석 포인트다. `turn_resolution.py`, `run.py` 같은 실제 파일 경로는 노트에만. Tool의 특정 사용 결과로 즉시 종료하는 설정 같은 SDK별 정책을 예시로 설명한다.

**Mandatory correctness refinement:** OpenAI Agents SDK는 사용자의 App에서 실행되는 SDK; 관리형 Agents API와 혼동 금지.

**Likely Q&A:** Q. OpenAI Agents SDK 실행은 OpenAI 서버에 호스팅되나요? A. 코드 우선 SDK는 응용 프로그램에서 Runner를 실행합니다. 관리형 Agents API와 구분합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-O-RUN, OFFICIAL-O-ORCH`; legacy `S32` reference: [LOCAL-O2] §§6–9,15,22–25; [OFFICIAL-O-RUN].. **Trace:** No fake actual trace.

**Bridge:** “전문 Agent에게 일을 맡길 때 결과를 되돌려받느냐, 답변 책임을 넘기느냐?”

### F065 | S32 deep dive · OpenAI Runner의 NextStep

**Section/master/template:** OpenAI Agents SDK / `O-ARCH` / `T-SEQ`. **Question/purpose:** Runner는 다음 Model/Tool/Handoff/Final 실행 분기를 결정한다.

**Exact audience headline:** “Runner는 다음 Model/Tool/Handoff/Final 실행 분기를 결정한다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Agent 정의: model/instructions/tools/handoffs
- Runner 반복: model → inspect → Tool/Handoff/Final
- Session/RunState는 별도 수명

**Geometry and labeled visual (explicit construction):** O-ARCH 안에서 Runner 박스 크게, NextStep 분기 3개만 보여주고 다른 구현은 노트.

**Space-only semantic builds:**

- `F065-B01`: Runner 시작.
- `F065-B02`: 모델 응답.
- `F065-B03`: Tool 호출이면 실행.
- `F065-B04`: Handoff면 활성 Agent 변경.
- `F065-B05`: Final이면 반환.

**Speaker script (readable Korean):** “SDK를 사용하면 애플리케이션이 반복 while을 직접 작성하지 않아도 Runner가 핵심 분기를 수행합니다.”

**Technical explanation / caution / counterexample:** Runner 전체 동작을 OpenAI 호스팅 Agents API 실행과 혼동하지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-O-RUN` and same legacy `S32`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F066 | S33 · Agent-as-Tool vs Handoff — 제어권이 돌아오는 위치가 다르다

**Section/master:** OpenAI Agents SDK / `O-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Agent-as-Tool vs Handoff — 제어권이 돌아오는 위치가 다르다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `As-tool: Manager가 마지막 답변 책임` / `Handoff: 활성 Agent가 Specialist로 전환`.

**Diagram/layout specification:** 좌측 `User → Manager → Specialist-as-tool → Manager → User`; 우측 `User → Agent A --handoff--> Agent B → User`. **왼쪽의 specialist는 Tool 결과 반환, 오른쪽은 실행 주체 변경** 표시. `shared conversation / filtered history`는 조건부.

**Space-only semantic builds:**

- `F066-B01`: 전문성 위임 공통점.
- `F066-B02`: 결과 반환 경로.
- `F066-B03`: Guardrail·최종 출력 소유자 차이.
- `F066-B04`: 도메인 예시 ‘데이터만 조회 vs 이후 질문 담당’.

**Speaker script / detailed explanation:** 실제 사용법은 `Agent.as_tool()`과 `handoffs=[...]` 형태지만, 동일 구현이라고 오해하지 않는다. 이력 전달·필터링 및 권한 승인 상태도 선택에 따라 달라질 수 있다. PydanticAI의 내포 Agent 호출을 OpenAI Handoff와 무조건 동일하게 표기하지 않는다.

**Likely Q&A:** Q. Agent-as-Tool과 Handoff 모두 자식이 수행하면 같지 않나요? A. 아닙니다. 부모로 결과가 돌아오는지 활성 답변 주체가 전환되는지가 핵심입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-O-RUN, OFFICIAL-O-ORCH`; legacy `S33` reference: [LOCAL-O2] §§22–25; [OFFICIAL-O-RUN], [OFFICIAL-O-GUARD].. **Trace:** No fake actual trace.

**Bridge:** “그렇다면 Guardrail은 위임 체인 전체를 포괄할까?”

### F067 | S33 deep dive · Agent-as-Tool의 제어권

**Section/master/template:** OpenAI Agents SDK / `O-ARCH` / `T-SEQ`. **Question/purpose:** 전문 Agent가 호출되더라도 최종 답변 주체는 Parent.

**Exact audience headline:** “전문 Agent가 호출되더라도 최종 답변 주체는 Parent”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Manager → Specialist as Tool
- Specialist 내부 Run → 결과 반환
- Manager가 최종 답변/추가 Tool 결정

**Geometry and labeled visual (explicit construction):** O-ARCH의 Parent Loop 내부에 작게 Specialist Loop를 팝인 구조로. Parent는 중간에 응답 소유권을 잃지 않음.

**Space-only semantic builds:**

- `F067-B01`: Parent가 Tool 호출 선택.
- `F067-B02`: Specialist Run.
- `F067-B03`: 결과가 ToolResult로 환류.
- `F067-B04`: Parent가 다음 결정을 수행.

**Speaker script (readable Korean):** “상담 Agent가 분석 Agent를 부르고 다시 결과를 검토하는 경우처럼 부모에게 권한이 남습니다.”

**Technical explanation / caution / counterexample:** Context 전달은 API 설정에 의존; 전체 Parent History 자동 복제라 주장 금지. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-O-ORCH` and same legacy `S33`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F068 | S33 deep dive · Handoff의 제어권

**Section/master/template:** OpenAI Agents SDK / `O-ARCH` / `T-COMP`. **Question/purpose:** Handoff는 다른 Agent가 활성 주체가 되는 전환이다.

**Exact audience headline:** “Handoff는 다른 Agent가 활성 주체가 되는 전환이다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Agent A → Handoff event
- Agent B가 다음 응답 소유
- Agent-as-Tool과 결과 복귀 위치 차이

**Geometry and labeled visual (explicit construction):** 같은 Parent/Child 두 노드로 Handoff 실선 이동과 As Tool 왕복 점선 비교, 다른 색으로 최종 답변 표시.

**Space-only semantic builds:**

- `F068-B01`: Agent A 판단.
- `F068-B02`: Handoff 처리.
- `F068-B03`: Agent B 활성화.
- `F068-B04`: B의 결과와 history 의미.
- `F068-B05`: As-Tool과 최종 비교.

**Speaker script (readable Korean):** “Handoff를 Subagent가 잠깐 계산만 해 주는 패턴으로 해석하면 프레임워크 선택이 틀어집니다.”

**Technical explanation / caution / counterexample:** SDK Handoff의 역사/필터 구현은 실제 문서 확인 후 제한 조건 표기. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-O-ORCH` and same legacy `S33`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F069 | S34 · OpenAI Guardrail·RunState와 실제 재개 경계

**Section/master:** OpenAI Agents SDK / `O-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “OpenAI Guardrail·RunState와 실제 재개 경계”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Input Guardrail / Tool Guardrail / Output Guardrail은 적용 위치가 다르다` / `RunState ≠ Session History`.

**Diagram/layout specification:** 상단 Run 타임라인, 입력 Guardrail에 `parallel or blocking` 라벨; Tool 실행 바로 전 Tool Guardrail; 최종 응답 전에 Output Guardrail. 아래 `approval interruption → state snapshot → approve/reject → resume same run`, 옆 `Session = 대화 지속`.

**Space-only semantic builds:**

- `F069-B01`: 빠른 병렬 검사 시 Tool 부작용이 선행될 위험.
- `F069-B02`: 차단형 검사 선택.
- `F069-B03`: 승인 중단.
- `F069-B04`: RunState 복원.
- `F069-B05`: 외부 Tool 중복 실행 책임.

**Speaker script / detailed explanation:** 공식 문서에서 Input Guardrail은 첫 Agent, Output Guardrail은 최종 응답 Agent, Tool Guardrail은 연결된 Function Tool에 적용된다고 설명한다. 따라서 체인 전체·모든 도구가 동일한 전역 필터를 통과한다고 말하면 잘못이다. 저장된 RunState로 재개해도 DB 변경의 Exactly-once는 앱 별도 보장이다.

**Mandatory correctness refinement:** Input/Output/Tool guardrail은 적용 범위가 다르고 병렬 input guardrail은 side-effect 가능성 확인.

**Likely Q&A:** Q. Input Guardrail 하나로 전체 Agent 체인의 Tool을 막을 수 있나요? A. 적용 범위와 실행 타이밍이 다르고 특정 Tool에는 별도 가드와 실제 권한 검사가 필요합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-O-RUN, OFFICIAL-O-ORCH`; legacy `S34` reference: [OFFICIAL-O-GUARD]; [LOCAL-O2] §§17–24,26–28.. **Trace:** No fake actual trace.

**Bridge:** “이제 Agent 루프가 Python 밖에 있는 SDK를 보자.”

### F070 | S34 deep dive · Guardrail은 적용 범위를 가진다

**Section/master/template:** OpenAI Agents SDK / `O-ARCH` / `T-SEQ`. **Question/purpose:** Input/Output/Tool Guardrail은 모든 스텝에 무차별 적용되지 않는다.

**Exact audience headline:** “Input/Output/Tool Guardrail은 모든 스텝에 무차별 적용되지 않는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Input: 첫 Agent의 입력 경계
- Tool: 적용된 Function Tool 실행 경계
- Output: 최종 사용자 응답 경계

**Geometry and labeled visual (explicit construction):** O-ARCH 별도의 Gate 3개 위치 표시, 중간 Agent/Tool이 전부 동일하게 가려지는 보안막 금지.

**Space-only semantic builds:**

- `F070-B01`: Input guardrail.
- `F070-B02`: blocking/parallel 실행 시점.
- `F070-B03`: Tool guardrail.
- `F070-B04`: Output guardrail.
- `F070-B05`: 외부 App 정책.

**Speaker script (readable Korean):** “어느 정책이 어느 대상에 언제 적용되는지를 표기하지 않은 ‘가드레일 지원’ 비교는 실무에 충분하지 않습니다.”

**Technical explanation / caution / counterexample:** 트리거와 asyncio 병렬 동작은 고정 버전 검증; parallel input guardrail은 동시 Tool side effect 가능성 경고. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-O-GUARD` and same legacy `S34`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F071 | S35 · Claude Agent SDK 전체 구조 — SDK는 CLI Harness를 제어

**Section/master:** Claude Agent SDK / `S-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ARCH`.

**Exact audience headline:** “Claude Agent SDK 전체 구조 — SDK는 CLI Harness를 제어”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Python SDK ≠ 독립 Agent Loop 엔진` / `query/client → Transport → Claude Code CLI → Model/Tools`.

**Diagram/layout specification:** 좌측 `Host Python App: query() / ClaudeSDKClient / options`(S-APP) → `InternalClient / transport / control protocol`(S-TRANSPORT) → **프로세스 경계** → `Claude Code CLI Runtime`(S-RUNTIME) ↔ Claude model & built-in tools. 별도 `SDK MCP Server (Python-side)` 경로는 Runtime에서 Host App으로 왕복 화살표. 공개 Python/비공개 CLI 내부를 실선 경계와 음영으로 표시.

**Space-only semantic builds:**

- `F071-B01`: Python 설정.
- `F071-B02`: CLI 프로세스 구동.
- `F071-B03`: 메시지 스트림.
- `F071-B04`: Tool/권한 callback.
- `F071-B05`: Host에 결과.

**Speaker script / detailed explanation:** OpenAI Agents SDK와 비교할 때 핵심은 실행 엔진의 소유자가 다르다는 점. Python에서 Agent API를 사용해도 내부 Tool 루프를 모두 Python 코드로 수정할 수 있는 것은 아니다. `query()`와 `ClaudeSDKClient`의 연결 수명과 주고받는 메시지 형태를 구분한다.

**Likely Q&A:** Q. Claude SDK가 Python으로 CLI의 내부 Loop를 재구현하나요? A. 아닙니다. SDK가 Transport를 통해 Claude Code CLI 런타임을 제어합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-S`; legacy `S35` reference: [LOCAL-S2], [OFFICIAL-S].. **Trace:** No fake actual trace.

**Bridge:** “이 프로세스 경계 때문에 Permission과 상태는 어디에 남을까?”

### F072 | S35 deep dive · Claude SDK와 CLI의 프로세스 경계

**Section/master/template:** Claude Agent SDK / `S-ARCH` / `T-ARCH`. **Question/purpose:** Python SDK 호출은 별도 Claude Code CLI 런타임을 통해 수행된다.

**Exact audience headline:** “Python SDK 호출은 별도 Claude Code CLI 런타임을 통해 수행된다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Host Python query()/ClaudeSDKClient
- Transport/Control Protocol
- Claude Code CLI Runtime → Model/Tools

**Geometry and labeled visual (explicit construction):** S-ARCH의 Host/CLI 프로세스 경계 두꺼운 점선; SDK 공개 Python과 CLI 내부 비공개 구분.

**Space-only semantic builds:**

- `F072-B01`: Host Client 생성.
- `F072-B02`: CLI 프로세스/Transport.
- `F072-B03`: Model/Tool 실행.
- `F072-B04`: 메시지 스트림 회귀.
- `F072-B05`: Host App 결과 처리.

**Speaker script (readable Korean):** “SDK에서 Python 코드를 쓴다고 해서 Python으로 별도 Agent Runner 구현을 수정할 수 있는 구조는 아닙니다.”

**Technical explanation / caution / counterexample:** 구체 프로세스/바이너리 정책은 설치 버전의 SDK와 운영 방식에 따라 확인. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-S` and same legacy `S35`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F073 | S36 · Claude SDK: MCP 왕복, Permission·Session·Checkpoint의 경계

**Section/master:** Claude Agent SDK / `S-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Claude SDK: MCP 왕복, Permission·Session·Checkpoint의 경계”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `SDK-hosted MCP Tool = CLI가 Python 함수를 호출하는 역방향 통로` / `Session 저장 ≠ Workspace 복원`.

**Diagram/layout specification:** 상단 시퀀스 `CLI → transport control → Python SDK MCP handler → result → CLI`. 아래 4개 저장 객체 `CLI transcript / external session mirror / workspace files / tool side effects`를 분리. Permission 검사에 Hook/Rules/Mode/Callback을 **서로 다른 조건부 게이트**로 표시.

**Space-only semantic builds:**

- `F073-B01`: Tool이 Python으로 왕복.
- `F073-B02`: 승인 경로의 Callback이 항상 유일한 Gate가 아님.
- `F073-B03`: 세션 복원.
- `F073-B04`: 파일/환경 복원 별도.

**Speaker script / detailed explanation:** `allowed_tools`는 단독 인가 시스템이라고 주장하지 않는다. SDK SessionStore를 쓴다고 CI 파일·임시 분석 결과·도구 실행 상태가 자동으로 이동하지 않는다. 플랫폼별 실행 방식과 버전의 한계를 공식 문서로 확인 후 노트에 쓴다.

**Mandatory correctness refinement:** Session resume는 workspace/files/외부 side effects 자동 roll-back을 뜻하지 않음.

**Likely Q&A:** Q. 세션만 복원하면 CLI가 만든 파일과 Tool side effect도 복구되나요? A. 아닙니다. 대화 기록과 Workspace 파일·외부 변경의 상태는 다릅니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-S`; legacy `S36` reference: [LOCAL-S2] §§권한·세션·MCP; [OFFICIAL-S]. R07.. **Trace:** No fake actual trace.

**Bridge:** “다음은 실행 결과를 Event로 다루는 ADK.”

### F074 | S36 deep dive · SDK MCP의 역방향 호출

**Section/master/template:** Claude Agent SDK / `S-ARCH` / `T-SEQ`. **Question/purpose:** CLI가 Host Python의 함수를 Tool처럼 부를 수 있다.

**Exact audience headline:** “CLI가 Host Python의 함수를 Tool처럼 부를 수 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Python app: MCP Tool handler 등록
- Claude Code CLI → control transport → Python MCP handler
- 결과가 CLI Loop로 반환

**Geometry and labeled visual (explicit construction):** 두 프로세스 레인 시퀀스; 일반 원격 MCP 서버와 SDK-hosted MCP의 연결 위치 구분.

**Space-only semantic builds:**

- `F074-B01`: 도구 정의 등록.
- `F074-B02`: CLI에 노출된 schema.
- `F074-B03`: CLI가 Tool Call.
- `F074-B04`: Python callback 실행.
- `F074-B05`: result 반환.

**Speaker script (readable Korean):** “이 방식은 Python 앱이 CLI의 모든 내부 과정을 제어한다는 뜻이 아니라 특정 Tool의 Handler를 Python 쪽에 제공한다는 뜻입니다.”

**Technical explanation / caution / counterexample:** Permission callback 하나가 모든 경로를 막는다고 주장하지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-S` and same legacy `S36`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F075 | S37 · Google ADK 전체 아키텍처 — Event가 실행과 저장을 잇는다

**Section/master:** Google ADK / `G-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ARCH`.

**Exact audience headline:** “Google ADK 전체 아키텍처 — Event가 실행과 저장을 잇는다”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Runner는 Agent 실행에서 나온 Event를 Session/State로 연결한다`.

**Diagram/layout specification:** `Caller → Runner`(G-RUNNER) → `LlmAgent → BaseLlmFlow`(G-AGENT) ↔ `Model`(G-MODEL), 우측 `Tools / callbacks`(G-TOOL), 하단 `SessionService / State / MemoryService / ArtifactService`(G-STATE), 외곽 `Graph Workflow / Scheduler`(G-WORKFLOW). Tool 결과와 Event 저장을 다른 화살표로 분리.

**Space-only semantic builds:**

- `F075-B01`: Runner 시작.
- `F075-B02`: Flow 모델 호출 루프.
- `F075-B03`: Event 생성.
- `F075-B04`: State Delta 적용.
- `F075-B05`: 최종 Event/Workflow completion 구분.

**Speaker script / detailed explanation:** 기존 일반 Agent Loop를 다시 가르치지 않고 이 Event/Session 결합이 어떻게 책임을 분리하는지 설명한다. Runtime Event가 final이라는 사실을 전체 분석 파이프라인 완료로 해석하지 않는다. `temp:` 값이 어떤 범위까지 저장되는지는 Python 버전 고정 검증을 수반한다.

**Likely Q&A:** Q. Google ADK의 Event는 모델 응답과 같은 데이터인가요? A. Event는 실행·상태 변화를 잇는 단위로, 모델 응답 외의 정보와 수명 범위를 포함할 수 있습니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-G`; legacy `S37` reference: [LOCAL-G2] §§4–8,15–17; [OFFICIAL-G].. **Trace:** No fake actual trace.

**Bridge:** “이 Event들을 여러 Agent/Workflow에 배분할 때?”

### F076 | S37 deep dive · Google ADK Event 수명

**Section/master/template:** Google ADK / `G-ARCH` / `T-SEQ`. **Question/purpose:** Runner/Event/SessionService는 다른 책임을 맡는다.

**Exact audience headline:** “Runner/Event/SessionService는 다른 책임을 맡는다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Runner: Run 진입·Session 맥락 연결
- Agent/Flow: 모델과 Tool의 실행
- Event/SessionService: 결과와 State 변화 기록

**Geometry and labeled visual (explicit construction):** G-ARCH를 Request→Flow→Event→State delta 반시계 흐름으로. Event마다 producer/consumer 라벨.

**Space-only semantic builds:**

- `F076-B01`: Runner 호출.
- `F076-B02`: LlmAgent/Flow.
- `F076-B03`: Event 생성.
- `F076-B04`: State Delta 적용.
- `F076-B05`: 다음 Agent/Workflow.

**Speaker script (readable Korean):** “Agent의 최종 Event 하나가 기록되어도, 외부 Workflow 전체가 끝났다고 단정할 수 없습니다.”

**Technical explanation / caution / counterexample:** Event final 범위와 session commit 타이밍은 Python 버전 문서로 대조. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-G` and same legacy `S37`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F077 | S38 · ADK: Tool 병렬 ≠ 병렬 Agent ≠ Graph Workflow

**Section/master:** Google ADK / `G-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “ADK: Tool 병렬 ≠ 병렬 Agent ≠ Graph Workflow”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `세 동시성은 작업 단위가 다르다: 도구 / 독립 Agent / 그래프 노드`.

**Diagram/layout specification:** ① `ToolCalls → batch executor` ② `ParallelAgent(기존 Template) → concurrent child event streams` ③ `Graph Workflow → Node/Edge/Scheduler`. 각 그림 아래 `입력·결과 순서`, `상태`, `실패/취소 경계` 3개 아이콘.

**Space-only semantic builds:**

- `F077-B01`: 모델이 여러 도구 요청.
- `F077-B02`: 실행기 병렬 처리.
- `F077-B03`: 독립 Agent Event 합치기.
- `F077-B04`: Graph 스케줄러에서 Fan-out/Fan-in.

**Speaker script / detailed explanation:** 이전 Template Agent의 유지/Deprecated 여부를 고정 릴리스별로 확인하고, Graph Workflow로의 이동을 무조건 자동 마이그레이션이라 설명하지 않는다. Graph Join은 어떤 결과가 어느 Node의 어느 데이터 버전인지 연결 키가 필요하다.

**Mandatory correctness refinement:** ADK Graph Workflow 신·구 API, ParallelAgent의 상태는 실제 기준 릴리스 확인 없이 단정 금지.

**Likely Q&A:** Q. ParallelAgent는 Tool 병렬 처리와 똑같나요? A. 아닙니다. 병렬 Agent는 별도 Agent 실행/이벤트를 관리하고 Tool 병렬은 하나의 Agent 안 Handler 호출입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-G`; legacy `S38` reference: [LOCAL-G2] §§13–14,22–26; [OFFICIAL-G]. R06.. **Trace:** No fake actual trace.

**Bridge:** “Checkpoint는 정확히 무엇을 복원할까?”

### F078 | S38 deep dive · 세 종류의 동시성

**Section/master/template:** Google ADK / `G-ARCH` / `T-COMP`. **Question/purpose:** Parallel Tool, Parallel Agent, Graph Workflow는 다른 경계를 가진다.

**Exact audience headline:** “Parallel Tool, Parallel Agent, Graph Workflow는 다른 경계를 가진다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Tool 병렬: 한 Agent Loop의 여러 handler
- Parallel Agent: 각 Child의 Event stream
- Workflow: Node/Edge/Join의 명시 실행

**Geometry and labeled visual (explicit construction):** 서로 다른 3개 독립 패널을 한 화면이 아니라 순차 3 단계 또는 확대 3장으로. Tool/Agent/Graph 각각 번호.

**Space-only semantic builds:**

- `F078-B01`: Tool 병렬.
- `F078-B02`: Agent 병렬.
- `F078-B03`: Workflow fan-out.
- `F078-B04`: Join과 State merge.
- `F078-B05`: 실제 도구 부작용.

**Speaker script (readable Korean):** “동시에 작동한다는 사실만으로 실행 의미가 같지 않습니다. 중간 상태를 어떻게 합치고 실패하면 어디서 다시 실행하는지가 다릅니다.”

**Technical explanation / caution / counterexample:** Graph Workflow 가용성과 legacy ParallelAgent 상태는 고정 릴리스별 확인. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-G` and same legacy `S38`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F079 | S39 · ADK의 Event·Checkpoint·HITL — 'final'의 적용 범위

**Section/master:** Google ADK / `G-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “ADK의 Event·Checkpoint·HITL — 'final'의 적용 범위”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Agent final Event ≠ 전체 Workflow 완료` / `Resume는 재실행·부작용 문제를 남긴다`.

**Diagram/layout specification:** 이벤트 타임라인 `Node A Final → Node B waiting → Human approval → Node C → workflow completed`, 아래 `Session/Artifact/Checkpoint` 분리. 취소/복원 지점은 중단된 노드를 어떻게 다시 스케줄하는지 물음표로 표현.

**Space-only semantic builds:**

- `F079-B01`: 한 Agent 결과를 Event로 append.
- `F079-B02`: 나머지 Workflow 진행.
- `F079-B03`: 승인.
- `F079-B04`: Event Replay/Checkpoint.
- `F079-B05`: 중복 부작용 점검.

**Speaker script / detailed explanation:** 정적 분석에 복구 TODO/제약이 있다면 “Graph를 쓰면 완전한 내구 실행”이라 말하지 않는다. 정확한 재개 보장은 설치 버전으로 확인. 공정 자료는 보고서 Artifact ID/스냅샷 버전으로 연결해야 추적 가능하다.

**Likely Q&A:** Q. 하나의 Agent가 final을 내면 Workflow도 끝나나요? A. 아닙니다. 상위 Scheduler에서 후속 Agent/Node 및 Pending 승인이 남아 있을 수 있습니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-G`; legacy `S39` reference: [LOCAL-G2] §§15–17,24–27; R06.. **Trace:** No fake actual trace.

**Bridge:** “Microsoft는 이 정책과 Workflow를 다른 계층으로 배치한다.”

### F080 | S39 deep dive · Event Final vs 전체 완료

**Section/master/template:** Google ADK / `G-ARCH` / `T-SEQ`. **Question/purpose:** 작은 Agent의 final은 상위 파이프라인의 final이 아니다.

**Exact audience headline:** “작은 Agent의 final은 상위 파이프라인의 final이 아니다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Child A final Event
- Workflow B/C 진행 중
- 전체 종료는 상위 Scheduler 기준

**Geometry and labeled visual (explicit construction):** 이벤트 타임라인: A 종료 후에도 B pending, C running. 최상위 별도 Completed marker.

**Space-only semantic builds:**

- `F080-B01`: A의 final.
- `F080-B02`: B의 pending.
- `F080-B03`: 승인/재개.
- `F080-B04`: C의 실행.
- `F080-B05`: 전체 workflow 완료.

**Speaker script (readable Korean):** “상위 워크플로가 있고 그 안에서 특정 Agent가 final을 냈다면, 그 Agent 실행의 종료 여부만을 뜻할 수 있습니다.”

**Technical explanation / caution / counterexample:** Resume/Checkpoint 기능 범위는 설치 버전에서 검증, 외부 DB exactly-once는 별도. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-G` and same legacy `S39`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F081 | S40 · Microsoft Agent Framework 전체 아키텍처 — 실행 Pipeline과 Workflow의 분리

**Section/master:** Microsoft Agent Framework / `M-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ARCH`.

**Exact audience headline:** “Microsoft Agent Framework 전체 아키텍처 — 실행 Pipeline과 Workflow의 분리”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Agent/ChatClient/Function Tool Pipeline` + `별도 Harness` + `Graph/Functional Workflow`.

**Diagram/layout specification:** 가운데 `App → Agent → ContextProvider/History → ChatClient + Function Invocation → Model/Tools`(M-PIPE). 세 개의 Middleware 영역 `agent / chat / function`을 수직 띠. 오른쪽 별도 `Agent Harness(계획·Memory·Skills)`(M-HARNESS); 아래 `Workflow Executors ↔ Edges ↔ Supersteps ↔ Checkpoints`(M-WORKFLOW). **Tool Loop, Harness 재실행 Loop, Workflow 실행을 구별하는 선**.

**Space-only semantic builds:**

- `F081-B01`: 기본 Agent.
- `F081-B02`: Tool 호출 처리.
- `F081-B03`: Middleware 삽입.
- `F081-B04`: Harness의 상위 반복.
- `F081-B05`: Workflow.

**Speaker script / detailed explanation:** 모든 Agent 실행이 Workflow Superstep에 자동 포장된다는 뜻이 아니다. Python/Core 버전에 따라 API 구성이 달라질 수 있으므로 정확한 클래스명은 소스 검증 후. FIDES 등 실험 경로는 본문에 만능 방어로 소개하지 않는다.

**Mandatory correctness refinement:** Microsoft Pipeline / Harness / Workflow를 단일 엔진으로 합쳐 그리지 말 것.

**Likely Q&A:** Q. Microsoft Workflow는 단일 Agent의 모든 Tool 호출을 자동 Superstep에 넣나요? A. 기본 Agent Pipeline, 선택 Harness, 별도 Workflow Graph는 각각 다른 실행 범위입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-M-WORKFLOW`; legacy `S40` reference: [LOCAL-M2] §§Agent Pipeline·Middleware·Harness·Workflow; [OFFICIAL-M-OVERVIEW].. **Trace:** No fake actual trace.

**Bridge:** “정책은 어떤 함수 계층에서 실제 도구 실행을 막는가?”

### F082 | S40 deep dive · Microsoft의 세 가지 반복 경계

**Section/master/template:** Microsoft Agent Framework / `M-ARCH` / `T-ARCH`. **Question/purpose:** 기본 Tool invocation, 상위 Harness, Workflow는 각각 별도이다.

**Exact audience headline:** “기본 Tool invocation, 상위 Harness, Workflow는 각각 별도이다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Agent/Chat/Function Invocation Pipeline
- 선택 Harness의 상위 작업 루프
- Workflow Executor·Edge·Superstep

**Geometry and labeled visual (explicit construction):** M-ARCH 가로 3 구역을 서로 다른 실선 박스로, 사용자 API 입력→기본 실행/상위 실행/워크플로 연결을 별도 라벨.

**Space-only semantic builds:**

- `F082-B01`: 기본 Agent Pipeline.
- `F082-B02`: Function invocation.
- `F082-B03`: Middleware.
- `F082-B04`: 선택 Harness.
- `F082-B05`: Workflow.

**Speaker script (readable Korean):** “Microsoft Agent Framework의 Workflow를 쓴다는 것과 모든 단일 Agent의 Tool 호출이 그 Workflow의 Superstep으로 돌아간다는 뜻은 다릅니다.”

**Technical explanation / caution / counterexample:** 릴리스별 Harness 제공 범위와 Middleware API 이름 확인. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-M-OVERVIEW; OFFICIAL-M-WORKFLOW` and same legacy `S40`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F083 | S41 · Microsoft Middleware: 정상 Tool Error와 강제 정책 중단

**Section/master:** Microsoft Agent Framework / `M-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Microsoft Middleware: 정상 Tool Error와 강제 정책 중단”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `일반 Tool 실패 → Tool Result로 모델이 처리 가능` / `보안 Middleware 실패 → Run 중단 의도`.

**Diagram/layout specification:** 최상위 Agent → Chat → Function의 3겹 Policy Layer. `arguments transformed` 후에도 `final arguments + identity + data revision` 다시 검증. 두 개의 실패 경로: `ToolError result`와 `MiddlewareFailure`를 빨강/주황으로 분기.

**Space-only semantic builds:**

- `F083-B01`: Tool Call 생성.
- `F083-B02`: 인자 변형/검증.
- `F083-B03`: 중간 Middleware 실행.
- `F083-B04`: Tool Error vs Policy Failure.
- `F083-B05`: Resume/종료 정책.

**Speaker script / detailed explanation:** 검증 전에 승인받은 인자와 실제 실행된 인자가 다르면 감사가 어려워진다. 모든 에러를 동일하게 모델에게 “다시 시도해”라고 돌려보내면 금지 행동도 재시도될 수 있어 정책 위반은 별도 중단 경계가 적절하다.

**Likely Q&A:** Q. 금지된 Tool 요청도 일반 오류처럼 모델에게 다시 시도시키면 되나요? A. 보안 정책 위반은 모델 피드백 외 실제 실행 차단·중단이 필요할 수 있습니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-M-WORKFLOW`; legacy `S41` reference: [LOCAL-M2] §§Middleware·Guardrail·Tool Approval; [OFFICIAL-M-WORKFLOW].. **Trace:** No fake actual trace.

**Bridge:** “Workflow 쪽에서는 여러 Executor 상태를 언제 확정하나?”

### F084 | S41 deep dive · 실패를 모델에 돌려줄지 중단할지

**Section/master/template:** Microsoft Agent Framework / `M-ARCH` / `T-SEQ`. **Question/purpose:** 일반 Tool Error와 보안 정책 위반은 다른 복구 정책이 필요하다.

**Exact audience headline:** “일반 Tool Error와 보안 정책 위반은 다른 복구 정책이 필요하다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 일반 도구 오류: 모델에 Tool Result로 전달 가능
- 인가 정책 위반: 실행 자체 차단·Run 중단 고려
- 변경된 최종 인자 기준 승인·감사

**Geometry and labeled visual (explicit construction):** Agent→Chat→Function Middleware 중 Function Gate에서 일반 오류 주황/정책 차단 빨강 두 가지 경로.

**Space-only semantic builds:**

- `F084-B01`: 입력 인자 검증.
- `F084-B02`: Middleware 적용.
- `F084-B03`: Tool Error 경로.
- `F084-B04`: 강제 Policy Stop.
- `F084-B05`: Resume 판단.

**Speaker script (readable Korean):** “정책 위반을 그냥 모델에게 ‘다시 해 봐’라고만 보내면 같은 금지 요청을 다른 표현으로 반복할 수 있습니다.”

**Technical explanation / caution / counterexample:** 특정 MiddlewareFailure 클래스와 처리 옵션은 고정 소스에 맞춰 작성. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-M-OVERVIEW` and same legacy `S41`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F085 | S42 · Microsoft Workflow의 Superstep과 Checkpoint

**Section/master:** Microsoft Agent Framework / `M-ARCH`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “Microsoft Workflow의 Superstep과 Checkpoint”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `같은 단계에 실행할 Executor 처리 → State Commit → 다음 단계 메시지 → Checkpoint`.

**Diagram/layout specification:** Superstep 1 `A/B parallel` → Commit → pending messages → Superstep 2 `Join C` → Commit/Checkpoint. 아래 실패 도식 `DB write done / checkpoint not written → resume → write again?`. `정확히 한 번` 보장은 붉은 X로.

**Space-only semantic builds:**

- `F085-B01`: Fan-out.
- `F085-B02`: 각 Executor 처리.
- `F085-B03`: 내부 상태 적용.
- `F085-B04`: Checkpoint.
- `F085-B05`: 복원 가능 상태와 외부 DB 결과는 분리.

**Speaker script / detailed explanation:** 공식 Microsoft Workflow Checkpoint는 Superstep 경계에서 저장을 지원하며 Python에는 in-memory/file/외부 저장 옵션 등이 있다. Superstep 내부 Commit은 외부 DB의 원자적 트랜잭션과 다르다. 서로 다른 Source의 메시지 순서는 앱이 의미 있는 Join 키로 처리해야 한다. Functional Workflow의 단계별 캐싱과 Graph Superstep Checkpoint도 구분한다.

**Mandatory correctness refinement:** Superstep checkpoint와 DB exactly-once 다른 문제. Python 최신 release entry checkpoint 변경 여부 조사.

**Likely Q&A:** Q. Checkpoint가 있으면 외부 DB 반영은 정확히 한 번이라고 보장되나요? A. 아닙니다. Checkpoint는 Framework 상태에 대한 것이고 외부 쓰기에는 멱등성/트랜잭션 설계가 필요합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `OFFICIAL-M-WORKFLOW`; legacy `S42` reference: [OFFICIAL-M-CHECKPOINT], [OFFICIAL-M-WORKFLOW]; [LOCAL-M2] §§17–20.. **Trace:** No fake actual trace.

**Bridge:** “일곱 개를 같은 하나의 의사결정 표에 놓으면?”

### F086 | S42 deep dive · Superstep은 동기화 지점

**Section/master/template:** Microsoft Agent Framework / `M-ARCH` / `T-SEQ`. **Question/purpose:** 동일 단계 Executor 실행이 끝나야 다음 단계 메시지가 전달된다.

**Exact audience headline:** “동일 단계 Executor 실행이 끝나야 다음 단계 메시지가 전달된다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Superstep N: A/B 동시 처리
- Barrier → 다음 Superstep N+1 메시지 전달
- Checkpoint는 엔진 상태를 남긴다

**Geometry and labeled visual (explicit construction):** A/B → barrier → Join C의 고정 BSP 다이어그램, Checkpoint와 DB Side Effect를 다른 데이터 저장소로.

**Space-only semantic builds:**

- `F086-B01`: A/B 시작.
- `F086-B02`: 동기화 Barrier.
- `F086-B03`: 메시지 큐 전달.
- `F086-B04`: Checkpoint 생성.
- `F086-B05`: 재개 후 외부 부작용 확인.

**Speaker script (readable Korean):** “체크포인트는 워크플로의 내부 상태를 복원하는 수단이지, 외부 DB의 작업이 정확히 한 번 일어났다는 증명이 아닙니다.”

**Technical explanation / caution / counterexample:** 특정 Python 릴리스의 entry checkpoint 추가 등은 버전 차이 유의. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-M-WORKFLOW; OFFICIAL-M-CHECKPOINT` and same legacy `S42`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F087 | S43 · Agent Orchestration 4종을 한 번에 구분

**Section/master:** 종합/운영 / `MIXED`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-COMP`.

**Exact audience headline:** “Agent Orchestration 4종을 한 번에 구분”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Tool 병렬 / Agent-as-Tool / Handoff / 명시적 Workflow — 제어권이 다르다`.

**Diagram/layout specification:** 2×2 그리드. 위 왼쪽 Main → Tool A/B; 위 오른쪽 Parent → Child Agent → Parent; 아래 왼쪽 Agent A --control transfer--> Agent B; 아래 오른쪽 Program workflow `A→(B||C)→D`. 각 그림 하단 세 개의 질문 `누가 최종 답변? / 컨텍스트 얼마나 전달? / 누가 다음 단계 결정?`.

**Space-only semantic builds:**

- `F087-B01`: Tool 병렬은 LLM Loop 하나.
- `F087-B02`: Agent-as-Tool은 부모 복귀.
- `F087-B03`: Handoff는 활성 Agent 전환.
- `F087-B04`: Workflow는 개발자 제어.
- `F087-B05`: Subagent는 같은 프로세스/스레드인지와 OS 격리를 혼동하지 않음.

**Speaker script / detailed explanation:** 모든 프레임워크가 정확히 동일한 4개 API를 제공한다는 뜻이 아니라 **비교를 위한 설계 패턴**이다. PydanticAI의 코드 위임을 native Handoff와 일대일 대응하지 않는다. Multi-Agent를 쓴다고 정확도나 안전성이 자동 증가하지 않는다.

**Likely Q&A:** Q. Multi-Agent라는 표현으로 모든 위임 방식을 설명해도 되나요? A. Loop 소유권과 최종 답변 주체·컨텍스트 전달·다음 실행 결정자가 다르므로 패턴을 구분합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `LOCAL-CMP`; legacy `S43` reference: [LOCAL-CMP] §§7–9, 25–29.. **Trace:** No fake actual trace.

**Bridge:** “실제 도메인 Agent를 구현한다면 제공 범위와 남는 책임은?”

### F088 | S43 deep dive · 4가지 Orchestration의 핵심 질문

**Section/master/template:** 종합/운영 / `MIXED` / `T-COMP`. **Question/purpose:** 누가 다음 단계와 최종 답변을 소유하는가.

**Exact audience headline:** “누가 다음 단계와 최종 답변을 소유하는가”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Tool 병렬: 동일 Loop
- Agent-as-Tool: 부모 복귀
- Handoff: 활성 Agent 전환
- Workflow: 코드/Graph가 다음 실행 결정

**Geometry and labeled visual (explicit construction):** 2x2 각 패턴이 하나씩 공개되고 마지막 전체 2x2; 같은 Parent node 색과 최종 화자 라벨.

**Space-only semantic builds:**

- `F088-B01`: Tool 병렬.
- `F088-B02`: Agent-as-Tool.
- `F088-B03`: Handoff.
- `F088-B04`: Workflow.
- `F088-B05`: 답변·상태 주체 비교.

**Speaker script (readable Korean):** “네 가지는 설계 패턴의 비교입니다. 모든 제품이 동일한 이름의 API를 제공한다는 뜻은 아닙니다.”

**Technical explanation / caution / counterexample:** PydanticAI Code delegation을 OpenAI native Handoff와 동일하게 쓰지 않는다. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `OFFICIAL-O-ORCH; LOCAL-CMP` and same legacy `S43`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F089 | S44 · 무엇이 제공되는가보다 누가 책임지는가

**Section/master:** 종합/운영 / `MIXED`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-COMP`.

**Exact audience headline:** “무엇이 제공되는가보다 누가 책임지는가”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Framework 제공: Loop·Schema·Event·Hook` / `개발자 책임: 데이터 인가·근거·평가·멱등성·운영`.

**Diagram/layout specification:** 7개 기술을 행, 비교 축 `Loop 소유`, `Tool 실행 경계`, `Memory/State`, `승인·복구`, `개발자 구현 범위` 5열로만 둔 압축 책임 매트릭스. 초록/붉은 승패 점수 금지. 동작 방식이 다르면 `Harness-owned`, `App-owned`, `Core + App`, `CLI-owned`로 표기.

**Space-only semantic builds:**

- `F089-B01`: 현재 화면의 비교 축과 출발 주체를 한 가지씩 표시.
- `F089-B02`: Hermes → Claude → Pydantic → 나머지의 소유권 열만 차례로 강조. 오른쪽 BIN 시나리오에서 `허용 Lot`, `as-of time`, `SOP revision`, `Tool call ID`, `prediction version` 예시 필드.
- `F089-B03`: 해당 실행 경계의 확인 가능한 결과와 개발자 책임을 구분해 표시.

**Speaker script / detailed explanation:** 타입 검사로 분석의 사실성을 보장하지 못하며, Guardrail이 있다 해서 모든 Tool 경로를 차단한다고 단정할 수 없다. Checkpoint만으로 외부 변경의 exactly-once도 안 된다. 이 표는 요구사항 수집의 시작점이다.

**Likely Q&A:** Q. Framework가 Guardrail을 지원하면 운영팀의 정책 책임이 없어지나요? A. 아닙니다. 데이터 인가, 소스 근거, 로그, 평가, 실패 복구는 앱·운영 계층에서 책임을 정의해야 합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `LOCAL-CMP`; legacy `S44` reference: [LOCAL-CMP] §§16–22,30–36.. **Trace:** No fake actual trace.

**Bridge:** “그렇다면 운영하는 위치는 어디로 정할까?”

### F090 | S44 deep dive · 보안·근거·복구는 제품 밖에도 남는다

**Section/master/template:** 종합/운영 / `MIXED` / `T-DECISION`. **Question/purpose:** Loop 제공 여부와 데이터 품질 책임을 분리해야 한다.

**Exact audience headline:** “Loop 제공 여부와 데이터 품질 책임을 분리해야 한다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 프레임워크가 제공하는 것: Loop/Validation/Event/Hook
- 개발자가 보장할 것: AuthZ/Source/Idempotency/Evals
- 최종 판단: 팀이 통제할 실행 계약

**Geometry and labeled visual (explicit construction):** 7종 책임 Matrix는 한 장에 전부 꽉 채우지 않고 소유권 열→정책/상태 열→통합 최종 순으로 3장 또는 build 3단계.

**Space-only semantic builds:**

- `F090-B01`: Loop의 주인.
- `F090-B02`: Tool 허가 경계.
- `F090-B03`: State와 복구.
- `F090-B04`: 업무 데이터의 근거.
- `F090-B05`: 비교결론.

**Speaker script (readable Korean):** “형식 검증과 실행 성공, 실제 도메인에서 의미 있는 결과는 세 가지 서로 다른 통과 기준입니다.”

**Technical explanation / caution / counterexample:** 성능 벤치마크·검증하지 않은 우열 주장 금지. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `LOCAL-CMP §16–22` and same legacy `S44`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F091 | S45 · 중앙 Agent 서버 vs 사용자 PC Agent + 중앙 LLM

**Section/master:** 종합/운영 / `MIXED`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-COMP`.

**Exact audience headline:** “중앙 Agent 서버 vs 사용자 PC Agent + 중앙 LLM”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `Agent Runtime 위치와 LLM Server 위치는 독립적으로 결정 가능`.

**Diagram/layout specification:** 나란히 3안 중 우선 두 안 강조. **A** `Browser → API/Auth → Agent Workers/Queue/State → Tool/DB → LLM Gateway/vLLM`. **B** `Desktop Agent(사용자 로컬 실행·파일 접근) → 중앙 LLM Gateway/vLLM`, 중앙은 정책·인증·업데이트/Telemetry 별도 관리. **C** 혼합형을 점선으로만. 오른쪽 `세션/자격증명/파일/Tool/배포/Trace/취소` 책임표.

**Space-only semantic builds:**

- `F091-B01`: 중앙형 장점·한계.
- `F091-B02`: 로컬형 장점·한계.
- `F091-B03`: 혼합의 필요 조건.
- `F091-B04`: 동시 사용자와 GPU 요청은 별도 제한.

**Speaker script / detailed explanation:** 중앙형에서는 사용자 격리, 큐와 워커, Secret 관리, Tool Sandbox, SSE/비동기 Job, 취소·로그가 필요하다. 로컬형에서는 설치 서명, 자동 업데이트/롤백, OS 호환, 로컬 권한·파일 접근, 중앙 인증 및 모델 API 사용량 한도가 필요하다. 로컬 Agent라도 LLM을 중앙에서 서빙할 수 있다. 데이터 외부 전송 규정이 모델 요청/Trace 설계에 영향을 준다.

**Mandatory correctness refinement:** 중앙 LLM과 중앙 Agent 실행 위치는 독립 설계 변수.

**Likely Q&A:** Q. 중앙 LLM을 쓰면 Agent도 반드시 중앙 서버에 있어야 하나요? A. 아닙니다. 로컬 사용자 PC Agent와 중앙 vLLM 모델 조합도 가능합니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `LOCAL-CMP`; legacy `S45` reference: 인계 §4.7 B24 / R11, [LOCAL-CMP] §§19–22.. **Trace:** No fake actual trace.

**Bridge:** “다음 단계에서 우리가 우선 검증해야 하는 것은?”

### F092 | S45 deep dive · 중앙 Agent 런타임

**Section/master/template:** 종합/운영 / `MIXED` / `T-ARCH`. **Question/purpose:** 중앙 서버에서 Tool과 Agent를 돌리고 모델은 별도일 수 있다.

**Exact audience headline:** “중앙 서버에서 Tool과 Agent를 돌리고 모델은 별도일 수 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- Browser/API → Auth/Queue → Agent Workers
- Worker → 권한 있는 Tool/DB
- Worker → 별도 LLM Gateway/vLLM

**Geometry and labeled visual (explicit construction):** 중앙형 배포도 1개만. 사용자 세션과 Worker concurrency, GPU 요청량을 각각 다른 카운터/경계로.

**Space-only semantic builds:**

- `F092-B01`: 브라우저 요청.
- `F092-B02`: 인증/큐잉.
- `F092-B03`: Agent Worker.
- `F092-B04`: Tool/DB ACL.
- `F092-B05`: LLM Gateway.
- `F092-B06`: 로그/취소·재시도 책임.

**Speaker script (readable Korean):** “중앙형은 관리와 공통 업데이트가 쉬운 대신 사용자·테넌트 격리, 큐, 승인, 관측 시스템을 설계해야 합니다.”

**Technical explanation / caution / counterexample:** 실측 사용자당 GPU 메모리 수치 발명 금지. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `LOCAL-CMP §19–22` and same legacy `S45`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F093 | S45 deep dive · 로컬 Agent+중앙 LLM

**Section/master/template:** 종합/운영 / `MIXED` / `T-ARCH`. **Question/purpose:** Agent 위치와 모델 위치를 분리해 설계할 수 있다.

**Exact audience headline:** “Agent 위치와 모델 위치를 분리해 설계할 수 있다”.

**Exact on-screen copy (show only what fits; preserve this wording):**

- 사용자 PC: Agent Runtime + Local Tools
- 네트워크 → 중앙 LLM Gateway/vLLM
- 중앙: API 인증/사용량·권한·로그 정책

**Geometry and labeled visual (explicit construction):** 로컬PC 영역과 중앙서버 영역 2개만. 로컬 Tool 실행은 PC 안, 모델 응답/요청은 외부. 민감 데이터가 모델 입력에 포함될 수 있는 경계 경고.

**Space-only semantic builds:**

- `F093-B01`: 로컬 사용자 요청.
- `F093-B02`: 로컬 Agent Tool.
- `F093-B03`: 중앙 LLM 추론.
- `F093-B04`: 클라이언트 업데이트·비밀정보 관리.
- `F093-B05`: 혼합형 적용 조건.

**Speaker script (readable Korean):** “로컬에서 Agent가 움직여도 중앙으로 보내는 프롬프트 데이터의 보안 요건과 토큰 사용량이 사라지지 않습니다.”

**Technical explanation / caution / counterexample:** 원격 모델 API로 실제 민감 데이터 전송 금지; 정책 적합성 판단 필요. This section zooms into the preceding main slide; use the parent slide's long technical notes and source mapping, but do not repeat its overview screen text. Include at least one specific why/why-not Q&A.

**Sources:** `LOCAL-CMP §19–22` and same legacy `S45`; verify each rendered implementation statement against official sources/target package. **Trace mapping:** no runtime evidence claimed until real run.

### F094 | S46 · 최종 결론 — 제품 선택보다 실행 계약 검증

**Section/master:** 종합/운영 / `MIXED`. **Role:** baseline overview or principal mechanism (the next `Fxxx` details must deepen, not repeat this unit). **Template:** `T-ZOOM`.

**Exact audience headline:** “최종 결론 — 제품 선택보다 실행 계약 검증”.

**On-screen copy (literal content, wrap or divide naturally, never paste large paragraphs):** `① 어떤 상태가 모델로 전달되는가?` `② 어떤 행동을 Runtime이 실제로 수행하는가?` `③ 누가 안전성과 재현성을 보장하는가?` / `다음 단계: 최소 도메인 Agent 구현·검증`.

**Diagram/layout specification:** 7개 작은 아키텍처 카드와 가운데 공통 '실행 계약' 다이어그램. 다음 세미나의 과제 `data snapshot → tool auth → trace → evaluation → deployment` 한 줄. `실제 성능 수치 없음 / 데모 Trace 검증 후 완성` 풋노트.

**Space-only semantic builds:**

- `F094-B01`: 실코드로 본 경계.
- `F094-B02`: Hermes/PydanticAI에서 직접 관찰.
- `F094-B03`: 요구조건 중심 선정.
- `F094-B04`: Q&A.

**Speaker script / detailed explanation:** 오늘의 성과는 일곱 제품이 똑같은 기능을 제공한다는 표가 아니라, 실제로 어디에서 Loop·정책·복구·위임이 결정되는지 비교할 수 있다는 것이다. 데모 결과가 미검증인 경우 수치·완료율·개선 효과를 발표하지 않는다.

**Likely Q&A:** Q. 최종 도입 결정 기준은 무엇인가요? A. 실행 주체, 입력·출력 근거, 보안·복구·평가와 배포 책임을 시험 가능한 계약으로 확인하는 것입니다. 추가로 설치 버전·구현 경계를 확인해야 하는 예외 질문 한 개를 노트에 추가하라.

**Source IDs & research map:** `LOCAL-CMP`; legacy `S46` reference: [LOCAL-CMP], 인계 §1·§9.. **Trace:** No fake actual trace.

**Bridge:** Q&A 및 부록.


## 9. Demo architecture and presentation contracts — two *separate* authentic web viewers

These are **not fake browser diagrams** of Agents and not animation approximations of execution. Produce real functioning Hermes and PydanticAI applications, record their observable events with source integrity, and offer separate **Space-only prerecorded REAL Trace viewers** for the lecture. At slide `S13/S14` (renumbered `Fxxx`) presenter navigates in advance to `seminar_2/demos/hermes/viewer` and returns; at `S31` to `seminar_2/demos/pydanticai/viewer`. Avoid audience clicking tabs or launching live Tool calls. A deterministic replay of real runs is better teaching evidence than an unreliable live demo that may fail or hang.

**Three independent subsystems:** (1) operator-only data generation and recorders, (2) actual framework + tools + model endpoint, (3) read-only presenter viewer. The replay app **only reads persisted data**, must never invent missing intermediate states, and cannot change the model's actual execution order. Avoid making an imitation of Hermes/PydanticAI that only renders mock Loop cards. If you cannot run the framework, make the viewer display `실제 Trace 없음 / 실행 검증 대기`; keep the explanatory presentation usable but mark the demo path blocked.

**Same scenario and data** (§5), **separate implementation** for Hermes and PydanticAI, **one shared source-preserving trace normalization library**, individual `run_manifest.json`, and separate viewer routes/HTML. Both model clients point at **the same Codex-side `127.0.0.1:10000`** local OpenAI-compatible endpoint while on the development machine. When port 10000 routes to the target PC's vLLM proxy, only Provider configuration/adapter should need replacement, subject to the compatibility matrix; do not rewrite Tool business logic or alter trace facts.

### 9.1 Provenance classes (show persistent concise label, no mode selector)

| Marker | When valid | Audience statement |
|---|---|---|
| `REAL` | Completed actual installed framework run observed/captured with exact version and local/synthetic data | “실제 런타임 수행 중 수집” |
| `REPLAY (REAL TRACE)` | A stored hash-verified REAL run is being stepped through | “실제 기록을 Space로 재생” |
| `CONTROLLED_TEST` | Framework executed under test model/fixed Provider responses to force a branch | “실행 분기 검증용 통제 시험” |
| `ILLUSTRATIVE` | Slide-only fake/explanatory events or synthetic sequence with no actual run | “설명용 도식, 실제 실행 로그 아님” |
| `NOT_OBSERVED` | Feature was available or expected but never occurred in this run | “이번 실행에서 관측되지 않음” |

**Never** render an ILLUSTRATIVE fixture with a `REAL` run ID. `CONTROLLED_TEST` is not a claim that a live model autonomously chose the fixed Tool Call. Distinguish `RUNTIME_OBSERVED` from `DOC_CONFIRMED` for each demonstrated step, including `INTENT_PERSISTED`, compaction, hook cancellations, parallel calls, and any actual provider wire payload. Annotate capture boundary with the visible origin.

### 9.2 Trace event model and stable replay state

Use this explicit **viewer-owned schema**, not a claimed standard of seven frameworks:

```json
{
  "schema_version": "trace-v1",
  "run_id": "RUN_REDACTED",
  "session_id": "SESSION_REDACTED",
  "parent_run_id": null,
  "event_id": "evt_0001",
  "sequence": 1,
  "timestamp_utc": "<recorded ISO8601>",
  "framework": "hermes_or_pydanticai",
  "framework_version": "<actual installation>",
  "mode": "REAL | CONTROLLED_TEST",
  "kind": "model_request_prepared | tool_start | ...",
  "node": "<observed source layer>",
  "model_call_id": null,
  "tool_call_id": null,
  "parent_span_id": null,
  "capture_layer": "FRAMEWORK_EVENT | SDK_OBJECT | PROVIDER_REQUEST | WIRE_PAYLOAD | VIEW_DERIVED",
  "verification": "OBSERVED | DOCUMENTED | UNOBSERVED",
  "payload_redacted": {},
  "source_ref": "<redacted recorder span or file>",
  "duration_ms": null,
  "error": null
}
```

Event kinds (capture if real, *never fabricate*): `run_start`, `system_prompt_snapshot`, `model_request_prepared`, `provider_request_sent`, `model_response`, `tool_call_requested`, `tool_arguments_validated`, `policy_approval_pending`, `policy_approved`, `policy_denied`, `tool_start`, `tool_end`, `tool_error`, `history_appended`, `memory_written`, `context_compacted`, `agent_delegate_start`, `agent_delegate_end`, `output_validated`, `run_interrupted`, `run_completed`, `run_failed`, `run_cancelled`. For time-based figures store **observed start/end timestamps separately**; the cursor index is merely a viewer order, not the concurrency start order. Preserve parent span/Tool Call IDs for causal grouping.

`capture_layer` meaning: `SDK_OBJECT`=internal model request/message object; `PROVIDER_REQUEST`=adapter-created parameters; `WIRE_PAYLOAD`=redacted bytes at trusted local transport capture point; `FRAMEWORK_EVENT`=documented runtime event; `VIEW_DERIVED`=explicit calculation/aggregation made by viewer. Never call SDK_OBJECT the exact wire request or claim to capture TLS plaintext from a third-party endpoint. The **local owned relay** may safely capture field-level *redacted* request metadata because it receives clients' cleartext locally; never log API Key, authorization header, raw sensitive prompts, cookie or confidential Lot data.

`run_manifest.json` must contain schema version, source/installation version and commit, model id (nonsecret), proxy/backend type, capture method and layer, dataset snapshot/seed, run start/end times, SHA-256 for event files, redaction version, controlled/real status, failure statuses, and allowed tool list. A viewer verifies manifest hashes and refuses to show a mismatched run as `REAL`. Dynamic viewer must not expose the raw SDK/Tool debugging endpoint on audience routes.

**Viewer layout (Space only):** 16:9 frame with fixed top line `Framework / installed version / REPLAY / run_id / model`, left 25% **same architecture master**, center 40% single semantic event timeline/loop, right 35% **current event's field/source details**; a bottom build progress indicator but **no buttons, tabs, filters, inputs, hover cards, clickable replay controls**. Unlike the original 46-slide concept of eight tabs, treat the eight *conceptual views* as sequential internally generated scenes with **one authoritative cursor**:

1. Overview/Run manifest → 2. actual Request and capture layer → 3. Loop/model response → 4. requested vs validated Tool/authorization/handler → 5. Result appended and next model call → 6. context/history/memory changes (only if observed) → 7. delegation/approval (if observed, else separate CONTROLLED_TEST route) → 8. result, snapshot, output provenance and end reason.

Each viewer scene is multiple atomic Space steps if needed, with one event/relationship per step. A static captured log may contain many events; group redundant token deltas **only if they are visually presented as a derivative aggregation** and preserve the raw event source, hash and causal order. A browser reset, trace selection or recording trigger belongs only on the operator CLI/preparation screen, never the audience page. No secret printed into the browser or trace.

### 9.3 Recorder implementation and observational equivalence

Instrument least invasively: official callback/events/tracing → SDK/Provider wrapper at documented boundary → source checkout with reversible patch only when absolutely necessary and separately diffed. Do not change scheduling, Tool Call order, retry semantics, error handling, permission policy or data results to collect a pretty trace. Use buffered/nonblocking structured logs; record recorder version. For a deterministic test-model input, compare pre/post-instrumentation Tool count, handler invocations, arguments, result shape, failures and state updates to demonstrate observer equivalence. Live model outputs are nondeterministic: do not compare their response text as evidence of equivalence. Record cancellation and leftover background task conditions separately.

**Data hygiene:** sanitize/allowlist *before writing*; redact or hash principal/user IDs, local paths, tokens, internal URLs and prompts. No external manufacturing datasets, real credentials, private chain-of-thought or actual tool secrets in any artifact. Tools with writes are hard-restricted to an isolated synthetic demo workspace and optional mock publication table keyed by idempotency key.

## 10. Demo 1 — real Hermes Harness anatomy

**Primary goal:** use actual Hermes Agent installation/code/CLI and preserve its native Loop, Tool Registry, sessions and provider integration. Do not replace Hermes with a hand-built “Hermes-like” Agent. Run T1→T2→T3 using read-only synthetic BIN tools and capture **one actual model request, Tool Call, handler execution, ToolResult and next model request, final answer and session write**. Other features (Skills, Memory, Plugin, MCP, subagents, compaction, approval, Cron, Gateway) may be demonstrated in **additional distinct runs** only after they are genuinely observed; absent features are `NOT_OBSERVED`.

**Hermes setup and isolation:**

1. Detect OS/Python version, installed Hermes CLI `--help`, package or source ZIP, source tag/commit and checksum, configured `HERMES_HOME`/Profile. Do not guess commands. Existing user's Hermes Profile, `MEMORY.md`, `USER.md`, SQLite DB and Skills must be **left untouched**. Create an isolated disposable demo profile/home and read-only backup/diff manifest; document remove/restore. A target machine's existing zipped Hermes package is inventory only until inspected; preserve it.
2. Confirm Hermes supports an OpenAI-compatible custom endpoint for the installed API mode. Use tested Hermes config keys and actual help output, not invented `DEMO_*` native keys. Point only this isolated profile to `http://127.0.0.1:10000/v1` with the relay's exposed model ID (not arbitrary upstream model string unless the relay supports that mapping).
3. Register synthetic Tools using the least invasive supported official mechanism: user/project Plugin, builtin/custom Registry, or MCP Server, **with clear source-level registration and dispatch trace**. Explain Tool/Plugin/MCP as separate expansion concepts. Never edit global Hermes imports or personal Tool/Memory configuration for a demo. If needed, write a reversible patch with diff/rollback and tag-verified source functions.
4. Observe, in order: Run start/session identity → stable/context/volatile prompt construction or snapshot → Provider request object → model response with Tool Calls → Registry lookup and pre-Tool Hook → verified handler args/authorization → Tool execution start/end → result append to History → next Model request → final output and session persistence. **Capture source layer accurately**. Tool intent persistence before execution is a **testable question**, not a universal asserted property.
5. Optional tests, if supported: Memory tool writes to separate Memory files and snapshot refresh (state hashes before/after), SQLite FTS5 lexical session search, selected Skill load, Plugin hook, MCP roundtrip, multiple concurrent Tools vs separate child Agent runs, Gateway session routing and Cron new-run behavior, context compaction. Use separate `CONTROLLED_TEST` label when forcing responses; no fake `cache_hit` metrics.
6. Produce `hermes_source_audit.md` mapping observed hooks to tag file/symbol, `hermes_config_adapter.py` as needed, `run-recording.md`, real trace manifest/files, viewer `index.html`, expected-results assertions and `rollback.md`.

**Learning scenes for Hermes viewer:** H-T1 user session to model; H-T2 exact *capture layer* of prompt/schema/history; H-T3 model returns Tool Call; H-T4 Tool dispatch/Policy/Handler, actual args; H-T5 result returned and next model call; H-T6 state persisted and snapshot comparison; H-T7 final answer and unobserved-feature list. Connect the learned `H-ARCH` component ID to each actual trace event. If Tool Call did not occur, preserve evidence of no Tool Call, do not fabricate H-T3.

**Hermes pitfalls:** CLI tool completion order may differ from request order; Session FTS5 is lexical; model caching/prefill is Provider-dependent; background Cron may spawn new run rather than continuing an old one; Subagent History is distinct but OS isolation isn't implied; tool-intent durability/fail-closed semantics require real source proof; HTTP/Tool failures are not all retried automatically.

## 11. Demo 2 — real PydanticAI Core plus explicit developer-owned boundary

**Primary goal:** show the essential difference between **developer-authored Python** and **PydanticAI-owned internal Graph/ToolManager/Output** with a working Core Agent. Implement T1–T3 with synthetic read-only Tools, typed arguments and result. Core comes **first**; `pydantic_ai_harness`/optional Capabilities are an optional **separate package/step** only after the Core demo is working and version-compatible. Do not silently add LangGraph or a custom “agent loop” in place of the internal Core Graph.

**Required implementation steps:**

1. Pin installed versions of `pydantic-ai`/`pydantic-graph` and relevant optional packages; verify actual `Agent`, Tool decorators, output types, `RunContext.deps`, run method names, `end_strategy` and deferred tool types against release docs/source. Build own Python venv + lockfile and no machine-global installation.
2. Implement an application-owned `Deps` or equivalent with `SyntheticDatasetStore`, `principal`/authorized Lot set, observation cutoff and runtime tracing context. **Do not serialize DB handle/credentials to ModelRequest**. In the Tool handler, perform actual authorization, temporal filtering and dataset snapshot validation before returning permissible data.
3. Register `get_bin_rates`, `get_measurements`, `read_sop`, `predict_bins` and optionally all §5 Tools using version-correct APIs. Use typed Tool argument/structured Output contracts and corresponding Python `BaseModel` schemas, with app-level semantic validators for numerator/denominator/time/revision. A typed valid result can still be semantically false; show this as a separate negative test.
4. Capture `run` + `run_stream_events` or `iter` where supported, choose a primary full-graph observation path based on actual version behavior, and record **UserPromptNode/ModelRequestNode/CallToolsNode/End** when the installed Core exposes those states. Map app-defined Tool handler events separately from SDK internal events; do not claim the observer sees Provider wire payload unless the selected adapter/relay actually captured it.
5. Display **all five main run methods** in the slides: `run_sync()`, `run()`, `run_stream()`, `run_stream_events()`, `iter()`; explain that `run_stream_sync()` is a variant and that `run_stream_events` returns an async event stream ending in a result event according to current docs. Demonstration code should use correct installed signature and context manager behavior.
6. **Controlled EndStrategy experiment:** construct a fixed model response containing valid *output tool* A, function Tool B and additional output candidate C. Execute independently with `end_strategy='early'`, `'graceful'`, `'exhaustive'` using an approved **mock-only** side-effect Tool counter to measure actual executed handlers. Also test failed-output validation and recovery. Distinguish model's response selection from framework's handler dispatch. Where streaming `run_stream` finalizes first valid output and does not behave like `run`, show it as a separate scenario. This experiment is labeled `CONTROLLED_TEST`, not an autonomous live model result. Read exact version behavior (including default graceful) before showing checkmarks.
7. **Parallelism experiment:** two independent read Tools and a sequential barrier/side-effect mock; verify actual timestamps and whether installed `sequential=True` semantics match diagrams. Don't interpret `asyncio` concurrency as automatically multiple processes/threads or a global database transaction lock.
8. **Guardrail vs Validation:** wrong JSON/type → Pydantic argument validation/retry; unauthorized Lot → app/DB authorization rejection; correct schema with false data → semantic data-truth rejection. They are distinct mechanisms with distinct examples.
9. **Approval / Deferred:** optional controlled separate T4 mock report publication with full approval key `(request_id, principal, final_tool_args_hash, dataset_revision)`. Persist pending/resume state as supported; approval and tool execution must remain sandbox-only and idempotent. A resumed Run does not imply external DB exactly-once automatically.
10. **History/Memory/Harness:** use first run to produce History and explicitly feed into second run; show what is persisted in the app vs what the Core returns. Optional Harness Skills/Memory/Compaction only with explicitly verified package/runtime. If unavailable, label the feature as an optional, untested extension rather than representing it as Core-owned behavior.

**Pydantic viewer scenes:** P-T1 App user request and declared Agent/Deps; P-T2 actual model-visible messages/Tool Schema vs deps; P-T3 internal Graph node transition; P-T4 ToolManager argument validation and Tool handler ownership; P-T5 Tool execution result→History→next Model request; P-T6 Output type validation/EndStrategy effect (controlled test separate from normal run); P-T7 final RunResult and app persistence; P-T8 optional approval/deferred and unobserved features. Include the actual Python code fragment adjacent to its corresponding Runtime event **only when it can fit on an independent slide or viewer scene**; keep code in a separate magnified step if necessary.

**Version-specific acceptance:** do not present source code that is only pseudocode as runnable. If a currently installed package moved APIs since the research baseline, write a tested compatibility adapter and a note `release-baseline → installed release`. Do not collapse these into “PydanticAI supports everything.”

## 12. Codex port 10000 bridge: local OpenAI API now, vLLM proxy later

### 12.1 Non-negotiable routing

```text
[Codex-produced Hermes Agent] ---\
                                 +---> http://127.0.0.1:10000/v1  (same client contract)
[Codex-produced PydanticAI] ----/               |
                                                  | Current development PC
                                                  v
                                    [Codex local compatibility relay]
                                       -- TLS, OPENAI_API_KEY --> [OpenAI API]

                                                  | DIFFERENT TARGET PC
                                                  v
                                    [Existing localhost:10000 proxy]
                                                  |
                                            [vLLM serving model]
```

**Only port 10000 here.** Antigravity's **10001** is reserved for the other implementation and should **not** be touched/bound by Codex. The local demo Agents must not know whether the upstream is OpenAI or vLLM. The browser must never call OpenAI directly or hold an API Key. The relay listens only on `127.0.0.1:10000` by default (local only), implements the exact supported OpenAI-compatible surface and exposes a **stable alias** of the model id if upstream name changes.

**Local relay implementation requirements:** Python FastAPI/Starlette + `httpx` or a similar minimal web server, with tests and dependencies pinned. Prefer API endpoint `POST /v1/chat/completions` because both Framework adapters can be configured for OpenAI-compatible chat; optional `GET /v1/models` and `GET /health` are **your local relay endpoints**, not assertions about target PC proxy. Support `messages`, `model`, `tools`, `tool_choice`, optional `temperature`, `max_tokens`/`max_completion_tokens` compatibility, streaming `stream=true` only if fully tested with SSE and Tool Call delta assembly, API error mapping, timeouts, rate limits, and sanitized logs. Forward the actual request to the official OpenAI endpoint using server-side `OPENAI_API_KEY` header over TLS; allowlist request fields and map model alias to configurable `OPENAI_UPSTREAM_MODEL`. Never leak `Authorization`, API Key, raw sensitive prompt, relay private settings or full upstream errors in the response. No arbitrary URL forwarding, open proxy behavior or public network binding. Return true OpenAI-compatible `choices[0].message.tool_calls` when upstream provides it; a model response that merely prints JSON-shaped text is **not** the same API Tool Call.

**Environment example (names are our implementation contract, not the SDK's auto-loaded variables):**

```dotenv
# Never commit .env with real secrets; use process environment or secure .env ignored by git.
DEMO_AGENT_BASE_URL=http://127.0.0.1:10000/v1
DEMO_SERVED_MODEL_ID=seminar-agent-model
DEMO_DATA_MODE=synthetic
DEMO_TRACE_REDACTION=on
DEMO_RELAY_HOST=127.0.0.1
DEMO_RELAY_PORT=10000
OPENAI_UPSTREAM_MODEL=<real model chosen after capability test>
OPENAI_API_KEY=<supply only in server environment, never write value to repo>
```

`/v1/models` in **your relay** may return `seminar-agent-model` alias. On target PC the **existing** proxy may return a different served model ID, which the adapters must accept via env/config without code modification. Do not assume unsupported request fields, responses mode, strict JSON schema or `parallel_tool_calls` pass unmodified. Implement actual capability probes rather than blindly forwarding unknown fields. Demonstrate at least chat + one real Tool Call from each Agent before declaring demo integration complete. Avoid arbitrary retries of Tool/side-effect calls; if the upstream API requires a specific model-feature flag, document it.

**Critical logistics:** If port 10000 is occupied by an unknown process, inspect ownership and configuration; never kill it or rebind silently. Either use a project-isolated host/namespace in which 10000 is free or stop and report the exact blocker. WSL/Docker `localhost` refers to the container/namespace, not always the Windows host. Scripts must test reachability from **the actual client runtime**. Do not expose or overwrite Antigravity port 10001 or its worktree.

### 12.2 Capability probe before running real demos

| Probe (in this order) | Exact evidence | Failure handling |
|---|---|---|
| Local owned `/health` or actual documented endpoint | status and relay/process identity | only local expected endpoints, never assume target supports it |
| Local alias `/v1/models` or target provider's documented discovery | actual served model id | configure model id from probe; no guess |
| Text-only chat | HTTP response with role/finish_reason | fix auth/routing/model compatibility |
| Named Tool Call / Tool choice if supported | structured `tool_calls`, exact args | if absent, don't present a real Tool demo |
| Automatic Tool choice | structured `tool_calls` under auto path | check model/template/parser, not just prompt text |
| Sequential and multiple Tool Calls | correct IDs/return integration | degrade only that feature and label untested |
| Structured output and tool-based output | accepted schema + app validation | use compatible mode when supported |
| Streaming | proper SSE/Tool deltas/termination | viewer REPLAY still works; disable live streaming |
| Token accounting / prompt-cache metrics | actual non-null provider fields | show `미제공/미검증`, no invented counts |
| Cancel/timeouts/retry | verified effect on Agent and Tool | do not claim end-to-end cancellation without checking |

A `supported` checkbox is allowed **only with captured test evidence**. A feature may work in the local OpenAI relay but fail on target vLLM because of model chat template, `--enable-auto-tool-choice`, `--tool-call-parser`, structured output decoding, request fields and streaming behavior. This is an engine-and-checkpoint compatibility problem, not necessarily an Agent-framework bug. No arbitrary “Qwen 3.8” checkpoint/model ID; use what the actual target proxy reports. Do not claim port `10000` is vLLM on the current PC: it is **our OpenAI API relay** here.

## 13. Target-machine migration, preservation and rollback (port remains 10000)

1. Inventory target OS (Windows/WSL/Linux), Python/uv, Node/browser, ports, permissions, network namespace, Hermes ZIP/source install and profile, configured model proxy, exact provider route, model served ID, package versions. Never write into the target's installed Hermes user profile or database; preserve config/memory/session/skills and hashes.
2. Back up existing installed app/config/assets and produce a manifest. Create a separate `seminar_2` demo worktree / Python env / synthetic DB / isolated Hermes profile. Verify no exposed production data or credentials. Copy only needed versioned project artifacts and synthetic fixtures.
3. Find the actual `localhost:10000` proxy endpoint/protocol/auth/version. `/health` and `/v1/models` are **candidates only**, not universal guarantees. If the model service is across WSL/Docker/SSH namespace boundaries, configure host forwarding or proven actual address without altering port ownership or writing secrets to repo.
4. Swap only `ModelEndpoint`/Provider adapter configuration, `DEMO_SERVED_MODEL_ID`, auth/timeouts/model profile as needed; preserve Python Tool contracts, scenario, fixture and view state. Do not deploy the local OpenAI relay over the target vLLM proxy.
5. Run probes from §12.2 on target: text → one Tool Call → multiple calls → structured output → streaming → usage. Record `supported / unsupported / conditional / untested` with raw redacted evidence; choose viable mode (e.g. non-streaming + Tool Output) only when validated.
6. Run T1–T3 **read only** on Hermes and PydanticAI, compare expected synthetic calculations and exact provenance, capture native trace and manifest hashes; verify failures/negative authorization tests.
7. Test approval, duplicate mock execution, cancel, re-run and version switching in sandbox only. Record which side effects, sessions and checkpoints actually recover. A good replay does not certify an external Tool was exactly once.
8. Test both viewers in the target browser with Space only and offline built slide bundle. Run a presenter rehearsal using saved actual `REPLAY` paths. Deliver target-specific commands, working directory, environment variables **without values**, port, exact package versions, source/trace hashes, startup/shutdown and rollback.
9. If any portion cannot be tested on that machine, mark `TARGET_UNVERIFIED`; never report fully portable based on local OpenAI relay success alone.

**Required `migration/compatibility-matrix.md`:** each tool/model feature has local-OpenAI status, target-vLLM status, evidence hash, corrective action, accepted fallback, owner and last test date. **Required `migration/rollback.md`:** how to restore original target config and Hermes profile and remove isolated demos, without deleting unrelated files.

## 14. Skills — installation, safety and controlled use with Codex

Use reputable, inspectable agent Skills as tools for implementation/testing; the user-defined deck design/Space control is nonnegotiable. Skill recommendation is not a guarantee the Skill is installed or compatible with this Codex release. Before running third-party install scripts review the repo and permissions. Do not pass secrets or actual company data to a Skill.

| Role | Skill | Original source | Use boundary |
|---|---|---|---|
| HTML presentation | `frontend-slides` | https://github.com/zarazhangrui/frontend-slides | prefer it for semantic 16:9 slides and reveal mechanics; ignore its visual/theme defaults if conflicting |
| Typography/layout | `frontend-design` | https://github.com/anthropics/skills/tree/main/skills/frontend-design | use for balanced hierarchy and spacing, never new color palette |
| Browser QA | `webapp-testing` | https://github.com/anthropics/skills/tree/main/skills/webapp-testing | Playwright screenshots, keyboard regression and overflow tests |
| Optional visual accessibility review | `web-design-guidelines` | https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines | post-implementation static/UI audit only |

**Suggested project-local installation, when package CLI/Node is present and after verifying current syntax:**

```powershell
# From the project repository root. Confirm `npx skills --help` first.
npx skills add zarazhangrui/frontend-slides --skill frontend-slides --agent codex
npx skills add anthropics/skills --skill frontend-design --agent codex
npx skills add anthropics/skills --skill webapp-testing --agent codex
# Optional:
npx skills add vercel-labs/agent-skills --skill web-design-guidelines --agent codex
```

Check project-local `.agents/skills/<name>/SKILL.md` or the actual installation path, `npx skills list` and Codex's recognized Skill list. Invoke Skills when available; if unavailable due to network/permissions, continue with the explicit requirements in this document using standard HTML/CSS/SVG/Playwright and report the limitation. Do not claim successful install without checking. Keep a shared project-root `AGENTS.md`: **read existing and merge minimally** rather than overwriting, with the user-defined theme/Space-only/real trace/file preservation rules. External Skill source/style prompts are lower priority.

## 15. File tree, work phases, acceptance criteria, and final report

```text
study_for_agent_framework/
├── AGENTS.md                                # merge project rules; never wipe
├── .agents/skills/                          # only when installed/verified
└── seminar_2/
    ├── README.md                            # exact setup, start, space, shutdown
    ├── blueprint/
    │   ├── agent_framework_seminar_ii_codex_final_blueprint.md
    │   ├── slide-id-map.json                # Fxxx→legacy Sxx→sources
    │   ├── source-map.json
    │   └── claim-ledger.md                  # version-tagged factual audit
    ├── slides/
    │   ├── index.html                       # offline-capable 16:9 Space-only stage
    │   ├── src/tokens.css
    │   ├── src/keyboard-controller.ts
    │   ├── src/slides-data.ts
    │   ├── src/diagrams/                    # seven reusable SVG master graphs
    │   ├── speaker-notes.json
    │   └── presentation-snapshot/           # saved visual QA evidence
    ├── fixtures/
    │   ├── synthetic-data-generator.py
    │   ├── synthetic-dataset.sqlite
    │   ├── data-dictionary.md
    │   └── expected-results.json
    ├── common/
    │   ├── trace-schema.json
    │   ├── trace-recorder.py
    │   ├── redaction.py
    │   ├── manifest.py
    │   └── provider-compat.py
    ├── relay/
    │   ├── server.py                        # local 127.0.0.1:10000 → OpenAI
    │   ├── .env.example                     # never includes API Key value
    │   └── tests/
    ├── demos/
    │   ├── hermes/                          # isolated actual installed Hermes
    │   │   ├── viewer/
    │   │   ├── recording/
    │   │   ├── configs/
    │   │   ├── traces/real/
    │   │   ├── traces/controlled/
    │   │   └── hermes_source_audit.md
    │   └── pydanticai/
    │       ├── app/
    │       ├── viewer/
    │       ├── recording/
    │       ├── traces/real/
    │       ├── traces/controlled/
    │       └── version-audit.md
    ├── tests/
    │   ├── slide-navigation.spec.ts
    │   ├── slide-visual.spec.ts
    │   ├── diagram-source-consistency.spec.ts
    │   ├── trace-integrity.spec.ts
    │   ├── test_tool_authorization.py
    │   ├── test_pydantic_output_strategy.py
    │   └── test_provider_compat.py
    ├── migration/
    │   ├── compatibility-matrix.md
    │   ├── install-and-run.md
    │   └── rollback.md
    ├── evidence/                             # screenshots, tests, anonymized logs
    └── QA_REPORT.md
```

**Implementation phases with concrete exit gates:**

- **Phase A / Audit:** repo inventory, `AGENTS.md` preservation, actual first-session design inspection, version/source claim ledger, source maps. Exit = no high-risk on-screen claim without official URL or explicit pending verification.
- **Phase B / Foundations:** tokens, seven reusable masters, semantic slide contract, keyboard state machine, synthetic fixture and independent known-answer assertions. Exit = navigation works with 3 sample slides and no missing architecture IDs.
- **Phase C / Full content:** implement all 94 initial units, speaker notes, 8 optional appendix pages and source maps; add slides when split is needed. Exit = every `Fxxx` has actual content/diagram/steps/notes/QA; no too-small text, no source gaps, no missing slides.
- **Phase D / Real backends:** isolated Hermes T1–T3 and PydanticAI T1–T3, version-correct Tools/Deps, local model compatibility. Exit = each framework has at least one verified **REAL** model→Tool→model run or an explicit blocker documented; never silently substitute synthetic Trace.
- **Phase E / Safe Trace and viewers:** manifest, redaction and replay; controlled EndStrategy/approval if supported. Exit = integrity checks and viewer Space path pass; unobserved states plainly gray.
- **Phase F / Port & migration:** local OpenAI relay on **10000** and target vLLM proxy probe/adapter. Exit = local real Tool Call E2E demonstrated and target marked exactly as tested; **10001 untouched**.
- **Phase G / QA/handoff:** automated browser/per-page screenshot and read-through, source contradiction audit, real version/source mapping, initial/last states, all routes, startup/shutdown/rollback guide. Exit = completed `QA_REPORT.md` with pass/fail evidence and no inflated success claims.

**Quantitative quality gates (fail explicitly):**

1. 94 initial main slide units present, in correct 7-framework order, plus 8 appendix scenes; splits may raise count. **Not necessarily 94 visible DOM slides if further split**, but mapping must remain complete.
2. All **seven** master graphs exist, render before a zoom, and reuse their original node IDs for highlights. No diagram labels omitted by hidden hover.
3. Every slide has real `onScreen`, `visual`, `buildSteps`, complete presenter explanation and source(s). At least one concrete expected Q&A per major concept, and full reference link in notes/claim ledger.
4. Single continuous Space sequence from first slide to last; repeated key and browser default scroll tests pass. No other audience control needed, no controls visible in separate demo viewer. Last Space never wraps.
5. Screenshot QA at 1920×1080, 1366×768, 1280×720 on **all main slides and representative build states**, ideally every build; any clipping/overlap must be fixed by splitting, not shrinking text indiscriminately.
6. Synthetic tool tests verify `denominator>0`, authorization, time boundaries, snapshot ID, SOP revision, temporal holdout, zero unseen real data; rate and baseline values calculated, never handwritten guesses.
7. Every REAL Trace has valid manifest, hashes, real version and capture layer, no leaked API keys, synthetic only; observer equivalence tested where deterministic. `REAL` vs `CONTROLLED_TEST` display never confused.
8. Both real demo backends target `http://127.0.0.1:10000/v1` through a documented adapter on this PC. Local port 10000 relay uses real OpenAI API auth only on server; **port 10001 is untouched**. Target PC assumptions are **not** passed off as tested.
9. Reproduction: clean environment (where possible) executes `install → fixture generation → relay start → framework runs → trace capture → viewers → build/test` using documented commands. Include failures and exit codes in QA report.
10. README's “presentation operator path” is a **simple sequence**: open slides/fullscreen before presentation, press Space throughout, switch to prepared Hermes/Pydantic viewer window at prescribed bridge, Space through actual recorded trace, return to original slide, finish. Operator setup is permitted before audience session, not during slide advancement.

**Final report format:** artifacts and paths; verified installed versions; source-audit exceptions and corrections; screenshot location; tests run/pass/fail; actual Hermes/Pydantic run IDs/trace integrity and capture limits; port 10000 upstream/target distinction; remaining blockers; target machine migration checklist and rollback; **what remains untested**. Never say “done” for an unexecuted real Agent demo or target vLLM migration.

## 16. Optional appendix scenes A01–A08 (build these too, outside default run)

Appendix slides are **supplemental standalone scenes accessible as a prepared second presentation path**. Do **not** add an audience slide selection menu or keyboard shortcut; prepare optional appendix route before the talk, then Space-only in that route. They must follow the same detailed schema/source/visual/notes requirements as the 94 units.

| ID | Onscreen Korean headline and 2–3 facts | Visual / Space steps / speaking focus |
|---|---|---|
| A01 | “제품명이 아니라 실행 경계를 비교한다” / Harness, SDK, Core, Platform은 절대적 배타 분류가 아님 / Claude SDK→CLI, PydanticAI→선택 Harness | 동일 7개 master 작은 경계 표시 → owner 강조 → 제품의 다층성 설명. 근거 각 공식 개요. |
| A02 | “실제 Agent Loop 코드는 기술별로 다른 위치에 있다” / Hermes 공개 Loop / PydanticAI 내부 Graph / OpenAI Runner / Google Flow / Microsoft Pipeline | 각 실행 소유 노드 1개씩, 5 build reveal. Claude 내부 비공개 경계 분명히. |
| A03 | “Retry 네 가지는 부작용 위험이 다르다” / Model 재질의, Validation Retry, Provider HTTP Retry, Job/Workflow Retry | 같은 요청의 네 실패·재시도 상태 기계. idempotency key를 외부 DB 경계에. |
| A04 | “Prompt Cache는 Compaction이 아니다” / KV Prefill 캐시 ≠ 메시지 요약 / Context Window 입력 길이와 연산 재사용 구분 | 두 입력 token bars → Cache 조건 → History 축약 → 정보 손실 반례. |
| A05 | “승인과 재개는 프레임워크별 다른 상태를 보존한다” / Pydantic Deferred / OpenAI RunState / Claude Permission / Microsoft checkpoint | approve(request, principal, args-hash, revision) + resume 단계. 외부 DB side-effect 보존 범위 따로. |
| A06 | “Session ≠ Memory ≠ Artifact ≠ Checkpoint” / 저장 대상·지속성·복구 범위 | 5개 저장소와 actor 화살표. 실제 인수 전이·ToolResult 표시. |
| A07 | “6개의 실패 사례로 안전성을 검증한다” / wrong args, unauthorized Lot, side effect before guard, cancel, changed approval args, old SOP memory | 한 사건씩 Space로 reveal; 정책 적용 위치와 상태 저장을 질문한다. |
| A08 | “제품 선택 전에 요구사항과 실행 실험을 정의한다” / AuthZ, state, model compatibility, evaluation, deployment, operations | 요구사항 → 평가 실험 → 책임 분담 → 결정 순서. 성능 순위/허위 수치 금지. |

## 17. Final Codex reminders — what not to accidentally simplify

- **No 46-slide cap, no 60-minute cap.** This document intentionally plans 94 base+expanded teaching units, and readability is permission to add more, never to erase technical meaning.
- **No clicky website.** Space alone controls both the presentation and viewers, without manual tab/toggle/mode selection. Operator CLI/configuration is a separate surface.
- **No fake traces.** One real Hermes run and one real PydanticAI run are important; if environment prevents them, report a blocker without fabricating a screenshot/sequence or treating a `CONTROLLED_TEST` as REAL.
- **No blind code-name copying.** Baseline version notes and latest public docs may differ; pin and verify before writing code or slides. In particular, the legacy Hermes Tool Intent durability claim is not automatically proven by its general architecture docs.
- **No rewrite of the Agent frameworks.** Keep authentic Hermes Harness and PydanticAI Core; add adapters, synthetic Tools and recorders around them. Do not claim a test-model script is a live model's autonomous action.
- **No application secrets, internal semiconductor data, or real process mutation.** Authorization and semantic validation are in actual Tool/DB, not only model instructions.
- **No port confusion:** this Codex project alone owns **local 10000 OpenAI relay**; target **10000 vLLM proxy**, while **10001 is reserved for Antigravity**. Do not claim the target is connected when it hasn't been probed.
- **No self-invented success.** Completion evidence comprises command output, verified sources, browser screenshots, tests, real hash-verified traces and the migration matrix.

*End of standalone Codex final production blueprint. A finalized deck must be created and verified from this specification; this MD itself is not a claim that implementation work has already been executed.*
