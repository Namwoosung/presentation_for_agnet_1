# 발표자료 검수 기록

검수일: 2026-11-03. 대상: 개정판 60장 HTML 발표자료. 테스트 환경: Windows / 설치된 Google Chrome / Playwright.

## 수행 완료

| 항목 | 결과 | 증거 |
|---|---|---|
| S01~S60 정확히 60장, 순서·고유 ID | PASS | slide_map.json, slides/slide-data.json |
| 60장 발표자 설명·도식 요구·출처 연결 | PASS | docs/presenter-notes.md |
| 전체 60장 렌더와 시각 검수 | PASS | evidence/screenshots/S01.png~S60.png, contact-01.png~contact-15.png |
| 밝은 배경, 한글 텍스트와 편집 가능한 SVG | PASS | 두 HTML 및 60장 캡처 |
| 7개 프레임워크 마스터 필수 노드 | PASS | evidence/browser-report.json |
| 텍스트 화면 이탈 | PASS: 0건 | browser-report.json bounds |
| 텍스트 간 겹침 | PASS: 0건 | browser-report.json overlap |
| 노드 내부 텍스트 넘침 | PASS: 0건 | browser-report.json nodeOverflow |
| 1920×1080 / 1366×768 / 1280×720 | PASS: 각 60장 프레임 확인 | browser-report.json viewports |
| 추가 390×844 화면에서 전체 stage 비율·범위 유지 | PASS | browser-report.json viewports |
| 194개 의미 상태를 Space로 순서대로 진행 | PASS | browser-report.json visitedStates |
| 길게 누르기·event.repeat·전환 중 중복 진행 방지 | PASS | tests/browser.cjs |
| Arrow/Enter가 진행을 바꾸지 않음, 마지막 장 정지 | PASS | tests/browser.cjs |
| 브라우저 JavaScript 오류 | PASS: 0건 | browser-report.json errors |
| 외부 이미지·스크립트·폰트·iframe 의존성 | PASS: 0건 | browser-report.json externalDependencies |
| 원문과 기존 v2 보존 | PASS | 기존 파일을 덮어쓰지 않고 seminarv3 안에 추가 생성 |

자동 레이아웃 검사는 시각 검토를 대신하지 않는다. 전체 60장을 4장씩 묶은 15개 contact sheet로 확인했고, 변경한 페이지는 다시 렌더해 재검토했다. 수정에는 SVG marker 식별자, 화면 전환 시 투명도, 긴 라벨, 입력 경로 방향, Core 반복의 복귀 지점, Agent 병렬 분기, Workflow의 Start/Join 표기가 포함된다.

## 미검증 또는 요청 범위 밖

| 항목 | 상태 | 이유 |
|---|---|---|
| Hermes / PydanticAI 실제 실행과 데모 | NOT_TESTED | 사용자 요청으로 제외 |
| 모델 API 호출·relay·vLLM 호환성 | NOT_TESTED | 발표자료만 제작 |
| 실제 Tool Call ID, event_id, Trace hash | NOT_TESTED | 수집한 실행 이벤트 없음 |
| S31 API 예시 실행 | NOT_TESTED | 모델·인증·fixture는 앱 주입 항목, 실행 가능 표시 없음 |
| 설치 버전별 EndStrategy·Deferred·병렬 실행 | NOT_TESTED | 공식 문서/공개 소스 검토와 실제 관측을 구분 |
| 대상 PC의 폰트 및 프로젝터 가독성 | NOT_TESTED | 이 PC의 Chrome에서만 검수 |
| 실제 DB·업무 데이터·제조 설비 연결 | NOT_TESTED | 접근하거나 변경하지 않음 |

S18/S19/S41/S42는 실행 전 확인 계획으로 표시한다. 실제 캡처나 관측 로그처럼 보이는 가상 데이터를 넣지 않았다. 이 보고서의 PASS는 발표자료 렌더·구조·진행에 대한 결과이며, 프레임워크의 실제 실행 성공을 뜻하지 않는다.

## 재현 명령

프로젝트 폴더에서:

```powershell
python scripts/build.py
python scripts/write_claims.py
node tests/browser.cjs
node tests/contact-sheets.cjs
```

최종 빌드 해시는 evidence/build.json에 기록한다. 원문/표시문구/근거의 차이는 docs/claims.md에서 확인할 수 있다. 현재 발표자료 사용을 막는 blocker는 없다. 후속 데모 단계에서는 설치 릴리스 고정과 실제 Trace 수집이 필요하다.
