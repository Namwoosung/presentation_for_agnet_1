# 세미나 발표·데모 실행 가이드

## 바로 시작

`dist/presentation.html`을 브라우저에서 열면 서버·인터넷·API key 없이 발표할 수 있습니다. 원본 C/D와 데모 연결까지 함께 사용할 때는 **dist 폴더 전체**를 유지하세요. Chrome/Edge 등 현대 브라우저를 사용합니다.

로컬 서버를 사용할 경우 PowerShell에서 다음 명령을 실행합니다.

```powershell
Set-Location 'C:\Users\namws\OneDrive\Desktop\presentation_for_agnet_1\seminar'
.\start.ps1
```

Node가 PATH에 없으면 이 PC의 Codex 번들 Node를 자동으로 찾습니다. 다른 PC는 Node.js 20 이상을 PATH에 설치하세요. `npm`과 추가 패키지는 필요하지 않습니다. PowerShell 실행 정책으로 스크립트가 차단되면 정책을 바꾸지 않고 `node scripts/serve.mjs`로 실행할 수 있습니다.

기본 화면: `http://127.0.0.1:4173`. 포트를 바꾸려면 `start.ps1 -Port 4174`를 사용합니다. 이미 사용 중인 다른 서비스는 종료하지 않습니다. 실행기 서버 종료는 `stop.ps1`, 터미널에서 직접 실행한 서버 종료는 Ctrl+C입니다.

## 발표 조작

| 조작 | 동작 |
|---|---|
| → / Space | 현재 장의 다음 build, 이후 다음 장 |
| ← | 이전 build, 첫 단계에서는 이전 장 마지막 build |
| T / 목차 | ID·제목 검색과 점프 |
| N | 현재 발표자 노트·그림 기준·출처 |
| R / Reset | 현재 장의 첫 build |
| 최종 상태 | 현재 장 전체 단계 표시 |
| 자동 재생 / Pause | 4.5초 간격 단계 진행 / 정지 |
| 동작 줄이기 | 전환 효과 해제, 자동 재생 대신 수동 조작 |
| Esc | 열린 최상위 오버레이 닫기 |
| Sources | 고정 버전·증거 등급·로컬 원본·계승 공식 링크 |

입력창·textarea·선택 목록에서는 발표 단축키를 가로채지 않습니다. 본문 번호는 1/41, build 번호는 별도입니다. 부록은 X 번호로 독립하며 호출한 본문·단계로 복귀합니다. 직접 URL로 연 부록은 S00으로 돌아갑니다.

목차에서 전체 41장 / 축약 36장 경로를 선택할 수 있습니다. 축약 경로는 S08/S10/S26/S31/S34를 제외합니다. 45–55분 수준의 추가 압축은 블루프린트 A-7의 발표자 편집 지침을 사용합니다. 실제 발표 소요 시간을 측정하지 않았습니다.

발표자 보기는 별도 창에 노트·현재 단계·다음 장·시계를 표시합니다. HTTP로 같은 origin에서 열면 청중 창 위치를 수신합니다. 팝업이 차단되면 `index.html?presenter=1#S03/0`을 새 창에서 직접 여세요. file://에서의 창 동기화는 브라우저별 제한이 있으므로 로컬 서버 사용을 권장합니다. 일반 청중 창에는 노트가 자동으로 나타나지 않습니다.

## 별도 Demo 1 / Demo 2

S11 → `demo.html?demo=hermes`, S21 → `demo.html?demo=pydantic`으로 이동합니다. 복귀 링크는 원래 slide ID와 build를 복원합니다. 현재 둘 다 **설명용 고정 도식**이며 실제 Runtime·Provider 기록이 없습니다.

- Demo 1: Prompt·Schema → 모델의 Tool 제안 → Intent → 정책 → Handler 경계 → 결과 기록 → 다음 Context.
- Demo 2: Agent 계약 → 내부 Node → 검증·Retry 질문 → Deferred 연결점 → History·종료.

이벤트 선택, 이전/다음/Space, Reset, 최종 상태, 자동 재생/Pause, 동작 줄이기, Payload 요소별 보기가 가능합니다. 예시 조회 비율·분모·기간은 `null`입니다. 예측값과 실행 성공 로그를 만들지 않습니다. 가상 도구명은 발표용이며 제품 API가 아닙니다.

## 실제 기록을 나중에 연결하기

데모의 **실제 기록 파일 열기**는 5MB 이하 JSON을 로컬 메모리에서 읽습니다. 서버 업로드·파일 보관 기능은 없습니다. `demo-prep/trace-contract.md`의 형식을 따릅니다. `dist/trace.js`에서 형식과 모드·메타데이터·이벤트 ID를 확인하며, 실제 기록은 `redacted: true`가 필요합니다. 가져온 파일의 진위나 실제 실행 성공을 검증하는 기능은 아닙니다.

