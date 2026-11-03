# 주장·근거 검토 기록

확인일: 2026-11-03. 사용자 요청 범위는 발표자료 60장이다. 모델 API, Hermes/PydanticAI 데모, relay, 외부 Tool을 실행하지 않았다.

## 검토 기준

- DOC_CONFIRMED: 저장한 공식 문서의 공개 계약을 확인했다. 설치 환경에서 동일 동작을 재현했다는 뜻은 아니다.
- SOURCE_CONFIRMED: 특정 commit의 공개 소스에서 심볼·구조를 확인했다. 실행 관측과 구분한다.
- DESIGN_ONLY: 교육용 사례 또는 도입·운영 설계 제안이다.
- NOT_VERIFIED: 실제 설치·실행·Trace 검증은 수행하지 않았다.
- 이 제작본에는 RUN_OBSERVED 주장이 없다. 원고의 이전 릴리스 숫자를 최신판 또는 설치 버전으로 표기하지 않았다.

## 슬라이드별 주장

| 슬라이드 | 화면 주장 | 근거 | 검토 범위 |
|---|---|---|---|
| S01 | 모델·Runtime·Tool·상태 저장의 역할을 분리한다 / 요청부터 실행과 기록까지의 흐름을 따라간다 / Harness와 SDK의 개발·운영 범위를 비교한다 | BASE | DESIGN_ONLY |
| S02 | 완성형: Hermes와 Claude Code / 개발형: PydanticAI·OpenAI SDK·ADK·Microsoft / Claude Agent SDK는 Claude Code 실행 기능과 연결 | BASE, S, C, M | DESIGN_ONLY |
| S03 | 합성 LOT-A / BIN-X / synthetic-v1 / 지표 조회·원인 후보·예측을 공통 사례로 사용 / 데모 실행은 후속 단계에서 검증 | BASE | DESIGN_ONLY |
| S04 | 입력 채널이 달라도 AIAgent 실행 흐름으로 모인다 / 모델 연결·Tool Dispatch·대화 기록을 런타임이 조정 / 개발자는 확장 도구·정책·실행 환경을 구성 | H-ARCH, H-LOOP | DOC_CONFIRMED |
| S05 | ① 입력과 이전 대화로 모델 요청을 만든다 / ② 모델의 Tool Call을 실행하고 결과를 되돌린다 / ③ 최종 응답이 나올 때까지 필요한 만큼 반복한다 | H-LOOP | DOC_CONFIRMED |
| S06 | 모델: Tool 이름과 입력 인자 제안 / 런타임: 사용 가능 여부·권한 확인 후 Handler 실행 / 결과: Tool 메시지로 다시 모델 입력에 합류 | H-LOOP, H-TOOLS | DOC_CONFIRMED |
| S07 | 외부 접점: run_agent.py / 반복과 분기: conversation_loop.py / Tool 실행: tool_executor.py / model_tools.py | H-ARCH, H-LOOP, H-SRC | DOC_CONFIRMED + SOURCE_CONFIRMED |
| S08 | 인자 오류·접근 거부·Tool 예외를 구분 / Runtime은 실패 결과를 기록하거나 실행을 중단 / 모델 재질문·재시도는 정책과 남은 반복 예산에 따름 | H-LOOP, H-TOOLS | DOC_CONFIRMED |
| S09 | System Prompt + 대화 History + 사용 가능한 Tool Schema / Memory/Skill은 필요 시 프롬프트나 Tool을 통해 반영 / DB 전체와 실제 OS 상태가 자동으로 전달되지는 않는다 | H-PROMPT, H-SESSION | DOC_CONFIRMED |
| S10 | Prefix Cache: 같은 접두부의 연산 재사용 / Compaction: 이력을 요약해 입력 크기 축소 / 캐시 지원 조건과 요약 정보 손실을 구분 | H-LOOP | DOC_CONFIRMED |
| S11 | Session: 그 대화에서 실제 오간 메시지·Tool 결과 / Memory: 다음에도 유용한 사실·선호·메모 / Skill: 반복 가능한 절차·작업법 | H-SESSION, H-MEMORY, H-SKILL | DOC_CONFIRMED |
| S12 | 대화 중 얻은 유용한 사실을 Memory로 보존 / 반복 작업 절차를 Skill로 정리해 재사용 / 검색·저장·로드는 명시적 경로와 조건을 거친다 | H-MEMORY, H-SKILL | DOC_CONFIRMED |
| S13 | Tool: Agent가 호출하는 작업 단위 / MCP: 외부 Tool/Resource를 연결하는 통신 규약 / Plugin: Tool·Hook 등 런타임 확장 등록 | H-TOOLS, H-ARCH | DOC_CONFIRMED |
| S14 | 모델의 지시 준수만으로 위험 Tool을 막을 수 없다 / Tool Dispatch 전 승인과 실행 환경 권한이 중요 / 실제 DB 읽기/쓰기 권한은 운영 환경에서 강제 | H-TOOLS | DOC_CONFIRMED |
| S15 | 병렬 Tool: 하나의 Agent 턴에서 여러 Handler 호출 / Subagent: 별도 실행 문맥을 가진 하위 Agent에 작업 위임 / 반환 결과·맥락·공유 자원 및 충돌 위험이 달라진다 | H-LOOP, H-TOOLS | DOC_CONFIRMED |
| S16 | CLI: 사용자의 직접 대화 / Gateway: 플랫폼 메시지를 인증·세션 라우팅 / Cron: 정해진 시각에 새로운 작업 실행 | H-ARCH | DOC_CONFIRMED |
| S17 | 이미 있는 것: 대화 Loop·기본 Tool·세션·다중 진입점 / 설정/확장할 것: 모델·Tool·Skill·플랫폼·승인 규칙 / 직접 책임질 것: 데이터 접근권·업무 검증·운영 장애 | H-ARCH | DESIGN_ONLY |
| S18 | T1: 합성 LOT-A의 BIN-X 비율 조회 / 요청·handler·결과·최종 응답을 연결해 확인 / 실행 전: 실제 Trace와 event_id는 아직 없음 | H-LOOP, DEMO | DESIGN_ONLY |
| S19 | Tool Call ID와 실제 결과를 연결 / 오류 처리와 History 갱신을 관찰 / Session 저장과 Memory 갱신을 구별 | DEMO, H-SESSION | DESIGN_ONLY |
| S20 | 구현된 Harness를 빠르게 활용할 수 있다 / Loop·Prompt·Tool·Memory·Gateway의 책임 경계가 분명하다 / 품질·권한·데이터 진실성은 운영 설계가 결정한다 | H-ARCH | DOC_CONFIRMED |
| S21 | 공통: 모델과 Tool을 반복하는 실행 구조 / 파일·명령 실행은 Runtime과 Tool이 담당 / 차별점은 프로젝트 규칙과 개발 도구 통합 | C | DOC_CONFIRMED |
| S22 | 코드베이스 탐색 → 파일 수정 → 명령/테스트 실행 / CLI·IDE·Desktop 등 개발 접점과 연결 / 여러 파일·프로젝트 규칙을 함께 고려 | C | DOC_CONFIRMED |
| S23 | CLAUDE.md: 프로젝트별 지속 지시·규칙 / Skill: 특정 작업에서 불러 쓰는 절차 / Memory: 이전 작업에서 남긴 유용한 맥락 | C-MEM, C-SKILL | DOC_CONFIRMED |
| S24 | Permissions: Tool 호출 허용·승인 정책 / Hooks: 정해진 지점에서 사용자 코드 개입 / Sandbox: 실제 실행 환경의 접근 범위 제한 | C-POLICY, C-HOOK, C-SANDBOX | DOC_CONFIRMED |
| S25 | Subagent: 특정 역할에 작업을 맡기고 결과를 부모에 전달 / Agent Teams: 구성원 간 조정·공유 작업 관리가 핵심 / 독립 Context가 곧 독립 파일 시스템은 아니다 | C-SUB, C-TEAM | DOC_CONFIRMED |
| S26 | 요구 분석 → 변경 계획 → 코드 수정 → 테스트 → 검토 / 역할별 Subagent로 분담하고 주 실행에서 통합 / Hooks/CI/승인으로 품질 관문 배치 | C | DESIGN_ONLY |
| S27 | Hermes: 다채널·주기 작업·Memory/Skill 운용 / Claude Code: 저장소 탐색·수정·테스트 / 권한·데이터·상태의 운영 책임은 공통 | H-ARCH, C | DESIGN_ONLY |
| S28 | 완성형: 기존 앱에서 실행 루프·도구를 주로 설정/확장 / SDK: 애플리케이션 코드가 Agent 정의·Tool·상태 결합 / PydanticAI는 이 경계를 가장 먼저 보여줄 사례 | P-AGENT, O | DESIGN_ONLY |
| S29 | Pydantic: 데이터 구조·검증 라이브러리 / PydanticAI Core: 실행 Loop·Tool·Output·Retry 제공 / 선택 Harness/Capability는 Core와 별도 계층 | P-AGENT, P-OUTPUT | DOC_CONFIRMED |
| S30 | 직접: Agent 설정·도메인 Tool 함수·Deps·Output 타입 / Core 제공: 모델 왕복·Tool 인자 처리·검증·재시도·종료 / 별도 구현: API 서버·DB 권한·업무 규칙·영속화 | P-AGENT, P-TOOLS | DOC_CONFIRMED |
| S31 | 모델·Instructions·Output 타입을 선언 / Python Tool을 등록하고 앱 자원을 연결 / run 결과를 앱의 후속 처리에 사용 | P-AGENT, P-TOOLS | DOC_CONFIRMED / 실제 실행 NOT_VERIFIED |
| S32 | 시작: UserPromptNode에서 입력을 준비 / 중간: ModelRequestNode ↔ CallToolsNode 반복 / 종료: 검증된 최종 Output 또는 에러/제한 | P-AGENT, P-SRC | DOC_CONFIRMED + SOURCE_CONFIRMED |
| S33 | Instructions: 모델에 전달할 지침 / Deps: Tool이 접근하는 Python 런타임 의존성 / History: 앱이 전달/관리하는 대화 문맥 | P-AGENT, P-TOOLS, P-DEPS | DOC_CONFIRMED |
| S34 | 모델 요청 인자를 Python 함수 인자로 검증 / Tool 함수가 실제 읽기/계산을 수행 / 실패·재시도·권한 거부는 별도 경로 | P-TOOLS | DOC_CONFIRMED |
| S35 | 자연어 대신 정해진 BinResult 구조로 받기 / 모델 출력의 형식·타입 검증과 재시도 지원 / 유효한 JSON도 도메인 정답과는 별개 | P-OUTPUT | DOC_CONFIRMED |
| S36 | 유효한 Output Tool과 함수 Tool이 함께 온 경우 / early / graceful / exhaustive를 구분 / Streaming 확정 시점과 부작용은 별도 검토 | P-OUTPUT | DOC_CONFIRMED |
| S37 | 서로 독립인 읽기 Tool은 병렬 처리 가능 / 순서가 중요한 Tool은 직렬화·동기화가 필요 / 비결정적 완료 순서와 결과 해석은 분리 | P-TOOLS, P-ADV | DOC_CONFIRMED |
| S38 | run: async 최종 결과 / run_sync: 동기 코드에서 실행 / run_stream: 생성 중 결과를 스트리밍 | P-AGENT | DOC_CONFIRMED |
| S39 | 외부 승인 흐름: Deferred 요청을 앱에 반환 / History와 승인·실행 결과로 후속 run 시작 / 외부 부작용의 중복 방지는 앱이 구현 | P-DEFER | DOC_CONFIRMED |
| S40 | Python 서비스에 Agent를 직접 내장할 때 / 타입 안정성·Tool 구현·테스트가 중요한 업무 / DB·권한·API 서버를 개발팀이 소유하고 싶을 때 | P-AGENT | DESIGN_ONLY |
| S41 | T1: 직접 작성한 get_bin_ratio 함수 / T2: 측정값·유효 SOP를 근거로 원인 후보 제시 / 실행 전: Core와 함수의 실제 이벤트 수집 예정 | P-AGENT, DEMO | DESIGN_ONLY |
| S42 | Core: 모델 Loop·인자 검증·결과 수집 / 앱: SQL·계산·권한·검산·영속화 / 실측되지 않은 재시도와 승인은 검증 예정 | P-AGENT, DEMO | DESIGN_ONLY |
| S43 | Hermes: 기존 실행 환경을 설정·확장 / PydanticAI: 앱 코드로 Agent·Tool·Output 조립 / 같은 데이터라도 운영 책임의 배치가 달라짐 | H-ARCH, P-AGENT | DESIGN_ONLY |
| S44 | 공통: Agent 정의 → Model → Tool → Model 반복 / 공통: 앱 코드가 데이터·권한·배포와 통합 / 비교할 차이: 위임·세션/이벤트·정책·Workflow | O, S, G, M | DESIGN_ONLY |
| S45 | Agent: 지침·Tool·Handoff 등 동작 정의 / Runner: 모델 응답에 따라 Tool/위임/최종 출력 분기 / 서버·업무 Tool·저장은 애플리케이션이 소유 | O | DOC_CONFIRMED |
| S46 | Agent-as-Tool: 하위 결과를 원래 Agent가 돌려받는다 / Handoff: 활성 Agent가 다른 담당 Agent로 전환된다 / 둘 다 여러 Agent라 해도 실행 주체는 다르다 | O-ORCH | DOC_CONFIRMED |
| S47 | Input·Tool·Output 검사는 적용 지점이 다름 / 승인이 필요한 Tool은 실행을 보류할 수 있음 / RunState 복구가 DB 부작용까지 되돌리지는 않음 | O-GUARD, O-HITL | DOC_CONFIRMED |
| S48 | 공통: Agent Loop·Tool·Context를 이용 / 차별: Python/TypeScript SDK가 Claude Code 실행 기능을 노출 / 호스트 앱과 CLI 런타임 사이 프로세스 경계가 존재 | S, S-SRC | DOC_CONFIRMED + SOURCE_CONFIRMED |
| S49 | 호스트 코드가 MCP Tool callback을 제공할 수 있음 / 실행 요청은 Runtime↔SDK 경계를 왕복 / Permission·Hook 적용 지점과 Session 유지 확인 | S-MCP | DOC_CONFIRMED |
| S50 | 기존 개발용 Agent 기능을 서비스·배치 Python 코드로 호출 / 프로젝트 도구·권한·세션 이벤트를 프로그래밍으로 관찰 / 실행 환경·설치·비밀키와 비용 관리는 호스트가 책임 | S | DESIGN_ONLY |
| S51 | Runner가 Agent 실행·세션과 연결 / Agent/Flow가 Tool과 Model 단계를 진행 / Event가 출력·상태 변경을 전달하고 기록 | G | DOC_CONFIRMED |
| S52 | Sequential: Agent를 정해진 순서대로 실행 / Parallel: 독립 Branch Agent를 실행 후 결과 수집 / 일반 Tool 병렬과 Workflow 제어는 구분 | G-WORKFLOW | DOC_CONFIRMED |
| S53 | Event는 출력과 state 변경을 전달 / Session·Memory·Artifact는 서로 다른 목적 / Agent final과 전체 Workflow 완료를 구분 | G, G-EVENT, G-STATE | DOC_CONFIRMED |
| S54 | 공통: Agent가 모델·Tool과 상호작용 / 차별: Middleware와 명시적 Workflow 조합 / 선택적 Harness Agent는 별도 기능 계층 | M | DOC_CONFIRMED |
| S55 | 입력·함수 호출·출력 주변에 공통 처리 지점 / 로깅·검증·정책·오류 전환을 집중 관리 / Tool 에러와 강제 실행 중단은 구분 | M-MIDDLE | DOC_CONFIRMED |
| S56 | Executor들을 Edge로 연결하고 fan-out/fan-in / Superstep 경계에서 병렬 작업을 동기화 / Checkpoint는 Workflow 복구 지점이지 DB 트랜잭션이 아님 | M-WORKFLOW, M-CHECKPOINT | DOC_CONFIRMED |
| S57 | 병렬 Tool: 하나의 Loop 안에서 기능 동시 호출 / Subagent/Agent-as-Tool: 하위 결과가 원래 실행으로 복귀 / Handoff/Workflow: 제어 주체 교체 또는 명시적 그래프 단계 | O-ORCH, G-WORKFLOW, M-WORKFLOW | DESIGN_ONLY |
| S58 | 바로 쓸 실행 환경인가, 앱에 내장할 SDK인가 / Tool·데이터 통제인가, 위임·Workflow 통제인가 / 기록·검증·복구를 팀이 어디까지 운영할 수 있나 | BASE, H-ARCH, C, P-AGENT, O, S, G, M | DESIGN_ONLY |
| S59 | 중앙 Runtime: 인증·격리·큐·운영을 중앙 관리 / 로컬 Runtime: 사용자 파일·OS 권한과 연결 / 모델 연결·지연·배포·데이터 경계를 별도 검토 | DEPLOY | DESIGN_ONLY |
| S60 | Harness를 쓰면 이미 구현된 실행 구조를 활용한다 / SDK를 쓰면 앱이 원하는 구조를 직접 조립·운영한다 / 어느 쪽이든 Tool 권한·근거·상태·검증은 끝까지 확인한다 | BASE | DESIGN_ONLY |

