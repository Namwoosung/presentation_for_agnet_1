# Agent Framework 세미나 2차 — Codex 발표자료 제작 지시서 (개정판)

> **용도:** Codex가 이 파일 하나로 한국어 HTML 발표자료와 독립적인 Hermes/PydanticAI 실행 데모를 만들기 위한 제작 명세.  
> **기획 기준:** 2026-11-03. **구성:** 본편 60장, 밝은 배경, 기술 원리·활용 중심.  
> **상태:** 발표 제작을 위한 설계 문서. 실제 HTML·API 호출·Hermes/PydanticAI 실행·Trace·vLLM 테스트는 **아직 검증 결과가 아님**.  
> **대상:** Codex 작업 환경 / 로컬 모델 중계 **127.0.0.1:10000**. Antigravity에 할당된 **10001** 포트를 사용·변경하지 않는다.

## 0. 가장 중요한 제작 의도

**세미나 종료 후 청중이 말할 수 있어야 하는 것**

1. “Hermes는 이미 만들어진 Agent인데, 사용자 입력을 받은 뒤 **어떤 코드와 시스템을 거쳐** 모델을 호출하고 Tool을 실행하고 History/Memory를 남기는지 알겠다.”
2. “Claude Code도 같은 Agent Loop를 쓰지만 **프로젝트 파일·개발 도구·규칙·권한·서브에이전트**가 코딩 작업에 맞게 통합되어 있구나.”
3. “PydanticAI를 쓰면 내가 **Agent 선언, Tool 함수, 데이터 접근, Output 타입, API/DB/권한**을 어느 수준까지 개발하고, Core는 그 안에서 어떻게 돌리는지 알겠다.”
4. “다른 SDK도 기본 원리는 유사하지만 **Handoff·CLI 연결·Event·Middleware/Workflow** 같은 차별점이 있고, 어떤 상황에 쓰면 될지 알겠다.”

**기술 정확성 > 이해되는 흐름 > 화면 가독성 > 시각적 일관성.** 기술적으로 중요한 원리와 분기만 남긴다. 반복 설명과 함수 내부의 잔가지·숫자 암기는 과감히 줄인다. **현재 원고는 60장 초안**이므로 제작 시 실제 콘텐츠를 임의로 생략하거나 장수를 다시 94장으로 늘리지 않는다. 독립된 오류를 고치거나 불가피한 화면 과밀이 있으면 변경 제안을 별도 보고하고, 메인 원고는 사용자 검토용 60장 구조를 우선 유지한다.

### Codex 실행 절차

1. 프로젝트 폴더와 기존 `AGENTS.md`·1차 HTML 스타일·연구 MD가 있으면 확인한다. 없더라도 **이 파일만으로 제작**한다. 기존 파일을 덮어쓰거나 읽지 못한 자료를 읽었다고 주장하지 않는다.
2. 60장 슬라이드 ID와 내용·실제 문구·도식·Space 단계·발표자 설명을 **먼저 데이터화**한다. 구현 시작 전에 `slide_map.json`을 생성하고 중복/누락을 검사한다.
3. 아래 공식 자료와 고정 릴리스를 확인해 `claims.md`에 주장→공식 URL/태그/소스→검증 상태를 기록한다. **코드 표기는 실행하는 버전에서 검증한 후** 화면에 사용한다.
4. 밝은 16:9 HTML 발표자료를 구현하고, 별도의 실제 실행 Demo 1(Hermes), Demo 2(PydanticAI), 기록 도구, Space-only Trace viewer, 10000번 중계기를 만든다.
5. 60장 전체를 브라우저에서 눈으로 확인하고 Playwright로 키 입력·가독성·도식·근거·데모 무결성을 테스트한다. 미완료/미검증은 완성이라고 말하지 말고 보고서에 남긴다.

**우선순위:** 이 파일의 사용자 의도 > 실제 공식 소스/실행 결과로 확인한 기술적 사실 > 기존 1차 디자인의 충돌하지 않는 특징 > 프로젝트 규칙 > 제3자 Skill 기본 디자인. 사실 오류가 있으면 원고를 수정하고 근거를 남긴다.

## 1. 슬라이드 화면 정책 — 밝고, 읽기 쉽고, 흐름 중심

| 요소 | **강제 기준** |
|---|---|
| 비율 | PC 프로젝터용 16:9 HTML(기준 1920×1080, 1366×768/1280×720 테스트) |
| 기본 배경 | **밝은 회백색 `#F7F9FC`**; 카드 `#FFFFFF` |
| 본문·보조 | 진한 남색 `#17243A`, 보조 `#526279`, 경계 `#D9E2ED` |
| 의미 색 | 모델 파랑 `#1D63B7`; Runtime/SDK 보라 `#7545AA`; Tool 초록 `#147E61`; Memory/Context 주황 `#B66813`; 경고 빨강 `#B6384B` |
| 레이아웃 | 한 장 = 한 가지 핵심 설명. 제목은 **결론형 문장**, 본문은 최대 3개 짧은 요지(예외적으로 4개). 도식 중심. |
| 타입 | 기준 1920에서 제목 40~52px, 본문 24~30px, 도식 19~24px, 코드 20~23px; 실측 가독성 우선 |
| 도식 | 편집 가능한 SVG/HTML 선·노드. 화살표마다 `요청/실행/반환/저장/승인` 의미 표시. 마스터 구조는 섹션 내 노드 ID 재사용 |
| 코드 | 실제 구현 설명에 **필요할 때만** 6~15줄을 발췌. 실행 가능 코드·실제 원문·의사 코드가 섞이지 않게 라벨 |
| 애니메이션 | 1 Space = 의미 있는 정확히 1 단계. 0.2~0.4초 가벼운 강조만; 클릭·토글·탭·커서·자동 전환 금지 |
| 발표자 설명 | 자세한 개념과 전제는 노트에 저장. **화면에 장문의 노트나 출처 URL 전문 노출 금지** |

- 전체 밝은 디자인. 검정/짙은 남색 배경의 타이틀 슬라이드도 만들지 말 것. 강조 카드·코드 블록도 밝은 배경이 원칙이다.
- 네온, 3D, 글래스모피즘, 불필요한 아이콘·애니메이션·장식적 사진, 오밀조밀한 표를 피한다.
- 1차 자료가 있을 경우 구조도 표현법, 상하 여백, 발표 전개감은 계승하되 **이번의 밝은 테마와 60장 설계가 우선**.
- `MODEL`, `RUNTIME`, `TOOL`, `STATE`, `APP-OWNED` 경계는 전 섹션 동일 범례. SDK에서 **누가 API를 호출하고 어디서 코드가 실행되는지** 항상 표시한다.
- `Space`가 유일한 **관객용 진행 입력**이다. `event.repeat` 방지, 기본 스크롤 방지, 마지막 페이지 자동 순환 금지. 마지막 빌드가 끝난 뒤 다음 Space에서 다음 장 첫 빌드로 이동. 관객용 UI에 설정 폼·페이지 이동 버튼 없음. 발표자 준비/녹화는 별도 CLI·운영 화면으로.

## 2. 설명 설계 원칙과 공통 아키텍처

**고정 순서:** Hermes → Claude Code → PydanticAI → OpenAI Agents SDK → Claude Agent SDK → Google ADK → Microsoft Agent Framework → 종합. 기초 Agent 정의는 반복 강의하지 않는다. LangChain/LangGraph·Mistral AI Studio·vLLM/SGLang 내부는 별도 발표 범위라서 설명하지 않는다. vLLM은 모델 접속·이관에 필요한 만큼만 다룬다.

**공통 Lens:** `진입(User/Host)` → `Agent Loop/Runner/Harness` ↔ `LLM Provider/Model` → `Tool 실행기` ↔ `외부 데이터/OS`, 그리고 주변에 `Instructions/Context`, `Session/Memory`, `Policy/승인`, `실패/중단/재개`. **모델은 도구 호출을 요청할 뿐 직접 파일·DB를 조작하지 않는다.**

**마스터 노드 ID(각 섹션 첫 구조도에서 전부 등장, 이후 확대/강조):**

- `H-ARCH`: `H-IN`(CLI/Gateway/Cron) / `H-CORE`(AIAgent Loop) / `H-PROV` / `H-LLM` / `H-TOOLS`(Builtin/MCP/Plugin) / `H-STATE`(Session/Memory/Skill) / `H-POLICY`.
- `C-ARCH`: `C-IN`(CLI/IDE/Desktop) / `C-CORE`(Claude Code runtime) / `C-LLM` / `C-TOOLS`(Read/Edit/Bash/MCP) / `C-RULES`(CLAUDE.md/Skill/Memory) / `C-POLICY` / `C-DELEGATE`.
- `P-ARCH`: `P-APP`(Agent/Tool/Deps/Output 정의) / `P-CORE`(Internal Graph) / `P-LLM` / `P-HANDLER` / `P-OUT` / `P-APPSTATE` / 선택 `P-HARNESS`.
- `O-ARCH`: `O-APP` / `O-RUNNER` / `O-LLM` / `O-FUNCTOOLS` / `O-HANDOFF` / `O-GUARD` / `O-STATE`.
- `S-ARCH`: `S-HOST` / `S-SDK` / `S-CLI`(Claude Code runtime) / `S-LLM` / `S-TOOL` / `S-MCP-HOST` / `S-POLICY` / `S-STATE`.
- `G-ARCH`: `G-CALLER` / `G-RUNNER` / `G-AGENT` / `G-LLM` / `G-TOOLS` / `G-EVENT` / `G-SESSION` / 선택 `G-WORKFLOW`, `G-MEMORY`, `G-ARTIFACT`.
- `M-ARCH`: `M-APP` / `M-AGENT` / `M-MODEL` / `M-TOOL` / `M-MIDDLE` / `M-WORKFLOW` / 선택 `M-HARNESS` / `M-CHECKPOINT`.

모든 구조도의 선에는 `요청`, `실행`, `Tool result`, `DB write`, `handoff`, `resume` 중 실제 의미를 붙이고, 모델·SDK·앱·운영 체제의 소유권을 한눈에 알 수 있게 한다. **모델 서버의 위치와 Agent 실행기의 위치는 별개 변수**다.

### 공통 교육용 예제(실제 제조 데이터 사용 금지)

- 합성 `LOT-A`, `BIN-X`, `snapshot_id='synthetic-v1'`. T1: 지정 기간 BIN-X `분자/분모 × 100` 비율 조회. T2: 같은 기간 측정값과 유효 SOP 버전 조회 후 **원인 후보/반례** 제시. T3: 시간 누수 없는 과거 데이터로 단순 예측/검증. 모든 수치·시간·Lot ID는 교육용.
- Tool 계약 예시: `get_bin_ratio(lot_id, start_utc, end_utc)`, `get_measurement(lot_id, metric, start_utc, end_utc)`, `get_sop(revision_or_time)`, `fit_baseline(train_cutoff_utc, target_period)`.
- Tool이 만든 계산값과 모델이 작성한 해석·가설은 서로 다른 데이터다. 지표의 정의/집계 분모/기간·타임존, SOP validity, 비시계열 누수를 체크한다.
- **데모 T1~T3는 읽기 전용**. T4 보고서 게시 승인은 별도의 **완전한 샌드박스 Mock**으로만 시험한다. 실제 파일·사내 DB·제조 설비 변경 절대 금지.

## 3. 기술 근거와 사실 검증 규칙

**공식 출처 인덱스(약칭은 각 페이지 끝에 붙임):**

