# 발표자 원고 — Agent Framework Seminar II

발표 범위: 60장. 실제 데모는 수행하지 않았으며 S18/S19/S41/S42는 확인 계획입니다.

## S01 — Agent는 모델 밖의 실행 구조에서 움직인다

1차에서 Agent·Tool Calling 개념은 학습했다. 오늘은 누가 모델에 요청하고, 누구의 코드가 Tool을 실행하며, 다음 턴에 무엇이 남는지 따라간다. 핵심은 제품 기능 나열이 아니라 실제 실행 구조다.

### 화면 문구

- 모델·Runtime·Tool·상태 저장의 역할을 분리한다
- 요청부터 실행과 기록까지의 흐름을 따라간다
- Harness와 SDK의 개발·운영 범위를 비교한다

### 단계별 전개

1. 질문과 공통 5개 노드
2. LLM의 요청과 Runtime 실행을 다른 색 화살표로 구분
3. Harness와 SDK의 선택이라는 발표 목표 노출

### 원문 도식 요구

화면 중앙에 사용자→Agent Runtime↔LLM→Tool→상태 저장의 5개 노드. 모델은 파랑, 실행기는 보라, 도구는 초록. 아래 Harness/SDK 두 갈래를 얇은 띠로 구분.

출처: BASE

## S02 — 제공된 실행 환경에 따라 개발 범위가 달라진다

프레임워크·SDK·Harness 명칭 자체보다 제공된 실행 루프와 개발자가 구현할 범위를 기준으로 이해한다. Microsoft에도 선택적 Harness가 존재하므로 무조건 SDK=맨바닥이란 뜻은 아니다.

### 화면 문구

- 완성형: Hermes와 Claude Code
- 개발형: PydanticAI·OpenAI SDK·ADK·Microsoft
- Claude Agent SDK는 Claude Code 실행 기능과 연결

### 단계별 전개

1. Hermes·Claude Code 강조
2. 개발형 프레임워크 묶음 등장
3. Claude Agent SDK→Claude Code 런타임 연결

### 원문 도식 요구

왼쪽 완성형 제품 카드 2개, 오른쪽 개발형 4개와 Claude Agent SDK를 다른 모양 연결 카드로 표시. 상단에 사용자 운영 책임의 연속선; 절대적 양분이라는 문구는 쓰지 않는다.

출처: BASE, S, C, M

## S03 — 같은 합성 사례로 일곱 기술의 실행을 비교한다

실제 반도체 제조 데이터가 아닌 교육용 고정 CSV/SQLite만 사용한다. 모델이 만들어 낸 원인 설명은 검증된 인과관계가 아니라 가설임을 명시한다. 동일 작업을 여러 런타임에 통과시켜 차이를 시각화한다.

### 화면 문구

- 합성 LOT-A / BIN-X / synthetic-v1
- 지표 조회·원인 후보·예측을 공통 사례로 사용
- 데모 실행은 후속 단계에서 검증

### 단계별 전개

1. 합성 시나리오
2. 관찰 지점 세 개
3. 데모 두 위치

### 원문 도식 요구

합성 자료 배지와 세 단계 T1~T3 타임라인. 우측 작은 비교 범주 `누가 루프를 소유? | 무엇을 개발? | 어떤 확장이 특기?`.

출처: BASE

## S04 — Hermes는 실행 루프가 이미 들어 있는 완성형 Agent다

프롬프트만 던져 모델이 알아서 코드를 실행하는 것이 아니다. Hermes 런타임이 모델 응답의 구조를 해석하고 실제 Tool Handler에 전달한다. 완성형이라고 운영 정책이 자동 보장되는 것은 아니다.

### 화면 문구

- 입력 채널이 달라도 AIAgent 실행 흐름으로 모인다
- 모델 연결·Tool Dispatch·대화 기록을 런타임이 조정
- 개발자는 확장 도구·정책·실행 환경을 구성

### 단계별 전개

1. 입력→AIAgent
2. Model 왕복
3. Tool·기록·보안 영역
4. 운영 접점 강조

### 원문 도식 요구

첫 Hermes 마스터 H-ARCH 완전 지도: CLI/Gateway/Cron → AIAgent → Provider ↔ Model; AIAgent ↔ Tool Registry/MCP/Plugin; 아래 Session DB/Memory/Skills; 위험 경로에 Approval/OS. Cron은 새로운 run 라인으로 분리.

출처: H-ARCH, H-LOOP

## S05 — 한 번의 사용자 요청은 이렇게 흘러간다

일반 Agent Loop를 Hermes의 실행 관점으로 보여준다. `run_conversation()`이 사용자 턴을 처리하고, 내부 턴 모듈이 요청·응답·도구 분기를 담당한다. 모델이 호출을 제안하지만 파일·명령을 직접 실행하지는 않는다.

### 화면 문구

- ① 입력과 이전 대화로 모델 요청을 만든다
- ② 모델의 Tool Call을 실행하고 결과를 되돌린다
- ③ 최종 응답이 나올 때까지 필요한 만큼 반복한다

### 단계별 전개

1. 입력/메시지 준비
2. 모델이 구조화된 Tool Call 반환
3. Runtime Tool 실행/Tool Result 저장
4. 모델 재호출 또는 종료

### 원문 도식 요구

H-ARCH 확대. 좌→우 `User → AIAgent → LLM → Tool Call → Registry/Handler → Tool Result → LLM → Final`의 곡선 루프. 화살표마다 `모델이 요청`, `런타임이 실행` 표기.

출처: H-LOOP

## S06 — 모델은 요청하고, Runtime이 Tool을 실행한다

모델은 요청자이고 Hermes의 코드는 집행자다. Tool Schema는 모델에 기능을 설명하지만 실제 구현·인증·DB 권한은 Tool 측에 있다. 단순히 JSON 형태의 문장이 나왔다고 Tool Calling이 된 것은 아니다.

### 화면 문구

- 모델: Tool 이름과 입력 인자 제안
- 런타임: 사용 가능 여부·권한 확인 후 Handler 실행
- 결과: Tool 메시지로 다시 모델 입력에 합류

### 단계별 전개

1. 모델 요청
2. 정책/Handler 경계
3. 결과 메시지
4. 허가 실패는 실제 실행이 아님

### 원문 도식 요구

세로 스윔레인 `LLM / Hermes Runtime / Tool·OS`; example call `get_bin_ratio({lot_id:"LOT-A"})` → Read-only DB → `{"ratio":0.12,...}`. 값은 예시 표기. 아래 허가되지 않은 Tool 분기 표시.

출처: H-LOOP, H-TOOLS

## S07 — 대화 Loop와 Tool 실행 코드는 경계가 나뉜다

소스의 구조를 읽는 법을 보여준다. 최신 소스는 모듈로 나뉘므로 과거 모든 로직이 run_agent.py 한 파일에 있다고 설명하지 않는다. 실제 코드 인용은 사용한 태그·라인을 명시하고, 의사 코드는 반드시 표시한다.

### 화면 문구

- 외부 접점: run_agent.py
- 반복과 분기: conversation_loop.py
- Tool 실행: tool_executor.py / model_tools.py

### 단계별 전개

1. 퍼블릭 API와 Loop의 위치
2. 응답의 Tool Calls 검사
3. Executor로 위임
4. 다음 Iteration으로 복귀

### 원문 도식 요구

왼쪽 8줄 의사 코드, 오른쪽 실제 파일 경로 3개 카드; 소스 라인 범위를 검증해 링크하도록. 실제 코드가 짧게 맞으면 해당 릴리스의 원문 6~12줄로 교체할 수 있다.

