# Agent Framework Seminar II — 개정판 전체 발표자료

본편 **60장(S01~S60)**. 밝은 16:9 HTML, 외부 인터넷·설치·서버 없이 실행합니다.

## 열기

- **index.html**: 발표용. Space 한 번에 의미 단위 하나씩 나타나며, 마지막 빌드 다음에 다음 장으로 이동합니다.
- **preview.html**: 검토용. 각 장의 완성 화면을 바로 표시하고 Space 한 번에 다음 장으로 이동합니다.

브라우저에서 파일을 직접 여세요. 원하는 장에서 시작하려면 준비 단계에 URL 뒤에 `?slide=31`처럼 붙일 수 있습니다. 관객용 페이지에는 이동 버튼이나 설정 폼이 없습니다. 마지막 장에서는 멈춥니다. 처음으로 돌아가려면 새로고침합니다. 전체 화면은 발표 시작 전에 브라우저에서 설정하세요.

## 포함한 범위

Hermes → Claude Code → PydanticAI → OpenAI Agents SDK → Claude Agent SDK → Google ADK → Microsoft Agent Framework → 종합. 원문의 60개 ID와 순서를 유지했습니다. 문장은 화면용으로 다듬었으며, 원문 본문·도식 요구·발표자 노트는 보존했습니다.

**데모는 제작·실행하지 않았습니다.** S18/S19/S41/S42는 향후 관측할 항목과 실행 전 상태를 설명합니다. 실제 Trace·event_id·캡처·모델 API 호출·10000 relay·fixture 실행기는 없습니다. 코드 화면은 의사 코드 또는 API 형태 예시이며 실행 가능 예제로 표시하지 않았습니다.

## 편집과 근거

- `slide_map.json`: 제작 전 데이터화한 원문 60장 계약
- `slides/slide-data.json`: 실제 화면 문구·순서·단계·출처
- `slides/content.py`: 페이지별 도식과 화면용 문구
- `slides/diagrams.py`: 편집 가능한 SVG 및 재사용 마스터
- `slides/theme.css`: 색상·강조 설정
- `slides/controller.js`: Space 진행 규칙
- `docs/presenter-notes.md`: 60장 발표자 원고와 전제
- `docs/claims.md`: 주장별 공식 근거와 변경·미검증 사항
- `docs/source-map.json`: 실제 URL·수집 해시·공개 소스 commit
- `docs/qa-report.md`: 렌더·브라우저 검수 결과

최종 HTML에는 CSS·SVG·JS가 모두 들어 있습니다. `index.html` 또는 `preview.html` 한 파일만 옮겨도 열립니다. 시스템의 Malgun Gothic, Segoe UI 계열 글꼴을 사용합니다. 다른 OS에서는 대체 글꼴에 따라 표시를 다시 확인하세요.

## 다시 만들기

프로젝트 폴더에서 다음을 실행합니다. Python 표준 라이브러리만 필요합니다.

```powershell
python scripts/build.py
python scripts/write_claims.py
```

`prepare.py`는 원문 데이터를 다시 추출할 때만 사용합니다. `audit_sources.py`는 공식 문서를 다시 검토할 때 사용하며 인터넷에 접근합니다. 현재 주장 기록과 원문 수집 시점을 함께 업데이트해야 합니다.

테스트는 Playwright와 Chrome을 사용합니다. `tests/browser.cjs`의 Playwright 경로와 브라우저 실행 파일 경로는 이 PC 기준이므로 다른 PC에서는 수정하세요.

```powershell
node tests/browser.cjs
node tests/contact-sheets.cjs
```

기존 seminar_v2, archive 및 기준 문서는 변경하지 않았습니다. 포트 10001과 기존 모델 프록시는 사용하거나 변경하지 않았습니다.