| ID | 기술/확인할 경로 |
|---|---|
| BASE | 프로젝트 인계 기준 및 공통 Agent 모델(이 문서 내 명세) |
| H-ARCH | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/architecture.md |
| H-LOOP | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/agent-loop.md |
| H-PROMPT | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/prompt-assembly.md |
| H-SESSION | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/sessions.md |
| H-MEMORY | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/which-file-does-what.md |
| H-SKILL | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md |
| H-COMPACT | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/agent-loop.md (Compression and Persistence) |
| H-TOOLS | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/architecture.md (Tools Runtime) |
| H-SECURITY | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/agent-loop.md (Tool Execution) |
| H-GATEWAY | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/architecture.md (Gateway Message/Cron Job) |
| C | https://code.claude.com/docs/en/overview ; https://code.claude.com/docs/en/how-claude-code-works |
| C-MEM | https://code.claude.com/docs/en/memory ; https://code.claude.com/docs/en/skills |
| C-POLICY | https://code.claude.com/docs/en/permissions ; https://code.claude.com/docs/en/hooks ; https://code.claude.com/docs/en/sandboxing |
| C-SUB | https://code.claude.com/docs/en/sub-agents ; https://code.claude.com/docs/en/agent-teams |
| P-AGENT | https://pydantic.dev/docs/ai/core-concepts/agent/ |
| P-TOOLS | https://pydantic.dev/docs/ai/tools-toolsets/tools/ |
| P-OUTPUT | https://pydantic.dev/docs/ai/core-concepts/output/ |
| P-DEFER | https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools/ |
| P-SRC | https://github.com/pydantic/pydantic-ai (고정 태그의 내부 Graph 구현) |
| O | https://developers.openai.com/api/docs/guides/agents/sdk ; https://developers.openai.com/api/docs/guides/agents/running-agents |
| O-ORCH | https://developers.openai.com/api/docs/guides/agents/orchestration |
| O-GUARD | https://developers.openai.com/api/docs/guides/agents/guardrails-approvals |
| S | https://code.claude.com/docs/en/agent-sdk/overview ; https://code.claude.com/docs/en/agent-sdk/agent-loop |
| S-MCP | https://code.claude.com/docs/en/agent-sdk/custom-tools ; https://code.claude.com/docs/en/agent-sdk/permissions |
| G | https://adk.dev/runtime/ ; https://github.com/google/adk-python |
| G-WORKFLOW | https://adk.dev/agents/workflow-agents/ ; https://adk.dev/agents/multi-agents/ |
| M | https://learn.microsoft.com/en-us/agent-framework/overview/ |
| M-MIDDLE | https://learn.microsoft.com/en-us/agent-framework/agents/middleware/ |
| M-WORKFLOW | https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/ |
| DEPLOY | https://docs.vllm.ai/en/latest/features/tool_calling/ |
| DEMO | 이 문서의 실제 실행·Trace·검산 규칙. 실행 전에는 주장 근거가 아니라 구현 명세 |

**주의:** 위 링크는 출발점이며 문서 경로가 이동할 수 있다. Codex는 **실제로 열리는 URL과 설치 버전 소스**를 확인하고 바뀐 링크는 고친다. `main` 브랜치 내용과 이전 분석의 고정 태그를 혼용하지 않는다. 기존 조사의 버전 메모(Hermes 0.22.5, Claude Code CLI 2.1.314, PydanticAI 2.61.0, OpenAI Agents SDK 0.24.0, Claude Agent SDK 0.2.176, Google ADK 2.13.0, Microsoft AF python-1.24.0 등)는 **참고 기록이지 현재 최신판이 아님**. 존재하지 않는 Tag/클래스/함수는 추측하지 않는다.

주장 상태: `DOC_CONFIRMED / SOURCE_CONFIRMED / RUN_OBSERVED / DESIGN_ONLY / NOT_VERIFIED`. 화면에는 확정된 동작을 쓰고, 기능 플래그/모델 파서/버전 의존 사항은 노트에 조건을 표기한다. `참고 코드`는 API 형태 예시, `의사 코드`는 가상 로직, `실제 원문`은 소스 위치·해시·릴리스 태그, `실행 Trace`는 저장한 실제 로그와 증거가 있어야 한다.

---

## 4. 최종 슬라이드 60장: 화면 문구·도식·Space 전개·발표자 노트

**이하 각 슬라이드는 Codex가 실제로 제작할 페이지 원고다.** `화면` 문구는 화면에서 보이는 텍스트를 우선한 짧은 원고이며, `구조도`와 `전개`에 기술된 도형/관계/애니메이션은 실제 구현한다. `발표자`는 노트용 기술 설명으로, 화면에 통째로 넣지 않는다. 이 페이지의 모든 `Sxx`는 새 ID이고 끝의 `(기존 Syy)`는 이전 46장 설계에서 참고할 주제만 표시한다. 이전 파일을 읽지 않아도 현재 설명으로 만들 수 있다.

### S01 · 이번 세미나의 질문: Agent는 실제로 어떻게 돌아갈까?  
*섹션: 도입 / 기존 자료 대응: S01 / 기준 도식: 공통*

**화면:** Agent의 정의가 아닌 실제 동작 원리를 살펴본다 · 모델·런타임·도구·상태 저장을 분리해 본다 · 완성형 Agent와 개발용 SDK의 선택 기준을 이해한다

**구조도:** 화면 중앙에 사용자→Agent Runtime↔LLM→Tool→상태 저장의 5개 노드. 모델은 파랑, 실행기는 보라, 도구는 초록. 아래 Harness/SDK 두 갈래를 얇은 띠로 구분.

**Space 전개:** 질문과 공통 5개 노드 → LLM의 요청과 Runtime 실행을 다른 색 화살표로 구분 → Harness와 SDK의 선택이라는 발표 목표 노출

**발표자:** 1차에서 Agent·Tool Calling 개념은 학습했다. 오늘은 누가 모델에 요청하고, 누구의 코드가 Tool을 실행하며, 다음 턴에 무엇이 남는지 따라간다. 핵심은 제품 기능 나열이 아니라 실제 실행 구조다.

**출처 키:** `BASE`

### S02 · 같은 Agent라도 어디까지 만들어져 있느냐가 다르다  
*섹션: 도입 / 기존 자료 대응: S02 / 기준 도식: 공통*

**화면:** 완성형: Hermes · Claude Code · 개발형: PydanticAI · OpenAI Agents SDK · Google ADK · Microsoft Agent Framework · 특수 관계: Claude Agent SDK는 Claude Code의 실행 기능을 코드에서 사용

**구조도:** 왼쪽 완성형 제품 카드 2개, 오른쪽 개발형 4개와 Claude Agent SDK를 다른 모양 연결 카드로 표시. 상단에 사용자 운영 책임의 연속선; 절대적 양분이라는 문구는 쓰지 않는다.

**Space 전개:** Hermes·Claude Code 강조 → 개발형 프레임워크 묶음 등장 → Claude Agent SDK→Claude Code 런타임 연결

**발표자:** 프레임워크·SDK·Harness 명칭 자체보다 제공된 실행 루프와 개발자가 구현할 범위를 기준으로 이해한다. Microsoft에도 선택적 Harness가 존재하므로 무조건 SDK=맨바닥이란 뜻은 아니다.

**출처 키:** `BASE`, `S`, `C`, `M`

### S03 · 같은 사례로 보는 일곱 기술의 차이  
*섹션: 도입 / 기존 자료 대응: S03 / 기준 도식: 공통*

**화면:** 예제: 합성 LOT-A의 BIN-X 지표 조회 → 원인 후보 분석 → 단순 예측 · 공통 관찰: 입력 → 모델 판단 → Tool → 결과 → 기록 · 데모: Hermes와 PydanticAI에서 실제 실행 확인

**구조도:** 합성 자료 배지와 세 단계 T1~T3 타임라인. 우측 작은 비교 범주 `누가 루프를 소유? | 무엇을 개발? | 어떤 확장이 특기?`.

**Space 전개:** 합성 시나리오 → 관찰 지점 세 개 → 데모 두 위치

**발표자:** 실제 반도체 제조 데이터가 아닌 교육용 고정 CSV/SQLite만 사용한다. 모델이 만들어 낸 원인 설명은 검증된 인과관계가 아니라 가설임을 명시한다. 동일 작업을 여러 런타임에 통과시켜 차이를 시각화한다.

**출처 키:** `BASE`

### S04 · Hermes는 실행 루프가 이미 들어 있는 완성형 Agent다  
*섹션: Hermes / 기존 자료 대응: S04 / 기준 도식: H-ARCH*

**화면:** 입력 채널이 달라도 AIAgent 실행 흐름으로 모인다 · 모델 연결·Tool Dispatch·대화 기록을 런타임이 조정 · 개발자는 확장 도구·정책·실행 환경을 구성

**구조도:** 첫 Hermes 마스터 H-ARCH 완전 지도: CLI/Gateway/Cron → AIAgent → Provider ↔ Model; AIAgent ↔ Tool Registry/MCP/Plugin; 아래 Session DB/Memory/Skills; 위험 경로에 Approval/OS. Cron은 새로운 run 라인으로 분리.

**Space 전개:** 입력→AIAgent → Model 왕복 → Tool·기록·보안 영역 → 운영 접점 강조

**발표자:** 프롬프트만 던져 모델이 알아서 코드를 실행하는 것이 아니다. Hermes 런타임이 모델 응답의 구조를 해석하고 실제 Tool Handler에 전달한다. 완성형이라고 운영 정책이 자동 보장되는 것은 아니다.

**출처 키:** `H-ARCH`, `H-LOOP`

### S05 · 한 번의 사용자 요청은 이렇게 흘러간다  
*섹션: Hermes / 기존 자료 대응: S05 / 기준 도식: H-ARCH*

**화면:** ① 입력과 이전 대화로 모델 요청을 만든다 · ② 모델의 Tool Call을 실행하고 결과를 되돌린다 · ③ 최종 응답이 나올 때까지 필요한 만큼 반복한다

**구조도:** H-ARCH 확대. 좌→우 `User → AIAgent → LLM → Tool Call → Registry/Handler → Tool Result → LLM → Final`의 곡선 루프. 화살표마다 `모델이 요청`, `런타임이 실행` 표기.

**Space 전개:** 입력/메시지 준비 → 모델이 구조화된 Tool Call 반환 → Runtime Tool 실행/Tool Result 저장 → 모델 재호출 또는 종료

**발표자:** 일반 Agent Loop를 Hermes의 실행 관점으로 보여준다. `run_conversation()`이 사용자 턴을 처리하고, 내부 턴 모듈이 요청·응답·도구 분기를 담당한다. 모델이 호출을 제안하지만 파일·명령을 직접 실행하지는 않는다.

**코드/발췌 원칙:** Hermes 실제 공개 API 예시: `agent.chat("합성 LOT-A 지표 조회")` 또는 `agent.run_conversation(user_message="...")`. 개념 시퀀스는 의사 코드로 표시.

**출처 키:** `H-LOOP`

### S06 · Tool Call의 앞뒤에서 누가 무엇을 하는가?  
*섹션: Hermes / 기존 자료 대응: S05 / 기준 도식: H-ARCH*

**화면:** 모델: Tool 이름과 입력 인자 제안 · 런타임: 사용 가능 여부·권한 확인 후 Handler 실행 · 결과: Tool 메시지로 다시 모델 입력에 합류

**구조도:** 세로 스윔레인 `LLM / Hermes Runtime / Tool·OS`; example call `get_bin_ratio({lot_id:"LOT-A"})` → Read-only DB → `{"ratio":0.12,...}`. 값은 예시 표기. 아래 허가되지 않은 Tool 분기 표시.

**Space 전개:** 모델 요청 → 정책/Handler 경계 → 결과 메시지 → 허가 실패는 실제 실행이 아님

**발표자:** 모델은 요청자이고 Hermes의 코드는 집행자다. Tool Schema는 모델에 기능을 설명하지만 실제 구현·인증·DB 권한은 Tool 측에 있다. 단순히 JSON 형태의 문장이 나왔다고 Tool Calling이 된 것은 아니다.

**출처 키:** `H-LOOP`, `H-TOOLS`

### S07 · 실제 코드에서는 Loop와 Tool Dispatch가 분리되어 있다  
*섹션: Hermes / 기존 자료 대응: S06 / 기준 도식: H-ARCH*

**화면:** `run_agent.py`: 외부에서 쓰는 AIAgent 접점 · `agent/conversation_loop.py`: 대화 반복과 분기 · `agent/tool_executor.py`·`model_tools.py`: Tool 실행 경계

**구조도:** 왼쪽 8줄 의사 코드, 오른쪽 실제 파일 경로 3개 카드; 소스 라인 범위를 검증해 링크하도록. 실제 코드가 짧게 맞으면 해당 릴리스의 원문 6~12줄로 교체할 수 있다.

**Space 전개:** 퍼블릭 API와 Loop의 위치 → 응답의 Tool Calls 검사 → Executor로 위임 → 다음 Iteration으로 복귀