출처: H-ARCH, H-LOOP, H-SRC

## S08 — Tool 실패와 강제 중단은 처리 경로가 다르다

Agent가 Tool 오류를 받으면 모델이 수정된 인자로 다시 시도할 수 있지만, 모든 오류가 자동 복구되지는 않는다. 안전상 중단과 평범한 예외를 분리한다. 외부 부작용이 있는 Tool을 무작정 반복 호출하면 중복 실행 위험이 있다.

### 화면 문구

- 인자 오류·접근 거부·Tool 예외를 구분
- Runtime은 실패 결과를 기록하거나 실행을 중단
- 모델 재질문·재시도는 정책과 남은 반복 예산에 따름

### 단계별 전개

1. Tool 시작
2. 오류 유형 분기
3. Runtime 처리와 모델 재검토

### 원문 도식 요구

한 개 Tool Call에서 3가지 분기: 정상 결과→다시 모델, 인자/도구 에러→Tool Result/재검토, 강제 승인 거부·취소→중단. 재시도가 자동 동일 DB 쓰기로 이어지는 형태를 금지.

출처: H-LOOP, H-TOOLS

승인 거부가 항상 전체 run 중단을 뜻하지 않는다. Tool 실패 반환과 정책에 의한 강제 run 종료를 구분한다. 화면은 세 가지 가능한 처리 범주를 설명한다.

## S09 — 모델은 조립된 입력만 보고 판단한다

Hermes는 시스템 프롬프트를 단계별로 조립하고, 세션에서 재사용 가능한 스냅샷과 API 호출 시 임시 맥락을 구분한다. 메모리 파일은 저장된 사실이나 지침이지 LLM의 자체 파라미터 업데이트가 아니다.

### 화면 문구

- System Prompt + 대화 History + 사용 가능한 Tool Schema
- Memory/Skill은 필요 시 프롬프트나 Tool을 통해 반영
- DB 전체와 실제 OS 상태가 자동으로 전달되지는 않는다

### 단계별 전개

1. Prompt 층
2. History와 Tool Schema 합류
3. 모델에 보이지 않는 실행 상태 강조

### 원문 도식 요구

세 개 프롬프트 층 카드 `stable/context/volatile` → 모델 요청. 측면에 모델이 보지 못하는 OS/DB 원본·Credential 저장소를 점선 경계로 배치.

출처: H-PROMPT, H-SESSION

## S10 — Cache는 연산을 재사용하고, Compaction은 이력을 줄인다

Cache는 전송된 이력을 줄이는 기능이 아니다. Compression은 입력 History 자체를 요약·재배치하므로 증거 누락 위험이 있다. 실제 트리거 임계값이나 보호 개수는 설치 버전에서 확인한 값만 발표에 쓴다.

### 화면 문구

- Prefix Cache: 같은 접두부의 연산 재사용
- Compaction: 이력을 요약해 입력 크기 축소
- 캐시 지원 조건과 요약 정보 손실을 구분

### 단계별 전개

1. 긴 History 문제
2. Prefix Cache 동작
3. Compaction과 손실 위험

### 원문 도식 요구

위아래 두 타임라인. 위 Prefix 동일 앞부분을 파란 막대로, 아래 10개 메시지→요약+최근 N개 메시지로 축약한 형태. 출처 버전별 차이는 노트에.

출처: H-LOOP

## S11 — Session·Memory·Skill은 저장 목적이 다르다

Session DB, 기억 파일, Skill을 모두 장기 메모리라고 부르면 안 된다. 과거 대화 검색은 FTS5를 사용하는 사례가 있으나 매번 임베딩 RAG가 작동한다고 주장하면 오류다. 어느 자료가 모델에 들어가는지는 시점과 설정에 따라 달라진다.

### 화면 문구

- Session: 그 대화에서 실제 오간 메시지·Tool 결과
- Memory: 다음에도 유용한 사실·선호·메모
- Skill: 반복 가능한 절차·작업법

### 단계별 전개

1. Session 소개
2. Memory 소개
3. Skill 소개 및 비교

### 원문 도식 요구

3단 적층 카드: SQLite+FTS5/대화 검색, MEMORY.md·USER.md/사실, Skills/절차. 화살표는 Memory 또는 Skill이 필요 시 다음 프롬프트/Tool에 반영되는 경우에만.

출처: H-SESSION, H-MEMORY, H-SKILL

## S12 — 기록한 경험과 절차를 다음 실행에 재사용한다

Hermes의 자기개선이라는 표현은 경험의 외부 기록과 절차 업데이트를 의미한다. 모델의 파라미터 자체를 매 턴 fine-tuning한다고 오해하지 않게 설명한다. 자동 작성·승인 여부는 해당 설정에 따라 달라지며 실제 검증한다.

### 화면 문구

- 대화 중 얻은 유용한 사실을 Memory로 보존
- 반복 작업 절차를 Skill로 정리해 재사용
- 검색·저장·로드는 명시적 경로와 조건을 거친다

### 단계별 전개

1. 발견
2. Memory/Skill 저장
3. 다음 실행에 적용
4. 학습(재학습)과 구별

### 원문 도식 요구

`사용→발견→Memory 또는 Skill 생성/수정→다음 요청에서 활용` 순환 고리. LLM 모델 가중치 변경과는 분리해 작은 X 마크.

출처: H-MEMORY, H-SKILL

## S13 — Tool·MCP·Plugin은 같은 확장이 아니다

MCP는 실행 계약이지 모델이 직접 서버를 호출하는 기능이 아니다. Hermes가 MCP 클라이언트를 통해 요청하고 실제 서버의 실행은 서버 쪽에서 일어난다. Plugin은 Tool 등록뿐 아니라 Hook으로 생명주기에 관여할 수 있다.

### 화면 문구

- Tool: Agent가 호출하는 작업 단위
- MCP: 외부 Tool/Resource를 연결하는 통신 규약
- Plugin: Tool·Hook 등 런타임 확장 등록

### 단계별 전개

1. Built-in Tool
2. MCP 왕복
3. Plugin·Hook 경계

### 원문 도식 요구

H-ARCH 확대. 내부 Tool Registry에 Built-in Tool, MCP client↔외부 MCP server, Plugin→Registry/Hook의 서로 다른 3색 경로. Code source를 LLM에 통째로 전달하는 화살표 금지.

출처: H-TOOLS, H-ARCH

## S14 — 실행 통제는 승인과 OS·DB 권한에서 이루어진다

Hermes의 위험 명령 승인 기능이 모든 도구와 외부 시스템의 보안을 보장한다고 확대하지 않는다. 승인과 인증/인가, 실패 처리, Tool 결과 기록은 다른 단계다. 합성 데모는 읽기 전용을 기본으로 한다.

### 화면 문구

- 모델의 지시 준수만으로 위험 Tool을 막을 수 없다
- Tool Dispatch 전 승인과 실행 환경 권한이 중요
- 실제 DB 읽기/쓰기 권한은 운영 환경에서 강제

### 단계별 전개

1. 요청
2. 허용/승인
3. 실제 권한
4. 거부와 Tool 에러

### 원문 도식 요구

LLM→요청→위험도 평가/승인→Tool Handler→DB ACL 연속 게이트. 불허 시 Tool 호출 실패 반환. OS/DB 권한은 Tool Handler 바깥 이중 벽.

출처: H-TOOLS

## S15 — Tool 병렬과 Subagent 위임은 구조적으로 다르다

