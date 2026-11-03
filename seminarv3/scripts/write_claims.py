from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
sources=json.loads((R/'docs/source-map.json').read_text(encoding='utf-8'))
slides=json.loads((R/'slides/slide-data.json').read_text(encoding='utf-8'))
sources['BASE']={'url':'../agent_framework_seminar_ii_codex_revised_blueprint.md','status':'USER_SPEC'}
sources['DEMO']={'url':'../agent_framework_seminar_ii_codex_revised_blueprint.md#5','status':'DESIGN_ONLY'}
for s in slides:
 for key in s['sources']:assert key in sources,(s['id'],key)
out=['# 주장·근거 검토 기록','','확인일: 2026-11-03. 사용자 요청 범위는 발표자료 60장이다. 모델 API, Hermes/PydanticAI 데모, relay, 외부 Tool을 실행하지 않았다.','','## 검토 기준','','- DOC_CONFIRMED: 저장한 공식 문서의 공개 계약을 확인했다. 설치 환경에서 동일 동작을 재현했다는 뜻은 아니다.','- SOURCE_CONFIRMED: 특정 commit의 공개 소스에서 심볼·구조를 확인했다. 실행 관측과 구분한다.','- DESIGN_ONLY: 교육용 사례 또는 도입·운영 설계 제안이다.','- NOT_VERIFIED: 실제 설치·실행·Trace 검증은 수행하지 않았다.','- 이 제작본에는 RUN_OBSERVED 주장이 없다. 원고의 이전 릴리스 숫자를 최신판 또는 설치 버전으로 표기하지 않았다.','','## 슬라이드별 주장','','| 슬라이드 | 화면 주장 | 근거 | 검토 범위 |','|---|---|---|---|']
for s in slides:
 state='DESIGN_ONLY' if s['status'] in ['개념 / 설계','실행 전 · 검증 계획'] else 'DOC_CONFIRMED'
 if s['id'] in ['S07','S32','S48']:state+=' + SOURCE_CONFIRMED'
 if s['id']=='S31':state+=' / 실제 실행 NOT_VERIFIED'
 out.append('| '+s['id']+' | '+' / '.join(s['screen']).replace('|','/')+' | '+', '.join(s['sources'])+' | '+state+' |')
out+=['','## 수정 및 조건','','1. S03/S18/S19/S41/S42: 데모 수행 표현을 실행 전 확인 계획으로 바꿨다. event_id, 캡처, 가상 Trace를 만들지 않았다.','2. S06: 원문의 ratio 0.12는 단위가 모호하므로 교육용 예시 12/10,000 × 100 = 0.12%로 명시했다. 계산은 실제 DB 관측이 아니다.','3. S08/S14: 승인 거부는 Tool 실패로 반환될 수도 있다. 정책에 의한 전체 run 강제 중단과 혼동하지 않는다. DANGEROUS_PATTERNS의 위험 명령 승인은 모든 Tool에 자동 적용되는 보안 보장이 아니다.','4. S09: Stable/Context/Volatile은 시스템 프롬프트 층이다. Volatile을 모두 호출별 임시 입력으로 동일시하지 않았다. 세션 스냅샷과 호출 시 임시 맥락을 분리했다.','5. S24: Hook/Permission 순서를 하나로 고정하지 않고 적용 지점별 계층으로 설명한다. Sandbox의 플랫폼·설정 조건은 설치 환경에서 확인해야 한다.','6. S25: Teams 지원 설정·환경과 독립 Context/공유 파일 충돌은 별개다.','7. S31: API 형태는 문서·공개 소스와 대조했지만 실행 가능한 독립 예제가 아니다. model과 fixture 함수는 앱 주입 항목이다. 실행 가능/실제 원문 라벨을 사용하지 않았다.','8. S36: 현재 공식 문서는 graceful을 기본으로 설명한다. early/exhaustive만 나누던 초안을 세 정책으로 보완했다. 비교 조건은 유효한 Output Tool + 함수 Tool 혼합 응답이다. Native/Prompted 출력과 plain text의 조건, Streaming 조기 확정은 노트에서 분리했다.','9. S37: 실행 동시성과 모델의 병렬 Tool Call 생성은 다르다. 실제 병렬 시간 측정은 하지 않았다.','10. S39: 외부 승인 흐름은 DeferredToolRequests를 반환한 뒤 History + DeferredToolResults로 후속 run을 시작한다. 현재 문서의 inline handler 경로는 선택 방식으로 노트에 기록했다.','11. S47: Input guardrail은 첫 Agent, Output guardrail은 최종 Agent 출력에 적용된다. Function Tool guardrail과 Hosted Tool/handoff의 범위를 일반화하지 않았다.','12. S48: Python SDK의 subprocess transport 소스를 확인했지만 모든 언어·배포 방식이 동일한 프로세스 구현이라는 의미는 아니다.','13. S53/S56: Agent final은 전체 Workflow 완료와 다르며, Checkpoint는 외부 DB exactly-once를 보장하지 않는다. 언어별 지원 범위와 저장 구현은 별도 검증한다.','14. 출처 키 CC와 P는 원고의 C와 P-AGENT로 정규화했다. 이동된 문서 URL은 아래 실제 응답 URL을 사용했다.','','## 공개 소스 고정점','']
for key in ['H-SRC','P-SRC','S-SRC']:
 out+=['- '+key+': '+sources[key].get('url','')+'  ', '  commit: `'+sources[key].get('commit','unavailable')+'`']
out+=['','Hermes 확인 파일: run_agent.py, agent/conversation_loop.py, agent/tool_executor.py, model_tools.py. PydanticAI 확인 심볼: UserPromptNode, ModelRequestNode, CallToolsNode. Claude SDK 확인 파일: src/claude_agent_sdk/_internal/transport/subprocess_cli.py. 저장 사본은 evidence/sources 아래에 있다.','','## 공식 자료 URL과 수집 증거','','| ID | 실제 URL | 상태 |','|---|---|---|']
for key,val in sources.items():out.append(f"| {key} | {val.get('url','')} | {val['status']} |")
out+=['','수집 원문 해시는 source-map.json에 기록했다. FETCHED는 수집 성공 상태이며, 문서 내용 검토는 위 슬라이드별 행과 수정 기록으로 구분한다. 설치 버전별 동작·성능·실제 재개 가능성은 모두 NOT_VERIFIED다.']
(R/'docs/claims.md').write_text('\n'.join(out),encoding='utf-8')
(R/'docs/source-map.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2),encoding='utf-8')
print('Claim ledger and sources complete')