**발표자:** 소스의 구조를 읽는 법을 보여준다. 최신 소스는 모듈로 나뉘므로 과거 모든 로직이 run_agent.py 한 파일에 있다고 설명하지 않는다. 실제 코드 인용은 사용한 태그·라인을 명시하고, 의사 코드는 반드시 표시한다.

**코드/발췌 원칙:** ```python
# [개념 의사 코드 / 실제 소스 발췌 아님]
while within_budget:
    response = call_model(messages, tool_schemas)
    if response.tool_calls:
        for call in response.tool_calls:
            result = dispatch_tool(call)
            messages.append(make_tool_result(call.id, result))
        continue
    return response.final_text
```

**출처 키:** `H-ARCH`, `H-LOOP`

### S08 · Tool 실행이 실패하면 Loop는 어떻게 대응할까?  
*섹션: Hermes / 기존 자료 대응: S05 / 기준 도식: H-ARCH*

**화면:** 인자 오류·접근 거부·Tool 예외를 구분 · Runtime은 실패 결과를 기록하거나 실행을 중단 · 모델 재질문·재시도는 정책과 남은 반복 예산에 따름

**구조도:** 한 개 Tool Call에서 3가지 분기: 정상 결과→다시 모델, 인자/도구 에러→Tool Result/재검토, 강제 승인 거부·취소→중단. 재시도가 자동 동일 DB 쓰기로 이어지는 형태를 금지.

**Space 전개:** Tool 시작 → 오류 유형 분기 → Runtime 처리와 모델 재검토

**발표자:** Agent가 Tool 오류를 받으면 모델이 수정된 인자로 다시 시도할 수 있지만, 모든 오류가 자동 복구되지는 않는다. 안전상 중단과 평범한 예외를 분리한다. 외부 부작용이 있는 Tool을 무작정 반복 호출하면 중복 실행 위험이 있다.

**출처 키:** `H-LOOP`, `H-SECURITY`

### S09 · 모델은 실제로 무엇을 보고 판단할까?  
*섹션: Hermes / 기존 자료 대응: S06 / 기준 도식: H-ARCH*

**화면:** System Prompt + 대화 History + 사용 가능한 Tool Schema · Memory/Skill은 필요 시 프롬프트나 Tool을 통해 반영 · DB 전체와 실제 OS 상태가 자동으로 전달되지는 않는다

**구조도:** 세 개 프롬프트 층 카드 `stable/context/volatile` → 모델 요청. 측면에 모델이 보지 못하는 OS/DB 원본·Credential 저장소를 점선 경계로 배치.

**Space 전개:** Prompt 층 → History와 Tool Schema 합류 → 모델에 보이지 않는 실행 상태 강조

**발표자:** Hermes는 시스템 프롬프트를 단계별로 조립하고, 세션에서 재사용 가능한 스냅샷과 API 호출 시 임시 맥락을 구분한다. 메모리 파일은 저장된 사실이나 지침이지 LLM의 자체 파라미터 업데이트가 아니다.

**출처 키:** `H-PROMPT`, `H-SESSION`

### S10 · 대화가 길어지면 Cache와 Compaction은 다른 일을 한다  
*섹션: Hermes / 기존 자료 대응: S07 / 기준 도식: H-ARCH*

**화면:** Prefix Cache: 같은 프롬프트 접두부 연산을 재활용(지원 모델·제공자 조건) · Compaction: 긴 History 일부를 요약해 입력 표현을 축소 · Cache는 기억을 삭제하지 않고, 요약은 정보 손실 가능

**구조도:** 위아래 두 타임라인. 위 Prefix 동일 앞부분을 파란 막대로, 아래 10개 메시지→요약+최근 N개 메시지로 축약한 형태. 출처 버전별 차이는 노트에.

**Space 전개:** 긴 History 문제 → Prefix Cache 동작 → Compaction과 손실 위험

**발표자:** Cache는 전송된 이력을 줄이는 기능이 아니다. Compression은 입력 History 자체를 요약·재배치하므로 증거 누락 위험이 있다. 실제 트리거 임계값이나 보호 개수는 설치 버전에서 확인한 값만 발표에 쓴다.

**출처 키:** `H-COMPACT`

### S11 · Session·Memory·Skill은 서로 다른 저장 구조다  
*섹션: Hermes / 기존 자료 대응: S08 / 기준 도식: H-ARCH*

**화면:** Session: 그 대화에서 실제 오간 메시지·Tool 결과 · Memory: 다음에도 유용한 사실·선호·메모 · Skill: 반복 가능한 절차·작업법

**구조도:** 3단 적층 카드: SQLite+FTS5/대화 검색, MEMORY.md·USER.md/사실, Skills/절차. 화살표는 Memory 또는 Skill이 필요 시 다음 프롬프트/Tool에 반영되는 경우에만.

**Space 전개:** Session 소개 → Memory 소개 → Skill 소개 및 비교

**발표자:** Session DB, 기억 파일, Skill을 모두 장기 메모리라고 부르면 안 된다. 과거 대화 검색은 FTS5를 사용하는 사례가 있으나 매번 임베딩 RAG가 작동한다고 주장하면 오류다. 어느 자료가 모델에 들어가는지는 시점과 설정에 따라 달라진다.

**출처 키:** `H-SESSION`, `H-MEMORY`, `H-SKILL`

### S12 · Hermes의 특색: 경험을 다음 실행에 반영하는 구조  
*섹션: Hermes / 기존 자료 대응: S08 / 기준 도식: H-ARCH*

**화면:** 대화 중 얻은 유용한 사실을 Memory로 보존 · 반복 작업 절차를 Skill로 정리해 재사용 · 검색·저장·로드는 명시적 경로와 조건을 거친다

**구조도:** `사용→발견→Memory 또는 Skill 생성/수정→다음 요청에서 활용` 순환 고리. LLM 모델 가중치 변경과는 분리해 작은 X 마크.

**Space 전개:** 발견 → Memory/Skill 저장 → 다음 실행에 적용 → 학습(재학습)과 구별

**발표자:** Hermes의 자기개선이라는 표현은 경험의 외부 기록과 절차 업데이트를 의미한다. 모델의 파라미터 자체를 매 턴 fine-tuning한다고 오해하지 않게 설명한다. 자동 작성·승인 여부는 해당 설정에 따라 달라지며 실제 검증한다.

**출처 키:** `H-MEMORY`, `H-SKILL`

### S13 · Tool·MCP·Plugin은 같은 확장이 아니다  
*섹션: Hermes / 기존 자료 대응: S09 / 기준 도식: H-ARCH*

**화면:** Tool: Agent가 호출하는 작업 단위 · MCP: 외부 Tool/Resource를 연결하는 통신 규약 · Plugin: Tool·Hook 등 런타임 확장 등록

**구조도:** H-ARCH 확대. 내부 Tool Registry에 Built-in Tool, MCP client↔외부 MCP server, Plugin→Registry/Hook의 서로 다른 3색 경로. Code source를 LLM에 통째로 전달하는 화살표 금지.

**Space 전개:** Built-in Tool → MCP 왕복 → Plugin·Hook 경계

**발표자:** MCP는 실행 계약이지 모델이 직접 서버를 호출하는 기능이 아니다. Hermes가 MCP 클라이언트를 통해 요청하고 실제 서버의 실행은 서버 쪽에서 일어난다. Plugin은 Tool 등록뿐 아니라 Hook으로 생명주기에 관여할 수 있다.

**출처 키:** `H-TOOLS`, `H-ARCH`

### S14 · Guardrail은 모델의 예절이 아니라 실행 경계에 둔다  
*섹션: Hermes / 기존 자료 대응: S10 / 기준 도식: H-ARCH*

**화면:** 모델의 지시 준수만으로 위험 Tool을 막을 수 없다 · Tool Dispatch 전 승인과 실행 환경 권한이 중요 · 실제 DB 읽기/쓰기 권한은 운영 환경에서 강제

**구조도:** LLM→요청→위험도 평가/승인→Tool Handler→DB ACL 연속 게이트. 불허 시 Tool 호출 실패 반환. OS/DB 권한은 Tool Handler 바깥 이중 벽.

**Space 전개:** 요청 → 허용/승인 → 실제 권한 → 거부와 Tool 에러

**발표자:** Hermes의 위험 명령 승인 기능이 모든 도구와 외부 시스템의 보안을 보장한다고 확대하지 않는다. 승인과 인증/인가, 실패 처리, Tool 결과 기록은 다른 단계다. 합성 데모는 읽기 전용을 기본으로 한다.

**출처 키:** `H-SECURITY`

### S15 · Tool 병렬과 Subagent 위임은 구조적으로 다르다  
*섹션: Hermes / 기존 자료 대응: S11 / 기준 도식: H-ARCH*

**화면:** 병렬 Tool: 하나의 Agent 턴에서 여러 Handler 호출 · Subagent: 별도 실행 문맥을 가진 하위 Agent에 작업 위임 · 반환 결과·맥락·공유 자원 및 충돌 위험이 달라진다

**구조도:** 윗줄 LLM→2 Tools→동일 Parent Loop. 아랫줄 Parent→Child Agent Loop↔LLM/Tools→Summary→Parent. Shared filesystem은 별도 점선 경계.

**Space 전개:** 병렬 Tool → Subagent 생성 → Parent 복귀와 공유자원 주의

**발표자:** 병렬 Tool은 호출 단위 동시성이고 subagent는 별도의 모델-도구 반복 수명을 만든다. 컨텍스트가 별개여도 파일·OS·DB까지 자동 격리되지는 않는다. 같은 데이터 읽기는 합성 예제로 보여준다.

**출처 키:** `H-LOOP`, `H-TOOLS`

### S16 · CLI·Gateway·Cron은 실행을 시작하는 방식이 다르다  
*섹션: Hermes / 기존 자료 대응: S12 / 기준 도식: H-ARCH*

**화면:** CLI: 사용자의 직접 대화 · Gateway: 플랫폼 메시지를 인증·세션 라우팅 · Cron: 정해진 시각에 새로운 작업 실행

**구조도:** 세 레인 입력 경로가 AIAgent에 모이지만 Gateway의 사용자/세션 바인딩과 Cron의 새 실행을 별도 점선 박스로 표시.

**Space 전개:** CLI 경로 → Gateway 경로 → Cron 경로 및 기존 대화와의 차이

**발표자:** 입력 채널은 하나의 실행 엔진 위에서 돌아갈 수 있으나 각 실행의 권한과 History는 동일하다고 가정할 수 없다. Cron이 기존 사용자의 대화 한 턴을 그대로 재생한다고 단정하지 않는다.

**출처 키:** `H-ARCH`, `H-GATEWAY`

### S17 · Hermes를 활용하면 무엇을 직접 만들지 않아도 될까?  
*섹션: Hermes / 기존 자료 대응: S13 / 기준 도식: H-ARCH*

**화면:** 이미 있는 것: 대화 Loop·기본 Tool·세션·다중 진입점 · 설정/확장할 것: 모델·Tool·Skill·플랫폼·승인 규칙 · 직접 책임질 것: 데이터 접근권·업무 검증·운영 장애

**구조도:** 좌 `Hermes 제공`, 우 `프로젝트 책임` 두 리스트와 가운데 합성 LOT 쿼리 Tool 연결.

**Space 전개:** Hermes 제공 → 추가 개발/설정 → 도입 전 운영 책임

**발표자:** 직접 모든 Agent Loop를 구현하지 않고 시작할 수 있다. 대신 사내 데이터용 읽기 전용 도구, 사용자 권한, 로그 정제, 재현 가능한 분석 데이터는 애플리케이션 담당자가 만들거나 구성해야 한다.

**출처 키:** `H-ARCH`

### S18 · 데모 1: 요청 하나가 실제 Tool 실행까지 가는지 보자  
*섹션: Hermes / 기존 자료 대응: S13 / 기준 도식: H-ARCH*

**화면:** T1: 합성 LOT-A의 BIN-X 비율 조회 · 관찰: 모델 요청 → 실제 Tool → 결과 메시지 → 최종 요약 · 동일 입력·동일 합성 DB로 실행 Trace 저장

