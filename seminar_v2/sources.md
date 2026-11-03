# 근거와 확인 범위

확인일: 2026-11-03. 설치 버전이나 특정 릴리스 검증을 주장하지 않습니다. 공식 문서의 현재 공개 계약만 사용하며, 실제 Runtime 실행 관찰은 하지 않았습니다.

| ID | 공식 근거 | 사용 내용 | 상태 |
|---|---|---|---|
| H-ARCH | https://hermes-agent.nousresearch.com/docs/developer-guide/architecture | AIAgent, 진입점, provider, Tool dispatch, session 구조 | DOC_CONFIRMED |
| H-LOOP | https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop | 모델 호출, Tool 실행, 결과를 history에 추가하고 반복 | DOC_CONFIRMED |
| P-DEPS | https://pydantic.dev/docs/ai/core-concepts/dependencies/ | Python deps와 RunContext 접근, 지침 및 Tool에서 명시적으로 데이터 사용 | DOC_CONFIRMED |
| O-ORCH | https://openai.github.io/openai-agents-python/multi_agent/ | as-tool의 Manager 유지, handoff의 활성 Agent 전환 | DOC_CONFIRMED |
| BLUEPRINT F091 | ../agent_framework_seminar_ii_codex_final_blueprint.md | 중앙/로컬 Runtime과 중앙 모델의 배치안 | DESIGN_OR_ILLUSTRATIVE |

F009의 BIN-X 함수와 F049의 Python 코드는 설명용 예시 및 의사코드입니다. F049의 인가·데이터 선택은 애플리케이션 책임이며 SDK의 자동 보안 기능을 뜻하지 않습니다. dependencies 값이 instructions나 반환 데이터에 명시적으로 포함되면 모델에 전달될 수 있습니다.

F006의 정책 박스는 적용 경계를 요약한 것입니다. 모든 Tool에 동일한 검사 순서나 승인 동작이 있음을 보장하지 않습니다. 실제 실행 전 intent의 영속화나 exactly-once 보장을 주장하지 않습니다. F066에서 handoff는 해당 실행의 활성 Agent를 바꾸는 것이며 이후 세션 전체에 영구적으로 유지된다는 뜻은 아닙니다.

이번 샘플에는 원문의 릴리스 번호를 표기하지 않았습니다. 전체 덱 제작 시 릴리스 고정 및 소스 수준 검증을 추가해야 합니다. 원문이 참조하는 별도 연구 폴더는 이번 작업의 제공 범위에 없으므로 본 문서와 공식 자료를 사용했습니다.
