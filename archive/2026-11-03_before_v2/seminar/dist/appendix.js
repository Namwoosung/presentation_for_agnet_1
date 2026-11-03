import {blocks} from './markdown.js';
const prose=(title,text)=>({title,block:{type:'text',text}});
const code=(title,text)=>({title,block:{type:'code',text}});
export function appendixTabs(slide){const all=blocks(slide.body),tables=all.filter(x=>x.type==='table'),codes=all.filter(x=>x.type==='code');const table=(title,i)=>({title,block:tables[i]});
 switch(slide.id){
 case 'X01':return tables[0].rows.map((row,i)=>({title:row[0],architecture:['hermes','pydantic','openai','adk','maf','claude-code','claude-sdk'][i],block:{type:'table',headers:['대표 경로','공개 범위'],rows:[[row[1],row[2]]]}}));
 case 'X02':return [prose('Tool 7단계','정의 → Schema → 선택 → Parse/Validate → Policy/Approval → 실행 → Result 기록'),table('네 종류의 실패',0),table('종료와 중단',1),prose('EndStrategy 추적 질문','early / graceful / exhaustive\nFinal 후보 + Function Tool, 검증 실패, 이미 실행 중인 Tool, Streaming일 때 실제 분기를 고정 버전 소스로 확인합니다. 상세 순서·기본값은 이 자료에서 확정하지 않습니다.')];
 case 'X03':return [table('병렬성 다섯 종류',0),prose('기술별 실행 단위','Hermes: 스레드 계열 + 구간/장벽\nPydanticAI: async Task + sequential 장벽\nOpenAI: async Tool + 상한 설정\nADK: Tool batch / 별도 ParallelAgent·TaskGroup\nMAF: Function invocation / Workflow Superstep\nClaude Code: 문서화된 동시 작업 계약\nClaude SDK: CLI 스케줄 결과 수신'),prose('위임의 공유 범위','Child ID·Parent Link / Context·Tool·예산·종료\n반환 계약 / 실패·취소 전파 / 부모의 결과 재검증\n부모 종료 시 detach·cancel·background 정책\n독립 Context는 OS·테넌트 격리 증거가 아닙니다.')];
 case 'X04':return [table('저장물 여섯 범주',0),table('요청 변환 다섯 방식',1),prose('Cache / 저장 정책','Provider cache / cache control / Prefix 안정화 / 앱 캐시를 구분합니다.\n압축은 삭제 정책이 아닙니다. 실제 저장 History의 변환 여부는 구현별로 확인합니다.\nPrompt Cache와 앱 결과 캐시는 별도입니다.')];
 case 'X05':return [prose('Skill 품질 단계','INF · 품질 설계 권고\n생성 → 검증 → 평가 → 승인·버전 → 로딩 → 로그 회수·수정'),prose('검증에서 배포까지','Candidate 식별 / 초안 / Schema·경로·권한 검증\n샘플 Dry-run·Eval / 검토 / 버전·서명 등록\n점진 로딩 / 오류 회수\n제품 기본 자동 기능이 아닌 설계 권고입니다.'),prose('MCP / Plugin 신뢰 경계','절차 문서 → Context / Tool 실행 → 외부 변경\nMCP Server는 프로토콜 노출, Plugin은 호스트 규약 확장입니다.\n중복 Tool의 이름·정책·감사 경로 충돌을 확인합니다.')];
 case 'X06':return [prose('설계 참조 상태도','Running → Pending → Authorized → Revalidate → Running / Completed\n거절 / 만료 / 실패 분기를 별도로 둡니다.\n단순 승인·Checkpoint는 Exactly-once 보장이 아닙니다.'),table('승인과 실행에 결합할 정보',0),prose('제품별 제공 수단','Hermes: Approval / Tool Policy\nPydanticAI: Deferred requests / results\nOpenAI: RunState\nADK: Event / Confirmation / Workflow\nMAF: Approval / HITL RequestPort / Checkpoint\nClaude CLI: Prompt / Hook\nClaude SDK: Permission / callback\n동일 내구성·저장 형식을 보장하는 표가 아닙니다.')];
 case 'X07':return ['호출 / 실행','정책 / 복구','Context / 지식','운영 / 변경'].map((title,i)=>({title,block:{...tables[0],rows:tables[0].rows.slice(i*6,i*6+6)}}));
 case 'X08':return [{title:'참조 인터페이스 · PSEUDO',block:codes[0]},{title:'최소 Runtime · PSEUDO',block:codes[1]},prose('상태와 외부 변경의 경계','principal / deadline / expected_version / idempotency_key\nState commit과 외부 변경의 원자성은 별개입니다.\nOutbox / 완료 조회 / 조정이 필요할 수 있습니다.')];
 case 'X09':return [table('설계 선택',0),table('연구 적합성',1),prose('Host / Provider 점검','Host: Auth·Tenant·Session / Credential 분리 / Worker·Tool·LLM 동시성 / deadline·취소 / 영속 상태 / 로그 보존\nProvider: Tool arguments / Structured Output / Stream chunk / 취소 / 토큰 / Cache / Retry / 병렬 호출\n중앙 Agent와 로컬 Agent + 중앙 LLM은 책임 위치를 비교합니다. 용량·속도 수치는 미확정입니다.')];
 case 'X10':return [table('발표자 Q&A · 30문항',0)];
 default:return all.map((block,i)=>({title:String(i+1),block}));
 }
}