**구조도:** 데모 시작 연결 카드: H-ARCH 미니맵 + 별도 viewer URL / `event_id` 매핑. 시연 순서 외의 클릭 UI 없음.

**Space 전개:** 질문과 데이터 스냅샷 → 실제 요청·Tool Call 이벤트 → 결과·반환 기록 → 데모 viewer로 이동하는 운영 안내

**발표자:** 실제 실행 Trace를 재생할 때는 모델 출력 텍스트, Tool 인자, 실제 DB 결과와 최종 응답을 구별한다. 로컬/대상에서 아직 실행하지 못했다면 ‘실행 전’으로 표시하고 합성 예시를 실제 관측이라고 표기하지 않는다.

**출처 키:** `H-LOOP`, `DEMO`

### S19 · 데모 1에서 꼭 확인할 네 가지  
*섹션: Hermes / 기존 자료 대응: S14 / 기준 도식: H-ARCH*

**화면:** Tool Call ID와 실제 Tool 결과가 맞는가? · 모델이 오류를 받으면 어떻게 다음 턴을 만들었나? · 세션·Memory 중 무엇이 실제 저장되었나?

**구조도:** 별도 Trace viewer의 4개 예시 캡처 슬롯: 요청/Tool/result/history. 저장된 이벤트가 없으면 Placeholder `[미검증]`를 명시.

**Space 전개:** 모델 요청 → 실제 핸들러 → History 갱신 → 결론·오류 경계

**발표자:** T1과 T2의 실제 순서, 실패도 관찰된 순서로만 기술한다. 시험에서 발생하지 않은 거부/재시도는 별도 계획 샌드박스 테스트로만 표현한다. 도메인 계산의 사실성은 모델이 아니라 결정적 Tool 결과로 검산한다.

**출처 키:** `DEMO`, `H-SESSION`

### S20 · Hermes에서 가져갈 결론  
*섹션: Hermes / 기존 자료 대응: S14 / 기준 도식: H-ARCH*

**화면:** 구현된 Harness를 빠르게 활용할 수 있다 · Loop·Prompt·Tool·Memory·Gateway의 책임 경계가 분명하다 · 품질·권한·데이터 진실성은 운영 설계가 결정한다

**구조도:** H-ARCH 전체 재등장. 이미 설명한 노드는 회색, `제공됨`과 `직접 설계`만 색 윤곽선. 다음 Claude Code로 향하는 연결 화살표.

**Space 전개:** 완성형 장점 → 책임 경계 → Claude Code와 비교 질문

**발표자:** 어떤 작업이 Agent 자체에서 진행되고 어떤 부분이 외부 DB/서비스의 몫인지를 정리한다. 이제 유사하게 완성형인 Claude Code가 코딩 환경에 맞게 무엇을 더 잘 묶는지 보겠다고 자연스럽게 연결한다.

**출처 키:** `H-ARCH`

### S21 · Claude Code도 기본 Agent Loop는 Hermes와 닮았다  
*섹션: Claude Code / 기존 자료 대응: S15 / 기준 도식: C-ARCH*

**화면:** 공통: LLM ↔ Tool 호출 반복, Context/History, 실행 정책 · 공통: 파일·명령 실행은 Runtime/Tool이 담당 · 다음 질문: 코딩 작업에서 Claude Code만의 강점은?

**구조도:** 좌 Hermes 미니맵, 우 Claude Code 마스터 C-ARCH. 공통 구성 노드를 동일 모양으로 정렬하고 차별 영역(IDE, project rules, edit/test workflow)만 강조.

**Space 전개:** 공통 Loop 4노드 → Tool/상태 공통점 → 차별 영역만 보라 테두리

**발표자:** 청중은 Hermes Loop를 방금 봤으므로 처음부터 다시 설명하지 않는다. Claude Code는 코딩 Harness를 제공하지만 내부 엔진 전체의 구현 세부는 공개 문서 범위를 넘어서 단정하지 않는다.

**출처 키:** `C`, `CC`

### S22 · Claude Code의 주 무대는 실제 개발 작업 환경이다  
*섹션: Claude Code / 기존 자료 대응: S15 / 기준 도식: C-ARCH*

**화면:** 코드베이스 탐색 → 파일 수정 → 명령/테스트 실행 · CLI·IDE·Desktop 등 개발 접점과 연결 · 여러 파일·프로젝트 규칙을 함께 고려

**구조도:** C-ARCH 전체 지도: Terminal/IDE→Claude Code Harness↔LLM; Read/Edit/Bash/MCP; CLAUDE.md/Skills/Memory; Permissions/Hooks/Sandbox; Subagents. 기능별 소유권 라벨.

**Space 전개:** 개발 요청 → 탐색·수정·시험 실행 → 도구/규칙/정책 → 별도 내부 구현 비공개 경계

**발표자:** 차별점은 Agent의 정의가 아니라 코드 작업을 위해 도구와 프로젝트 문맥, 테스트·git·IDE를 통합한 실행 환경이다. 단순 채팅보다 실제 저장소 변경과 검증에 초점을 둔다.

**출처 키:** `C`

### S23 · CLAUDE.md·Skill·Memory는 언제 도움이 될까?  
*섹션: Claude Code / 기존 자료 대응: S16 / 기준 도식: C-ARCH*

**화면:** CLAUDE.md: 프로젝트별 지속 지시·규칙 · Skill: 특정 작업에서 불러 쓰는 절차 · Memory: 이전 작업에서 남긴 유용한 맥락

**구조도:** 프로젝트 트리 아이콘과 3개 다른 접근 패턴(상시 지시/필요시 로드/자동 저장·검색). 모두 매번 전문이 주입된다고 표시하지 않는다.

**Space 전개:** 규칙 파일 → Skill → Memory와 구분

**발표자:** 해당 파일과 기능의 우선순위·로드 경로는 버전/설정에 따라 검증한다. 규칙을 기록했다고 그 자체로 OS 수준 실행 제한이 걸리는 것은 아니다. 코딩 작업 품질의 반복성을 만드는 방법이라는 점에 집중한다.

**출처 키:** `C-MEM`

### S24 · Permissions·Hooks·Sandbox를 함께 써야 실행을 통제한다  
*섹션: Claude Code / 기존 자료 대응: S17 / 기준 도식: C-ARCH*

**화면:** Permissions: Tool 호출 허용·승인 정책 · Hooks: 정해진 지점에서 사용자 코드 개입 · Sandbox: 실제 실행 환경의 접근 범위 제한

**구조도:** `모델 요청 → Permissions → Hooks(적용 지점별) → Sandbox/OS → Tool` 계층도. Hooks가 항상 Permission 앞뒤 동일하게 호출된다고 고정하지 말고 종류별 위치 노트 표시.

**Space 전개:** Permission 판단 → Hook 개입 → Sandbox/OS 경계

**발표자:** 프롬프트로 “삭제하지 마”라고 하는 것과 실제 권한 차단은 다르다. Hook은 이벤트마다 반환 코드·실행 방식이 다를 수 있고 샌드박스도 플랫폼/설정 의존적이다. 해당 버전 공식 문서에서 실행 순서를 확인한 경우에만 정확한 순서로 표시한다.

**출처 키:** `C-POLICY`

### S25 · Subagent와 Agent Teams는 협업 방식이 다르다  
*섹션: Claude Code / 기존 자료 대응: S18 / 기준 도식: C-ARCH*

**화면:** Subagent: 특정 역할에 작업을 맡기고 결과를 부모에 전달 · Agent Teams: 구성원 간 조정·공유 작업 관리가 핵심 · 독립 Context가 곧 독립 파일 시스템은 아니다

**구조도:** 윗줄 Parent→Subagent→Summary; 아랫줄 Team lead ↔ 팀원 2명/공유 태스크. 모델 비용·충돌 위험 아이콘.

**Space 전개:** Subagent 위임 → Teams 구조 → 동시 편집과 권한 관리 주의

**발표자:** 작업을 분담해 코딩 생산성을 높이지만 파일/브랜치/공유 상태 충돌을 자동으로 막아주지는 않는다. Teams 지원 여부는 제품 기능 플래그·버전·환경에서 확인하고 미지원이면 그 조건을 밝힌다.

**출처 키:** `C-SUB`

### S26 · Claude Code의 대표 활용: 기획에서 테스트까지  
*섹션: Claude Code / 기존 자료 대응: S18 / 기준 도식: C-ARCH*

**화면:** 요구 분석 → 변경 계획 → 코드 수정 → 테스트 → 검토 · 역할별 Subagent로 분담하고 주 실행에서 통합 · Hooks/CI/승인으로 품질 관문 배치

**구조도:** 4단 코드 워크플로와 중간 HITL gate, 서브에이전트 분기 후 합류. 구체적 개발자/검토자 역할 카드를 강조.

**Space 전개:** 작업 계획 → 수정·검증 → 권한·검토 및 회고

**발표자:** 코딩 중심 환경에서의 장점을 보여준다. 전자동 성공이나 모든 코드 정확도를 보장하지 않으며 실제 diff와 테스트 결과는 개발자가 검사한다. Hermes와 같은 구조를 다시 강의하지 않는다.

**출처 키:** `C`

### S27 · Hermes와 Claude Code는 어디서 선택 기준이 갈릴까?  
*섹션: Claude Code / 기존 자료 대응: S19 / 기준 도식: C-ARCH*

**화면:** Hermes: 다채널·주기 작업·Memory/Skill 운용에 강점 · Claude Code: 저장소 탐색·수정·테스트·개발 도구 통합 · 공통: 모델 외부의 실행·권한·상태 설계가 중요

**구조도:** 동일 축 2열 비교: 주된 진입점, 작업 단위, 확장/정책, 직접 개발 범위. 승자 배지/성능 순위 금지.

**Space 전개:** 공통점 빠른 복기 → 차별점만 비교 → 상황별 선택 예시

**발표자:** 비교의 핵심은 어떤 Agent가 더 똑똑한지가 아니다. 반복 운영·멀티채널 작업과 저장소 기반 개발 업무의 주 무대가 다르다. 둘 모두 LLM 제공자와 실행 환경을 구성해야 한다.

**출처 키:** `H-ARCH`, `C`

### S28 · 완성형에서 SDK로 넘어가면 무엇을 더 만들게 될까?  
*섹션: Claude Code / 기존 자료 대응: S19 / 기준 도식: C-ARCH*

**화면:** 완성형: 기존 앱에서 실행 루프·도구를 주로 설정/확장 · SDK: 애플리케이션 코드가 Agent 정의·Tool·상태 결합 · PydanticAI는 이 경계를 가장 먼저 보여줄 사례

**구조도:** Hermes/Claude Code의 통합 Runtime 카드가 부품 `Agent/Tool/State/API/Policy` 형태로 분해되어 개발자 앱으로 이동하는 전환 애니메이션.

**Space 전개:** 완성된 런타임 → 앱 소유의 구성요소 → PydanticAI 도입

**발표자:** 개발형 SDK도 Agent Loop의 상당 부분을 구현해주므로 “Loop를 전부 직접 짜야 한다”는 뜻이 아니다. 핵심은 도메인 애플리케이션, 저장·API·정책 조립과 운영 책임이 더 선명해진다는 것이다.

**출처 키:** `P`, `O`

### S29 · PydanticAI는 Agent를 Python 애플리케이션 안에 만든다  
*섹션: PydanticAI / 기존 자료 대응: S20 / 기준 도식: P-ARCH*

**화면:** Pydantic: 데이터 구조·검증 라이브러리 · PydanticAI Core: 실행 Loop·Tool·Output·Retry 제공 · 선택 Harness/Capability는 Core와 별도 계층

**구조도:** `Pydantic(타입)` → `PydanticAI Core(Agent Loop)` → `(선택) Harness`를 각기 다른 경계로 그린 계층도. Core만으로 업무 Agent 구현 가능 표시.

**Space 전개:** Pydantic 구분 → PydanticAI Core 추가 → 선택 Harness 구분

**발표자:** Pydantic 자체는 Agent가 아니고 PydanticAI Core는 모델 호출과 Tool Loop를 제공한다. 선택 Harness가 있다는 이유로 모든 PydanticAI Agent가 컴퓨터 사용 Agent로 실행되는 것은 아니다.

**출처 키:** `P-AGENT`, `P-OUTPUT`

