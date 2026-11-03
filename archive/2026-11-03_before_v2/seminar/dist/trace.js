export const kinds=['model.request','model.response','tool.intent','tool.policy','tool.start','tool.result','context.next','state.commit','node.enter','output.validate','run.end','run.error'];
export function validateTrace(t){
 if(!t||t.schema!=='seminar-trace/v1')throw Error('schema는 seminar-trace/v1이어야 합니다.');
 if(!['illustrative','recorded','scripted','live'].includes(t.mode))throw Error('mode가 올바르지 않습니다.');
 if(!['hermes','pydantic'].includes(t.framework))throw Error('framework는 hermes 또는 pydantic이어야 합니다.');
 for(const k of ['runId','sessionId','version','model','recordedAt','observationPoint'])if(typeof t[k]!=='string'||!t[k].trim())throw Error('기록 메타데이터 누락: '+k);
 if(!Array.isArray(t.events)||!t.events.length||t.events.length>10000)throw Error('events는 1–10,000개의 배열이어야 합니다.');
 const ids=new Set();for(const ev of t.events){if(!ev.id||ids.has(ev.id))throw Error('Event ID가 없거나 중복됩니다.');ids.add(ev.id);if(!kinds.includes(ev.kind))throw Error('지원하지 않는 event kind: '+ev.kind);if(typeof ev.label!=='string'||!ev.label.trim())throw Error('event label 누락');if(!ev.timestamp||Number.isNaN(Date.parse(ev.timestamp)))throw Error('유효한 event timestamp가 필요합니다.');if(!ev.payload||typeof ev.payload!=='object')throw Error('event payload 객체가 필요합니다.');if(['recorded','live'].includes(t.mode)&&ev.kind.startsWith('model.')&&!ev.modelId)throw Error('실제 모델 사건에는 modelId가 필요합니다.');if(['recorded','live'].includes(t.mode)&&ev.kind.startsWith('tool.')&&!ev.toolCallId)throw Error('실제 Tool 사건에는 toolCallId가 필요합니다.');}
 if(['recorded','live'].includes(t.mode)&&t.redacted!==true)throw Error('실제 기록은 저장 전 마스킹(redacted: true)을 확인해야 합니다.');
 return t;
}
const secretKeys=/^(api[_-]?key|authorization|password|secret|access[_-]?token|refresh[_-]?token|cookie)$/i;
export function redact(value){if(Array.isArray(value))return value.map(redact);if(value&&typeof value==='object')return Object.fromEntries(Object.entries(value).map(([k,v])=>[k,secretKeys.test(k)?'[REDACTED]':redact(v)]));if(typeof value==='string')return value.replace(/\bsk-[A-Za-z0-9_-]{12,}\b/g,'[REDACTED]').replace(/Bearer\s+[A-Za-z0-9_.-]+/gi,'Bearer [REDACTED]');return value;}
export function illustrative(framework){const hermes=framework==='hermes';const items=hermes?[
 ['model.request','Prompt와 Schema','model',{instructions:'조회 → 근거 비교 → 다른 구간 예측',context:['LOT-A','BIN-X','snapshot-v1','SOP-r3'],tools:['lookup_bin_rate','compare_measurements','predict_bin_rate']}],
 ['model.response','도구 호출을 제안','runtime',{tool:'lookup_bin_rate',arguments:{lot:'LOT-A',bin:'BIN-X',snapshot:'snapshot-v1'},note:'모델이 실제 생성한 응답이 아닌 설명용 고정 데이터'}],
 ['tool.intent','Tool Intent와 식별자 기록','memory',{intent:'설명용 요청',toolCallId:'illustrative-call-1',externalAtomicity:false}],
 ['tool.policy','조회 범위 인가 확인','risk',{principal:'analyst-A',scope:'실제 인가 결과 미연결'}],
 ['tool.start','Handler / Backend 경계','tool',{tool:'lookup_bin_rate',executed:false,required:['분모','기간','Snapshot ID']}],
 ['tool.result','결과 기록의 자리','tool',{rate:null,denominator:null,period:null,snapshot:'snapshot-v1',note:'실제 데이터 미연결. 조회값을 생성하지 않음'}],
 ['context.next','다음 Context에 결과 연결','memory',{required:['Tool Call / Result 쌍','원문 ID','다음 요청'],comparison:'비교·예측은 실제 근거와 target 정의 후 연결'}],
 ['run.end','관찰 질문으로 회수','runtime',{question:'어느 사건이 다음 반복을 만들었나?',status:'설명용 경로 종료 / 실제 Run 없음'}]
 ]:[
 ['node.enter','UserPromptNode','runtime',{entry:'Agent.run / Agent.iter',note:'대표 경계 설명용. 실제 Node 이벤트 미연결'}],
 ['model.request','Schema / Deps의 경계','model',{schema:'Tool의 입력 형식',dependencies:'Python 실행 자원. 자동 전체 Prompt 복사 아님'}],
 ['node.enter','ModelRequestNode','runtime',{boundary:'모델 요청 / 응답'}],
 ['node.enter','CallToolsNode','runtime',{boundary:'Tool 요청 / 출력 후보 분류·검증'}],
 ['output.validate','검증 실패와 Retry 질문','risk',{question:'형식 실패 / 사실 오류 / 인가 실패는 어디서 처리할까?',retryOccurred:false}],
 ['tool.policy','Deferred 계약의 연결점','risk',{requests:'DeferredToolRequests',results:'DeferredToolResults',appResponsibilities:['승인자','인자·버전','만료','재검증','멱등성'],approvalOccurred:false}],
 ['context.next','History와 다음 Node','memory',{transition:'Tool / Retry → 다음 모델 요청, 유효 Final → End',endStrategy:'세 전략 상세 순서 미확정'}],
 ['run.end','SDK와 앱 책임 회수','runtime',{status:'설명용 경로 종료 / 실제 Core Run 없음',question:'SDK가 해준 일과 앱이 구현한 일은 무엇인가?'}]
 ];return {schema:'seminar-trace/v1',mode:'illustrative',framework,version:hermes?'v0.22.5 (분석 기준)':'Core v2.61.0 (분석 기준)',model:'미연결',runId:'illustrative-only',sessionId:'no-real-session',recordedAt:'2026-11-03T00:00:00+09:00',observationPoint:'로컬 고정 설명 데이터 · Provider payload 아님',redacted:true,events:items.map(([kind,label,role,payload],i)=>({id:'illustration-'+(i+1),kind,label,role,payload,timestamp:'2026-11-03T00:00:'+String(i).padStart(2,'0')+'+09:00'}))};}
