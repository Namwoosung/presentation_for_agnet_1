from diagrams import *

# Screen edits retain the full original copy in slide_map.json and notes.
TITLES={
1:'Agent는 모델 밖의 실행 구조에서 움직인다',2:'제공된 실행 환경에 따라 개발 범위가 달라진다',3:'같은 합성 사례로 일곱 기술의 실행을 비교한다',
6:'모델은 요청하고, Runtime이 Tool을 실행한다',7:'대화 Loop와 Tool 실행 코드는 경계가 나뉜다',8:'Tool 실패와 강제 중단은 처리 경로가 다르다',9:'모델은 조립된 입력만 보고 판단한다',10:'Cache는 연산을 재사용하고, Compaction은 이력을 줄인다',11:'Session·Memory·Skill은 저장 목적이 다르다',12:'기록한 경험과 절차를 다음 실행에 재사용한다',
14:'실행 통제는 승인과 OS·DB 권한에서 이루어진다',17:'Hermes가 제공하는 실행 구조 위에 업무를 확장한다',18:'Hermes 실행 검증은 요청과 결과를 연결해야 한다',19:'Hermes 검증에서는 네 가지 증거를 확인한다',20:'Harness가 제공하는 기능과 운영 책임을 구분한다',
23:'CLAUDE.md·Skill·Memory가 프로젝트 맥락을 제공한다',24:'Permissions·Hooks·Sandbox는 서로 다른 경계를 통제한다',26:'Claude Code는 변경 계획부터 테스트까지 연결한다',27:'Hermes와 Claude Code는 주된 작업 환경이 다르다',28:'SDK를 쓰면 앱이 Agent 구성요소를 조립한다',30:'앱 코드와 Core가 서로 다른 일을 맡는다',31:'Agent·Tool·Output을 Python 코드로 연결한다',32:'Core는 모델 응답에 따라 Tool과 종료로 분기한다',33:'Instructions·Deps·History는 전달 범위가 다르다',34:'Schema 뒤에도 검증과 실제 함수 실행이 남는다',35:'Output 타입은 구조를 검증하고 후속 처리를 돕는다',36:'종료 정책에 따라 남은 Tool의 실행이 달라진다',38:'실행 API마다 결과를 받는 방식이 다르다',39:'승인 결과와 History를 전달해 실행을 이어간다',40:'Python 서비스 안에서 Agent를 제어할 때 적합하다',41:'Python Tool 검증은 함수와 Core의 경계를 확인한다',42:'검증할 증거도 Core와 앱의 책임에 따라 나뉜다',43:'Hermes와 PydanticAI는 업무를 연결하는 방식이 다르다',
44:'SDK마다 공통 Loop에 더하는 제어 방식이 다르다',45:'OpenAI Agents SDK의 Runner가 다음 실행을 결정한다',48:'Claude Agent SDK는 Claude Code 실행 기능을 연결한다',49:'커스텀 MCP Tool은 SDK 경계를 넘어 호스트에서 실행된다',50:'호스트 앱에서 Claude Code 실행을 업무 흐름에 넣는다',51:'ADK는 Event로 실행과 세션 상태를 연결한다',53:'Event·Session·Memory·Artifact는 역할이 다르다',54:'Microsoft Agent Framework는 Agent와 Workflow를 구분한다',56:'Superstep과 Checkpoint가 Workflow 실행을 조직한다',57:'Orchestration은 Loop와 결과의 귀속으로 구분한다',58:'실행 형태·제어 방식·운영 책임으로 선택한다',59:'Agent Runtime과 모델 서버는 따로 배치할 수 있다',60:'실행 계약을 이해해야 Agent를 설계하고 운영할 수 있다'}
COPY={
1:['모델·Runtime·Tool·상태 저장의 역할을 분리한다','요청부터 실행과 기록까지의 흐름을 따라간다','Harness와 SDK의 개발·운영 범위를 비교한다'],
2:['완성형: Hermes와 Claude Code','개발형: PydanticAI·OpenAI SDK·ADK·Microsoft','Claude Agent SDK는 Claude Code 실행 기능과 연결'],
3:['합성 LOT-A / BIN-X / synthetic-v1','지표 조회·원인 후보·예측을 공통 사례로 사용','데모 실행은 후속 단계에서 검증'],
7:['외부 접점: run_agent.py','반복과 분기: conversation_loop.py','Tool 실행: tool_executor.py / model_tools.py'],
10:['Prefix Cache: 같은 접두부의 연산 재사용','Compaction: 이력을 요약해 입력 크기 축소','캐시 지원 조건과 요약 정보 손실을 구분'],
18:['T1: 합성 LOT-A의 BIN-X 비율 조회','요청·handler·결과·최종 응답을 연결해 확인','실행 전: 실제 Trace와 event_id는 아직 없음'],
19:['Tool Call ID와 실제 결과를 연결','오류 처리와 History 갱신을 관찰','Session 저장과 Memory 갱신을 구별'],
21:['공통: 모델과 Tool을 반복하는 실행 구조','파일·명령 실행은 Runtime과 Tool이 담당','차별점은 프로젝트 규칙과 개발 도구 통합'],
27:['Hermes: 다채널·주기 작업·Memory/Skill 운용','Claude Code: 저장소 탐색·수정·테스트','권한·데이터·상태의 운영 책임은 공통'],
31:['모델·Instructions·Output 타입을 선언','Python Tool을 등록하고 앱 자원을 연결','run 결과를 앱의 후속 처리에 사용'],
36:['유효한 Output Tool과 함수 Tool이 함께 온 경우','early / graceful / exhaustive를 구분','Streaming 확정 시점과 부작용은 별도 검토'],
39:['외부 승인 흐름: Deferred 요청을 앱에 반환','History와 승인·실행 결과로 후속 run 시작','외부 부작용의 중복 방지는 앱이 구현'],
41:['T1: 직접 작성한 get_bin_ratio 함수','T2: 측정값·유효 SOP를 근거로 원인 후보 제시','실행 전: Core와 함수의 실제 이벤트 수집 예정'],
42:['Core: 모델 Loop·인자 검증·결과 수집','앱: SQL·계산·권한·검산·영속화','실측되지 않은 재시도와 승인은 검증 예정'],
43:['Hermes: 기존 실행 환경을 설정·확장','PydanticAI: 앱 코드로 Agent·Tool·Output 조립','같은 데이터라도 운영 책임의 배치가 달라짐'],
47:['Input·Tool·Output 검사는 적용 지점이 다름','승인이 필요한 Tool은 실행을 보류할 수 있음','RunState 복구가 DB 부작용까지 되돌리지는 않음'],
53:['Event는 출력과 state 변경을 전달','Session·Memory·Artifact는 서로 다른 목적','Agent final과 전체 Workflow 완료를 구분'],
58:['바로 쓸 실행 환경인가, 앱에 내장할 SDK인가','Tool·데이터 통제인가, 위임·Workflow 통제인가','기록·검증·복구를 팀이 어디까지 운영할 수 있나'],
59:['중앙 Runtime: 인증·격리·큐·운영을 중앙 관리','로컬 Runtime: 사용자 파일·OS 권한과 연결','모델 연결·지연·배포·데이터 경계를 별도 검토']}

