# 제작·검증 기록

검수일: 2026-11-03 (Asia/Seoul). 사용자 확정 범위: **설명용 재생과 실행 준비까지**.

## 산출물

- `dist/presentation.html`: 스타일·슬라이드 데이터·JS를 내장한 독립 발표 HTML.
- `dist/index.html`: 편집용 파일로 분리된 발표 앱. 본문 S00–S40, 부록 X01–X10.
- `dist/demo.html`: 별도 Hermes / PydanticAI 설명용 재생 및 Trace 파일 뷰어.
- `dist/sources`: 블루프린트, 내용 원본 C, 디자인 원본 D, 절별 추적표 사본.
- `GUIDE.md`, `demo-prep`: 실행·이관 가이드, 설정·Trace 계약, 선택 설치 준비 스크립트.

## 자동 검사

`node scripts/build.mjs`, `node scripts/check.mjs`, 생성 JS의 `node --check` 통과.

- 본문 41장·부록 10장·고유 ID·필수 화면 문구·노트·출처 확인.
- 일곱 아키텍처의 고유 노드와 Edge 참조 확인.
- 156회 전체 순방향 단계 전이와 동일 횟수의 역방향 복귀 확인.
- 축약 36장 경로와 제외 장에서 다음/이전 경로 연결 확인.
- 부록 실패·경계 질문 24개, Q&A 30개, 청중용 탭 데이터 확인.
- Trace 필수 메타데이터·고유 Event ID·모드·실제 기록 마스킹 확인 및 잘못된 형식 거절 확인.
- 독립 HTML의 외부 script·ES module 의존성 제거 확인.

## 브라우저 검사

로컬 HTTP 서버 + Codex in-app browser에서 검수.

- 1280×720과 1920×1080에서 본문 41장 최종 상태의 DOM 배치 확인. 본문 문구와 footer의 겹침 없음.
- 최종 단계의 잔여 비활성 요소 점검 중 S24의 단계 수 차이를 수정하고 재확인.
- 표지, Hermes 전체도, PydanticAI Node 전이도, Claude SDK 프로세스 경계, X09 매트릭스 화면을 이미지로 확인.
- S06의 X04 호출 후 S06 / build 2 복귀 확인.
- N 노트 열기·닫기, Q&A의 “승인” 검색, F01 사례 분석 틀 열기 확인.
- Demo 2 사건 탐색·최종 상태·S21 / build 3 복귀 확인.
- 청중 창 → 발표자 창 위치 수신, 발표자 창 조작 → 청중 창 S03 / build 1 반영 확인.
- 독립 HTML을 HTTP로 열어 정상 렌더링 확인. 확인 시점 브라우저 콘솔 오류 없음.
- `start.ps1 -Port 4174 -NoBrowser`의 서버 시작, HTTP 200, `stop.ps1`의 해당 서버 종료 확인.

`file://` 직접 열기는 검수 도구의 URL 정책이 허용하지 않아 자동 브라우저 검증하지 못했습니다. 대체 프로토콜이나 다른 브라우저를 통한 우회는 하지 않았습니다. 독립 HTML은 외부 script·스타일 의존성 없이 생성되며, 검증한 실행 경로는 로컬 HTTP입니다. 인쇄·브라우저별 file origin 동기화·팝업 제한은 별도 확인이 필요합니다.

## 환경·실행 범위

`node scripts/doctor.mjs`는 Node v24.22.1, Python 3.12.14, Git 2.55.0을 확인했습니다. 선택한 Python에서 PydanticAI/Hermes 배포 패키지는 발견하지 못했습니다. 검사한 환경변수에 API key·모델·데이터 경로가 설정되지 않았습니다. `reports/environment.json`에 세부 결과가 있습니다. PC 전체의 모든 가상환경을 검색한 결과는 아닙니다.

`demo-prep/prepare.ps1`은 **기본 계획 출력 모드만 실행**했습니다. 실제 SDK 설치·소스 복제·모델 호출은 하지 않았습니다. 기존 학습 프로젝트, 기존 Hermes 홈·Memory·DB·전역 패키지를 수정하지 않았습니다.

실제 Hermes/PydanticAI Run, Provider 최종 payload, 도메인 데이터·예측 품질, vLLM 기능 호환, 외부 정책·승인·복구, 다른 PC 동작은 **미검증**입니다. 고정 버전 공식 링크는 원문에서 계승했으며 최신 기능 조사나 외부 링크의 현재 유효성 검사는 수행하지 않았습니다. 설명용 데이터는 실제 실행 기록으로 표시하지 않습니다.