## 수정 및 조건

1. S03/S18/S19/S41/S42: 데모 수행 표현을 실행 전 확인 계획으로 바꿨다. event_id, 캡처, 가상 Trace를 만들지 않았다.
2. S06: 원문의 ratio 0.12는 단위가 모호하므로 교육용 예시 12/10,000 × 100 = 0.12%로 명시했다. 계산은 실제 DB 관측이 아니다.
3. S08/S14: 승인 거부는 Tool 실패로 반환될 수도 있다. 정책에 의한 전체 run 강제 중단과 혼동하지 않는다. DANGEROUS_PATTERNS의 위험 명령 승인은 모든 Tool에 자동 적용되는 보안 보장이 아니다.
4. S09: Stable/Context/Volatile은 시스템 프롬프트 층이다. Volatile을 모두 호출별 임시 입력으로 동일시하지 않았다. 세션 스냅샷과 호출 시 임시 맥락을 분리했다.
5. S24: Hook/Permission 순서를 하나로 고정하지 않고 적용 지점별 계층으로 설명한다. Sandbox의 플랫폼·설정 조건은 설치 환경에서 확인해야 한다.
6. S25: Teams 지원 설정·환경과 독립 Context/공유 파일 충돌은 별개다.
7. S31: API 형태는 문서·공개 소스와 대조했지만 실행 가능한 독립 예제가 아니다. model과 fixture 함수는 앱 주입 항목이다. 실행 가능/실제 원문 라벨을 사용하지 않았다.
8. S36: 현재 공식 문서는 graceful을 기본으로 설명한다. early/exhaustive만 나누던 초안을 세 정책으로 보완했다. 비교 조건은 유효한 Output Tool + 함수 Tool 혼합 응답이다. Native/Prompted 출력과 plain text의 조건, Streaming 조기 확정은 노트에서 분리했다.
9. S37: 실행 동시성과 모델의 병렬 Tool Call 생성은 다르다. 실제 병렬 시간 측정은 하지 않았다.
10. S39: 외부 승인 흐름은 DeferredToolRequests를 반환한 뒤 History + DeferredToolResults로 후속 run을 시작한다. 현재 문서의 inline handler 경로는 선택 방식으로 노트에 기록했다.
11. S47: Input guardrail은 첫 Agent, Output guardrail은 최종 Agent 출력에 적용된다. Function Tool guardrail과 Hosted Tool/handoff의 범위를 일반화하지 않았다.
12. S48: Python SDK의 subprocess transport 소스를 확인했지만 모든 언어·배포 방식이 동일한 프로세스 구현이라는 의미는 아니다.
13. S53/S56: Agent final은 전체 Workflow 완료와 다르며, Checkpoint는 외부 DB exactly-once를 보장하지 않는다. 언어별 지원 범위와 저장 구현은 별도 검증한다.
14. 출처 키 CC와 P는 원고의 C와 P-AGENT로 정규화했다. 이동된 문서 URL은 아래 실제 응답 URL을 사용했다.

