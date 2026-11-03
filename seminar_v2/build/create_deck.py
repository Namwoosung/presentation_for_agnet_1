from pathlib import Path
from html import escape
import json

ROOT=Path(__file__).resolve().parents[1]
BG='#0B1020'; FG='#EFF4FF'; MUT='#9EACC8'; LINE='#33415D'; BLUE='#60A5FA'; PURPLE='#B794F4'; GREEN='#34D399'; ORANGE='#FDBA74'; RED='#FB7185'
def text(x,y,s,size=26,color=FG,weight=400,anchor='start',mono=False):
    family='Consolas, monospace' if mono else 'Malgun Gothic, Segoe UI, sans-serif'
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" font-family="{family}">{escape(s)}</text>'
def rect(x,y,w,h,color=LINE,fill='#10182B',dash=False):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{color}" stroke-width="2"'+(' stroke-dasharray="9 8"' if dash else '')+'/>'
def line(x1,y1,x2,y2,color=LINE,dash=False):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2"'+(' stroke-dasharray="7 7"' if dash else '')+'/>'
def arrow(x1,y1,x2,y2,label='',color=MUT,dy=-13):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2.5" marker-end="url(#arr)"/>'+ (text((x1+x2)/2+(20 if x1==x2 else 0),(y1+y2)/2+dy,label,20,color,anchor=('start' if x1==x2 else 'middle')) if label else '')
def node(x,y,w,h,title,sub='',color=PURPLE,id=''):
    return f'<g id="{id}">'+rect(x,y,w,h,color)+text(x+24,y+44,title,28,color,600)+(text(x+24,y+79,sub,21,MUT) if sub else '')+'</g>'
def group(k,s):return f'<g data-build="{k}">{s}</g>'
def takeaway(a,b=''):
    return line(134,884,1786,884)+text(134,934,a,29,FG,600)+text(134,972,b,21,MUT)
slides=[]
def slide(id,section,title,sub,body,steps,sources):
    n=len(slides)+1
    header=text(134,86,'AGENT FRAMEWORK  /  SEMINAR II',19,MUT,600)+text(1786,86,f'{n:02d} / 05',20,MUT,anchor='end',mono=True)
    header+=text(134,166,title,50,FG,700)+text(134,219,sub,25,MUT)
    footer=line(134,1002,1786,1002)+text(134,1040,f'{section}   /   {id}',18,MUT)+text(620,1040,sources,16,MUT)+f'<text class="build-counter" x="1786" y="1040" text-anchor="end" fill="{MUT}" font-size="18"></text>'
    defs='<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0 L8 4 L0 8" fill="#9EACC8"/></marker></defs>'
    body=body.replace('#arr)', '#arr-'+id+')')
    defs=defs.replace('id="arr"', 'id="arr-'+id+'"')
    slides.append({'id':id,'steps':steps,'section':section,'sources':sources,'html':f'<section class="slide" data-id="{id}" data-steps="{steps}"><svg viewBox="0 0 1920 1080" role="img" aria-label="{escape(title)}">{defs}{header}{body}{footer}</svg></section>'})

# 01 / Architecture: stable semantic node IDs and actor boundaries.
b=text(134,290,'ENTRY POINTS',18,MUT,600)+text(650,290,'RUNTIME-OWNED',18,PURPLE,600)+text(1470,290,'PROVIDER / EXTERNAL',18,BLUE,600)
b+=group(0,node(134,365,300,100,'CLI / Gateway','사용자 요청',MUT,'H-ENTRY')+node(134,510,300,100,'ACP / Cron','프로토콜 진입 / 새 실행',MUT,'H-CRON'))
b+=group(1,rect(610,330,720,300,PURPLE, '#11192D')+text(650,386,'AIAgent',43,PURPLE,600)+text(650,430,'conversation loop',26,MUT)+node(650,477,280,105,'Provider resolver','요청 형식과 연결 선택',BLUE,'H-PROVIDER')+node(960,477,330,105,'Tool dispatch','등록된 handler 호출',GREEN,'H-TOOLS')+arrow(434,415,610,415,'request')+arrow(434,560,610,560,'new run'))
b+=group(2,node(1470,330,316,105,'LLM endpoint','추론 / Tool Call 요청',BLUE,'H-MODEL')+arrow(1330,378,1470,378,'request',BLUE)+arrow(1470,419,1330,419,'response',BLUE,26))
b+=group(3,node(1470,525,316,105,'Tool backends','내장 Tool / MCP / Plugin',GREEN,'H-BACKEND')+arrow(1330,556,1470,556,'dispatch',GREEN)+arrow(1470,602,1330,602,'return',GREEN,27)+text(1470,678,'실행 환경의 OS / DB 권한',21,RED))
b+=group(4,node(134,729,390,105,'Prompt builder','지침 / 컨텍스트 / Skills',ORANGE,'H-PROMPT')+node(650,729,395,105,'Session & Memory','SQLite / FTS5 / memory files',ORANGE,'H-STATE')+node(1150,729,315,105,'Policy / Approval','적용 조건은 Tool별 확인',RED,'H-POLICY')+arrow(524,776,610,630,'input',ORANGE)+arrow(848,630,848,729,'history',ORANGE)+arrow(1255,729,1255,630,'check',RED))
b+=takeaway('모델 호출, Tool 실행, 상태 관리를 AIAgent가 연결한다','선택적 child Agent는 별도 Loop를 실행하며, 결과를 부모에게 반환한다.')
slide('F006','HERMES','Hermes는 실행 환경을 연결하는 Harness다','하나의 요청을 중심으로 읽는 전체 구조',b,5,'H-ARCH / H-LOOP  ·  DOC_CONFIRMED')

# 02 / Sequence: time moves downward; actors remain fixed.
b=''
for x,t,c in [(430,'MODEL',BLUE),(940,'RUNTIME / HARNESS',PURPLE),(1500,'TOOL HANDLER',GREEN)]:
    b+=text(x,305,t,24,c,600,'middle')+line(x,334,x,837,LINE,True)
b+=group(0,arrow(940,380,430,380,'01   messages + Tool Schema',BLUE)+text(134,385,'요청 구성',22,MUT))
b+=group(1,arrow(430,480,940,480,'02   tool_calls',BLUE)+text(134,485,'모델의 제안',22,MUT)+text(465,523,'get_bin_summary(lot="BIN-X")',21,BLUE,mono=True))
b+=group(2,rect(860,555,220,75,RED,'#201B2B',True)+text(970,601,'정책 / 인자 검사',23,RED,600,'middle')+arrow(1080,590,1500,590,'03   dispatch',GREEN)+text(1530,596,'조회 실행',22,GREEN))
b+=group(3,arrow(1500,705,940,705,'04   ToolResult',GREEN)+text(965,751,'History에 결과 추가',22,ORANGE))
b+=group(4,arrow(940,811,430,811,'05   다음 model request',BLUE))
b+=takeaway('Tool Call은 요청이고, 실제 실행은 Runtime과 handler가 맡는다','BIN-X 호출은 설명용 예시다. 실제 실행 기록이나 승인 완료를 나타내지 않는다.')
slide('F009','HERMES','모델은 Tool 실행을 요청한다','요청에서 실행까지의 경계를 시간 순서로 보기',b,5,'H-LOOP  ·  DOC_CONFIRMED / 예시')

# 03 / Code and data boundary: dependency objects vs explicit model payload.
b=text(134,300,'PYTHON RUNTIME',22,PURPLE,600)+text(1110,300,'MODEL INPUT',22,BLUE,600)+line(1000,285,1000,838,RED,True)
b+=group(0,rect(134,330,775,205,LINE)+text(164,373,'RunContext.deps',29,PURPLE,600,mono=True)+text(164,426,'db_handle     principal     evaluator',25,ORANGE,mono=True)+text(164,490,'실행 자원은 Python 객체로 유지',25,MUT))
b+=group(1,text(150,594,'# 설명용 의사코드',20,MUT,mono=True)+text(150,640,'rows = ctx.deps.db.query(lot)',25,GREEN,mono=True)+text(150,685,'return select_allowed(rows)',25,GREEN,mono=True)+text(150,748,'인가와 반환 범위는 애플리케이션이 구현',23,MUT))
b+=group(2,node(1110,330,676,205,'Provider request','instructions / history / tool schemas',BLUE)+text(1134,471,'Tool 결과 중 선택한 데이터',26,GREEN)+arrow(815,675,1110,675,'ToolResult',GREEN)+text(1140,720,'BIN-X 요약 데이터',26,FG)+text(1140,758,'객체 참조와 인증정보 자체는 포함하지 않음',22,MUT))
b+=group(3,text(978,805,'×',40,RED,600,'middle')+text(1110,812,'Deps 전체의 자동 직렬화 경로 없음',23,RED))
b+=takeaway('Deps에 전달한 객체가 자동으로 모델 메시지가 되지는 않는다','단, 지침이나 Tool 반환값에 민감정보를 넣으면 모델 입력에 포함될 수 있다.')
slide('F049','PYDANTIC AI','Deps와 모델 입력은 서로 다른 경계다','실행 자원과 모델에 전달하는 데이터를 분리하기',b,4,'P-DEPS  ·  DOC_CONFIRMED / 의사코드')

# 04 / Return topology: identical scale, distinct return ownership.
b=line(960,285,960,845)+text(134,302,'01',25,PURPLE,600,mono=True)+text(195,302,'AGENT AS TOOL',26,PURPLE,600)+text(1040,302,'02',25,GREEN,600,mono=True)+text(1100,302,'HANDOFF',26,GREEN,600)
b+=group(0,node(230,360,250,100,'Manager','대화 제어 유지',PURPLE)+node(1040,360,260,100,'Agent A','요청 분류',PURPLE))
b+=group(1,node(585,530,275,100,'Specialist','부분 작업 수행',GREEN)+arrow(480,412,720,530,'tool call',PURPLE)+arrow(585,585,355,460,'result',GREEN,-4)+node(1460,530,300,100,'Agent B','활성 Agent로 전환',GREEN)+arrow(1300,412,1590,530,'handoff',GREEN))
b+=group(2,arrow(355,460,355,755,'final answer',PURPLE)+text(355,798,'User',28,FG,600,'middle')+arrow(1610,630,1610,755,'final answer',GREEN)+text(1610,798,'User',28,FG,600,'middle')+text(560,746,'최종 답변',22,MUT)+text(560,784,'Manager',30,PURPLE,600)+text(1040,746,'최종 답변',22,MUT)+text(1040,784,'Specialist',30,GREEN,600))
b+=group(3,takeaway('결과를 돌려받을지, 대화의 담당자를 바꿀지가 선택 기준이다','BIN-X 데이터 조회는 부분 작업 위임으로, 이후 질의 담당 변경은 handoff로 설계할 수 있다.'))
slide('F066','OPENAI AGENTS SDK','위임 방식에 따라 최종 답변의 주체가 달라진다','Agent-as-Tool과 Handoff의 제어권 비교',b,4,'O-ORCH  ·  DOC_CONFIRMED / 설계 예시')

# 05 / Deployment matrix with shared central model, rather than duplicated model boxes.
b=text(134,301,'A   중앙 Agent',28,PURPLE,600)+text(970,301,'B   사용자 PC Agent',28,PURPLE,600)
b+=group(0,rect(134,333,740,340,LINE, '#0D1526',True)+text(162,370,'CENTRAL SERVICE',18,MUT,600)+node(168,406,275,105,'API / Auth','사용자 요청과 인증',MUT)+node(520,406,315,105,'Agent workers','Loop / Queue / Session',PURPLE)+arrow(443,458,520,458,'request',MUT)+node(520,552,315,90,'Tools / DB','중앙 실행 권한',GREEN)+arrow(677,511,677,552,'invoke',GREEN))
b+=group(1,rect(970,333,816,340,LINE,'#0D1526',True)+text(998,370,'USER PC',18,MUT,600)+node(1005,406,350,105,'Desktop Agent','로컬 Loop / Session',PURPLE)+node(1440,406,310,105,'Local tools','사용자 파일 / OS 권한',GREEN)+arrow(1355,458,1440,458,'invoke',GREEN)+text(1005,599,'관리 책임: 설치 / 업데이트 / 로컬 권한',25,MUT))
b+=group(2,node(610,744,700,107,'중앙 LLM Gateway / Model server','두 배치 모두 같은 모델 서버를 사용할 수 있다',BLUE)+arrow(350,673,610,787,'model request',BLUE)+arrow(1500,673,1310,787,'model request',BLUE))
b+=group(3,takeaway('Agent Runtime 위치와 LLM Server 위치는 독립적으로 결정한다','중앙형은 격리와 운영, 로컬형은 배포와 권한 관리가 핵심이다. 혼합형은 이 책임을 함께 설계한다.'))
slide('F091','DEPLOYMENT','중앙 LLM을 써도 Agent는 로컬에서 실행할 수 있다','모델 위치와 실행 위치를 분리하는 두 가지 배치',b,4,'BLUEPRINT F091  ·  DESIGN_OR_ILLUSTRATIVE')

base=Path('C:/Users/namws/.codex/skills/frontend-slides/viewport-base.css').read_text(encoding='utf-8')
css='''
:root{--stage-bg:#070B15;--slide-bg:#0B1020}*{box-sizing:border-box}
svg{width:1920px;height:1080px} [data-build]{opacity:0;transition:opacity .3s ease-out}
[data-build].shown{opacity:1}[data-build].past{opacity:.58}
.overview [data-build]{opacity:1!important}
@media(prefers-reduced-motion:reduce){[data-build]{transition:none!important}}
@media print{[data-build]{opacity:1!important}}
'''
js='''
const slides=[...document.querySelectorAll('.slide')], stage=document.querySelector('.deck-stage');
const params=new URLSearchParams(location.search);let index=Math.min(4,Math.max(0,Number(params.get('slide')||1)-1)), step=0,held=false,locked=false;
const overview=params.get('view')==='overview';if(overview)document.body.classList.add('overview');
function fit(){const s=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(${(innerWidth-1920*s)/2}px,${(innerHeight-1080*s)/2}px) scale(${s})`;}
function render(){slides.forEach((el,i)=>{el.classList.toggle('active',i===index);el.setAttribute('aria-hidden',i!==index);});const el=slides[index],n=+el.dataset.steps;el.querySelectorAll('[data-build]').forEach(g=>{const k=+g.dataset.build;g.classList.toggle('shown',k<=step);g.classList.toggle('past',k<step);});el.querySelector('.build-counter').textContent=`build ${overview?n:step+1}/${n}    SPACE${index===4&&step===n-1?'  END':''}`;window.deckState={slideId:el.dataset.id,slideIndex:index,stepIndex:step,stepCount:n,sourceRefs:meta[index].sources};}
addEventListener('resize',fit);addEventListener('keydown',e=>{if(e.code!=='Space')return;if(/INPUT|TEXTAREA|SELECT/.test(e.target.tagName)||e.target.isContentEditable)return;e.preventDefault();if(e.repeat||held||locked)return;held=true;locked=true;setTimeout(()=>locked=false,320);if(overview){if(index<4)index++;}else if(step<+slides[index].dataset.steps-1)step++;else if(index<4){index++;step=0;}render();});addEventListener('keyup',e=>{if(e.code==='Space')held=false;});addEventListener('blur',()=>held=false);fit();render();
'''
meta=[{k:v for k,v in s.items() if k!='html'} for s in slides]
html='<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Agent Framework Seminar II · V2</title><style>'+base+css+'</style><body><main class="deck-viewport"><div class="deck-stage">'+''.join(s['html'] for s in slides)+'</div></main><script>const meta='+json.dumps(meta,ensure_ascii=False)+';'+js+'</script></body></html>'
(ROOT/'index.html').write_text(html,encoding='utf-8')
(ROOT/'slide-map.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
print('Created five slides:',len(html),'bytes')

(ROOT/'preview.html').write_text(html.replace("const overview=params.get('view')==='overview'", "const overview=true"),encoding='utf-8')