### S30 · 개발자가 작성하는 코드는 어디까지일까?  
*섹션: PydanticAI / 기존 자료 대응: S21 / 기준 도식: P-ARCH*

**화면:** 직접: Agent 설정·도메인 Tool 함수·Deps·Output 타입 · Core 제공: 모델 왕복·Tool 인자 처리·검증·재시도·종료 · 별도 구현: API 서버·DB 권한·업무 규칙·영속화

**구조도:** P-ARCH 전체 지도. 파란선 `app-owned`에 Agent 선언/Deps/DB, 보라선 `Core`에 내부 Graph/Tool Manager/output, 외부 Provider Model. 읽기 전용 Lot Tool 예시 연결.

**Space 전개:** 개발자 작성 블록 → Core 내부 실행 → 운영 애플리케이션 책임

**발표자:** 화면상 개발자가 얼마나 코딩해야 하는지 한 번에 전달한다. 실제 모델 클라이언트 생성과 Provider adapter는 버전별로 다르므로 사용하는 릴리스 기준으로 코드를 확인한다.

**출처 키:** `P-AGENT`, `P-TOOLS`

### S31 · 최소 Python 코드: Agent·Tool·Output  
*섹션: PydanticAI / 기존 자료 대응: S21 / 기준 도식: P-ARCH*

**화면:** Agent 인스턴스에 모델·Instructions·Output 타입 등록 · `@agent.tool`로 실행 함수를 등록 · `agent.run()` 결과를 앱에서 받아 사용

**구조도:** 왼쪽 실제 코드 14줄 이하, 오른쪽 `앱 선언 → Core Loop → Tool → Result` 미니 다이어그램. Tool에서는 합성 fixture만 조회하도록.

**Space 전개:** Agent/타입 선언 → Tool 함수 등록 → Run 호출/결과 처리

**발표자:** 예시 코드는 프로젝트가 채택한 PydanticAI 버전에서 직접 실행·수정한 뒤에만 `[실행 가능]` 표기를 붙인다. 아래 샘플은 개념을 보여주는 것이고 모델 및 인증 설정은 후속 환경 설정에서 주입한다. 타입 검증은 분석 결과의 사실성 검증이 아니다.

**코드/발췌 원칙:** ```python
# [API 형태 예시] 설치 버전과 모델 설정에 맞춰 실행 검증 필요
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

class BinResult(BaseModel):
    lot_id: str
    ratio: float

agent = Agent("openai:MODEL_ALIAS", output_type=BinResult)

@agent.tool
async def get_bin_ratio(ctx: RunContext[None], lot_id: str) -> dict:
    return await read_synthetic_fixture(lot_id)  # 사용자 구현 함수

result = await agent.run("합성 LOT-A BIN-X 비율 조회")
print(result.output)
```

**출처 키:** `P-AGENT`, `P-TOOLS`

### S32 · Core 안에서는 어떤 순서로 실행될까?  
*섹션: PydanticAI / 기존 자료 대응: S22 / 기준 도식: P-ARCH*

**화면:** 시작: UserPromptNode에서 입력을 준비 · 중간: ModelRequestNode ↔ CallToolsNode 반복 · 종료: 검증된 최종 Output 또는 에러/제한

**구조도:** 내부 Graph의 주요 Node 3개와 End. 조건 화살표 `tool?`, `final output?`, `retry/error?`. 앱의 외부 workflow graph와 명시적으로 분리.

**Space 전개:** UserPrompt → ModelRequest → CallTools → End/Retry

**발표자:** 이 노드 명칭은 해당 공개 구현에서 쓰이는 내부 Graph 설명이다. `pydantic-graph`로 개발자가 별도 workflow를 만든 것과 혼동하지 않는다. 모델 응답에 따라 Tool 단계가 생략되거나 반복된다.

**출처 키:** `P-AGENT`, `P-SRC`

### S33 · Instructions·Deps·History는 모델에 보이는 범위가 다르다  
*섹션: PydanticAI / 기존 자료 대응: S23 / 기준 도식: P-ARCH*

**화면:** Instructions: 모델에 전달할 지침 · Deps: Tool이 접근하는 Python 런타임 의존성 · History: 앱이 전달/관리하는 대화 문맥

**구조도:** 왼쪽 모델 입력 상자(Instructions, 전달 History, Tool Schema)와 오른쪽 런타임 Deps(DB client/권한 Context). Deps에서 모델로 직선 화살표 금지.

**Space 전개:** 모델 입력 → 런타임 Deps → DB 연결·History 유지 책임

**발표자:** `RunContext.deps`의 DB 핸들은 모델 프롬프트로 자동 직렬화되지 않는다. Tool이 결과를 반환한 뒤 해당 텍스트/값만 모델에 노출될 수 있다. 대화 History를 DB에 장기 영속화하는 것은 앱 정책에 달려 있다.

**출처 키:** `P-AGENT`, `P-TOOLS`

### S34 · Tool은 Schema만 만들면 끝나지 않는다  
*섹션: PydanticAI / 기존 자료 대응: S24 / 기준 도식: P-ARCH*

**화면:** 모델 요청 인자를 Python 함수 인자로 검증 · Tool 함수가 실제 읽기/계산을 수행 · 실패·재시도·권한 거부는 별도 경로

**구조도:** `JSON schema → model tool call → validation → Python function → result` 횡단 파이프라인; 입력 오류는 검증 루프로, 권한 부족은 실제 실행 차단으로 분기.

**Space 전개:** Schema 제공 → 입력 검증 → 실제 함수 실행 → 실패 분기

**발표자:** Pydantic 기반 검증은 타입과 형태를 보장하지만, 특정 Lot을 볼 권한과 계산의 참인지를 보장하지 않는다. Tool 안에 권한 검증과 결정적 계산을 구현해야 한다.

**출처 키:** `P-TOOLS`

### S35 · Output 타입은 왜 도움이 되나?  
*섹션: PydanticAI / 기존 자료 대응: S25 / 기준 도식: P-ARCH*

**화면:** 자연어 대신 정해진 `BinResult` 구조로 받기 · 모델 출력의 형식·타입 검증과 재시도 지원 · 유효한 JSON도 도메인 정답과는 별개

**구조도:** 왼쪽 `"12%쯤..."` 자유 텍스트, 오른쪽 `lot_id/ratio/snapshot_id` Pydantic 구조. Schema 실패 화살표→Retry.

**Space 전개:** 자유 형식 → 타입 지정 출력 → 검증·재시도 및 한계

**발표자:** Output 방식은 Tool 기반/Native JSON Schema/Prompted 등 모델·설정에 따라 달라진다. 모든 제공자·vLLM 서버가 같은 방식을 자동 지원한다고 단정하지 않는다.

**출처 키:** `P-OUTPUT`

### S36 · 종료 시점과 남은 Tool Call은 중요한 정책이다  
*섹션: PydanticAI / 기존 자료 대응: S26 / 기준 도식: P-ARCH*

**화면:** 모델이 최종 Output과 Tool Call을 함께 낼 수 있다 · `end_strategy` 등 정책에 따라 Tool 처리 경로가 달라진다 · 부작용 Tool은 승인·중복방지·재개 전략이 별도로 필요

**구조도:** 하나의 모델 응답이 `final output + read-only lookup + write report`를 동시에 포함한 경우의 2갈래 결정 트리. 정확한 `early/exhaustive` 결과는 코드·공식 문서에 맞춰 검증하여 기재.

**Space 전개:** 동일 응답에서 두 신호 → 종료 정책 분기 → Side effect 유의사항

**발표자:** `early`가 무조건 모든 Tool을 실행한다거나 `exhaustive`가 정확히 한 번 쓰기 보장을 제공한다고 설명하면 안 된다. 함수 Tool과 Output Tool의 유형, streaming에서 종료를 발견하는 시점에 따라 결과가 바뀔 수 있다. 데모는 읽기 전용 경로를 기본으로 하고 부작용은 Mock에서 시험한다.

**출처 키:** `P-OUTPUT`

### S37 · 병렬 Tool 실행과 안전한 순서는 다르다  
*섹션: PydanticAI / 기존 자료 대응: S26 / 기준 도식: P-ARCH*

**화면:** 서로 독립인 읽기 Tool은 병렬 처리 가능 · 순서가 중요한 Tool은 직렬화·동기화가 필요 · 비결정적 완료 순서와 결과 해석은 분리

**구조도:** 두 read-only 함수가 병렬 출발해 Join하는 도식과 `승인→게시`가 순서 의존적인 직렬 도식. 런타임/프로바이더/버전 설정으로 동작 검증 후 표시.

**Space 전개:** 병렬 조회 → 결과 합류 → 순서 필요한 Tool

**발표자:** ‘병렬 Tool Call을 모델이 생성’과 ‘Python 실행이 실제 병렬’은 다른 사실이다. 설치 버전의 설정과 측정 로그를 통해 실제 병렬 수행 여부를 확인한다.

**출처 키:** `P-TOOLS`

### S38 · `run`·`run_sync`·`run_stream`은 실행 관찰 방식이 다르다  
*섹션: PydanticAI / 기존 자료 대응: S27 / 기준 도식: P-ARCH*

**화면:** `run`: async 최종 결과 · `run_sync`: 동기 코드에서 실행 · `run_stream`: 생성 중 결과를 스트리밍

**구조도:** 세 개 API 카드와 아래 내부 Core Loop 공통 박스. 실행 방식과 Tool 정책을 독립 축으로 두고 API 하나씩만 설명.

**Space 전개:** run → run_sync → run_stream 및 주의

**발표자:** 시그니처·스트리밍 출력 확정 조건은 버전 의존적이다. 발표 본문에는 가장 자주 쓰는 세 가지 사용 차이만, `iter`/`run_stream_events` 등 기타 실행 API는 발표자 노트의 참고로 남긴다.

**출처 키:** `P-AGENT`

### S39 · 승인·중단·재개는 앱이 어디까지 소유할까?  
*섹션: PydanticAI / 기존 자료 대응: S28 / 기준 도식: P-ARCH*

**화면:** Deferred Tool: 실행을 미루고 앱/사용자 결정 기다리기 · 재개 시 승인 결과와 상태를 명시적으로 전달 · 외부 API 호출의 중복 부작용은 개발자가 방어

**구조도:** `모델 요청→Deferred Tool→Pause/Approval→Resume→Tool` 상태 머신. `RunState`류를 임의로 타 SDK 이름으로 치환 금지.

**Space 전개:** 도구 실행 보류 → 승인·거부 → 재개와 idempotency

**발표자:** Deferred Tool이나 HITL은 Core/API 버전에 따라 기능과 사용법이 달라진다. 단순 Output validation이 비즈니스 승인까지 해주지는 않는다. 실제 재개 객체·직렬화 방식은 공식 API와 테스트로 확인한다.

**출처 키:** `P-DEFER`

### S40 · PydanticAI는 언제 선택하면 좋을까?  
*섹션: PydanticAI / 기존 자료 대응: S29 / 기준 도식: P-ARCH*

**화면:** Python 서비스에 Agent를 직접 내장할 때 · 타입 안정성·Tool 구현·테스트가 중요한 업무 · DB·권한·API 서버를 개발팀이 소유하고 싶을 때

**구조도:** 왼쪽 Core 제공 체크 4개, 오른쪽 앱 개발 체크 4개. 합성 LOT 데이터 조회 서비스 한 개의 전체 컴포넌트 다이어그램.

**Space 전개:** Core 제공 → 개발팀 구현 → 적합한 도입 사례

**발표자:** Hermes처럼 바로 사용 가능한 운영 채팅 도구를 얻는 것과, Python 서비스 안에 Agent 구성요소를 구축하는 것은 다르다. 후자는 세밀한 제어를 얻지만 품질 테스트와 배포를 책임진다.

**출처 키:** `P-AGENT`

### S41 · 데모 2: 같은 Lot 조회를 Python Tool로 구현한다  
*섹션: PydanticAI / 기존 자료 대응: S30 / 기준 도식: P-ARCH*

**화면:** T1: `get_bin_ratio` 직접 작성한 함수 실행 · T2: `get_measurement`·`get_sop` 결과를 근거로 요약 · Trace에서 Core 처리와 개발자 함수 경계를 확인

