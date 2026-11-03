const __m2=(()=>{
// Stable node identities and positions are reused by overview/detail slides.
const n=(id,label,x,y,role='runtime',step=0)=>({id,label,x,y,role,step});
const architectures={
 'arch-hermes':{name:'Hermes · 공개 Harness',ref:'C §4.1 · SRC',boundary:[{x:275,y:180,w:430,h:320,label:'AIAgent / Harness'}],nodes:[n('host','CLI / Gateway / Cron',440,65,'runtime'),n('loop','AIAgent Loop',440,260,'runtime'),n('prompt','Prompt Builder',80,200,'memory',2),n('memory','Memory / Skills',80,390,'memory',2),n('model','Provider / Model',810,190,'model',1),n('tool','Tool Executor / Backend',810,380,'tool',1),n('store','SQLite Session / FTS5',440,610,'memory',2),n('extensions','Registry / MCP / Plugin',810,590,'tool',3)],edges:[['host','loop'],['prompt','loop'],['memory','prompt'],['loop','model'],['model','loop'],['loop','tool'],['tool','loop'],['loop','store'],['extensions','tool','설정·확장',true]]},
 'arch-claude-code':{name:'Claude Code · 공식 동작 계약',ref:'C §4.6 · DOC / UNV',boundary:[{x:260,y:145,w:465,h:420,label:'CLI Runtime · 핵심 엔진 비공개'}],nodes:[n('host','Host / CLI 입력',440,45),n('cli','Claude Code Runtime',440,265),n('context','Instructions / Memory / Skills',55,210,'memory',1),n('policy','Permissions / Hooks',440,455,'risk',2),n('model','Model',810,195,'model'),n('tool','Workspace / Tools / MCP',810,420,'tool',2),n('store','Session / Transcript',440,610,'memory',1)],edges:[['host','cli'],['context','cli','지침',true],['cli','model'],['cli','policy'],['policy','tool'],['cli','store']]},
 'arch-pydantic':{name:'PydanticAI · Core와 외부 책임',ref:'C §4.2 · SRC / INF',boundary:[{x:270,y:160,w:440,h:360,label:'Core · 내부 Agent Graph'}],nodes:[n('input','Agent / Dependencies',440,55),n('graph','내부 Graph',440,245),n('model','Model / Provider',810,185,'model',1),n('manager','ToolManager',810,390,'runtime',1),n('tools','App Tools / Backend',810,600,'tool',1),n('validator','History / Output Validator',440,455,'memory',1),n('capabilities','Capabilities / Hooks',55,200,'runtime',2),n('host','별도 Harness / Host / Store',55,460,'memory',3),n('workflow','별도 사용자 Workflow Graph',440,610,'runtime',3)],edges:[['input','graph'],['graph','model'],['graph','manager'],['manager','tools'],['graph','validator'],['capabilities','graph','개입',true],['host','graph','별도 구성',true],['workflow','input','선택',true]]},
 'arch-openai':{name:'OpenAI Agents SDK · Runner',ref:'C §4.3 · SRC',boundary:[{x:270,y:160,w:445,h:345,label:'Runner 실행 경계'}],nodes:[n('host','Host / Agent 설정',440,50),n('runner','Runner',440,240),n('resolver','ProcessedResponse / NextStep',440,440,'runtime',1),n('model','Model',810,180,'model'),n('tools','Tools / Function Guardrails',810,410,'tool',1),n('guards','Input / Output Guardrails',55,250,'risk',2),n('store','Session / RunState',440,610,'memory',3),n('trace','Tracing',55,565,'memory',3)],edges:[['host','runner'],['runner','model'],['model','resolver'],['resolver','tools'],['tools','runner'],['resolver','store'],['guards','runner','검사',true],['runner','trace','관찰',true]]},
 'arch-claude-sdk':{name:'Claude Agent SDK · 프로세스 경계',ref:'C §4.7 · SRC / UNV',boundary:[{x:0,y:140,w:350,h:470,label:'Python 프로세스 · 공개 SDK'},{x:395,y:140,w:335,h:470,label:'CLI 프로세스 · 내부 비공개'}],nodes:[n('api','query / ClaudeSDKClient',60,210),n('client','InternalClient',60,385),n('transport','SubprocessCLITransport',60,555),n('cli','Claude Code Runtime',440,285),n('control','Control / Hooks / Permission',440,505,'risk',2),n('model','Model',810,210,'model'),n('tools','Workspace / CLI Tools',810,440,'tool',1),n('messages','Parser / typed messages',440,625,'memory',3)],edges:[['api','client'],['client','transport'],['transport','cli','JSON stream'],['cli','model'],['cli','tools'],['cli','control'],['control','client','Callback'],['cli','messages','ResultMessage']]},
 'arch-adk':{name:'Google ADK · Flow와 Event 저장',ref:'C §4.4 · SRC · 대표 경로',boundary:[{x:265,y:145,w:450,h:365,label:'Agent / Flow 실행'}],nodes:[n('runner','Host / Runner',440,45),n('flow','LlmAgent / BaseLlmFlow',440,240),n('event','Event / State Delta',440,445,'memory',2),n('model','Model',810,190,'model',1),n('tools','Tool Batch',810,415,'tool',1),n('memory','MemoryService',55,220,'memory',3),n('artifact','ArtifactService',55,435,'memory',3),n('session','Runner / SessionService',440,610,'memory',2)],edges:[['runner','flow'],['flow','model'],['flow','tools'],['flow','event'],['event','session'],['memory','flow','Context',true],['artifact','flow','근거',true]]},
 'arch-maf':{name:'Microsoft · 서로 다른 세 반복',ref:'C §4.5 · SRC / DOC',boundary:[{x:255,y:155,w:480,h:370,label:'Agent Pipeline / Function Invocation'},{x:5,y:5,w:1055,h:540,label:'선택적 Harness · 매 Run 활성 보장 아님',dashed:true}],nodes:[n('agent','Agent / RawAgent',435,220),n('context','Context Providers',55,340,'memory'),n('chat','ChatClient',435,400,'model',1),n('tool','Function Tool Loop',810,420,'tool',1),n('harness','Harness Agent 재호출',435,55,'runtime',2),n('workflow','별도 Workflow Scheduler',435,620,'runtime',3),n('state','Executor / Superstep / Checkpoint',810,620,'memory',3)],edges:[['context','agent'],['agent','chat'],['chat','tool'],['tool','chat'],['harness','agent','선택',true],['workflow','agent','실행',true],['workflow','state','상태 전이']]}
};

return {architectures};
})();
const __m1=(()=>{
const {architectures}=__m2;
const colors={runtime:'#B794F4',model:'#60A5FA',tool:'#34D399',memory:'#FDBA74',risk:'#FB7185',success:'#5EEAD4'};
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const wrap=(s,max=24)=>{const words=s.split(/(\s+|\/| → | · )/);let lines=[''];for(const word of words){if((lines.at(-1)+word).length>max&&lines.at(-1))lines.push('');lines[lines.length-1]+=word;}return lines;};
function txt(s,x,y,size=24,fill='#EFF4FF',anchor='middle',max=24){const lines=wrap(s,max);return `<text x="${x}" y="${y-(lines.length-1)*size*.6}" fill="${fill}" font-size="${size}" text-anchor="${anchor}">${lines.map((l,i)=>`<tspan x="${x}" dy="${i?size*1.25:0}">${esc(l.trim())}</tspan>`).join('')}</text>`;}
const start=(label)=>`<svg class="diagram" viewBox="-25 -20 1130 770" role="img" aria-label="${esc(label)}"><defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#9EACC8" stroke-width="1.5"/></marker></defs>`;
function node(n,step,ref){const c=colors[n.role]||colors.runtime;return `<g data-node-id="${esc(n.id)}" data-role="${n.role||'runtime'}" data-source="${esc(ref||'')}" class="reveal ${n.step>step?'pending':''}"><title>${esc(ref||'대표 경로')}</title><rect x="${n.x}" y="${n.y}" width="245" height="90" rx="5" fill="#0d1528" stroke="${c}" stroke-width="2"/>${txt(n.label,n.x+122.5,n.y+50,21,c,'middle',24)}</g>`;}
function edge(a,b,label='',dash=false,step=0){const ax=a.x+122.5,ay=a.y+45,bx=b.x+122.5,by=b.y+45;let x1=ax,y1=ay,x2=bx,y2=by;if(Math.abs(bx-ax)>Math.abs(by-ay)){x1+=Math.sign(bx-ax)*123;x2-=Math.sign(bx-ax)*130;}else{y1+=Math.sign(by-ay)*45;y2-=Math.sign(by-ay)*53;}return `<g><path d="M${x1},${y1} L${x2},${y2}" fill="none" stroke="#9EACC8" stroke-width="2" ${dash?'stroke-dasharray="7 6"':''} marker-end="url(#arrow)"/>${label?txt(label,(x1+x2)/2,(y1+y2)/2-13,16,'#9EACC8'):''}</g>`;}
const architectureFor={S03:'hermes',S05:'hermes',S07:'hermes',S10:'hermes',S11:'hermes',S12:'claude-code',S14:'pydantic',S19:'pydantic',S21:'pydantic',S22:'openai',S25:'claude-sdk',S26:'claude-sdk',S27:'adk',S29:'maf'};
function architecture(key,step=99){const a=architectures[key];if(!a)return '';return start(a.name)+`<g id="${key}">${(a.boundary||[]).map(b=>`<rect x="${b.x}" y="${b.y}" width="${b.w}" height="${b.h}" rx="10" fill="none" stroke="#33415D" ${b.dashed?'stroke-dasharray="8 8"':''}/>${txt(b.label,b.x+15,b.y+26,16,'#9EACC8','start',60)}`).join('')}${a.edges.map(e=>edge(a.nodes.find(n=>n.id===e[0]),a.nodes.find(n=>n.id===e[1]),e[2],e[3])).join('')}${a.nodes.map(n=>node(n,step,a.ref)).join('')}</g>`+txt(a.ref,530,735,17,'#9EACC8')+'</svg>';}
const sequences={
 S04:{lanes:['Model','Runtime','Store','Tool'],events:[[1,0,'① 요청 / 응답'],[1,2,'② Tool Intent 기록'],[1,3,'③ Handler 실행'],[3,1,'결과 반환'],[1,2,'Tool Result 기록'],[1,0,'④ 다음 요청 / Final']],note:'Stop 가지: 예산 · 취소 · 정책 · 오류'},
 S16:{lanes:['Model','ToolManager','App Policy','Backend'],events:[[1,0,'① 타입 기반 Schema'],[0,1,'② Tool Call'],[1,2,'③ 인자 검증 / 인가'],[2,3,'④ 허용된 실행'],[3,1,'Tool Result']],note:'설계 예시 · Dependencies는 실행 자원, 자동 Prompt 복사가 아님'},
 S24:{lanes:['Guardrail','Model / Tool','RunState','Session'],events:[[0,1,'① 병행 가능 · 구성 확인'],[1,1,'② Tool 범위와 검사 시점'],[1,2,'③ 승인 대기 위치 저장'],[1,3,'대화 History 저장']],note:'Output 검사로 이전 Tool 부작용을 되돌리지 않음'},
 S33:{lanes:['Runtime','Journal','publish_report','복원 Run'],events:[[0,1,'① Intent 저장'],[0,2,'② 외부 발행 성공'],[2,0,'③ 응답 기록 전 Crash'],[1,3,'④ 상태 복원'],[3,2,'⑤ 완료 조회 / 멱등 키']],note:'INF · 설명용 장애 경로 · 실제 발행 / 장애 기록 아님'},
 S35:{lanes:['Client','Worker','Model / Tool','Store'],events:[[1,0,'① 부분 Token'],[2,1,'② Agent Final'],[1,3,'③ 정책 / 저장 Commit'],[1,0,'④ Client 수신']],note:'연결 종료 · 실행 종료 · 저장 완료 · 수신 완료를 구분'}
};
function sequence(spec,step){const xs=[95,380,665,950];return start(spec.note)+spec.lanes.map((l,i)=>txt(l,xs[i],30,22,colors[['model','runtime','memory','tool'][i]])+`<line x1="${xs[i]}" y1="65" x2="${xs[i]}" y2="655" stroke="#33415D" stroke-dasharray="5 6"/>`).join('')+spec.events.map(([a,b,label],i)=>{const y=115+i*86;const visible=i<=Math.round((spec.events.length-1)*Math.min(1,step/3));return `<g class="reveal ${visible?'':'pending'}">${a===b?`<path d="M${xs[a]},${y} h90 v35 h-90" fill="none" stroke="#B794F4" stroke-width="2" marker-end="url(#arrow)"/>`:`<line x1="${xs[a]}" y1="${y}" x2="${xs[b]+(a<b?-8:8)}" y2="${y}" stroke="#9EACC8" stroke-width="2" marker-end="url(#arrow)"/>`}${txt(label,(xs[a]+xs[b])/2,y-14,21,'#EFF4FF','middle',40)}</g>`;}).join('')+txt(spec.note,530,715,20,'#FDBA74','middle',65)+'</svg>';}
const flows={
 S02:[['행동','다음 단계 결정','runtime'],['상태','기록과 근거','memory'],['권한','실행 인가','risk'],['복구','재실행 범위','tool'],['근거','SRC / DOC / INF / UNV','model']],
 S06:[['Prefix Cache','동일 Prefix 재전송','model'],['계산 재사용','Provider hit에 종속','model'],['Compaction','History 선택·요약','memory'],['다음 요청','요약 + 최근 결과 + 원문 ID','memory']],
 S08:[['Skill','절차를 Context에 로딩','memory'],['Model','Tool 요청 생성','model'],['Runtime','Registry / Policy / Hook','runtime'],['Tool 실행','Local Handler / MCP Server','tool']],
 S09:[['Tool Round','A / B 병렬 후보','tool'],['충돌 장벽','공유 파일 · DB · 예산','risk'],['Parent Loop','위임과 결과 재검증','runtime'],['Child Loop','독립 Context / ID / 예산','runtime']],
 S13:[['Parent / Child','위임 → 결과 반환','runtime'],['Agent Teams','문서화된 협업 계약','runtime'],['Permission / Hook','Tool 앞 개입 지점','risk'],['Sandbox / Backend','실제 실행 권한','tool']],
 S15:[['UserPromptNode','Agent.run / Agent.iter','memory'],['ModelRequestNode','모델 요청','model'],['CallToolsNode','Tool / Output 분류·검증','runtime'],['End / 다음 요청','유효한 Final / Tool·Retry','success']],
 S17:[['모델 응답','Final 후보 + Function Tools','model'],['종료 정책','early / graceful / exhaustive','runtime'],['부작용 질문','이미 무엇이 실행되었나?','risk'],['출력 검증','형식과 사실 정확성 구분','success']],
 S18:[['Validation Retry','수정 요청 / 모델 피드백','model'],['다른 Retry','Transport / Tool / Node','runtime'],['독립 조회 A / B','병렬 실행 후보','tool'],['sequential 장벽','의존 작업 C / 외부 취소 확인','risk']],
 S20:[['DeferredToolRequests','Pending · 요청 보관','runtime'],['외부 승인 / 실행','승인자 · 인자 · 버전 · 만료','risk'],['Revalidate','변경 / 거절 / 만료 확인','risk'],['DeferredToolResults','결과 반영 / Run 이어가기','tool']],
 S23:[['as_tool','Specialist → Manager → Final','tool'],['Handoff','Agent A → Agent B → Final','runtime'],['Workflow','Scheduler가 다음 경로 결정','runtime']],
 S28:[['Agent A final','개별 발화 종료','model'],['Agent B / Join','남은 업무 수행','runtime'],['Event / State Delta','순서 · 중복 · 재개 범위','memory'],['업무 완료','Artifact ID / 업무 기준','success']],
 S30:[['Agent Middleware','Agent 실행 경계','runtime'],['Chat Middleware','Model 요청 경계','model'],['Function Middleware','최종 실행 인자 / 인가','tool'],['MiddlewareFailure','정책 거절 · 중단 전파 확인','risk']],
 S31:[['Executor A / B','Source 분기','runtime'],['Join / Superstep','업무 키 · Snapshot · 버전','runtime'],['Checkpoint','Workflow 상태 복원','memory'],['외부 DB','별도 Transaction / 장애 틈','risk']],
 S32:[['Transcript','무엇을 대화했나?','memory'],['RunState','어디서 멈췄나?','runtime'],['Event / Checkpoint','변경 이력 / 재개 위치','memory'],['Memory','다음에도 무엇을 기억하나?','memory'],['Side-effect Journal','실제 외부 변경은?','tool']],
 S34:[['Cron / Trigger','언제 시작할까?','runtime'],['Background / Job','누가 계속 소유할까?','runtime'],['Queue / Delivery','전달과 Retry','tool'],['Resume / State','어디서 이어갈까?','memory']],
 S36:[['Runtime','Tool / Output 계약','runtime'],['Adapter / Profile','Provider별 변환','runtime'],['Gateway / Model','Stream · 취소 · Error','model'],['호환성 검증','Token · Cache · 병렬 Calls','risk']],
 S37:[['Contract','Schema / Serializer','runtime'],['Scripted Runtime','고정 응답 · 분기 재현','runtime'],['Integration','실제 Provider / DB / MCP','tool'],['Task Eval','정답 · 근거 · 비용 · 정책','success']],
 S38:[['RunCoordinator','run / resume / cancel','runtime'],['Model / Context','ModelGateway / ContextBuilder','model'],['Tool / Policy','Catalog / PolicyEngine / Executor','tool'],['StateStore','expected_version / 감사','memory']],
 S39:[['통합 실행 환경','빠른 연결 / 설정·정책 이해','runtime'],['조립 가능한 계약','개입 유연성 / Host 설계','tool'],['Event / Snapshot','이력 / 복원 범위 선택','memory'],['자율 Memory','재사용 / 승인·버전 관리','risk']],
 S40:[['Loop와 제어권','누구에게 실행을 맡길까?','runtime'],['상태·권한·복구','우리가 지킬 계약은?','memory'],['데이터·정책·평가','어떤 조건으로 검증할까?','success']]
};
const gn=(id,label,x,y,role='runtime',step=0)=>({id,label,x,y,role,step});
function graph(title,nodes,edges,step,note,extra=''){return start(title)+txt(title,530,22,23,'#9EACC8')+edges.map(([from,to,label,dash])=>edge(nodes.find(n=>n.id===from),nodes.find(n=>n.id===to),label,dash)).join('')+nodes.map(n=>node(n,step,note)).join('')+extra+txt(note,530,720,18,'#FDBA74','middle',70)+'</svg>';}
function stateGraph(slide,step){
 if(slide.id==='S15')return graph('내부 Agent Graph · 대표 전이',[
 gn('user','UserPromptNode',20,150,'memory'),gn('request','ModelRequestNode',410,150,'model',1),gn('tools','CallToolsNode',800,150,'runtime',2),gn('end','End · 유효한 Final',800,485,'success',3)
 ],[['user','request','입력 준비'],['request','tools','응답 분류'],['tools','end','출력 검증']],step,'C §4.2 · 내부 Graph ≠ 사용자 Workflow Graph',`<path d="M922,240 V375 H532 V250" stroke="#B794F4" stroke-width="2" fill="none" marker-end="url(#arrow)"/>${txt('Tool Result / Retry → 다음 요청',530,405,25,'#B794F4')}`);
 if(slide.id==='S09')return graph('Tool Round와 Child Loop의 실행 단위',[
 gn('model','한 모델 응답',20,140,'model'),gn('a','Tool A',410,60,'tool',1),gn('b','Tool B',410,235,'tool',1),gn('barrier','충돌 장벽 / 결과',800,140,'risk',1),gn('parent','Parent Loop',20,510,'runtime',2),gn('child','Child Loop / Context',410,510,'runtime',2),gn('return','부모의 통합·재검증',800,510,'runtime',3)
 ],[['model','a','여러 요청'],['model','b'],['a','barrier'],['b','barrier'],['parent','child','위임'],['child','return','결과 반환']],step,'INF · 같은 파일 / Snapshot / 예산 / 취소 · 독립 Context는 OS 격리 증거가 아님');
 if(slide.id==='S20')return graph('Deferred와 앱 승인 계약',[
 gn('request','DeferredToolRequests',20,100),gn('pending','Pending / 요청 보관',410,100,'memory'),gn('auth','외부 승인 / 실행',800,100,'risk',1),gn('result','DeferredToolResults',20,450,'tool',3),gn('validate','Revalidate / 변경 확인',410,450,'risk',2),gn('deny','거절 / 만료 / 실패',800,450,'risk',3)
 ],[['request','pending'],['pending','auth'],['auth','validate','승인 대상 일치'],['validate','result','결과 연결'],['validate','deny','변경 / 거절']],step,'INF · 앱 책임: 요청 ID / 승인자 / 인자·버전 / 만료 · Exactly-once 별도');
 if(slide.id==='S31')return graph('Workflow 분기·결합과 저장 경계',[
 gn('a','Executor A',20,70),gn('b','Executor B',20,280),gn('join','Join / 다음 Superstep',410,170,'runtime',1),gn('checkpoint','Checkpoint',800,170,'memory',1),gn('external','외부 DB / 발행 API',410,505,'tool',2),gn('gap','외부 성공 ↔ 저장 장애 틈',800,505,'risk',2)
 ],[['a','join'],['b','join'],['join','checkpoint','Workflow 저장'],['join','external','외부 변경'],['external','gap']],step,'INF · 업무 키 예시: LOT-A + snapshot-v1 + SOP-r3 · 외부 원자성 별도');
 if(slide.id==='S38')return graph('INF · 일곱 책임의 참조 설계',[
 gn('coordinator','RunCoordinator',410,50),gn('context','ContextBuilder',20,225,'memory',1),gn('model','ModelGateway',800,225,'model',1),gn('catalog','ToolCatalog',20,450,'tool',2),gn('policy','PolicyEngine',410,450,'risk',2),gn('executor','ToolExecutor',800,450,'tool',2),gn('store','StateStore',410,610,'memory',3)
 ],[['coordinator','context'],['coordinator','model'],['coordinator','policy'],['catalog','policy','Schema'],['policy','executor','허용']],step,'principal / deadline / expected_version / idempotency_key · C §§32–33',`<path d="M655,95 H735 V655 H663" stroke="#9EACC8" fill="none" stroke-width="2" marker-end="url(#arrow)"/>${txt('상태 Commit',740,585,17,'#9EACC8')}`);
 return null;
}
function rows(items,step,{arrows=false,note=''}={}){const count=items.length,spacing=Math.min(145,650/count);return start(note||'책임과 경계')+items.map(([a,b,role],i)=>{const y=55+i*spacing,c=colors[role];return `<g class="reveal ${i>step?'pending':''}"><text x="5" y="${y+35}" font-size="20" fill="#9EACC8">${String(i+1).padStart(2,'0')}</text><line x1="60" y1="${y}" x2="60" y2="${y+85}" stroke="${c}" stroke-width="4"/>${txt(a,90,y+30,29,c,'start',42)}${txt(b,90,y+76,23,'#EFF4FF','start',60)}${arrows&&i<count-1?`<path d="M1010,${y+45} v${spacing-15}" stroke="#9EACC8" fill="none" marker-end="url(#arrow)"/>`:''}</g>`;}).join('')+txt(note,530,720,18,'#9EACC8','middle',70)+'</svg>';}
function diagram(slide,step){
 const state=stateGraph(slide,step);if(state)return state;
 if(slide.id==='S05')return rows([['stable','안정 지침 / Tool Schema','memory'],['context','Project / User / 선택된 Skill','memory'],['volatile','최근 History / 검색 결과 / Tool Result','memory'],['Prompt Builder → Provider','논리 계층 · API 필드 순서 보장 아님','model']],step,{arrows:true,note:'arch-hermes / Prompt Builder 확대 · 모든 저장 정보를 매번 로딩하지 않음'});
 if(slide.id==='S07')return rows([['SQLite Session','대화 / 실행 기록 → 현재 Context','memory'],['FTS5 검색','단어·구문 검색 → 원문 회수','memory'],['MEMORY.md / USER.md','선별 사실 → Context 주입','memory'],['Skills','재사용 절차 · 검색 방식과 별도','memory']],step,{note:'arch-hermes / 저장 영역 확대 · FTS도 RAG의 검색 수단이 될 수 있음'});
 if(architectureFor[slide.id])return architecture('arch-'+architectureFor[slide.id],step);
 if(sequences[slide.id])return sequence(sequences[slide.id],step>=slide.buildSteps.length-1?3:step);
 if(slide.id==='S01')return rows([['완성형 Harness','Hermes · Claude Code','runtime'],['실행 Framework / SDK','PydanticAI · OpenAI · ADK · Microsoft','tool'],['SDK → CLI','Claude Agent SDK → Claude Code Runtime','runtime'],['공통 의존 영역','Model / Provider / Environment','model']],step,{note:'상호 배타적 분류가 아님 · 성숙도 / 성능 축 아님'});
 const items=flows[slide.id]||[];const mappedStep=step>=slide.buildSteps.length-1?99:Math.round(step*(items.length-1)/Math.max(1,slide.buildSteps.length-1));
 return rows(items,mappedStep,{arrows:['S15','S20','S28','S34','S36','S38'].includes(slide.id),note:['S09','S20','S31','S33','S38'].includes(slide.id)?'INF · 도메인 / 참조 설계 예시':'실선: 실행 / 명시적 전송   점선: 설정 / 관찰 / 선택 연결'});
}

return {architecture,diagram};
})();
const __m3=(()=>{
const kinds=['model.request','model.response','tool.intent','tool.policy','tool.start','tool.result','context.next','state.commit','node.enter','output.validate','run.end','run.error'];
function validateTrace(t){
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
function redact(value){if(Array.isArray(value))return value.map(redact);if(value&&typeof value==='object')return Object.fromEntries(Object.entries(value).map(([k,v])=>[k,secretKeys.test(k)?'[REDACTED]':redact(v)]));if(typeof value==='string')return value.replace(/\bsk-[A-Za-z0-9_-]{12,}\b/g,'[REDACTED]').replace(/Bearer\s+[A-Za-z0-9_.-]+/gi,'Bearer [REDACTED]');return value;}
function illustrative(framework){const hermes=framework==='hermes';const items=hermes?[
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

return {kinds,validateTrace,redact,illustrative};
})();
const __m4=(()=>{
const escapeHtml=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function inline(s){return escapeHtml(s).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');}
function blocks(source){const result=[];const lines=source.replace(/\r/g,'').trim().split('\n');for(let i=0;i<lines.length;i++){const l=lines[i];if(!l.trim())continue;if(l.startsWith('```')){const code=[];while(++i<lines.length&&!lines[i].startsWith('```'))code.push(lines[i]);result.push({type:'code',text:code.join('\n')});}else if(l.startsWith('|')){const rows=[];do{if(!/^\|[-:\s|]+\|$/.test(lines[i]))rows.push(lines[i].split('|').slice(1,-1).map(s=>s.trim()));i++;}while(i<lines.length&&lines[i].startsWith('|'));i--;result.push({type:'table',headers:rows[0],rows:rows.slice(1)});}else{const p=[l];while(i+1<lines.length&&lines[i+1].trim()&&!/^(\||```)/.test(lines[i+1]))p.push(lines[++i]);result.push({type:'text',text:p.join('\n')});}}return result;}
function renderBlock(b){if(b.type==='code')return '<pre>'+escapeHtml(b.text)+'</pre>';if(b.type==='text')return '<p>'+inline(b.text).replace(/\n/g,'<br>')+'</p>';return '<table><thead><tr>'+b.headers.map(x=>'<th>'+inline(x)+'</th>').join('')+'</tr></thead><tbody>'+b.rows.map(row=>'<tr>'+row.map(x=>'<td>'+inline(x)+'</td>').join('')+'</tr>').join('')+'</tbody></table>';}

return {escapeHtml,inline,blocks,renderBlock};
})();
const __m0=(()=>{
const {architecture}=__m1;
const {illustrative,validateTrace,redact}=__m3;
const {escapeHtml:e}=__m4;
const params=new URLSearchParams(location.search),framework=params.get('demo')==='pydantic'?'pydantic':'hermes';
let trace=illustrative(framework),index=0,timer=null,reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
const $=s=>document.querySelector(s);const labels={illustrative:'설명용 고정 도식 · 실제 실행 기록 미연결',recorded:'실제 사전 기록 · 파일 메타데이터 기준',scripted:'Scripted Runtime 시험 · 실제 Provider 평가와 구분',live:'live 출처의 가져온 기록 · 현재 연결은 없음'};
const returnId=['S11','S21'].includes(params.get('return'))?params.get('return'):framework==='hermes'?'S11':'S21';const returnStep=Math.max(0,Math.min(3,Number(params.get('step'))||0));$('#back').href='index.html#'+returnId+'/'+returnStep;
$('#demo-title').textContent=framework==='hermes'?'Demo 1 · Hermes 요청과 실행의 연결':'Demo 2 · PydanticAI 코드와 Node 경계';
$('#question').textContent=framework==='hermes'?'모델 요청, 실행 의도, Handler 실행, 결과 기록 중 어느 사건까지 관찰했습니까?':'Node 전이·검증·승인·저장 중 SDK가 제공한 경계와 앱의 책임은 무엇입니까?';
$('#contract').textContent=framework==='hermes'?'[PSEUDO · 발표용 가상 도구]\nlookup_bin_rate → compare_measurements → predict_bin_rate\n요청: LOT-A / BIN-X / snapshot-v1 / SOP-r3\n필수 근거: 분모 / 기간 / Snapshot ID\n발행: 정확한 버전 / 대상 / 승인 / 멱등성':'[PSEUDO · 실제 실행 코드 아님]\nAgent 설정 / Tool Schema / Dependencies\nUserPromptNode → ModelRequestNode → CallToolsNode\nTool·Retry → 다음 요청 / 유효 Final → End\nDeferredToolRequests ↔ DeferredToolResults\n승인 UI / 내구 저장 / 업무 인가는 앱 계약';
function pause(){clearInterval(timer);timer=null;$('#play').textContent='자동 재생';}
function render(){const ev=trace.events[index];$('#mode').textContent=labels[trace.mode];$('#meta').textContent=`${trace.version} · 모델 ${trace.model} · Run ${trace.runId} · Session ${trace.sessionId}\n기록 시점 ${trace.recordedAt} · 관찰 지점: ${trace.observationPoint}`;$('#count').textContent=`${index+1} / ${trace.events.length}`;$('#architecture').innerHTML=architecture('arch-'+(framework==='hermes'?'hermes':'pydantic'),Math.min(3,index));$('#events').innerHTML=trace.events.map((ev,i)=>`<button class="${i===index?'active':''}" data-index="${i}">${i+1}. ${e(ev.label)}<span>${e(ev.kind)}</span></button>`).join('');$('#event-title').textContent=ev.label;$('#event-kind').textContent=`${ev.kind} · ${ev.id} · ${ev.timestamp} ${ev.toolCallId?'· '+ev.toolCallId:''}`;$('#payload-view').innerHTML='<option value="all">Payload 전체</option>'+Object.keys(ev.payload).map((k,i)=>`<option value="${i}">${e(k)}</option>`).join('');renderPayload();$('#prev').disabled=index===0;$('#next').disabled=index===trace.events.length-1;$('#motion').textContent=`동작 줄이기: ${reduced?'켬':'끔'}`;document.body.classList.toggle('reduced',reduced);}
function renderPayload(){const payload=trace.events[index].payload;const choice=$('#payload-view').value;const selected=choice==='all'?payload:payload[Object.keys(payload)[Number(choice)]];$('#payload').textContent=JSON.stringify(selected,null,2);}
$('#prev').onclick=()=>{pause();index=Math.max(0,index-1);render();};$('#next').onclick=()=>{pause();index=Math.min(trace.events.length-1,index+1);render();};$('#reset').onclick=()=>{pause();index=0;render();};$('#final').onclick=()=>{pause();index=trace.events.length-1;render();};$('#motion').onclick=()=>{reduced=!reduced;pause();render();};$('#play').onclick=()=>{if(timer){pause();return;}if(reduced){$('#error').textContent='동작 줄이기를 끄거나 수동으로 탐색하세요.';return;}timer=setInterval(()=>{if(index===trace.events.length-1){pause();return;}index++;render();},2200);$('#play').textContent='Pause';};$('#payload-view').onchange=renderPayload;
$('#events').onclick=ev=>{const b=ev.target.closest('button');if(b){pause();index=Number(b.dataset.index);render();}};
$('#illustrative').onclick=()=>{pause();trace=illustrative(framework);index=0;$('#error').textContent='';render();};
$('#trace-file').onchange=async ev=>{pause();try{const file=ev.target.files[0];if(!file)return;if(file.size>5*1024*1024)throw Error('Trace는 5MB 이하 JSON 파일이어야 합니다.');const parsed=validateTrace(JSON.parse(await file.text()));if(parsed.framework!==framework)throw Error('현재 데모와 framework가 다릅니다.');trace=redact(parsed);index=0;$('#error').textContent='가져오기 완료. 파일의 실행 여부·출처 진위는 별도 확인이 필요합니다.';render();}catch(err){$('#error').textContent=err.message;}ev.target.value='';};
document.addEventListener('keydown',ev=>{if(ev.target.closest('input,select,textarea,[contenteditable=true]'))return;if([' ','ArrowRight','ArrowLeft','r','R'].includes(ev.key)){ev.preventDefault();if(ev.key==='ArrowLeft')$('#prev').click();else if(ev.key.toLowerCase()==='r')$('#reset').click();else $('#next').click();}});render();

return {};
})();