병렬 Tool은 호출 단위 동시성이고 subagent는 별도의 모델-도구 반복 수명을 만든다. 컨텍스트가 별개여도 파일·OS·DB까지 자동 격리되지는 않는다. 같은 데이터 읽기는 합성 예제로 보여준다.

### 화면 문구

- 병렬 Tool: 하나의 Agent 턴에서 여러 Handler 호출
- Subagent: 별도 실행 문맥을 가진 하위 Agent에 작업 위임
- 반환 결과·맥락·공유 자원 및 충돌 위험이 달라진다

### 단계별 전개

1. 병렬 Tool
2. Subagent 생성
3. Parent 복귀와 공유자원 주의

### 원문 도식 요구

윗줄 LLM→2 Tools→동일 Parent Loop. 아랫줄 Parent→Child Agent Loop↔LLM/Tools→Summary→Parent. Shared filesystem은 별도 점선 경계.

출처: H-LOOP, H-TOOLS

## S16 — CLI·Gateway·Cron은 실행을 시작하는 방식이 다르다

입력 채널은 하나의 실행 엔진 위에서 돌아갈 수 있으나 각 실행의 권한과 History는 동일하다고 가정할 수 없다. Cron이 기존 사용자의 대화 한 턴을 그대로 재생한다고 단정하지 않는다.

### 화면 문구

- CLI: 사용자의 직접 대화
- Gateway: 플랫폼 메시지를 인증·세션 라우팅
- Cron: 정해진 시각에 새로운 작업 실행

### 단계별 전개

1. CLI 경로
2. Gateway 경로
3. Cron 경로 및 기존 대화와의 차이

### 원문 도식 요구

세 레인 입력 경로가 AIAgent에 모이지만 Gateway의 사용자/세션 바인딩과 Cron의 새 실행을 별도 점선 박스로 표시.

출처: H-ARCH

## S17 — Hermes가 제공하는 실행 구조 위에 업무를 확장한다

직접 모든 Agent Loop를 구현하지 않고 시작할 수 있다. 대신 사내 데이터용 읽기 전용 도구, 사용자 권한, 로그 정제, 재현 가능한 분석 데이터는 애플리케이션 담당자가 만들거나 구성해야 한다.

### 화면 문구

- 이미 있는 것: 대화 Loop·기본 Tool·세션·다중 진입점
- 설정/확장할 것: 모델·Tool·Skill·플랫폼·승인 규칙
- 직접 책임질 것: 데이터 접근권·업무 검증·운영 장애

### 단계별 전개

1. Hermes 제공
2. 추가 개발/설정
3. 도입 전 운영 책임

### 원문 도식 요구

좌 `Hermes 제공`, 우 `프로젝트 책임` 두 리스트와 가운데 합성 LOT 쿼리 Tool 연결.

출처: H-ARCH

## S18 — Hermes 실행 검증은 요청과 결과를 연결해야 한다

실제 실행 Trace를 재생할 때는 모델 출력 텍스트, Tool 인자, 실제 DB 결과와 최종 응답을 구별한다. 로컬/대상에서 아직 실행하지 못했다면 ‘실행 전’으로 표시하고 합성 예시를 실제 관측이라고 표기하지 않는다.

### 화면 문구

- T1: 합성 LOT-A의 BIN-X 비율 조회
- 요청·handler·결과·최종 응답을 연결해 확인
- 실행 전: 실제 Trace와 event_id는 아직 없음

### 단계별 전개

1. 합성 질문과 스냅샷
2. 모델 요청·Tool Call 수집 계획
3. Tool 결과·반환 확인 계획
4. 실행 전 상태와 다음 검증 안내

### 원문 도식 요구

데모 시작 연결 카드: H-ARCH 미니맵 + 별도 viewer URL / `event_id` 매핑. 시연 순서 외의 클릭 UI 없음.

출처: H-LOOP, DEMO

이번 전달본은 실행 전 계획이다. Viewer 이동·캡처·event_id·실제 Trace는 제공하지 않는다.

## S19 — Hermes 검증에서는 네 가지 증거를 확인한다

T1과 T2의 실제 순서, 실패도 관찰된 순서로만 기술한다. 시험에서 발생하지 않은 거부/재시도는 별도 계획 샌드박스 테스트로만 표현한다. 도메인 계산의 사실성은 모델이 아니라 결정적 Tool 결과로 검산한다.

### 화면 문구

- Tool Call ID와 실제 결과를 연결
- 오류 처리와 History 갱신을 관찰
- Session 저장과 Memory 갱신을 구별

### 단계별 전개

1. 요청 증거
2. 실제 handler 증거
3. History 갱신 증거
4. 저장·오류 경계의 확인 계획

### 원문 도식 요구

별도 Trace viewer의 4개 예시 캡처 슬롯: 요청/Tool/result/history. 저장된 이벤트가 없으면 Placeholder `[미검증]`를 명시.

출처: DEMO, H-SESSION

이번 전달본은 실행 전 계획이다. Viewer 이동·캡처·event_id·실제 Trace는 제공하지 않는다.

## S20 — Harness가 제공하는 기능과 운영 책임을 구분한다

어떤 작업이 Agent 자체에서 진행되고 어떤 부분이 외부 DB/서비스의 몫인지를 정리한다. 이제 유사하게 완성형인 Claude Code가 코딩 환경에 맞게 무엇을 더 잘 묶는지 보겠다고 자연스럽게 연결한다.

### 화면 문구

- 구현된 Harness를 빠르게 활용할 수 있다
- Loop·Prompt·Tool·Memory·Gateway의 책임 경계가 분명하다
- 품질·권한·데이터 진실성은 운영 설계가 결정한다

### 단계별 전개

1. 완성형 장점
2. 책임 경계
3. Claude Code와 비교 질문

### 원문 도식 요구

H-ARCH 전체 재등장. 이미 설명한 노드는 회색, `제공됨`과 `직접 설계`만 색 윤곽선. 다음 Claude Code로 향하는 연결 화살표.

출처: H-ARCH

## S21 — Claude Code도 기본 Agent Loop는 Hermes와 닮았다

청중은 Hermes Loop를 방금 봤으므로 처음부터 다시 설명하지 않는다. Claude Code는 코딩 Harness를 제공하지만 내부 엔진 전체의 구현 세부는 공개 문서 범위를 넘어서 단정하지 않는다.

### 화면 문구

- 공통: 모델과 Tool을 반복하는 실행 구조
- 파일·명령 실행은 Runtime과 Tool이 담당
- 차별점은 프로젝트 규칙과 개발 도구 통합

### 단계별 전개

1. 공통 Loop 4노드
2. Tool/상태 공통점
3. 차별 영역만 보라 테두리

### 원문 도식 요구

좌 Hermes 미니맵, 우 Claude Code 마스터 C-ARCH. 공통 구성 노드를 동일 모양으로 정렬하고 차별 영역(IDE, project rules, edit/test workflow)만 강조.

출처: C

## S22 — Claude Code의 주 무대는 실제 개발 작업 환경이다

차별점은 Agent의 정의가 아니라 코드 작업을 위해 도구와 프로젝트 문맥, 테스트·git·IDE를 통합한 실행 환경이다. 단순 채팅보다 실제 저장소 변경과 검증에 초점을 둔다.

### 화면 문구

- 코드베이스 탐색 → 파일 수정 → 명령/테스트 실행
- CLI·IDE·Desktop 등 개발 접점과 연결
- 여러 파일·프로젝트 규칙을 함께 고려

### 단계별 전개