원시 요청은 **관찰 지점**을 명시해야 합니다. Provider 변환 전 객체를 최종 전송 payload로 표시하지 마세요. 수집기 단계에서 key·민감 데이터·비공개 추론을 제거해야 합니다. 뷰어의 추가 키 기반 마스킹은 모든 민감정보를 찾아내는 기능이 아닙니다.

자연 모델에서 발생하지 않은 Tool·Child·압축·승인은 미발생으로 남깁니다. Scripted Runtime 분기는 `scripted`, 실제 사전 기록은 `recorded`로 구분합니다. `live` 출처 파일을 열어도 현재 실시간 연결을 제공하지는 않습니다.

## 실제 Runtime 실행 전 준비

환경 점검은 API를 호출하거나 기존 설치를 바꾸지 않습니다.

```powershell
node scripts/doctor.mjs
```

결과는 `reports/environment.json`에 저장합니다. Node/Python/Git, 선택한 Python 환경의 패키지, 환경변수 **존재 여부**만 기록합니다. 이 점검은 PC 전체의 모든 가상환경을 검색하는 설치 재고 조사와 다릅니다.

`demo-prep/config.example.json`은 미확정 데이터를 명시한 설정 템플릿입니다. 실제 연결 전 아래를 고정합니다.

1. 데이터 파일, 기간·분모·측정 기준, Snapshot, 예측 target·평가 방법.
2. 모델 ID·Provider·Adapter·인증 환경변수·endpoint. 현재 PC와 다른 PC vLLM은 별도 검증.
3. Hermes 소스 경로·버전·기존 HERMES_HOME. 기존 Memory·DB는 복사본/별도 홈으로 보호.
4. PydanticAI Core 버전, 선택 Harness의 별도 버전. 프로젝트 전용 venv에 설치.
5. Tool·Output Schema, 실제 Hook·관찰 지점, 승인·정책·저장·멱등성 계약.
6. Contract → Scripted Runtime → Integration → Task Eval의 각 성공 기준.

선택 설치 준비 절차는 `demo-prep/prepare.ps1`에 있습니다. 기본 실행은 계획만 출력합니다. `-Install -PythonPath <실제 Python 경로>`를 명시해야 `.venv`에 고정 PydanticAI를 설치하고 `vendor`에 Hermes 고정 태그를 별도 복제합니다. 이 제작에서는 실제 Runtime 설치·모델 호출을 수행하지 않았습니다. 태그나 패키지가 저장소에 없으면 자동 최신 버전으로 대체하지 않고 실패합니다.

환경변수 이름은 `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `SEMINAR_MODEL`, `SEMINAR_DATA`, `HERMES_SOURCE`, `HERMES_HOME`, `SEMINAR_PYTHON`을 준비했습니다. **발표 앱이 이 변수를 읽거나 실제 Run을 시작하지 않습니다.** 실제 런타임 어댑터는 데이터·모델·Hook 확정 후 별도 구현·검증해야 합니다. API key는 웹 화면이나 JSON 설정 파일에 넣지 마세요.

## 재생성·검증·이관

```powershell
node scripts/build.mjs
node scripts/check.mjs
node scripts/doctor.mjs
```

`build`는 루트 블루프린트에서 51개 ID·화면 문구·노트·출처·부록을 추출하고, classic JS 번들과 독립 HTML을 생성합니다. 처음 제작한 PC에서는 C/D의 로컬 원본을 `dist/sources`에 복사합니다. 다른 PC에서는 이미 동봉된 사본을 유지합니다. `dist/data.js`를 직접 수정하지 말고 블루프린트를 수정한 뒤 재생성하세요. 도식은 `dist/architectures.js`, `dist/diagrams.js`, 부록 청중용 편집은 `dist/appendix.js`, 토큰은 `dist/tokens.css`에 있습니다.

`check`는 장수·고유 ID·필수 콘텐츠·7개 구조도 연결·156회 순방향/역방향 단계 전이·부록 24개 실패 질문과 30개 Q&A·Trace 형식과 마스킹을 검증합니다. 브라우저 화면 검수와 실제 SDK 실행 검증을 대체하지 않습니다. 수행 범위는 `reports/validation.md`에 기록합니다.

이관은 `seminar` 폴더 전체와 루트 블루프린트를 함께 복사합니다. `.venv`, `private`, 인증 파일은 자동 이관 대상이 아닙니다. 다른 PC 실행·vLLM 호환·데이터 품질은 검증하지 않았습니다. 설치 원복은 `prepare.ps1`이 새로 만든 `.venv`·`vendor`만 경로를 확인한 뒤 삭제하며, 기존 전역 설치나 Hermes 홈을 삭제하지 않습니다.