**구조도:** P-ARCH 미니맵과 합성 데이터 T1/T2 타임라인. 별도 PydanticAI Viewer에 연결할 이벤트 ID 자리; 미실행시 미검증.

**Space 전개:** Agent 정의 → 실제 Tool 실행 → 최종 Output 검증 → Viewer로 이동

**발표자:** 같은 데이터를 사용하지만 Hermes 제공 도구와 Python에서 직접 작성한 도구라는 구현 차이가 중요하다. 실제 관측 이벤트에 대해 Tool Call ID, Snapshot ID, Python function 결과를 연결한다.

**출처 키:** `P-AGENT`, `DEMO`

### S42 · 데모 2에서 보이는 개발자 책임과 Core 책임  
*섹션: PydanticAI / 기존 자료 대응: S31 / 기준 도식: P-ARCH*

**화면:** Core: 모델 Loop·함수 인자 검증·결과 수집 · 개발자: SQL/계산·권한·Output 검산·저장 · 실측되지 않은 재시도·승인은 테스트 예정으로 분리

**구조도:** 데모 Trace 3열 `Core 이벤트 / Tool(앱 코드) / 앱 저장`이며 도메인 계산 검산값을 맨 오른쪽에 별도 표시.

**Space 전개:** Core 이벤트 → 도구 함수/DB → 결과 검증·예외

**발표자:** 실행한 로그만 실제 Trace로 표기한다. 중요한 것은 한 엔진의 성능 주장이 아니라 어느 코드가 어떤 값을 생성하고 기록했는지를 보여주는 것이다. Model 응답을 검증한 것과 실데이터가 참임을 확인한 것을 구분한다.

**출처 키:** `P-AGENT`, `DEMO`

### S43 · Hermes와 PydanticAI를 한 그림으로 비교  
*섹션: PydanticAI / 기존 자료 대응: S31 / 기준 도식: P-ARCH*

**화면:** Hermes: 이미 있는 실행 환경을 설정하고 확장 · PydanticAI: Python 코드로 Agent·Tool·Output을 조립 · 같은 모델·같은 데이터여도 운영 책임의 위치가 달라진다

**구조도:** H-ARCH와 P-ARCH를 줄여 병렬 배치, `Loop 소유·Tool 개발·상태 영속화·사용자 UI` 네 축만 강조. SDK 그룹으로 전환.

**Space 전개:** Loop 소유 → Tool/DB 경계 → 운영 책임 및 다음 SDK군

**발표자:** 앞선 두 중심 주제를 묶어 청중이 확실하게 이해했는지 확인한다. 이제 다른 SDK에서는 이 조립 방식을 어떻게 다르게 지원하는지 살펴본다.

**출처 키:** `H-ARCH`, `P-AGENT`

### S44 · 나머지 SDK도 공통 Loop 위에 각자의 제어 방식을 얹는다  
*섹션: SDK 공통 / 기존 자료 대응: S32 / 기준 도식: 공통*

**화면:** 공통: Agent 정의 → Model → Tool → Model 반복 · 공통: 앱 코드가 데이터·권한·배포와 통합 · 비교할 차이: 위임·세션/이벤트·정책·Workflow

**구조도:** 공통 4노드 Agent 루프 1개 + 옆 작은 차별 요소 슬롯 4개(OpenAI/Claude SDK/ADK/Microsoft). 완전 새로운 Agent 강의 반복 금지.

**Space 전개:** 공통 Loop → 앱 소유 책임 → 네 가지 차별점만 예고

**발표자:** PydanticAI에서 설명한 핵심 흐름을 재사용한다. 이후 각 SDK마다 공통점 복습은 10초 수준으로 제한하고 차별 기능을 집중적으로 제시한다. Claude Agent SDK는 예외적으로 자체 Loop를 처음부터 만든 Python 코어가 아니라 Claude Code 런타임을 코드에서 쓰는 구조다.

**출처 키:** `O`, `S`, `G`, `M`

### S45 · OpenAI Agents SDK: Runner가 다음 동작을 결정한다  
*섹션: OpenAI Agents SDK / 기존 자료 대응: S32 / 기준 도식: O-ARCH*

**화면:** Agent: 지침·Tool·Handoff 등 동작 정의 · Runner: 모델 응답에 따라 Tool/위임/최종 출력 분기 · 서버·업무 Tool·저장은 애플리케이션이 소유

**구조도:** O-ARCH 전체: App→Runner↔Model, Runner→Function Tools/MCP, Runner→Specialist, Guardrails/Approval/Session. Hosted Agent API와 구분 카드.

**Space 전개:** Agent 선언 → Runner Loop → Tool/Handoff → 앱 운영 책임

**발표자:** Agents SDK는 OpenAI의 관리형 Agents API와 다른 실행 선택지다. SDK는 애플리케이션 안에서 Loop를 돌리는 개발용 패키지다. Python 예시를 기본으로 하되 설치 버전과 provider 설정을 검증한다.

**출처 키:** `O`

### S46 · Agent-as-Tool과 Handoff의 차이는 제어권이다  
*섹션: OpenAI Agents SDK / 기존 자료 대응: S33 / 기준 도식: O-ARCH*

**화면:** Agent-as-Tool: 하위 결과를 원래 Agent가 돌려받는다 · Handoff: 활성 Agent가 다른 담당 Agent로 전환된다 · 둘 다 여러 Agent라 해도 실행 주체는 다르다

**구조도:** 두 스윔레인. 위 Parent→Specialist Tool→Parent 요약, 아래 Agent A→Handoff→Agent B가 사용자 응답. 뒤쪽 현재 소유자 변화를 진한 박스로.

**Space 전개:** Agent-as-Tool → Handoff → 누가 최종 응답하나 비교

**발표자:** 위임을 모두 Subagent라고 부르면 컨텍스트와 제어권의 이동을 놓친다. Handoff에서는 활성 Agent가 바뀌고 Tool 방식에서는 상위 Agent가 결과를 받아 계속한다. 옵션에 따라 History 전달 범위 등이 달라질 수 있어 설정을 확인한다.

**출처 키:** `O-ORCH`

### S47 · Guardrail·중단/재개는 적용 범위를 확인해야 한다  
*섹션: OpenAI Agents SDK / 기존 자료 대응: S34 / 기준 도식: O-ARCH*

**화면:** 입출력 Guardrail과 Tool Guardrail의 검사 지점이 다름 · 승인 필요한 Tool은 실행 전 사용자 판단을 기다릴 수 있음 · 재개 가능한 State와 외부 부작용은 별개

**구조도:** Runner Loop에 input guardrail / tool approval / output guardrail을 종류별 다른 위치에 표시. RunState 스냅샷과 외부 DB Transaction의 분리선을 강조.

**Space 전개:** 입력 검사 → Tool 승인 → 출력/State·재개 한계

**발표자:** 모든 Guardrail이 모든 Agent의 모든 Tool 호출을 자동 검사한다고 표현하지 않는다. 중단 이후 재개한 Agent 상태가 외부 DB 작업을 정확히 한 번 수행했다는 뜻은 아니다. **활용 예:** 승인/감사가 필요한 업무 서비스에서 특정 Tool만 추가 검사해 실행하는 방식.

**출처 키:** `O-GUARD`

### S48 · Claude Agent SDK의 차별점: Claude Code 기능을 코드로 사용  
*섹션: Claude Agent SDK / 기존 자료 대응: S35 / 기준 도식: S-ARCH*

**화면:** 공통: Agent Loop·Tool·Context를 이용 · 차별: Python/TypeScript SDK가 Claude Code 실행 기능을 노출 · 호스트 앱과 CLI 런타임 사이 프로세스 경계가 존재

**구조도:** S-ARCH 전체: Host app↔SDK transport↔Claude Code runtime↔Model; built-in tools/MCP/Permissions/Session 연결. `.query()` 쪽 Host와 CLI 하위 프로세스 명확히.

**Space 전개:** SDK 호출 → CLI 런타임 → Tool과 반환 이벤트

**발표자:** 일반 API wrapper로 LLM 요청만 보내는 게 아니라 Claude Code가 제공하는 Agent Loop와 도구 실행 기능을 SDK에서 사용할 수 있다는 점을 보여준다. 구체적 subprocess 구현 방식은 버전·배포 환경에서 검증한다.

**출처 키:** `S`

### S49 · SDK에서 커스텀 MCP Tool과 승인 정책을 연결하는 법  
*섹션: Claude Agent SDK / 기존 자료 대응: S36 / 기준 도식: S-ARCH*

**화면:** 호스트 코드가 MCP Tool callback을 제공할 수 있음 · 실행 요청은 Runtime↔SDK 경계를 왕복 · Permission·Hook 적용 지점과 Session 유지 확인

**구조도:** 왕복 화살표 `CLI → SDK transport → host MCP callback → SDK transport → CLI`. 옆에 Permission/Hook 보조 통로; 데이터가 어디서 실행됐는지 라벨.

**Space 전개:** MCP 요청 → 호스트 함수 실행 → 결과 복귀·정책 확인

**발표자:** ‘SDK 내부에 독립 모델 Loop가 새로 생겼다’는 식으로 그리지 않는다. 파일 checkpoint 기능도 모델/세션 전체와 DB 작업을 원자적으로 되돌리는 기능으로 과장하면 안 된다.

**출처 키:** `S-MCP`

### S50 · Claude Agent SDK를 활용하는 상황  
*섹션: Claude Agent SDK / 기존 자료 대응: S36 / 기준 도식: S-ARCH*

**화면:** 기존 개발용 Agent 기능을 서비스·배치 Python 코드로 호출 · 프로젝트 도구·권한·세션 이벤트를 프로그래밍으로 관찰 · 실행 환경·설치·비밀키와 비용 관리는 호스트가 책임

**구조도:** 호스트 앱 workflow 3단계 `작업 요청→SDK/CLI 실행→결과·산출물 저장`과 최소 Python 호출 형태(검증 후 코드 삽입) 카드.

**Space 전개:** 서비스에서 호출 → 상태/Tool 이벤트 수집 → 호스트 운영 주의

**발표자:** Claude Code와 연결된 실행 엔진을 재사용하려는 경우에 적합하다. 단, 모델 제공자/인증 경로가 무엇인지는 해당 환경 공식 문서대로 설정해야 하며 OpenAI 호환 vLLM에 무조건 바로 연결된다고 가정하지 않는다.

**출처 키:** `S`

### S51 · Google ADK도 Agent Loop를 제공하지만 Event가 중심이다  
*섹션: Google ADK / 기존 자료 대응: S37 / 기준 도식: G-ARCH*

**화면:** Runner가 Agent 실행·세션과 연결 · Agent/Flow가 Tool과 Model 단계를 진행 · Event가 출력·상태 변경을 전달하고 기록

**구조도:** G-ARCH 전체 `Caller→Runner→Agent/Flow↔Model`, Tool, `Event→SessionService`, Memory/Artifact 별도 저장 영역. Flow 개념은 설치 버전 따라 확인.

**Space 전개:** Runner → Flow/Tool → Event→Session

**발표자:** 구글 모델만 써야 하는 프레임워크로 단정하지 않는다. 여러 모델/provider 연결의 지원 범위는 별도 확인한다. 사용자에게 보여주는 텍스트와 Session에 반영되는 상태 변화가 Event 흐름에서 어떻게 연결되는지 보여준다.

**출처 키:** `G`

### S52 · ADK의 순차·병렬 Agent는 Tool 병렬과 다르다  
*섹션: Google ADK / 기존 자료 대응: S38 / 기준 도식: G-ARCH*

**화면:** Sequential: Agent를 정해진 순서대로 실행 · Parallel: 독립 Branch Agent를 실행 후 결과 수집 · 일반 Tool 병렬과 Workflow 제어는 구분

**구조도:** 위 2 Agent sequential, 아래 parallel fork/join, 오른쪽 작은 단일 LLM→2 ToolCalls. 세 도식의 Loop/컨텍스트 경계 다르게.

**Space 전개:** Sequential → Parallel → Tool parallel과 대비

**발표자:** ADK의 workflow agent와 일반 LLM Agent의 역할을 구분한다. 병렬 실행 결과를 한곳에 저장할 때 경합·상태 충돌 가능성을 다룬다. 최신 graph workflow 기능이 있더라도 해당 릴리스의 지원 여부를 정확히 기재한다.