1. 개발 요청
2. 탐색·수정·시험 실행
3. 도구/규칙/정책
4. 별도 내부 구현 비공개 경계

### 원문 도식 요구

C-ARCH 전체 지도: Terminal/IDE→Claude Code Harness↔LLM; Read/Edit/Bash/MCP; CLAUDE.md/Skills/Memory; Permissions/Hooks/Sandbox; Subagents. 기능별 소유권 라벨.

출처: C

## S23 — CLAUDE.md·Skill·Memory가 프로젝트 맥락을 제공한다

해당 파일과 기능의 우선순위·로드 경로는 버전/설정에 따라 검증한다. 규칙을 기록했다고 그 자체로 OS 수준 실행 제한이 걸리는 것은 아니다. 코딩 작업 품질의 반복성을 만드는 방법이라는 점에 집중한다.

### 화면 문구

- CLAUDE.md: 프로젝트별 지속 지시·규칙
- Skill: 특정 작업에서 불러 쓰는 절차
- Memory: 이전 작업에서 남긴 유용한 맥락

### 단계별 전개

1. 규칙 파일
2. Skill
3. Memory와 구분

### 원문 도식 요구

프로젝트 트리 아이콘과 3개 다른 접근 패턴(상시 지시/필요시 로드/자동 저장·검색). 모두 매번 전문이 주입된다고 표시하지 않는다.

출처: C-MEM, C-SKILL

## S24 — Permissions·Hooks·Sandbox는 서로 다른 경계를 통제한다

프롬프트로 “삭제하지 마”라고 하는 것과 실제 권한 차단은 다르다. Hook은 이벤트마다 반환 코드·실행 방식이 다를 수 있고 샌드박스도 플랫폼/설정 의존적이다. 해당 버전 공식 문서에서 실행 순서를 확인한 경우에만 정확한 순서로 표시한다.

### 화면 문구

- Permissions: Tool 호출 허용·승인 정책
- Hooks: 정해진 지점에서 사용자 코드 개입
- Sandbox: 실제 실행 환경의 접근 범위 제한

### 단계별 전개

1. Permission 판단
2. Hook 개입
3. Sandbox/OS 경계

### 원문 도식 요구

`모델 요청 → Permissions → Hooks(적용 지점별) → Sandbox/OS → Tool` 계층도. Hooks가 항상 Permission 앞뒤 동일하게 호출된다고 고정하지 말고 종류별 위치 노트 표시.

출처: C-POLICY, C-HOOK, C-SANDBOX

## S25 — Subagent와 Agent Teams는 협업 방식이 다르다

작업을 분담해 코딩 생산성을 높이지만 파일/브랜치/공유 상태 충돌을 자동으로 막아주지는 않는다. Teams 지원 여부는 제품 기능 플래그·버전·환경에서 확인하고 미지원이면 그 조건을 밝힌다.

### 화면 문구

- Subagent: 특정 역할에 작업을 맡기고 결과를 부모에 전달
- Agent Teams: 구성원 간 조정·공유 작업 관리가 핵심
- 독립 Context가 곧 독립 파일 시스템은 아니다

### 단계별 전개

1. Subagent 위임
2. Teams 구조
3. 동시 편집과 권한 관리 주의

### 원문 도식 요구

윗줄 Parent→Subagent→Summary; 아랫줄 Team lead ↔ 팀원 2명/공유 태스크. 모델 비용·충돌 위험 아이콘.

출처: C-SUB, C-TEAM

## S26 — Claude Code는 변경 계획부터 테스트까지 연결한다

코딩 중심 환경에서의 장점을 보여준다. 전자동 성공이나 모든 코드 정확도를 보장하지 않으며 실제 diff와 테스트 결과는 개발자가 검사한다. Hermes와 같은 구조를 다시 강의하지 않는다.

### 화면 문구

- 요구 분석 → 변경 계획 → 코드 수정 → 테스트 → 검토
- 역할별 Subagent로 분담하고 주 실행에서 통합
- Hooks/CI/승인으로 품질 관문 배치

### 단계별 전개

1. 작업 계획
2. 수정·검증
3. 권한·검토 및 회고

### 원문 도식 요구

4단 코드 워크플로와 중간 HITL gate, 서브에이전트 분기 후 합류. 구체적 개발자/검토자 역할 카드를 강조.

출처: C

## S27 — Hermes와 Claude Code는 주된 작업 환경이 다르다

비교의 핵심은 어떤 Agent가 더 똑똑한지가 아니다. 반복 운영·멀티채널 작업과 저장소 기반 개발 업무의 주 무대가 다르다. 둘 모두 LLM 제공자와 실행 환경을 구성해야 한다.

### 화면 문구

- Hermes: 다채널·주기 작업·Memory/Skill 운용
- Claude Code: 저장소 탐색·수정·테스트
- 권한·데이터·상태의 운영 책임은 공통

### 단계별 전개

1. 공통점 빠른 복기
2. 차별점만 비교
3. 상황별 선택 예시

### 원문 도식 요구

동일 축 2열 비교: 주된 진입점, 작업 단위, 확장/정책, 직접 개발 범위. 승자 배지/성능 순위 금지.

출처: H-ARCH, C

## S28 — SDK를 쓰면 앱이 Agent 구성요소를 조립한다

개발형 SDK도 Agent Loop의 상당 부분을 구현해주므로 “Loop를 전부 직접 짜야 한다”는 뜻이 아니다. 핵심은 도메인 애플리케이션, 저장·API·정책 조립과 운영 책임이 더 선명해진다는 것이다.

### 화면 문구

- 완성형: 기존 앱에서 실행 루프·도구를 주로 설정/확장
- SDK: 애플리케이션 코드가 Agent 정의·Tool·상태 결합
- PydanticAI는 이 경계를 가장 먼저 보여줄 사례

### 단계별 전개

1. 완성된 런타임
2. 앱 소유의 구성요소
3. PydanticAI 도입

### 원문 도식 요구

Hermes/Claude Code의 통합 Runtime 카드가 부품 `Agent/Tool/State/API/Policy` 형태로 분해되어 개발자 앱으로 이동하는 전환 애니메이션.

출처: P-AGENT, O

## S29 — PydanticAI는 Agent를 Python 애플리케이션 안에 만든다

Pydantic 자체는 Agent가 아니고 PydanticAI Core는 모델 호출과 Tool Loop를 제공한다. 선택 Harness가 있다는 이유로 모든 PydanticAI Agent가 컴퓨터 사용 Agent로 실행되는 것은 아니다.

### 화면 문구

- Pydantic: 데이터 구조·검증 라이브러리
- PydanticAI Core: 실행 Loop·Tool·Output·Retry 제공
- 선택 Harness/Capability는 Core와 별도 계층

### 단계별 전개

1. Pydantic 구분
2. PydanticAI Core 추가
3. 선택 Harness 구분

### 원문 도식 요구

`Pydantic(타입)` → `PydanticAI Core(Agent Loop)` → `(선택) Harness`를 각기 다른 경계로 그린 계층도. Core만으로 업무 Agent 구현 가능 표시.

출처: P-AGENT, P-OUTPUT

## S30 — 앱 코드와 Core가 서로 다른 일을 맡는다

화면상 개발자가 얼마나 코딩해야 하는지 한 번에 전달한다. 실제 모델 클라이언트 생성과 Provider adapter는 버전별로 다르므로 사용하는 릴리스 기준으로 코드를 확인한다.

### 화면 문구