## 공개 소스 고정점

- H-SRC: https://github.com/NousResearch/hermes-agent/tree/6112c2adb9e11f69734a29be9d2696f345ffa06a  
  commit: `6112c2adb9e11f69734a29be9d2696f345ffa06a`
- P-SRC: https://github.com/pydantic/pydantic-ai/tree/a56a6d6f138d1e3a9c45a9697ea513bef47a6cea  
  commit: `a56a6d6f138d1e3a9c45a9697ea513bef47a6cea`
- S-SRC: https://github.com/anthropics/claude-agent-sdk-python/tree/e0da9b95223d3d112bfbccad41d2a32bad923bb5  
  commit: `e0da9b95223d3d112bfbccad41d2a32bad923bb5`

Hermes 확인 파일: run_agent.py, agent/conversation_loop.py, agent/tool_executor.py, model_tools.py. PydanticAI 확인 심볼: UserPromptNode, ModelRequestNode, CallToolsNode. Claude SDK 확인 파일: src/claude_agent_sdk/_internal/transport/subprocess_cli.py. 저장 사본은 evidence/sources 아래에 있다.

## 공식 자료 URL과 수집 증거

| ID | 실제 URL | 상태 |
|---|---|---|
| H-ARCH | https://hermes-agent.nousresearch.com/docs/developer-guide/architecture | FETCHED |
| H-LOOP | https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop | FETCHED |
| H-PROMPT | https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly | FETCHED |
| H-SESSION | https://hermes-agent.nousresearch.com/docs/user-guide/sessions | FETCHED |
| H-MEMORY | https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what | FETCHED |
| H-SKILL | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | FETCHED |
| H-TOOLS | https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime | FETCHED |
| H-DELEGATE | https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns | FETCHED |
| C | https://code.claude.com/docs/en/how-claude-code-works | FETCHED |
| C-MEM | https://code.claude.com/docs/en/memory | FETCHED |
| C-SKILL | https://code.claude.com/docs/en/skills | FETCHED |
| C-POLICY | https://code.claude.com/docs/en/permissions | FETCHED |
| C-HOOK | https://code.claude.com/docs/en/hooks | FETCHED |
| C-SANDBOX | https://code.claude.com/docs/en/sandboxing | FETCHED |
| C-SUB | https://code.claude.com/docs/en/sub-agents | FETCHED |
| C-TEAM | https://code.claude.com/docs/en/agent-teams | FETCHED |
| P-AGENT | https://pydantic.dev/docs/ai/core-concepts/agent/ | FETCHED |
| P-TOOLS | https://pydantic.dev/docs/ai/tools-toolsets/tools/ | FETCHED |
| P-ADV | https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced/ | FETCHED |
| P-OUTPUT | https://pydantic.dev/docs/ai/core-concepts/output/ | FETCHED |
| P-DEPS | https://pydantic.dev/docs/ai/core-concepts/dependencies/ | FETCHED |
| P-DEFER | https://pydantic.dev/docs/ai/tools-toolsets/deferred-tools/ | FETCHED |
| P-HARNESS | https://pydantic.dev/docs/ai/capabilities/overview/ | FETCHED |
| O | https://openai.github.io/openai-agents-python/running_agents/ | FETCHED |
| O-ORCH | https://openai.github.io/openai-agents-python/multi_agent/ | FETCHED |
| O-GUARD | https://openai.github.io/openai-agents-python/guardrails/ | FETCHED |
| O-HITL | https://openai.github.io/openai-agents-python/human_in_the_loop/ | FETCHED |
| S | https://code.claude.com/docs/en/agent-sdk/overview | FETCHED |
| S-MCP | https://code.claude.com/docs/en/agent-sdk/custom-tools | FETCHED |
| S-POLICY | https://code.claude.com/docs/en/agent-sdk/permissions | FETCHED |
| G | https://adk.dev/runtime/ | FETCHED |
| G-EVENT | https://adk.dev/events/ | FETCHED |
| G-STATE | https://adk.dev/sessions/ | FETCHED |
| G-WORKFLOW | https://adk.dev/agents/workflow-agents/ | FETCHED |
| M | https://learn.microsoft.com/en-us/agent-framework/overview/ | FETCHED |
| M-MIDDLE | https://learn.microsoft.com/en-us/agent-framework/concepts/agents/middleware/ | FETCHED |
| M-WORKFLOW | https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/ | FETCHED |
| M-CHECKPOINT | https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints | FETCHED |
| DEPLOY | https://docs.vllm.ai/en/latest/features/tool_calling/ | FETCHED |
| H-SRC | https://github.com/NousResearch/hermes-agent/tree/6112c2adb9e11f69734a29be9d2696f345ffa06a | PINNED_COMMIT |
| P-SRC | https://github.com/pydantic/pydantic-ai/tree/a56a6d6f138d1e3a9c45a9697ea513bef47a6cea | PINNED_COMMIT |
| S-SRC | https://github.com/anthropics/claude-agent-sdk-python/tree/e0da9b95223d3d112bfbccad41d2a32bad923bb5 | PINNED_COMMIT |
| BASE | ../agent_framework_seminar_ii_codex_revised_blueprint.md | USER_SPEC |
| DEMO | ../agent_framework_seminar_ii_codex_revised_blueprint.md#5 | DESIGN_ONLY |

수집 원문 해시는 source-map.json에 기록했다. FETCHED는 수집 성공 상태이며, 문서 내용 검토는 위 슬라이드별 행과 수정 기록으로 구분한다. 설치 버전별 동작·성능·실제 재개 가능성은 모두 NOT_VERIFIED다.