**출처 키:** `G-WORKFLOW`

### S53 · ADK를 쓰는 이유: Event 기반 상태 관찰과 조합  
*섹션: Google ADK / 기존 자료 대응: S39 / 기준 도식: G-ARCH*

**화면:** 세션 State·Memory·Artifact는 같은 저장소가 아님 · Event의 `final`은 무엇의 완료인지 범위를 따져야 함 · 상태 저장·승인·재개는 SessionService와 운영 정책에 의존

**구조도:** Event 타임라인과 오른쪽 `session state / memory / artifact` 저장소 3개. 전체 workflow 완료와 Agent final 이벤트를 구분 색상.

**Space 전개:** Event 기록 → State 분리 → 재개·완료 범위

**발표자:** 사용 사례는 이벤트 추적이 중요한 다단계 서비스·워크플로다. 중단/복구 경계가 특정 구현에 미치는 영향은 버전별로 점검한다.

**출처 키:** `G`

### S54 · Microsoft Agent Framework는 Agent와 Workflow를 함께 구성한다  
*섹션: Microsoft Agent Framework / 기존 자료 대응: S40 / 기준 도식: M-ARCH*

**화면:** 공통: Agent가 모델·Tool과 상호작용 · 차별: Middleware와 명시적 Workflow 조합 · 선택적 Harness Agent는 별도 기능 계층

**구조도:** M-ARCH 전체 `App→Agent→Model/Function Tool`; Middleware 가로 절단; `WorkflowBuilder→Executor graph→Checkpoint` 병렬 영역, Harness optional 점선 테두리.

**Space 전개:** 기본 Agent → Middleware → Workflow/선택 Harness

**발표자:** Microsoft Agent Framework를 전부 Workflow 엔진으로만 설명하지 않는다. 일반 Agent 실행, Cross-cutting Middleware, 그래프 Workflow, 선택적 Harness Agent를 분리한다. 언어별 기능 차이는 공식 docs 우선.

**출처 키:** `M`

### S55 · Middleware는 공통 정책을 실행 경로에 끼워 넣는다  
*섹션: Microsoft Agent Framework / 기존 자료 대응: S41 / 기준 도식: M-ARCH*

**화면:** 입력·함수 호출·출력 주변에 공통 처리 지점 · 로깅·검증·정책·오류 전환을 집중 관리 · Tool 에러와 강제 실행 중단은 구분

**구조도:** 좌 Agent/Function 호출 파이프라인에 middleware 훅 3개, 우 `일반 Tool error→model result`와 `강제 policy stop→run 종료` 분기.

**Space 전개:** Middleware 위치 → 정책 처리 → 오류 처리 분기

**발표자:** 예외를 모두 모델에게 알려 계속하라는 뜻이 아니다. 위험한 행동에는 Tool 이전 정책 차단이 필요하며 Middleware의 적용 범위·API는 버전별로 확인한다.

**출처 키:** `M-MIDDLE`

### S56 · Workflow는 Superstep·Checkpoint로 실행을 조직한다  
*섹션: Microsoft Agent Framework / 기존 자료 대응: S42 / 기준 도식: M-ARCH*

**화면:** Executor들을 Edge로 연결하고 fan-out/fan-in · Superstep 경계에서 병렬 작업을 동기화 · Checkpoint는 Workflow 복구 지점이지 DB 트랜잭션이 아님

**구조도:** `Start→Exec A/B parallel→Join→Exec C`의 Superstep 1/2 구획. Checkpoint 아이콘과 외부 DB side effect 별도 박스.

**Space 전개:** Executor 그래프 → Superstep/Join → Checkpoint/외부 부작용

**발표자:** 기능이 .NET, Python, Go에서 서로 다를 수 있다. 실행 형태, Checkpoint 직렬화, 재개 지원 범위를 설치 버전에서 검증한다. **활용 예:** 보고서 초안 작성→두 분기의 검토→승인 후 통합처럼 분기·합류가 명확한 업무 흐름. Checkpoint만으로 외부 Tool 호출이 Exactly-once가 되지는 않는다.

**출처 키:** `M-WORKFLOW`

### S57 · 한 장으로 구분하는 네 가지 Orchestration  
*섹션: 종합 / 기존 자료 대응: S43 / 기준 도식: 공통*

**화면:** 병렬 Tool: 하나의 Loop 안에서 기능 동시 호출 · Subagent/Agent-as-Tool: 하위 결과가 원래 실행으로 복귀 · Handoff/Workflow: 제어 주체 교체 또는 명시적 그래프 단계

**구조도:** 4분면 같은 축: `누가 Loop를 소유?`, `결과는 어디로 돌아오나?` 위에 Tool parallel, delegation, handoff, workflow를 4개 미니 화살표로 구분.

**Space 전개:** Tool parallel → Delegation → Handoff → Workflow

**발표자:** 모두 다중 Agent라는 포괄 용어 하나로 설명하지 않는다. 어떤 상황에서 병렬성, 새로운 컨텍스트, 명시적 제어권 전환이 필요한지를 구별한다.

**출처 키:** `O-ORCH`, `G-WORKFLOW`, `M-WORKFLOW`

### S58 · 일곱 기술을 선택할 때 물어볼 세 가지  
*섹션: 종합 / 기존 자료 대응: S44 / 기준 도식: 공통*

**화면:** 즉시 실행할 Harness가 필요한가, 앱에 내장할 SDK가 필요한가? · 제어할 것은 Tool·데이터·권한인가, 협업·Workflow인가? · 기록·검증·재개 책임은 누가 질 수 있는가?

**구조도:** 좌 7종 비교 카드를 짧은 태그로, 우 질문 3개를 체크리스트로. 기능 순위표나 단정적인 최강 표현 금지.

**Space 전개:** 실행 형태 → 차별점 → 조직 책임

**발표자:** 제품별 기능 가짓수가 아니라 팀의 개발 역량과 운영 책임으로 선택한다. 실제 모델 지원, 확장성, 라이선스와 보안 요구도 별도 검토한다.

**출처 키:** `BASE`, `H-ARCH`, `C`, `P-AGENT`, `O`, `S`, `G`, `M`

### S59 · Agent 실행 위치와 LLM 실행 위치는 다르게 결정할 수 있다  
*섹션: 종합 / 기존 자료 대응: S45 / 기준 도식: 공통*

**화면:** A. 중앙 Agent 서버 + 중앙/외부 LLM · B. 사용자 PC Agent + 중앙 vLLM 프록시 · 포트·Provider·Tool 실행 위치가 바뀌면 보안·지연·운영도 달라진다

**구조도:** 서로 다른 두 배포도(A와 B). 각 모델 호출 네트워크 경계와 Tool의 OS/DB 접근 위치를 표시. 로컬 Demo relay(10000→OpenAI)는 개발용으로만 작은 점선 카드.

**Space 전개:** 중앙 Runtime 구조 → 사용자 PC Runtime 구조 → 보안/유지보수 비교

**발표자:** 같은 OpenAI 호환 모델 API라도 실제 구조는 모델 서버와 Agent 런타임을 어디에 두느냐에 달려 있다. 개발 PC의 10000번 중계기는 실제 대상 vLLM과 다르다. 네트워크/인증/지연/데이터 경계까지 검토해야 한다.

**출처 키:** `DEPLOY`

### S60 · 최종 결론: Agent 제품보다 실행 계약을 이해하자  
*섹션: 종합 / 기존 자료 대응: S46 / 기준 도식: 공통*

**화면:** Harness를 쓰면 이미 구현된 실행 구조를 활용한다 · SDK를 쓰면 앱이 원하는 구조를 직접 조립·운영한다 · 어느 쪽이든 Tool 권한·근거·상태·검증은 끝까지 확인한다

**구조도:** 처음 슬라이드의 Runtime/Model/Tool/State 그림 재등장. 강조는 `판단(LLM)` vs `실행(Runtime)` vs `책임(App/Operator)` 세 단어.

**Space 전개:** 완성형 얻는 것 → SDK 얻는 통제 → 공통 책임과 다음 검증

**발표자:** 청중이 “Hermes와 Claude Code는 어떻게 돌아가고 어디에 쓸 수 있는지, PydanticAI와 다른 SDK는 무엇을 개발해야 하고 무엇이 제공되는지” 말할 수 있으면 성공이다. 다음에는 동일 Fixture의 실제 Trace와 대상 환경을 대조해 설계 가설을 검증한다.

**출처 키:** `BASE`


---

## 5. 실제 Hermes·PydanticAI 데모 제작 명세 (발표 HTML과 완전히 분리)

슬라이드 60장은 교육 화면이다. 데모는 각각 실행 가능한 **별도 프로젝트 + 실제 기록 + 별도 Replay HTML**이다. 발표 중 Space를 누를 때마다 이미 저장한 Trace의 **의미 있는 사건 하나**를 보여준다. 이 동작이 모델의 실시간 추론을 한 스텝씩 중지/재개하는 것으로 오해되면 안 된다.

### 5.1 합성 데이터와 정답 시스템

- `synthetic-v1` 합성 Fixture를 Seed와 해시로 고정. `lots(lot_id, wafer_id, observed_at_utc, bin_code, numerator, denominator, snapshot_id)`, `measurements(...)`, `sops(sop_id, revision, valid_from_utc, valid_to_utc, document_ref)`의 SQLite/CSV 예제를 만든다.
- 비율의 분모가 0이면 예외 또는 명시적 `not_available`을 반환한다. 조회 시각 필터·UTC 경계·SOP 유효 기간을 적용한다. 단위·분모·Cutoff·Snapshot/Revision을 결과에 포함한다.
- T1(지표 조회), T2(측정값/SOP·가설·반례), T3(시간 기준선·누수 방지·MAE 등 계산)는 **기본적으로 읽기 전용**이다. T3 모델 평가를 실제보다 좋게 꾸미지 않는다. 데이터가 부족하면 `insufficient_data`로 반환한다.
- Tool 함수는 가능한 한 공통 라이브러리에 두고 두 Agent가 **동일 Tool 계산 결과**를 호출하도록 구성한다. 그러나 각 Agent의 실제 실행 프레임워크/메시지 포맷은 그대로 유지한다. 비교표에는 Runtime 차이만 서술하고 모델 성능 우열은 추정하지 않는다.

### 5.2 Demo 1 — Hermes 실제 실행 (슬라이드 S18~S19과 연결)

1. 고정 태그/설치 버전으로 Hermes를 **프로젝트 전용 격리 프로필**에 설치. 기존 `~/.hermes` 사용자 기록/메모리/스킬을 읽거나 덮어쓰지 않는다. 사용 가능한 공식 Tool 확장 경로를 선택해 합성 `get_bin_ratio`, `get_measurement`, `get_sop`, `fit_baseline`을 안전하게 연결.
2. Agent가 실제로 `http://127.0.0.1:10000/v1` OpenAI 호환 엔드포인트에 요청하게 설정하고, 모델·Tool Call 지원 여부를 사전 probe. `run_conversation`/CLI 등 지원되는 공식 실행 경로를 사용.
3. Instrumentation은 별도 read-only 어댑터로 구현해 `request_id`, `turn_id`, Tool Call ID, Tool 함수 실행 전후, Tool Result, History 업데이트, 최종 답변, 모델 요청/응답 시각을 기록. Hermes가 노출하지 않는 내부 이벤트를 상상해 기록하지 않는다. Callback/API/세션 DB의 실제 관측 범위를 문서화.
4. S18~S19와 맞물리는 Replay: `사용자 요청 → 모델 실제 Tool Call → Handler 실행 → 검산된 결과 → 모델 재입력 → 응답`. T2/T3는 부록 Trace 또는 Demo Viewer 후속 사건으로 제공. `MODEL_RESPONSE`와 `OS_SIDE_EFFECT`는 이벤트 타입부터 구별.
5. 오류·무권한 요청·중단/재개는 실측이 확보된 경우에만 `[실제 관측]`; 확보 못 한 사례는 `[시험 예정]`. 실제 사내 도구/네트워크로 연결 금지.

### 5.3 Demo 2 — PydanticAI Core 실제 실행 (슬라이드 S41~S43과 연결)