- 직접: Agent 설정·도메인 Tool 함수·Deps·Output 타입
- Core 제공: 모델 왕복·Tool 인자 처리·검증·재시도·종료
- 별도 구현: API 서버·DB 권한·업무 규칙·영속화

### 단계별 전개

1. 개발자 작성 블록
2. Core 내부 실행
3. 운영 애플리케이션 책임

### 원문 도식 요구

P-ARCH 전체 지도. 파란선 `app-owned`에 Agent 선언/Deps/DB, 보라선 `Core`에 내부 Graph/Tool Manager/output, 외부 Provider Model. 읽기 전용 Lot Tool 예시 연결.

출처: P-AGENT, P-TOOLS

## S31 — Agent·Tool·Output을 Python 코드로 연결한다

예시 코드는 프로젝트가 채택한 PydanticAI 버전에서 직접 실행·수정한 뒤에만 `[실행 가능]` 표기를 붙인다. 아래 샘플은 개념을 보여주는 것이고 모델 및 인증 설정은 후속 환경 설정에서 주입한다. 타입 검증은 분석 결과의 사실성 검증이 아니다.

### 화면 문구

- 모델·Instructions·Output 타입을 선언
- Python Tool을 등록하고 앱 자원을 연결
- run 결과를 앱의 후속 처리에 사용

### 단계별 전개

1. Agent/타입 선언
2. Tool 함수 등록
3. Run 호출/결과 처리

### 원문 도식 요구

왼쪽 실제 코드 14줄 이하, 오른쪽 `앱 선언 → Core Loop → Tool → Result` 미니 다이어그램. Tool에서는 합성 fixture만 조회하도록.

출처: P-AGENT, P-TOOLS

화면의 API 형태는 공개 문서와 대조했다. model과 read_synthetic_fixture는 앱이 주입하는 이름이며 독립 실행 파일이 아니다. 실제 모델 호출은 하지 않았다.

## S32 — Core는 모델 응답에 따라 Tool과 종료로 분기한다

이 노드 명칭은 해당 공개 구현에서 쓰이는 내부 Graph 설명이다. `pydantic-graph`로 개발자가 별도 workflow를 만든 것과 혼동하지 않는다. 모델 응답에 따라 Tool 단계가 생략되거나 반복된다.

### 화면 문구

- 시작: UserPromptNode에서 입력을 준비
- 중간: ModelRequestNode ↔ CallToolsNode 반복
- 종료: 검증된 최종 Output 또는 에러/제한

### 단계별 전개

1. UserPrompt
2. ModelRequest
3. CallTools
4. End/Retry

### 원문 도식 요구

내부 Graph의 주요 Node 3개와 End. 조건 화살표 `tool?`, `final output?`, `retry/error?`. 앱의 외부 workflow graph와 명시적으로 분리.

출처: P-AGENT, P-SRC

## S33 — Instructions·Deps·History는 전달 범위가 다르다

`RunContext.deps`의 DB 핸들은 모델 프롬프트로 자동 직렬화되지 않는다. Tool이 결과를 반환한 뒤 해당 텍스트/값만 모델에 노출될 수 있다. 대화 History를 DB에 장기 영속화하는 것은 앱 정책에 달려 있다.

### 화면 문구

- Instructions: 모델에 전달할 지침
- Deps: Tool이 접근하는 Python 런타임 의존성
- History: 앱이 전달/관리하는 대화 문맥

### 단계별 전개

1. 모델 입력
2. 런타임 Deps
3. DB 연결·History 유지 책임

### 원문 도식 요구

왼쪽 모델 입력 상자(Instructions, 전달 History, Tool Schema)와 오른쪽 런타임 Deps(DB client/권한 Context). Deps에서 모델로 직선 화살표 금지.

출처: P-AGENT, P-TOOLS, P-DEPS

## S34 — Schema 뒤에도 검증과 실제 함수 실행이 남는다

Pydantic 기반 검증은 타입과 형태를 보장하지만, 특정 Lot을 볼 권한과 계산의 참인지를 보장하지 않는다. Tool 안에 권한 검증과 결정적 계산을 구현해야 한다.

### 화면 문구

- 모델 요청 인자를 Python 함수 인자로 검증
- Tool 함수가 실제 읽기/계산을 수행
- 실패·재시도·권한 거부는 별도 경로

### 단계별 전개

1. Schema 제공
2. 입력 검증
3. 실제 함수 실행
4. 실패 분기

### 원문 도식 요구

`JSON schema → model tool call → validation → Python function → result` 횡단 파이프라인; 입력 오류는 검증 루프로, 권한 부족은 실제 실행 차단으로 분기.

출처: P-TOOLS

## S35 — Output 타입은 구조를 검증하고 후속 처리를 돕는다

Output 방식은 Tool 기반/Native JSON Schema/Prompted 등 모델·설정에 따라 달라진다. 모든 제공자·vLLM 서버가 같은 방식을 자동 지원한다고 단정하지 않는다.

### 화면 문구

- 자연어 대신 정해진 BinResult 구조로 받기
- 모델 출력의 형식·타입 검증과 재시도 지원
- 유효한 JSON도 도메인 정답과는 별개

### 단계별 전개

1. 자유 형식
2. 타입 지정 출력
3. 검증·재시도 및 한계

### 원문 도식 요구

왼쪽 `"12%쯤..."` 자유 텍스트, 오른쪽 `lot_id/ratio/snapshot_id` Pydantic 구조. Schema 실패 화살표→Retry.

출처: P-OUTPUT

## S36 — 종료 정책에 따라 남은 Tool의 실행이 달라진다

`early`가 무조건 모든 Tool을 실행한다거나 `exhaustive`가 정확히 한 번 쓰기 보장을 제공한다고 설명하면 안 된다. 함수 Tool과 Output Tool의 유형, streaming에서 종료를 발견하는 시점에 따라 결과가 바뀔 수 있다. 데모는 읽기 전용 경로를 기본으로 하고 부작용은 Mock에서 시험한다.

### 화면 문구

- 유효한 Output Tool과 함수 Tool이 함께 온 경우
- early / graceful / exhaustive를 구분
- Streaming 확정 시점과 부작용은 별도 검토

### 단계별 전개

1. 동일 응답에서 두 신호
2. 종료 정책 분기
3. Side effect 유의사항

### 원문 도식 요구

하나의 모델 응답이 `final output + read-only lookup + write report`를 동시에 포함한 경우의 2갈래 결정 트리. 정확한 `early/exhaustive` 결과는 코드·공식 문서에 맞춰 검증하여 기재.

출처: P-OUTPUT

현재 공식 Output 문서에서 graceful이 기본값이다. 화면 표는 유효한 Output Tool이 포함된 경우이며 plain text와 Native/Prompted output의 혼합 조건에는 그대로 일반화하지 않는다. Streaming은 첫 적합 출력을 확정하는 시점이 달라진다. 실제 설치 릴리스에서는 재검증한다.

## S37 — 병렬 Tool 실행과 안전한 순서는 다르다

‘병렬 Tool Call을 모델이 생성’과 ‘Python 실행이 실제 병렬’은 다른 사실이다. 설치 버전의 설정과 측정 로그를 통해 실제 병렬 수행 여부를 확인한다.

### 화면 문구

- 서로 독립인 읽기 Tool은 병렬 처리 가능
- 순서가 중요한 Tool은 직렬화·동기화가 필요
- 비결정적 완료 순서와 결과 해석은 분리

### 단계별 전개

1. 병렬 조회
2. 결과 합류
3. 순서 필요한 Tool

### 원문 도식 요구

