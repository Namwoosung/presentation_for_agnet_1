# seminar-trace/v1

실제 기록이 없는 상태에서 사용할 **형식 템플릿**입니다. 아래 JSON은 성공 로그가 아닙니다. `recorded`로 사용하려면 실제 수집값으로 모든 메타데이터·이벤트를 채우고 저장 전에 마스킹해야 합니다. 실제 예제 Trace 파일은 제공하지 않습니다.

```json
{
  "schema": "seminar-trace/v1",
  "mode": "recorded",
  "framework": "hermes",
  "version": "실제 실행 버전",
  "model": "실제 모델 ID",
  "runId": "실제 run ID",
  "sessionId": "실제 session ID",
  "recordedAt": "ISO-8601 기록 시각",
  "observationPoint": "Provider 변환 전/후 등 실제 관찰 지점",
  "redacted": true,
  "events": [{
    "id": "고유 event ID",
    "kind": "model.request",
    "label": "실제 관찰 사건 설명",
    "timestamp": "ISO-8601 사건 시각",
    "modelId": "모델 요청 식별자",
    "toolCallId": "해당하는 경우 실제 tool call ID",
    "parentId": "해당하는 경우 부모 event / run ID",
    "payload": {"redactedRequest": "관찰된 공개 입력만 포함"}
  }]
}
```

`framework`: `hermes` / `pydantic`. `mode`: `illustrative`(설명용 고정 데이터), `scripted`(고정 응답 Runtime 시험), `recorded`(실제 사전 기록), `live`(live 출처에서 가져온 기록). 뷰어는 실시간 스트림 수집기가 아닙니다.

이벤트 종류: `model.request`, `model.response`, `tool.intent`, `tool.policy`, `tool.start`, `tool.result`, `context.next`, `state.commit`, `node.enter`, `output.validate`, `run.end`, `run.error`. 실제 모델 이벤트에는 `modelId`, Tool 이벤트에는 `toolCallId`가 필요합니다. Event ID는 고유해야 합니다.

Provider 비밀 key·Authorization·DB 자격증명·민감 원문·비공개 추론은 수집 전에 제거합니다. 기록에는 해당 사건의 실행 주체·도구 인자·근거 ID·정책 버전·부모 관계를 적절히 연결합니다. 비발생 사건을 추가하거나 가짜 모델 응답을 실제 기록에 끼워 넣지 않습니다. UI 단계 탐색은 실행 기록의 재생이며 Runtime을 매 단계 강제 정지시키는 기능이 아닙니다.