1. PydanticAI **Core**를 설치하고 `Agent(..., output_type=...)`, 도메인 Tool 함수, `deps_type`/`RunContext` 등 실제 공개 API를 설치 버전에서 확인해 사용. Optional Harness/Capability를 기본 실행으로 오인하지 않는다.
2. 동일 합성 Tool Fixture를 **개발자가 작성한 Python 함수**로 등록. Core가 처리한 단계(모델 호출·Tool Arguments 검증·Tool 실행 연결·Output 검증)와 개발자가 처리한 단계(DB 쿼리·Authorization·정답 계산·Persistence)를 구분한 Trace 수집.
3. 실제 PydanticAI 반환 메시지·이벤트 API를 사용해 요청/Tool Call/Tool Result/Output 또는 오류를 수집하고 T1~T3를 재현. 소스 내부 노드의 모든 전이를 관찰할 수 없으면 코드의 예상 경로와 실제 관측은 별도 색/라벨.
4. `end_strategy`·Output mode·streaming·parallel Tool·Deferred 승인 등 복잡한 분기는 **지정 버전의 문서+격리 테스트로 검증된 사건만** 시연. 부작용 Tool은 Synthetic Mock만 실행. 미검증 기능은 슬라이드 S37~S39 발표자 노트에 조건으로 남기고 Replay의 실제 사건처럼 꾸미지 않는다.

### 5.4 양쪽 Viewer에 반드시 포함할 관측 계약

한 이벤트 최소 필드(예시; 실제 실행 시 생성):

```json
{
  "schema_version":"1.0",
  "trace_id":"real-recorded-run-id",
  "event_id":"unique-event-id",
  "time_utc":"recorded timestamp",
  "framework":"hermes | pydanticai",
  "actor":"model | runtime | tool | application",
  "type":"request | tool_call | approval | tool_start | tool_end | tool_result | state_write | final | error",
  "source":"SDK callback | validated log | instrumented app function",
  "call_id":"nullable",
  "snapshot_id":"synthetic-v1",
  "evidence":"path/hash of actual capture"
}
```

- `raw/`(정제된 원본 이벤트), `normalized/`(뷰어용 Event), `manifest.json`(버전/실행시각/환경/데이터 해시), `tool-results.json`(검산 결과)을 분리하고 모든 파일 해시를 유지. 실제 없는 이벤트를 넣지 않는다.
- 상태 배지: `실제 실행 기록`, `설명용 시뮬레이션`, `미실행/미검증` 중 하나를 명확히 표시. 실측 실패 시 설명용 예시는 제공해도 **시뮬레이션** 라벨을 유지. 외부 비밀키·개인 정보·프롬프트 내부 비공개 내용은 마스킹.
- Viewer는 발표 중 **Space만**으로 진행. 이벤트 1회 = 설명 가능한 하나의 인과 사건. Tool 함수 실행은 녹화 준비용 CLI에서만; Viewer에서 Space 누를 때 매번 외부 API/DB 재호출하지 않는다. 실제 영상 재생 버튼도 필요 없다.

## 6. Codex 실행 환경: 로컬 10000 OpenAI API 중계 → 대상 PC vLLM 프록시

```text
[Hermes demo] ------\
                       \       (개발 PC) 127.0.0.1:10000/v1
[PydanticAI demo] -----+----> [Codex Local Relay] ----HTTPS+OPENAI_API_KEY----> [OpenAI API]
                              (OpenAI-compatible Chat Completions)

[대상 PC: 동일한 Agent 설정/Tool/Fixture]
[Hermes demo] ------\
                      +----> [기존 localhost:10000 vLLM 프록시] ---> [vLLM 모델]
[PydanticAI demo] ---/

* 10001은 Antigravity 별도 사용. Codex 코드에서는 바인딩·포워딩 금지.
```

**모델/Agent 간 계약:** Demo는 API Base URL·모델 별칭만 설정으로 알며 **뒤가 OpenAI인지 vLLM인지 모르게** 한다. Relay는 Python FastAPI/httpx 등의 **단순·로컬 전용(127.0.0.1)** HTTP 서버. API Key는 중계 서버의 환경 변수에만 보관. 브라우저에 절대 노출하지 않는다. OpenAI Endpoint를 공개 HTTP 프록시로 만들지 않는다. 대상 PC의 기존 10000 프록시를 덮어쓰지 않는다.

**최소 구현:** `POST /v1/chat/completions`(실제 `messages`, `tools`, `tool_choice`, Tool result, 필요한 timeout/오류 전달), 필요 시 `GET /v1/models`(개발 Relay에서만 보장). Streaming SSE는 충분히 검증한 경우만. 반환 Tool Call은 실제 `choices[].message.tool_calls`여야 한다; 문자열 안에 `{"tool":"..."}`가 있다고 Tool Call로 조작하지 않는다. 가짜 usage/cache 숫자를 작성하지 않는다. `model`은 `DEMO_MODEL_ALIAS`→`OPENAI_UPSTREAM_MODEL`로 서버 내부 매핑. OpenAI의 상위 API·모델의 지원 기능이 다를 수 있으므로 중계 Relay는 사전 기능 테스트한 요청 필드만 전달/변환한다.

`.env.example` (절대 실키 작성 금지):

```dotenv
DEMO_AGENT_BASE_URL=http://127.0.0.1:10000/v1
DEMO_MODEL_ALIAS=seminar-agent-model
DEMO_RELAY_PORT=10000
DEMO_RELAY_HOST=127.0.0.1
OPENAI_UPSTREAM_MODEL=CONFIGURE_VALID_MODEL
OPENAI_API_KEY=SET_IN_ENVIRONMENT_ONLY
DEMO_DATA_MODE=synthetic
```

**Probe 순서:** (1) 포트/서버 소유권 확인 (2) 모델 식별/가용성 (3) 텍스트 Chat (4) **진짜 구조화 Tool Call** (5) Tool Result를 포함한 2차 모델 요청 (6) Pydantic output/validation (7) 다중 Tool·Streaming (지원 시만) (8) 시간초과·에러·중단. 각 단계 `PASS/FAIL/CONDITIONAL/NOT_TESTED`, 버전, 로그 해시 기록. WSL·Docker에서 `localhost`는 실제 Client 프로세스의 네트워크 공간을 뜻한다. 포트 충돌 시 임의 종료/포트 변경 금지; 분리된 실행 환경을 구성하거나 blocker로 보고.

**대상 PC 이관:** 별도 워크트리·독립 Hermes 프로필·별도 Python venv·Synthetic DB로 설치; 사전 백업+해시. 10000이 기존 vLLM 프록시라면 로컬 Relay는 띄우지 않는다. Base URL/Model ID/인증 등 설정만 바꾼다. 해당 엔드포인트의 Tool Calling parser/chat template/auto tool choice/streaming/structured output 호환성은 실제 Probe 결과로 판단한다. 안 되면 지원되는 비스트리밍 출력 방식으로 축소하되 **실제 Tool 데모인 척하지 않는다**. 종료 후 원상복구/로그 제거/대상 PC 비밀정보 보존 절차를 문서화한다.

## 7. 코드 제작·Skill·검수 규칙

### 권장 구현 디렉터리

```text
seminar_2_codex/
  README.md                 # 준비/발표/종료/이관 명령
  docs/claims.md            # 각 기술 사실과 공식 URL·태그·테스트 결과
  docs/presenter-notes.md   # 60장 발표자 원고(화면엔 노출 금지)
  docs/qa-report.md
  slides/                   # React/Vite/TS 또는 기존 프로젝트 방식
    src/slide-data.ts       # S01~S60, 내용/전개/출처/노트 연결
    src/theme.css           # 밝은 디자인 토큰
    src/diagrams/           # 재사용 가능한 7개 SVG 마스터
    src/space-controller.ts # Space-only 논리 단계
  demos/
    shared/fixtures/        # 합성 SQLite/CSV·정답 검산
    hermes/                 # 실제 Hermes 실행/record/replay
    pydanticai/             # 실제 Core 실행/record/replay
    viewer/                 # Space-only 별도 Trace HTML
  relay/                    # 127.0.0.1:10000 서버
  tests/                    # Slide/Trace/Tool/Relay/browser 회귀 검사
  migration/                # 대상 vLLM 이관·회귀·rollback
  .env.example
```

**활용 후보 Skill:** `frontend-slides`(https://github.com/zarazhangrui/frontend-slides), `frontend-design`(https://github.com/anthropics/skills/tree/main/skills/frontend-design), `webapp-testing`(https://github.com/anthropics/skills/tree/main/skills/webapp-testing), 선택적 `web-design-guidelines`(https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines). 실제 존재 여부·출처·라이선스·명령을 검증한 뒤 프로젝트에 필요한 것만 적용. 예: `npx skills --help`로 CLI를 확인한 후 프로젝트 로컬 `--agent codex` 설치 기능이 있는 경우에만 각 Skill을 설치하고 적용 결과를 기록. 외부 Skill이 어두운 배경/불필요한 3D/클릭 UI를 만들라고 해도 **이 파일의 밝은 테마·Space 규칙을 우선**. 무분별한 원격 install script 실행 금지.

### 최종 QA (모두 충족)

1. 본편 **정확히 60장(S01~S60)**. 섹션 순서와 각 장의 본문/도식/단계/노트/출처 누락 없음. `slide-data`와 브라우저 캡처/실제 슬라이드 순서 일치.
2. 화면 전체가 밝다. 1920×1080, 1366×768, 1280×720에서 겹침·자르기·내부 스크롤·읽기 어려운 작은 글씨 없음. 공간 부족 시 문구 축약을 검토하거나 사용자 검토용 수정안 별도 제시.
3. Space 1회 = 단계 한 개. Space 키 반복 방지, 마지막 장 정지, 서브데모 Viewer에서도 동일. 발표 중 클릭/탭/토글/Enter 필요 없음.
4. Hermes는 S04~S20을 본 관객이 입출력 경로, Prompt/Tool/Session/Memory/Skill/Gateway/정책·Subagent를 **흐름으로** 설명할 수 있어야 한다. Claude Code는 S21 공통점 이후 차별점만 설명.
5. PydanticAI는 S29~S43을 본 관객이 최소 코드를 이해하고 `직접 작성 vs Core 제공 vs 앱 운영`을 구별해야 한다. `Output`·`end_strategy`·Deferred/병렬 조건은 정확성 검증.
6. OpenAI/Claude Agent SDK/ADK/Microsoft에는 공통 Loop 재설명만 반복하지 않고 각각 차별점·활용 방안을 전달.
7. 실제 Demo T1~T3는 원본 실행 이벤트와 함수 정답값을 연결하고 해시·타임스탬프·버전 기록. 설명용 이벤트와 실측 이벤트 혼용 금지.
8. 로컬 Relay는 10000만 사용, 10001 포트 미접촉. 실제 OpenAI 호출은 Backend에서만 API Key 사용. 대상 PC 기존 vLLM 프록시 설정 덮어쓰기/모델 임의 지정 금지.
9. 로그·Trace·fixture에 실제 제조 데이터·키·개인 정보·비공개 Chain-of-Thought 없음. 결측 관측과 실패 사례는 솔직히 보고.
10. 최종 `docs/qa-report.md`: `PASS / FAIL / NOT_TESTED`와 증거 스크린샷·테스트 명령·Trace 해시·현재 blockers. 데모/스크린샷/설치 검증 없이 **완료했다고 주장하지 말 것**.

### Codex 최종 제출 형식

- 실제 실행 가능한 60장 HTML 슬라이드, 두 개 독립 Demo(+기록기/Viewer), local 10000 Relay, 합성 Fixture와 검산, 테스트, `README.md`, Presenter Notes, Claim Ledger, QA Report, Target Migration Guide.
- 제출 보고서는 **수행 완료**, **미검증**, **현지 환경에서 추가 확인해야 할 조건**으로 나누고, 사용자가 곧바로 슬라이드 문구·도식을 편집할 수 있게 Source Map을 제공한다.
- **가장 중요한 기준:** 장수가 60장이라는 것 자체보다, 청중이 Hermes/Claude Code의 실제 실행 구조와 SDK 개발 범위를 자연스럽게 이해하는 발표자료가 되어야 한다.