두 read-only 함수가 병렬 출발해 Join하는 도식과 `승인→게시`가 순서 의존적인 직렬 도식. 런타임/프로바이더/버전 설정으로 동작 검증 후 표시.

출처: P-TOOLS, P-ADV

## S38 — 실행 API마다 결과를 받는 방식이 다르다

시그니처·스트리밍 출력 확정 조건은 버전 의존적이다. 발표 본문에는 가장 자주 쓰는 세 가지 사용 차이만, `iter`/`run_stream_events` 등 기타 실행 API는 발표자 노트의 참고로 남긴다.

### 화면 문구

- run: async 최종 결과
- run_sync: 동기 코드에서 실행
- run_stream: 생성 중 결과를 스트리밍

### 단계별 전개

1. run
2. run_sync
3. run_stream 및 주의

### 원문 도식 요구

세 개 API 카드와 아래 내부 Core Loop 공통 박스. 실행 방식과 Tool 정책을 독립 축으로 두고 API 하나씩만 설명.

출처: P-AGENT

## S39 — 승인 결과와 History를 전달해 실행을 이어간다

Deferred Tool이나 HITL은 Core/API 버전에 따라 기능과 사용법이 달라진다. 단순 Output validation이 비즈니스 승인까지 해주지는 않는다. 실제 재개 객체·직렬화 방식은 공식 API와 테스트로 확인한다.

### 화면 문구

- 외부 승인 흐름: Deferred 요청을 앱에 반환
- History와 승인·실행 결과로 후속 run 시작
- 외부 부작용의 중복 방지는 앱이 구현

### 단계별 전개

1. 도구 실행 보류
2. 승인·거부
3. 재개와 idempotency

### 원문 도식 요구

`모델 요청→Deferred Tool→Pause/Approval→Resume→Tool` 상태 머신. `RunState`류를 임의로 타 SDK 이름으로 치환 금지.

출처: P-DEFER

외부 승인을 기다리는 stop-the-world 흐름은 DeferredToolRequests로 run을 끝낸 뒤, message history와 DeferredToolResults를 후속 run에 전달한다. 현재 문서에는 같은 프로세스의 handler로 inline 해결하는 선택지도 있다.

## S40 — Python 서비스 안에서 Agent를 제어할 때 적합하다

Hermes처럼 바로 사용 가능한 운영 채팅 도구를 얻는 것과, Python 서비스 안에 Agent 구성요소를 구축하는 것은 다르다. 후자는 세밀한 제어를 얻지만 품질 테스트와 배포를 책임진다.

### 화면 문구

- Python 서비스에 Agent를 직접 내장할 때
- 타입 안정성·Tool 구현·테스트가 중요한 업무
- DB·권한·API 서버를 개발팀이 소유하고 싶을 때

### 단계별 전개

1. Core 제공
2. 개발팀 구현
3. 적합한 도입 사례

### 원문 도식 요구

왼쪽 Core 제공 체크 4개, 오른쪽 앱 개발 체크 4개. 합성 LOT 데이터 조회 서비스 한 개의 전체 컴포넌트 다이어그램.

출처: P-AGENT

## S41 — Python Tool 검증은 함수와 Core의 경계를 확인한다

같은 데이터를 사용하지만 Hermes 제공 도구와 Python에서 직접 작성한 도구라는 구현 차이가 중요하다. 실제 관측 이벤트에 대해 Tool Call ID, Snapshot ID, Python function 결과를 연결한다.

### 화면 문구

- T1: 직접 작성한 get_bin_ratio 함수
- T2: 측정값·유효 SOP를 근거로 원인 후보 제시
- 실행 전: Core와 함수의 실제 이벤트 수집 예정

### 단계별 전개

1. 앱 Agent 정의
2. Python Tool 실행 확인 계획
3. 최종 Output 검증 계획
4. 실행 전 상태와 기록 계획

### 원문 도식 요구

P-ARCH 미니맵과 합성 데이터 T1/T2 타임라인. 별도 PydanticAI Viewer에 연결할 이벤트 ID 자리; 미실행시 미검증.

출처: P-AGENT, DEMO

이번 전달본은 실행 전 계획이다. Viewer 이동·캡처·event_id·실제 Trace는 제공하지 않는다.

## S42 — 검증할 증거도 Core와 앱의 책임에 따라 나뉜다

실행한 로그만 실제 Trace로 표기한다. 중요한 것은 한 엔진의 성능 주장이 아니라 어느 코드가 어떤 값을 생성하고 기록했는지를 보여주는 것이다. Model 응답을 검증한 것과 실데이터가 참임을 확인한 것을 구분한다.

### 화면 문구

- Core: 모델 Loop·인자 검증·결과 수집
- 앱: SQL·계산·권한·검산·영속화
- 실측되지 않은 재시도와 승인은 검증 예정

### 단계별 전개

1. Core 처리의 증거
2. 앱 함수·DB의 증거
3. 검산·저장·예외 검증 계획

### 원문 도식 요구

데모 Trace 3열 `Core 이벤트 / Tool(앱 코드) / 앱 저장`이며 도메인 계산 검산값을 맨 오른쪽에 별도 표시.

출처: P-AGENT, DEMO

이번 전달본은 실행 전 계획이다. Viewer 이동·캡처·event_id·실제 Trace는 제공하지 않는다.

## S43 — Hermes와 PydanticAI는 업무를 연결하는 방식이 다르다

앞선 두 중심 주제를 묶어 청중이 확실하게 이해했는지 확인한다. 이제 다른 SDK에서는 이 조립 방식을 어떻게 다르게 지원하는지 살펴본다.

### 화면 문구

- Hermes: 기존 실행 환경을 설정·확장
- PydanticAI: 앱 코드로 Agent·Tool·Output 조립
- 같은 데이터라도 운영 책임의 배치가 달라짐

### 단계별 전개

1. Loop 소유
2. Tool/DB 경계
3. 운영 책임 및 다음 SDK군

### 원문 도식 요구

H-ARCH와 P-ARCH를 줄여 병렬 배치, `Loop 소유·Tool 개발·상태 영속화·사용자 UI` 네 축만 강조. SDK 그룹으로 전환.

출처: H-ARCH, P-AGENT

## S44 — SDK마다 공통 Loop에 더하는 제어 방식이 다르다

PydanticAI에서 설명한 핵심 흐름을 재사용한다. 이후 각 SDK마다 공통점 복습은 10초 수준으로 제한하고 차별 기능을 집중적으로 제시한다. Claude Agent SDK는 예외적으로 자체 Loop를 처음부터 만든 Python 코어가 아니라 Claude Code 런타임을 코드에서 쓰는 구조다.

### 화면 문구

- 공통: Agent 정의 → Model → Tool → Model 반복
- 공통: 앱 코드가 데이터·권한·배포와 통합
- 비교할 차이: 위임·세션/이벤트·정책·Workflow

### 단계별 전개

1. 공통 Loop
2. 앱 소유 책임
3. 네 가지 차별점만 예고

### 원문 도식 요구

공통 4노드 Agent 루프 1개 + 옆 작은 차별 요소 슬롯 4개(OpenAI/Claude SDK/ADK/Microsoft). 완전 새로운 Agent 강의 반복 금지.

출처: O, S, G, M

## S45 — OpenAI Agents SDK의 Runner가 다음 실행을 결정한다

Agents SDK는 OpenAI의 관리형 Agents API와 다른 실행 선택지다. SDK는 애플리케이션 안에서 Loop를 돌리는 개발용 패키지다. Python 예시를 기본으로 하되 설치 버전과 provider 설정을 검증한다.