def note(s,role='muted',y=810,x=134):return txt(x,y,s,23,role,limit=130)
def return_loop(k=2,label_text='ToolResult + History로 다음 요청'):
 return g(k,path([(1625,580),(1625,740),(560,740),(560,580)],label_text,'state',label_xy=(1080,725)))
def comparison_flow(top,bottom):
 return label(134,322,top[0],'runtime')+flow(top[1],top[2],y=360,h=112,steps=[0]*len(top[1]))+label(134,590,bottom[0],'tool')+flow(bottom[1],bottom[2],y=630,h=112,steps=[1]*len(bottom[1]))
def branch(labels,subs,role='runtime',start='Tool Call',steps=3):
 s=g(0,node(134,475,340,120,start,'Runtime에서 분기',role))
 for j,(title,sub) in enumerate(zip(labels,subs)):
  yy=320+j*175;k=min(j+1,steps-1);r=['tool','state','risk'][j%3]
  s+=g(k,path([(474,535),(660,535),(660,yy+57),(830,yy+57)],'판단','muted',label_xy=(740,yy+43))+node(830,yy,956,115,title,sub,r))
 return s

def render(i,s):
 n=len(s['builds'])
 if i in [4,20]:return master('H',n,{'H-CORE','H-TOOLS','H-POLICY'} if i==20 else None)
 if i in [21,22]:return master('C',n)
 if i==30:return master('P',n)
 if i==45:return master('O',n)
 if i==48:return sdk_master(n)
 if i==51:return adk_master()
 if i==54:return master('M',n)
 if i in [1,60]:
  b=flow([('User / Host','요청을 시작','muted'),('Runtime','실행과 반복','runtime'),('LLM','판단 / 호출 요청','model'),('Tool','파일 / DB / 함수','tool'),('State','대화와 결과','state')],['요청','API','호출 요청','기록'],steps=[0,0,0,1,1],y=415)
  # The model requests, but the runtime invokes the tool.
  b+=g(1,path([(615,415),(615,345),(1320,345),(1320,415)],'Runtime이 실제 Tool 실행','runtime',label_xy=(960,331)))
  b+=g(2,txt(134,704,'판단',42,'model',600)+txt(430,704,'실행',42,'runtime',600)+txt(730,704,'책임',42,'tool',600)+note('Harness는 실행 환경을 제공하고, SDK는 앱 안의 조립을 돕는다',y=780))
  return b
 if i==2:
  return columns(['완성형 실행 환경','앱에 내장하는 SDK'],[(('Hermes / Claude Code','기존 Loop·Tool·채널을 설정하고 확장'),('PydanticAI / OpenAI Agents SDK','Python 앱에 실행 구조와 도구를 조립')),(('운영 환경에 연결','업무 데이터와 정책은 직접 책임'),('Google ADK / Microsoft AF','Event·Middleware·Workflow로 제어')),(('Claude Code runtime','실행 기능을 제공'),('Claude Agent SDK','호스트 코드에서 런타임을 호출'))])
 if i==3:
  return label(134,318,'교육용 합성 데이터   LOT-A / BIN-X / synthetic-v1','state')+flow([('T1  지표 조회','분자 / 분모 × 100','tool'),('T2  원인 후보','측정값 + 유효 SOP','model'),('T3  단순 예측','시간 누수 없는 검증','runtime')],['근거 확장','검증'],steps=[0,0,0],y=390)+g(1,txt(134,653,'관찰 기준',25,'muted',600)+txt(134,701,'Loop 소유자             직접 개발 범위             확장·정책 경계',29,'ink',600))+g(2,note('Hermes와 PydanticAI의 실제 실행은 후속 데모에서 확인',role='state'))
 if i==5:
  return flow([('User input','이전 대화와 결합','muted'),('AIAgent','모델 요청 구성','runtime'),('LLM response','Tool Call / Final','model'),('Handler','실행 후 결과 반환','tool')],['요청','API','실행'],steps=[0,0,1,2])+return_loop(2)+g(3,note('Tool Call이면 재호출하고, 최종 응답이면 사용자 턴을 종료'))
 if i==6:
  return sequence([('MODEL','model'),('HERMES RUNTIME','runtime'),('TOOL / OS','tool')],[(0,1,'Tool Call: get_bin_ratio','model','요청'),(1,2,'정책 확인 후 dispatch','tool','실행'),(2,1,'ToolResult: 예시 0.12%','tool','반환'),(1,1,'권한 거부 시 실행 차단','risk','거부')])+note('교육용 예: 12 / 10,000 × 100 = 0.12%   ·   실제 관측값 아님',y=837,role='state')
 if i==7:
  lines=['while within_budget:','    response = call_model(messages)','    if response.tool_calls:','        for call in response.tool_calls:','            result = dispatch_tool(call)','            append_tool_result(call.id, result)','        continue','    return response.final_text']
  return codeblock(lines,groups=[0,0,1,1,2,2,3,3])+stack([('run_agent.py','공개 AIAgent 접점','runtime'),('conversation_loop.py','agent/ 아래 반복·분기','runtime'),('Tool executor / dispatch','agent/tool_executor.py / model_tools.py','tool')],x=1225,w=561,y=330,steps=[0,1,2])
 if i==8:return branch(['정상 결과','인자 / Tool 오류','강제 정책 중단 / 취소'],['ToolResult를 모델 입력에 추가','실패 정보로 모델이 재검토할 수 있음','정책에 따라 run 중단, 외부 부작용은 남을 수 있음'])
 if i==9:
  return stack([('Stable / Context / Volatile','시스템 프롬프트의 세 층 / 세션 스냅샷','state'),('History + Tool schemas','선택한 대화와 사용 가능한 기능 설명','state'),('Provider request','조립한 입력 + 호출 시 임시 맥락','model')],w=920)+g(2,node(1200,345,586,210,'모델 밖의 실행 상태','원본 DB / OS 상태 / Credential','muted')+note('자동으로 전부 전달되지 않는다',x=1200,y=625,role='risk'))
 if i==10:
  b=label(134,322,'PREFIX CACHE','model')
  for j,t in enumerate(['같은 접두부','같은 접두부','새 사용자 입력']):b+=g(1,node(134+j*550,360,485,112,t,'연산 재사용' if j<2 else '추가 추론','model'))
  b+=label(134,583,'COMPACTION','state')+g(0,txt(134,535,'대화가 길어지면 입력 비용과 문맥 길이 제약이 커진다',27,'ink'))
  b+=flow([('긴 History','메시지와 Tool 결과','state'),('요약 + 최근 메시지','입력 표현 자체를 축소','state'),('다음 모델 요청','일부 정보 손실 가능','model')],['요약','입력'],y=625,h=112,steps=[0,2,2])
  return b
 if i==11:
  return stack([('SESSION','SQLite / FTS5: 실제 대화와 Tool 결과','state'),('MEMORY','MEMORY.md / USER.md: 유용한 사실과 선호','state'),('SKILL','반복 작업의 절차와 사용법','tool')],w=1100)+g(2,node(1400,495,386,145,'다음 모델 입력','필요 시 검색·로드','model')+path([(1234,700),(1310,700),(1310,570),(1400,570)],'반영','state',label_xy=(1310,650)))
 if i==12:
  return flow([('사용과 발견','유용한 사실·절차','muted'),('Memory / Skill','외부 기록 생성·수정','state'),('다음 요청','조건에 따라 검색·로드','runtime')],['저장','재사용'],steps=[0,1,2])+g(3,note('모델 가중치를 바꾸는 재학습과는 다른 동작',role='risk',y=735))
 if i==13:
  return g(0,node(134,475,420,120,'Tool Registry / Dispatch','등록된 실행 경로 선택','runtime')+node(930,330,856,110,'Built-in Tool','내부 handler가 실행','tool')+path([(554,505),(735,505),(735,385),(930,385)],'실행','tool'))+g(1,node(930,510,856,110,'MCP client ↔ 외부 server','프로토콜 요청 / 서버 측 실행 / 결과 반환','tool')+path([(554,555),(930,555)],'요청 / 반환','tool'))+g(2,node(930,710,856,110,'Plugin / Hook','Tool 등록과 생명주기 이벤트에 개입','runtime')+path([(930,765),(700,765),(700,595),(554,595)],'등록 / hook','runtime',label_xy=(790,748)))
 if i==14:
  return flow([('모델 요청','Tool 이름과 인자','model'),('Policy / Approval','설정에 따른 승인','risk'),('Tool handler','등록된 함수 실행','tool'),('OS / DB ACL','실제 접근권 강제','risk')],['요청','허용 시','접근'],steps=[0,1,2,2])+g(3,note('거부는 실행 성공이 아니다. Tool별 적용 범위와 오류 반환은 구분한다.',role='risk',y=746))
 if i==15:
  return label(134,315,'TOOL 병렬','tool')+fork('Tool A','Tool B',y=335,k=0)+label(134,635,'SUBAGENT 위임','runtime')+flow([('Parent','작업을 나눔','runtime'),('Child Agent Loop','별도 모델·Tool 반복','runtime'),('Parent','summary 수신','runtime')],['위임','반환'],y=665,h=112,steps=[1,1,1])+g(2,note('별도 Context라도 파일·DB가 자동 격리되는 것은 아니다',role='risk',y=835))
 if i==16:
  b=node(1340,485,446,135,'AIAgent','입력에 따른 실행 시작','runtime','H-CORE')
  for j,(title,sub,edge) in enumerate([('CLI','사용자 직접 대화','request'),('Gateway','플랫폼 인증 / 사용자·세션 바인딩','route'),('Cron','정해진 시각에 새로운 작업 실행','new run')]):
   y=330+j*175;b+=g(j,node(134,y,740,115,title,sub,'muted','H-IN')+path([(874,y+57),(1130,y+57),(1130,550),(1340,550)],edge,'runtime',label_xy=(1010,y+42)))
  return b
 if i==17:
  return columns(['Hermes 제공','프로젝트 책임'],[(('Loop / 기본 Tools','이미 구성된 실행 경로'),('업무 Tool / 데이터 접근','합성 Lot 쿼리를 실제 업무 계약에 맞춤')),(('Session / 다중 진입','대화와 채널 연결 구조'),('모델 / Skill / 승인 설정','환경에 맞는 기능과 실행 범위')),(('재사용 가능한 Harness','직접 Loop 조립 부담 감소'),('권한 / 검산 / 운영 장애','실데이터의 의미와 운영 품질 보장'))])
 if i in [18,41]:
  names=['모델 요청','실제 handler','결과 메시지','최종 검증'] if i==18 else ['Agent 정의','Python Tool','Output 검증','앱 저장']
  b=label(134,320,'실행 전 · 검증 계획', 'state')+flow([(t,'수집할 증거','runtime' if j%2==0 else 'tool') for j,t in enumerate(names)],['연결','연결','연결'],steps=[0,1,2,3],y=425)
  b+=g(0,note('합성 LOT-A / BIN-X   ·   snapshot_id: synthetic-v1',y=680,role='state'))
  b+=g(3,note('실제 Trace, event_id, Viewer는 후속 데모 단계에서 생성',y=765))
  return b
 if i==19:
  return flow([('REQUEST','모델 입력과 Tool Call','model'),('HANDLER','실제 인자와 실행 결과','tool'),('HISTORY','다음 요청에 포함된 결과','state'),('PERSISTENCE','Session / Memory 변화','state')],['ID 연결','반환','저장'],steps=[0,1,2,3],y=405)+g(3,note('모든 슬롯: 미검증   ·   캡처나 가상 로그를 실제 관측으로 사용하지 않음',y=740,role='risk'))
 if i==23:
  return stack([('CLAUDE.md','프로젝트별 지속 지시와 규칙','state'),('Skill','특정 작업에서 불러 쓰는 절차','tool'),('Memory','이전 작업에서 남긴 유용한 맥락','state')],w=1120)+g(2,txt(1360,435,'로드 시점',33,'runtime',600)+txt(1360,490,'전문이 매번\n들어가지는 않음',26,'muted')+txt(1360,675,'규칙 ≠ OS 권한',26,'risk',600))
 if i==24:
  return stack([('PERMISSIONS','허용 / 승인 / 거부할 Tool 호출 판단','risk'),('HOOKS','이벤트별 사용자 코드가 정책과 검증에 개입','runtime'),('SANDBOX / OS','파일·네트워크 등 실제 접근 범위 제한','risk')],w=1120)+g(2,txt(1330,410,'정책 경계',32,'risk',600)+txt(1330,475,'고정된 한 줄\n실행 순서가 아님',26,'muted')+note('플랫폼·설정 의존',x=1330,y=730))
 if i==25:
  b=label(134,315,'SUBAGENT','runtime')+flow([('Parent','역할 위임','runtime'),('Subagent','독립 Context','runtime'),('Parent','결과 통합','runtime')],['위임','summary'],y=350,h=112,steps=[0,0,0])
  team=node(134,640,330,100,'Team lead','작업 조정','runtime')+node(735,565,380,95,'Teammate A','독립 Context','runtime')+node(735,715,380,95,'Teammate B','독립 Context','runtime')+node(1436,640,350,100,'Shared tasks','공유 작업 관리','state')
  for yy in [612,762]:team+=path([(464,690),(600,690),(600,yy),(735,yy)],'할당','runtime',label_xy=(600,yy-15))+path([(1115,yy),(1290,yy),(1290,690),(1436,690)],'갱신','state',label_xy=(1270,yy-15))
  team+=path([(925,660),(925,715)],'상호 메시지','runtime',label_xy=(1045,695))
  return b+label(134,555,'AGENT TEAMS','runtime')+g(1,team)+g(2,note('지원 환경을 확인하고, 같은 파일의 동시 편집 충돌을 관리한다',role='risk',y=845))
 if i==26:
  return flow([('요구와 계획','작업 범위 결정','muted'),('코드 수정','역할별 작업 분담','tool'),('테스트','결과와 회귀 확인','tool'),('검토 / 승인','diff와 품질 관문','risk')],['계획','실행','검토'],steps=[0,1,1,2])+g(2,note('Subagent 결과는 주 실행에서 통합하고 Hooks·CI로 검증 경계를 둔다',y=740))
 if i==27:
  return columns(['Hermes','Claude Code'],[(('다채널 / 주기 작업','CLI·Gateway·Cron의 운영 흐름'),('저장소 / 개발 접점','CLI·IDE·Desktop의 개발 흐름')),(('Memory / Skill 활용','반복 작업과 기록 재사용'),('탐색 / 수정 / 테스트','프로젝트 규칙과 도구 통합')),(('업무 Tool과 정책 연결','데이터·권한·운영은 직접 설계'),('프로젝트 Tool과 정책 연결','diff·테스트·실행 환경은 직접 확인'))])
 if i==28:
  return flow([('완성형 Runtime','Hermes / Claude Code','runtime'),('구성요소 연결','Agent / Tool / State','tool'),('내 애플리케이션','API / DB / Policy','muted')],['확장 범위','조립'],steps=[0,1,2])+g(2,note('SDK도 Loop를 제공한다. 업무 서비스와 운영 경계는 앱이 결합한다.',y=740))
 if i==29:
  return stack([('PYDANTIC','데이터 구조와 타입 검증','tool'),('PYDANTIC AI CORE','Agent Loop / Tool / Output / Retry','runtime'),('선택 HARNESS / CAPABILITIES','환경 도구와 추가 기능 계층','runtime')],w=1230)+g(2,txt(1450,435,'Core만으로',27,'runtime',600)+txt(1450,490,'업무 Agent\n구현 가능',28,'ink'))
 if i==31:
  lines=['from pydantic import BaseModel','from pydantic_ai import Agent, RunContext','class BinResult(BaseModel):','    lot_id: str','    ratio: float','agent = Agent(model, output_type=BinResult,','              instructions="합성 지표를 조회")','@agent.tool','async def get_bin_ratio(ctx: RunContext[None],','                        lot_id: str) -> dict:','    return await read_synthetic_fixture(lot_id)','result = await agent.run("LOT-A BIN-X 조회")','print(result.output)']
  return codeblock(lines,'API 형태 예시 · 실행 미검증 / model·fixture는 앱 주입',w=1100,h=510,groups=[0]*7+[1]*4+[2]*2)+stack([('앱 선언','model / Tool / Output','muted'),('Core Loop','모델 왕복과 함수 처리','runtime'),('Result → 앱','검산과 후속 처리','state')],x=1320,w=466,y=330,steps=[0,1,2])
 if i==32:
  return flow([('UserPromptNode','입력 준비','runtime'),('ModelRequestNode','모델 요청 / 응답','model'),('CallToolsNode','Tool·Output 처리','tool'),('End / Error','검증된 출력 또는 종료','runtime')],['요청','응답','종료'],steps=[0,1,2,3])+g(3,path([(1175,566),(1175,740),(745,740),(745,566)],'ToolResult / Retry로 다음 모델 요청','state',label_xy=(960,718)))
 if i==33:
  return columns(['MODEL INPUT','PYTHON RUNTIME'],[(('Instructions','모델에 전달할 지침'),('RunContext.deps','DB client / principal / 서비스 객체')),(('History + Tool schemas','앱이 전달한 이력과 기능 설명'),('Tool handler','Deps를 사용해 실제 조회와 계산')),(('선택한 Tool 결과','반환된 데이터가 입력에 합류'),('별도 영속화 / 권한','History 저장·DB 인가는 앱 정책'))],roles=('model','runtime'))
 if i==34:
  return flow([('JSON schema','모델에 기능 설명','state'),('Tool Call','이름과 인자 제안','model'),('Validation','Python 인자 검증','runtime'),('Function','인가 후 읽기 / 계산','tool'),('Result','다음 모델 입력','state')],['전달','요청','실행','반환'],steps=[0,0,1,2,2])+g(3,note('타입 오류는 Retry 경로, 권한 부족은 실행 차단 경로로 설계',y=750,role='risk'))
 if i==35:
  return columns(['자유 텍스트','타입 지정 OUTPUT'],[(('“12%쯤으로 보입니다”','형식과 필드가 일정하지 않음'),('BinResult','lot_id / ratio / snapshot_id')),(('앱에서 다시 해석','문장 파싱과 누락 처리 필요'),('구조·타입 검증','실패 시 정책에 따라 Retry')),(('근거의 사실성','서술만으로 참이라고 판단할 수 없음'),('도메인 검산은 별도','유효한 JSON ≠ 올바른 분모와 기간'))],roles=('muted','runtime'))
 if i==36:
  b=label(134,299,'조건: 유효한 Output Tool + 함수 Tool을 같은 응답에 포함','model')
  b+=columns(['종료 정책','함수 Tool 처리'],[(('early','첫 유효 Output에서 종료'),('건너뜀','동시에 요청된 함수 Tool 실행 생략')),(('graceful · 현재 문서 기본','첫 유효 Output 선택'),('실행','함수 실패 시 최종 출력 재검토 가능')),(('exhaustive','추가 Output Tool까지 실행'),('실행','첫 유효 출력은 응답 순서로 결정'))],roles=('runtime','tool'),steps=[0,1,1])
  b+=g(2,note('Streaming 조기 확정은 별도. 세 정책 모두 외부 쓰기의 exactly-once 보장은 아님.',y=843,role='risk'))
  return b
 if i==37:
  return fork('BIN 비율 조회','측정값 조회',y=330,k=0)+g(1,note('반환 순서는 시작 순서와 다를 수 있다',y=655,role='state'))+g(2,node(134,710,480,105,'승인','정책 결정','risk')+path([(614,763),(1050,763)],'승인 이후에만','risk')+node(1050,710,736,105,'게시','순서 의존 작업은 직렬화·동기화','tool'))
 if i==38:
  b=g(0,node(134,355,500,126,'run','async 최종 결과','runtime'))+g(1,node(710,355,500,126,'run_sync','동기 코드에서 호출','runtime'))+g(2,node(1286,355,500,126,'run_stream','생성 중 결과 관찰','runtime'))
  for j,x in enumerate([384,960,1536]):b+=g(j,path([(x,481),(x,625)],'같은 실행 기반','runtime',label_xy=(x,565)))
  return b+node(134,625,1652,150,'공통 Core Loop','관찰 API와 Tool 실행 정책은 별도의 축','runtime')
 if i==39:
  return flow([('모델 요청','승인 대상 Tool','model'),('Deferred 요청','앱에 제어 반환','runtime'),('승인 / 거부','외부 UI·정책 결정','risk'),('후속 run','History + 승인 결과','runtime'),('Tool 처리','승인 시 실행','tool')],['보류','요청','resume','실행'],steps=[0,0,1,2,2])+g(2,note('외부 승인 흐름의 개념도. 동일 프로세스 내 handler 해결 방식도 별도로 지원한다.',y=740))
 if i==40:
  return columns(['CORE가 제공','개발팀이 구현'],[(('모델 왕복 / Tool 처리','실행 루프와 인자 처리'),('Python 업무 함수','합성 Lot 조회·집계·검산')),(('Output / Retry','타입과 형식 검증'),('DB / 권한 / API 서버','업무 규칙과 데이터 접근')),(('실행 관찰 API','결과와 스트리밍 접근'),('저장 / 배포 / 운영 테스트','서비스 수명과 장애 복구'))])
 if i==42:
  return flow([('CORE 이벤트','model / validation / result','runtime'),('앱의 Tool 코드','SQL / 계산 / 권한','tool'),('앱 저장·검산','snapshot / 분모 / 기간','state')],['실행','저장'],steps=[0,1,2])+g(2,note('실행 전 · 관측값 없음. 실제 함수 결과와 모델 해석을 별도 증거로 수집한다.',y=750,role='state'))
 if i==43:
  return columns(['HERMES','PYDANTIC AI'],[(('Loop / 기본 Tool','Harness가 제공'),('Core Loop / Python Tool','Core 제공 + 업무 함수를 직접 작성')),(('Session / 채널 UI','제공된 운영 환경을 구성'),('영속화 / 사용자 UI','앱의 API·DB·화면과 결합')),(('업무별 확장','Tool / Skill / 정책 설정'),('업무별 조립','Agent / Deps / Output 정의'))])
 if i==44:
  return flow([('Agent 정의','지침과 도구','muted'),('Model','판단과 호출 요청','model'),('Tool','앱 함수 실행','tool'),('다음 Model','결과 기반 반복','model')],['요청','Runtime 실행','반환'],steps=[0,0,0,0],y=360)+g(1,note('데이터·권한·배포는 앱과 운영 환경이 통합',y=615))+g(2,txt(134,720,'OpenAI',28,'runtime',600)+txt(134,770,'위임과 제어권',25,'muted')+txt(570,720,'Claude SDK',28,'runtime',600)+txt(570,770,'CLI 런타임 연결',25,'muted')+txt(1006,720,'Google ADK',28,'runtime',600)+txt(1006,770,'Event와 세션',25,'muted')+txt(1442,720,'Microsoft',28,'runtime',600)+txt(1442,770,'Middleware / Workflow',24,'muted'))
 if i==46:
  return comparison_flow(('AGENT AS TOOL',[('Manager','최종 응답 주체','runtime'),('Specialist','부분 작업 수행','tool'),('Manager','결과를 받아 답변','runtime')],['tool call','return']),('HANDOFF',[('Agent A','요청 분류','runtime'),('Handoff','활성 Agent 변경','runtime'),('Agent B','사용자에게 답변','tool')],['위임','제어 전환']))+g(2,note('같은 다중 Agent 구조라도 마지막 답변의 주체가 다르다',y=815,role='runtime'))
 if i==47:
  return stack([('INPUT GUARDRAIL','체인의 첫 Agent 입력 검사','risk'),('TOOL APPROVAL / TOOL GUARDRAIL','설정한 Tool과 지원 범위에서 실행 전후 검사','risk'),('OUTPUT / RUNSTATE','최종 출력 검사와 중단 상태 재개','state')],w=1120)+g(2,txt(1360,430,'외부 DB',34,'tool',600)+txt(1360,490,'트랜잭션·중복 방지는\n앱의 별도 책임',24,'muted')+txt(1360,740,'State ≠ rollback',24,'risk',600))
 if i==49:
  return sequence([('HOST CALLBACK','tool'),('SDK TRANSPORT','runtime'),('CLI RUNTIME','runtime')],[(2,1,'MCP Tool 요청','runtime','요청'),(1,0,'host 함수 실행','tool','실행'),(0,2,'SDK를 통해 결과 복귀','tool','반환')])+g(2,note('Permission / Hook은 종류별 지점에 적용. Session과 파일 checkpoint의 범위는 별도.',y=790))
 if i==50:
  return flow([('업무 서비스 / 배치','작업 요청과 실행 환경','muted'),('SDK ↔ CLI','도구·세션 이벤트 관찰','runtime'),('결과 / 산출물 저장','앱의 후속 처리','state')],['요청','반환'],steps=[0,1,2])+g(2,note('호스트는 설치·인증·비밀정보·비용을 관리한다. vLLM 직접 호환을 가정하지 않는다.',y=740,role='risk'))
 if i==52:
  b=label(134,315,'SEQUENTIAL AGENT','runtime')+flow([('Agent A','별도 실행 단위','runtime'),('Agent B','앞 단계 뒤 실행','runtime'),('결과','순서대로 전달','state')],['완료 후','반환'],y=350,h=112,steps=[0,0,0])
  parallel=node(134,640,330,100,'Fork','분기 시작','runtime')+node(735,565,380,95,'Branch Agent A','자신의 모델·Tool 실행','runtime')+node(735,715,380,95,'Branch Agent B','자신의 모델·Tool 실행','runtime')+node(1436,640,350,100,'Join','결과를 수집','state')
  for yy in [612,762]:parallel+=path([(464,690),(600,690),(600,yy),(735,yy)],'실행','runtime',label_xy=(600,yy-15))+path([(1115,yy),(1290,yy),(1290,690),(1436,690)],'합류','state',label_xy=(1270,yy-15))
  return b+label(134,555,'PARALLEL AGENT','runtime')+g(1,parallel)+g(2,note('Tool 병렬은 하나의 Agent 안의 handler 동시 실행이며, Branch Agent와 다르다.',y=845,role='tool'))
 if i==53:
  return stack([('SESSION STATE','현재 대화·작업의 상태','state'),('MEMORY','다른 실행에서 활용할 정보','state'),('ARTIFACT','파일 등 산출물 저장','tool')],x=1120,w=666)+g(0,txt(134,360,'Event',54,'runtime',600)+txt(134,420,'출력 / state delta / 실행 정보',27,'muted'))+g(1,path([(134,550),(990,550)],'Event stream','runtime'))+g(2,txt(134,660,'Agent final',30,'runtime',600)+txt(134,714,'전체 Workflow 완료와 범위를 구별',25,'risk')+txt(134,780,'SessionService와 운영 정책에 따라 저장·재개',23,'muted'))
 if i==55:
  return flow([('Agent / Function','실행 요청','runtime'),('Middleware','공통 정책과 관찰','risk'),('정상 실행','모델 / Tool 호출','tool')],['개입','계속'],steps=[0,0,1],y=340)+g(2,node(134,650,715,140,'일반 Tool error','정책에 따라 모델 결과로 전달','state')+node(1071,650,715,140,'강제 policy stop','위험 동작을 차단하고 run 종료','risk'))
 if i==56:
  return fork('Executor A','Executor B',y=340,k=0,workflow=True)+g(1,rule(1260,305,1260,660,'runtime',True)+label(735,315,'SUPERSTEP 1','runtime')+label(1436,315,'SUPERSTEP 2','runtime'))+g(2,node(134,705,720,115,'Checkpoint','실행 상태와 다음 단계 메시지 저장','state')+node(1070,705,716,115,'외부 DB side effect','중복 방지·원자성은 별도 설계','risk'))
 if i==57:
  def mini(x,y,w,t,r):return box(x,y,w,60,r)+txt(x+w/2,y+37,t,21,r,600,'middle')
  b=rule(960,310,960,835)+rule(134,565,1786,565)
  b+=g(0,label(134,330,'TOOL PARALLEL','tool')+mini(134,422,160,'Loop','runtime')+mini(420,375,160,'Tool A','tool')+mini(420,475,160,'Tool B','tool')+mini(720,422,160,'같은 Loop','runtime')+path([(294,452),(355,452),(355,405),(420,405)],'실행','tool',label_xy=(350,389))+path([(294,452),(355,452),(355,505),(420,505)],'실행','tool',label_xy=(350,532))+path([(580,405),(640,405),(640,452),(720,452)],'반환','tool',label_xy=(640,389))+path([(580,505),(640,505),(640,452),(720,452)],'반환','tool',label_xy=(640,532)))
  b+=g(1,label(994,330,'DELEGATION','runtime')+mini(994,422,180,'Parent','runtime')+mini(1300,422,180,'Child Loop','runtime')+mini(1606,422,180,'Parent','runtime')+path([(1174,452),(1300,452)],'위임','runtime')+path([(1480,452),(1606,452)],'summary','state'))
  b+=g(2,label(134,615,'HANDOFF','runtime')+mini(134,720,160,'Agent A','runtime')+mini(420,720,160,'Agent B','runtime')+mini(720,720,160,'User','muted')+path([(294,750),(420,750)],'제어 전환','runtime')+path([(580,750),(720,750)],'최종 응답','tool'))
  b+=g(3,label(994,615,'WORKFLOW','state')+mini(994,720,160,'Start','runtime')+mini(1280,675,160,'Exec A','tool')+mini(1280,775,160,'Exec B','tool')+mini(1606,720,180,'Join / Next','runtime')+path([(1154,750),(1210,750),(1210,705),(1280,705)],'분기','runtime',label_xy=(1210,686))+path([(1154,750),(1210,750),(1210,805),(1280,805)],'분기','runtime',label_xy=(1210,832))+path([(1440,705),(1520,705),(1520,750),(1606,750)],'합류','state',label_xy=(1520,686))+path([(1440,805),(1520,805),(1520,750),(1606,750)],'합류','state',label_xy=(1520,832)))
  return b
 if i==58:
  return checklist([('실행 형태','Hermes·Claude Code는 운영 환경, PydanticAI·OpenAI·ADK·Microsoft는 앱 내 구성'),('특화 제어','Claude SDK의 CLI 연결, OpenAI의 위임, ADK의 Event, Microsoft의 Middleware·Workflow'),('운영 책임','Tool 권한·검산·상태 저장·복구를 책임질 주체와 테스트 범위를 결정')])
 if i==59:
  b=label(134,320,'A  중앙 실행','runtime')+label(1000,320,'B  사용자 PC 실행','runtime')
  b+=g(0,box(134,345,760,345,'line',True,fill='#F0F3F8')+node(164,385,320,110,'API / Auth','요청과 사용자 인증','muted')+node(550,385,310,110,'Agent worker','중앙 Loop / Session','runtime')+path([(484,440),(550,440)],'요청','runtime')+node(550,550,310,110,'Tools / DB','서버 권한으로 실행','tool')+path([(705,495),(705,550)],'실행','tool',label_xy=(760,532)))
  b+=g(1,box(970,345,816,345,'line',True,fill='#F0F3F8')+node(1000,385,350,110,'Desktop Agent','로컬 Loop / Session','runtime')+node(1435,385,320,110,'Local tools','사용자 파일 / OS','tool')+path([(1350,440),(1435,440)],'실행','tool')+txt(1000,600,'설치·업데이트·로컬 권한 관리',24,'muted'))
  b+=g(2,node(550,745,1000,100,'중앙 / 외부 LLM endpoint','모델 요청 경계와 Tool 실행 위치는 독립','model')+path([(350,690),(350,795),(550,795)],'model API','model',label_xy=(350,748))+path([(1600,690),(1600,795),(1550,795)],'model API','model',label_xy=(1680,748)))
  return b
 raise ValueError(f'Missing diagram S{i:02}')