### 화면 문구

- Agent: 지침·Tool·Handoff 등 동작 정의
- Runner: 모델 응답에 따라 Tool/위임/최종 출력 분기
- 서버·업무 Tool·저장은 애플리케이션이 소유

### 단계별 전개

1. Agent 선언
2. Runner Loop
3. Tool/Handoff
4. 앱 운영 책임

### 원문 도식 요구

O-ARCH 전체: App→Runner↔Model, Runner→Function Tools/MCP, Runner→Specialist, Guardrails/Approval/Session. Hosted Agent API와 구분 카드.

출처: O

## S46 — Agent-as-Tool과 Handoff의 차이는 제어권이다

위임을 모두 Subagent라고 부르면 컨텍스트와 제어권의 이동을 놓친다. Handoff에서는 활성 Agent가 바뀌고 Tool 방식에서는 상위 Agent가 결과를 받아 계속한다. 옵션에 따라 History 전달 범위 등이 달라질 수 있어 설정을 확인한다.

### 화면 문구

- Agent-as-Tool: 하위 결과를 원래 Agent가 돌려받는다
- Handoff: 활성 Agent가 다른 담당 Agent로 전환된다
- 둘 다 여러 Agent라 해도 실행 주체는 다르다

### 단계별 전개

1. Agent-as-Tool
2. Handoff
3. 누가 최종 응답하나 비교

### 원문 도식 요구

두 스윔레인. 위 Parent→Specialist Tool→Parent 요약, 아래 Agent A→Handoff→Agent B가 사용자 응답. 뒤쪽 현재 소유자 변화를 진한 박스로.

출처: O-ORCH

## S47 — Guardrail·중단/재개는 적용 범위를 확인해야 한다

모든 Guardrail이 모든 Agent의 모든 Tool 호출을 자동 검사한다고 표현하지 않는다. 중단 이후 재개한 Agent 상태가 외부 DB 작업을 정확히 한 번 수행했다는 뜻은 아니다. **활용 예:** 승인/감사가 필요한 업무 서비스에서 특정 Tool만 추가 검사해 실행하는 방식.

### 화면 문구

- Input·Tool·Output 검사는 적용 지점이 다름
- 승인이 필요한 Tool은 실행을 보류할 수 있음
- RunState 복구가 DB 부작용까지 되돌리지는 않음

### 단계별 전개

1. 입력 검사
2. Tool 승인
3. 출력/State·재개 한계

### 원문 도식 요구

Runner Loop에 input guardrail / tool approval / output guardrail을 종류별 다른 위치에 표시. RunState 스냅샷과 외부 DB Transaction의 분리선을 강조.

출처: O-GUARD, O-HITL

## S48 — Claude Agent SDK는 Claude Code 실행 기능을 연결한다

일반 API wrapper로 LLM 요청만 보내는 게 아니라 Claude Code가 제공하는 Agent Loop와 도구 실행 기능을 SDK에서 사용할 수 있다는 점을 보여준다. 구체적 subprocess 구현 방식은 버전·배포 환경에서 검증한다.

### 화면 문구

- 공통: Agent Loop·Tool·Context를 이용
- 차별: Python/TypeScript SDK가 Claude Code 실행 기능을 노출
- 호스트 앱과 CLI 런타임 사이 프로세스 경계가 존재

### 단계별 전개

1. SDK 호출
2. CLI 런타임
3. Tool과 반환 이벤트

### 원문 도식 요구

S-ARCH 전체: Host app↔SDK transport↔Claude Code runtime↔Model; built-in tools/MCP/Permissions/Session 연결. `.query()` 쪽 Host와 CLI 하위 프로세스 명확히.

출처: S, S-SRC

## S49 — 커스텀 MCP Tool은 SDK 경계를 넘어 호스트에서 실행된다

‘SDK 내부에 독립 모델 Loop가 새로 생겼다’는 식으로 그리지 않는다. 파일 checkpoint 기능도 모델/세션 전체와 DB 작업을 원자적으로 되돌리는 기능으로 과장하면 안 된다.

### 화면 문구

- 호스트 코드가 MCP Tool callback을 제공할 수 있음
- 실행 요청은 Runtime↔SDK 경계를 왕복
- Permission·Hook 적용 지점과 Session 유지 확인

### 단계별 전개

1. MCP 요청
2. 호스트 함수 실행
3. 결과 복귀·정책 확인

### 원문 도식 요구

왕복 화살표 `CLI → SDK transport → host MCP callback → SDK transport → CLI`. 옆에 Permission/Hook 보조 통로; 데이터가 어디서 실행됐는지 라벨.

출처: S-MCP

## S50 — 호스트 앱에서 Claude Code 실행을 업무 흐름에 넣는다

Claude Code와 연결된 실행 엔진을 재사용하려는 경우에 적합하다. 단, 모델 제공자/인증 경로가 무엇인지는 해당 환경 공식 문서대로 설정해야 하며 OpenAI 호환 vLLM에 무조건 바로 연결된다고 가정하지 않는다.

### 화면 문구

- 기존 개발용 Agent 기능을 서비스·배치 Python 코드로 호출
- 프로젝트 도구·권한·세션 이벤트를 프로그래밍으로 관찰
- 실행 환경·설치·비밀키와 비용 관리는 호스트가 책임

### 단계별 전개

1. 서비스에서 호출
2. 상태/Tool 이벤트 수집
3. 호스트 운영 주의

### 원문 도식 요구

호스트 앱 workflow 3단계 `작업 요청→SDK/CLI 실행→결과·산출물 저장`과 최소 Python 호출 형태(검증 후 코드 삽입) 카드.

출처: S

## S51 — ADK는 Event로 실행과 세션 상태를 연결한다

구글 모델만 써야 하는 프레임워크로 단정하지 않는다. 여러 모델/provider 연결의 지원 범위는 별도 확인한다. 사용자에게 보여주는 텍스트와 Session에 반영되는 상태 변화가 Event 흐름에서 어떻게 연결되는지 보여준다.

### 화면 문구

- Runner가 Agent 실행·세션과 연결
- Agent/Flow가 Tool과 Model 단계를 진행
- Event가 출력·상태 변경을 전달하고 기록

### 단계별 전개

1. Runner
2. Flow/Tool
3. Event→Session

### 원문 도식 요구

G-ARCH 전체 `Caller→Runner→Agent/Flow↔Model`, Tool, `Event→SessionService`, Memory/Artifact 별도 저장 영역. Flow 개념은 설치 버전 따라 확인.

출처: G

## S52 — ADK의 순차·병렬 Agent는 Tool 병렬과 다르다

ADK의 workflow agent와 일반 LLM Agent의 역할을 구분한다. 병렬 실행 결과를 한곳에 저장할 때 경합·상태 충돌 가능성을 다룬다. 최신 graph workflow 기능이 있더라도 해당 릴리스의 지원 여부를 정확히 기재한다.

### 화면 문구

- Sequential: Agent를 정해진 순서대로 실행
- Parallel: 독립 Branch Agent를 실행 후 결과 수집
- 일반 Tool 병렬과 Workflow 제어는 구분

### 단계별 전개

1. Sequential
2. Parallel
3. Tool parallel과 대비

### 원문 도식 요구

위 2 Agent sequential, 아래 parallel fork/join, 오른쪽 작은 단일 LLM→2 ToolCalls. 세 도식의 Loop/컨텍스트 경계 다르게.

출처: G-WORKFLOW

## S53 — Event·Session·Memory·Artifact는 역할이 다르다

사용 사례는 이벤트 추적이 중요한 다단계 서비스·워크플로다. 중단/복구 경계가 특정 구현에 미치는 영향은 버전별로 점검한다.

### 화면 문구

- Event는 출력과 state 변경을 전달
- Session·Memory·Artifact는 서로 다른 목적
- Agent final과 전체 Workflow 완료를 구분

### 단계별 전개

1. Event 기록
2. State 분리
3. 재개·완료 범위

### 원문 도식 요구

Event 타임라인과 오른쪽 `session state / memory / artifact` 저장소 3개. 전체 workflow 완료와 Agent final 이벤트를 구분 색상.

출처: G, G-EVENT, G-STATE

## S54 — Microsoft Agent Framework는 Agent와 Workflow를 구분한다

Microsoft Agent Framework를 전부 Workflow 엔진으로만 설명하지 않는다. 일반 Agent 실행, Cross-cutting Middleware, 그래프 Workflow, 선택적 Harness Agent를 분리한다. 언어별 기능 차이는 공식 docs 우선.

### 화면 문구

- 공통: Agent가 모델·Tool과 상호작용
- 차별: Middleware와 명시적 Workflow 조합
- 선택적 Harness Agent는 별도 기능 계층

### 단계별 전개

1. 기본 Agent
2. Middleware
3. Workflow/선택 Harness

### 원문 도식 요구

M-ARCH 전체 `App→Agent→Model/Function Tool`; Middleware 가로 절단; `WorkflowBuilder→Executor graph→Checkpoint` 병렬 영역, Harness optional 점선 테두리.

출처: M

## S55 — Middleware는 공통 정책을 실행 경로에 끼워 넣는다

예외를 모두 모델에게 알려 계속하라는 뜻이 아니다. 위험한 행동에는 Tool 이전 정책 차단이 필요하며 Middleware의 적용 범위·API는 버전별로 확인한다.

### 화면 문구

- 입력·함수 호출·출력 주변에 공통 처리 지점
- 로깅·검증·정책·오류 전환을 집중 관리
- Tool 에러와 강제 실행 중단은 구분

### 단계별 전개

1. Middleware 위치
2. 정책 처리
3. 오류 처리 분기

### 원문 도식 요구

좌 Agent/Function 호출 파이프라인에 middleware 훅 3개, 우 `일반 Tool error→model result`와 `강제 policy stop→run 종료` 분기.

출처: M-MIDDLE

## S56 — Superstep과 Checkpoint가 Workflow 실행을 조직한다

기능이 .NET, Python, Go에서 서로 다를 수 있다. 실행 형태, Checkpoint 직렬화, 재개 지원 범위를 설치 버전에서 검증한다. **활용 예:** 보고서 초안 작성→두 분기의 검토→승인 후 통합처럼 분기·합류가 명확한 업무 흐름. Checkpoint만으로 외부 Tool 호출이 Exactly-once가 되지는 않는다.

### 화면 문구

- Executor들을 Edge로 연결하고 fan-out/fan-in
- Superstep 경계에서 병렬 작업을 동기화
- Checkpoint는 Workflow 복구 지점이지 DB 트랜잭션이 아님

### 단계별 전개

1. Executor 그래프
2. Superstep/Join
3. Checkpoint/외부 부작용

### 원문 도식 요구

`Start→Exec A/B parallel→Join→Exec C`의 Superstep 1/2 구획. Checkpoint 아이콘과 외부 DB side effect 별도 박스.

출처: M-WORKFLOW, M-CHECKPOINT

## S57 — Orchestration은 Loop와 결과의 귀속으로 구분한다

모두 다중 Agent라는 포괄 용어 하나로 설명하지 않는다. 어떤 상황에서 병렬성, 새로운 컨텍스트, 명시적 제어권 전환이 필요한지를 구별한다.

### 화면 문구

- 병렬 Tool: 하나의 Loop 안에서 기능 동시 호출
- Subagent/Agent-as-Tool: 하위 결과가 원래 실행으로 복귀
- Handoff/Workflow: 제어 주체 교체 또는 명시적 그래프 단계

### 단계별 전개

1. Tool parallel
2. Delegation
3. Handoff
4. Workflow

### 원문 도식 요구

4분면 같은 축: `누가 Loop를 소유?`, `결과는 어디로 돌아오나?` 위에 Tool parallel, delegation, handoff, workflow를 4개 미니 화살표로 구분.

출처: O-ORCH, G-WORKFLOW, M-WORKFLOW

## S58 — 실행 형태·제어 방식·운영 책임으로 선택한다

제품별 기능 가짓수가 아니라 팀의 개발 역량과 운영 책임으로 선택한다. 실제 모델 지원, 확장성, 라이선스와 보안 요구도 별도 검토한다.

### 화면 문구

- 바로 쓸 실행 환경인가, 앱에 내장할 SDK인가
- Tool·데이터 통제인가, 위임·Workflow 통제인가
- 기록·검증·복구를 팀이 어디까지 운영할 수 있나

### 단계별 전개

1. 실행 형태
2. 차별점
3. 조직 책임

### 원문 도식 요구

좌 7종 비교 카드를 짧은 태그로, 우 질문 3개를 체크리스트로. 기능 순위표나 단정적인 최강 표현 금지.

출처: BASE, H-ARCH, C, P-AGENT, O, S, G, M

## S59 — Agent Runtime과 모델 서버는 따로 배치할 수 있다

같은 OpenAI 호환 모델 API라도 실제 구조는 모델 서버와 Agent 런타임을 어디에 두느냐에 달려 있다. 개발 PC의 10000번 중계기는 실제 대상 vLLM과 다르다. 네트워크/인증/지연/데이터 경계까지 검토해야 한다.

### 화면 문구

- 중앙 Runtime: 인증·격리·큐·운영을 중앙 관리
- 로컬 Runtime: 사용자 파일·OS 권한과 연결
- 모델 연결·지연·배포·데이터 경계를 별도 검토

### 단계별 전개

1. 중앙 Runtime 구조
2. 사용자 PC Runtime 구조
3. 보안/유지보수 비교

### 원문 도식 요구

서로 다른 두 배포도(A와 B). 각 모델 호출 네트워크 경계와 Tool의 OS/DB 접근 위치를 표시. 로컬 Demo relay(10000→OpenAI)는 개발용으로만 작은 점선 카드.

출처: DEPLOY

## S60 — 실행 계약을 이해해야 Agent를 설계하고 운영할 수 있다

청중이 “Hermes와 Claude Code는 어떻게 돌아가고 어디에 쓸 수 있는지, PydanticAI와 다른 SDK는 무엇을 개발해야 하고 무엇이 제공되는지” 말할 수 있으면 성공이다. 다음에는 동일 Fixture의 실제 Trace와 대상 환경을 대조해 설계 가설을 검증한다.

### 화면 문구

- Harness를 쓰면 이미 구현된 실행 구조를 활용한다
- SDK를 쓰면 앱이 원하는 구조를 직접 조립·운영한다
- 어느 쪽이든 Tool 권한·근거·상태·검증은 끝까지 확인한다

### 단계별 전개

1. 완성형 얻는 것
2. SDK 얻는 통제
3. 공통 책임과 다음 검증

### 원문 도식 요구

처음 슬라이드의 Runtime/Model/Tool/State 그림 재등장. 강조는 `판단(LLM)` vs `실행(Runtime)` vs `책임(App/Operator)` 세 단어.

출처: BASE
