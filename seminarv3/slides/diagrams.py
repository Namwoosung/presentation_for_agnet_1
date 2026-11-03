"""Editable SVG diagrams. Coordinates use the same 1920x1080 stage throughout."""
from html import escape
import unicodedata
COL={'model':'#1D63B7','runtime':'#7545AA','tool':'#147E61','state':'#B66813','risk':'#B6384B','ink':'#17243A','muted':'#526279','line':'#D9E2ED'}
FILL={'model':'#EDF4FC','runtime':'#F3EDF9','tool':'#ECF6F2','state':'#FCF3E7','risk':'#FCEEF0','ink':'#FFFFFF','muted':'#FFFFFF'}
def width(s):return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in s)
def wrap(s,limit):
 out=[]
 for paragraph in str(s).split('\n'):
  words=paragraph.split(' ');row=''
  for word in words:
   if row and width(row+' '+word)>limit:out.append(row);row=word
   else:row=(row+' '+word).strip()
  out.append(row)
 return out
def txt(x,y,s,size=24,role='ink',weight=400,anchor='start',limit=None,mono=False):
 rows=wrap(s,limit) if limit else str(s).split('\n')
 face='Consolas, monospace' if mono else "'Malgun Gothic','Segoe UI',sans-serif"
 return '<text class="label" x="%s" y="%s" fill="%s" font-family="%s" font-size="%s" font-weight="%s" text-anchor="%s">'%(x,y,COL.get(role,role),face,size,weight,anchor)+''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.42}">{escape(row)}</tspan>' for i,row in enumerate(rows))+'</text>'
def box(x,y,w,h,role='muted',dash=False,fill=None):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill or FILL.get(role,"#FFFFFF")}" stroke="{COL.get(role,role)}" stroke-width="1.8"'+(' stroke-dasharray="8 7"' if dash else '')+'/>'
def rule(x,y,x2,y2,role='line',dash=False):
 return f'<path d="M{x} {y} L{x2} {y2}" fill="none" stroke="{COL[role]}" stroke-width="1.7"'+(' stroke-dasharray="7 7"' if dash else '')+'/>'
def path(points,label='',role='muted',label_xy=None,dash=False):
 d='M'+' L'.join(f'{x} {y}' for x,y in points)
 s=f'<path d="{d}" fill="none" stroke="{COL[role]}" stroke-width="2.5" marker-end="url(#ARROW)"'+(' stroke-dasharray="8 6"' if dash else '')+'/>'
 if label:
  if label_xy is None:
   a,b=points[0],points[-1];label_xy=((a[0]+b[0])/2,(a[1]+b[1])/2-15)
  x,y=label_xy
  # A light halo keeps edge labels legible without UI-like boxes.
  s+='<g class="edge-label">'+txt(x,y,label,19,role,anchor='middle')+'</g>'
 return s
def node(x,y,w,h,title,sub='',role='runtime',sid='',tag=''):
 rows=wrap(title,max(12,int((w-42)/(25*.53))))
 s=box(x,y,w,h,role)+txt(x+22,y+37,'\n'.join(rows),25,role,600)
 if sub:s+=txt(x+22,y+h-22,sub,20,'muted',limit=int((w-44)/10.5))
 if tag:s+=txt(x+w-12,y-12,tag,17,role,anchor='end')
 return f'<g class="node" data-node="{sid or title}" data-x="{x}" data-y="{y}" data-w="{w}" data-h="{h}">{s}</g>'
def g(k,s):return f'<g class="build" data-build="{k}">{s}</g>'
def label(x,y,s,role='muted'):return txt(x,y,s,20,role,600)
def flow(items,edges=None,y=440,steps=None,x=134,total=1652,h=126):
 n=len(items);gap=66;w=(total-gap*(n-1))/n;s=''
 for i,item in enumerate(items):
  title,sub,role=item;at=x+i*(w+gap);k=steps[i] if steps else i
  chunk=node(at,y,w,h,title,sub,role)
  if i:chunk=path([(at-gap,y+h/2),(at,y+h/2)],(edges or ['요청']*(n-1))[i-1],role)+chunk
  s+=g(k,chunk)
 return s
def columns(headings,rows,roles=('runtime','tool'),steps=None):
 xs=[134,994];s=rule(960,310,960,820)
 for j,head in enumerate(headings):s+=label(xs[j],330,head,roles[j])
 for i,row in enumerate(rows):
  k=steps[i] if steps else i;y=375+i*143
  content=''
  for j,cell in enumerate(row):
   title,sub=cell
   content+=rule(xs[j],y+112,xs[j]+755,y+112)+txt(xs[j],y+30,title,29,roles[j],600,limit=47)+txt(xs[j],y+78,sub,23,'muted',limit=57)
  s+=g(k,content)
 return s
def stack(items,x=134,y=330,w=1100,steps=None):
 s=''
 for i,(title,sub,role) in enumerate(items):
  s+=g(steps[i] if steps else i,node(x,y+i*155,w,120,title,sub,role))
 return s
def codeblock(lines,label_text='개념 의사 코드 · 실행 코드 아님',x=134,y=330,w=1030,h=470,groups=None):
 s=box(x,y,w,h,'line',fill='#FFFFFF')+label(x+28,y+35,label_text,'muted')+rule(x+28,y+55,x+w-28,y+55)
 for i,line in enumerate(lines):
  k=groups[i] if groups else min(2,i//4)
  s+=g(k,txt(x+28,y+91+i*30,f'{i+1:02}',19,'muted',mono=True)+txt(x+80,y+91+i*30,line,21,'runtime' if line.lstrip().startswith(('if','while','class','async','@','from','return','for')) else 'ink',mono=True))
 return s

# Master coordinates are reused unchanged within every framework section.
MASTERS={
'H': [('H-IN','CLI / Gateway / Cron','입력과 새 실행','muted'),('H-CORE','AIAgent Loop','모델 응답을 해석하고 실행','runtime'),('H-LLM','Model','Tool Call 요청 반환','model'),('H-TOOLS','Tools / MCP / Plugin','handler와 외부 서버 실행','tool'),('H-STATE','Session / Memory / Skill','대화 / 사실 / 절차','state'),('H-POLICY','Approval / OS 권한','실행 경계별 정책','risk'),('H-PROV','Provider adapter','API 형식과 연결','model')],
'C': [('C-IN','CLI / IDE / Desktop','개발 작업 진입','muted'),('C-CORE','Claude Code runtime','탐색 / 수정 / 테스트 Loop','runtime'),('C-LLM','Claude model','계획과 Tool Call 요청','model'),('C-TOOLS','Read / Edit / Bash / MCP','파일과 프로세스 실행','tool'),('C-RULES','CLAUDE.md / Skill / Memory','지속 지시와 작업 맥락','state'),('C-POLICY','Permissions / Hooks / Sandbox','서로 다른 통제 지점','risk'),('C-DELEGATE','Subagents / Teams','별도 문맥과 협업','runtime')],
'P': [('P-APP','Agent / Tool / Deps 정의','개발자가 작성','muted'),('P-CORE','PydanticAI Core','내부 Graph / Tool / Retry','runtime'),('P-LLM','Provider / Model','추론과 구조화된 응답','model'),('P-HANDLER','Python Tool handler','앱의 DB 조회와 계산','tool'),('P-OUT','Output validation','형식과 타입 확인','runtime'),('P-APPSTATE','API / DB / 영속화 / 권한','애플리케이션 운영 책임','state'),('P-HARNESS','선택 Harness / Capabilities','Core와 별도 기능 계층','runtime')],
'O': [('O-APP','Application','Agent 선언 / 서비스','muted'),('O-RUNNER','Runner','다음 실행 단계 결정','runtime'),('O-LLM','Provider / Model','Tool / Handoff / Output','model'),('O-FUNCTOOLS','Function tools / MCP','앱 함수와 외부 실행','tool'),('O-STATE','Session / RunState','대화와 중단 상태','state'),('O-GUARD','Guardrails / Approval','적용 범위별 검사','risk'),('O-HANDOFF','Specialist Agent','활성 Agent 변경','runtime')],
'S': [('S-HOST','Host application','업무 요청 / 결과 처리','muted'),('S-CLI','Claude Code runtime','Agent Loop 실행','runtime'),('S-LLM','Model provider','설정된 인증 경로','model'),('S-TOOL','Built-in tools','런타임 측 도구 실행','tool'),('S-STATE','Session','대화와 실행 문맥','state'),('S-POLICY','Permission / Hook','정책과 이벤트 처리','risk'),('S-SDK','Python / TypeScript SDK','호스트와 런타임 연결','runtime'),('S-MCP-HOST','Host MCP callback','호스트 함수 실행','tool')],
'G': [('G-CALLER','Caller / Application','사용자 입력 / 서비스','muted'),('G-RUNNER','Runner + Agent / Flow','실행과 세션 연결','runtime'),('G-LLM','Model','응답과 Tool 요청','model'),('G-TOOLS','Tool execution','외부 데이터와 함수','tool'),('G-SESSION','SessionService','대화 / state 저장','state'),('G-EVENT','Event','출력과 state delta 전달','state'),('G-AGENT','Agent / Workflow','Sequential / Parallel 등','runtime'),('G-MEMORY','Memory / Artifact','각기 다른 저장 목적','state')],
'M': [('M-APP','Application','Agent와 서비스 조립','muted'),('M-AGENT','Agent execution','모델과 Tool 반복','runtime'),('M-MODEL','Model provider','추론과 Tool 요청','model'),('M-TOOL','Function tools','업무 코드 실행','tool'),('M-CHECKPOINT','Workflow checkpoint','실행 복구 지점','state'),('M-MIDDLE','Middleware','공통 처리 / 정책','risk'),('M-WORKFLOW','Executor workflow','분기 / 합류 / superstep','runtime'),('M-HARNESS','선택 Harness','별도 기능 계층','runtime')]
}
def master(kind,steps=3,highlight=None):
 items=MASTERS[kind];s='';coords=[(134,345,360,110),(705,345,420,110),(1426,345,360,110),(1426,550,360,110),(705,710,420,110),(134,710,450,110),(705,540,420,110),(134,535,450,110)]
 # Shared paths are drawn before nodes to keep attachment points clean.
 s+=g(0,path([(494,400),(705,400)],'요청','runtime'))
 if kind=='H':
  s+=g(1,path([(915,455),(915,540)],'API 변환','model',label_xy=(988,504))+path([(1125,585),(1210,585),(1210,378),(1426,378)],'model request','model',label_xy=(1260,360))+path([(1426,428),(1125,428)],'response','model',label_xy=(1276,455)))
 else:
  s+=g(1,path([(1125,378),(1426,378)],'model request','model')+path([(1426,428),(1125,428)],'response','model',label_xy=(1276,455)))
 s+=g(min(2,steps-1),path([(1125,445),(1280,445),(1280,605),(1426,605)],'실행','tool',label_xy=(1330,530))+path([(1426,640),(1200,640),(1200,480),(1100,480),(1100,455)],'ToolResult','tool',label_xy=(1325,675)))
 if kind!='H':s+=g(min(2,steps-1),path([(915,455),(915,540)],{'C':'위임','P':'선택 확장','O':'handoff','G':'실행','M':'조립','S':'연결'}.get(kind,'연결'),'runtime',label_xy=(992,503),dash=kind in ['P','M']))
 if kind=='M':s+=g(2,path([(915,650),(915,710)],'checkpoint','state',label_xy=(995,674)))
 elif kind=='C':s+=g(2,path([(705,765),(680,765),(680,455),(705,455)],'지침 / 로드','state',label_xy=(600,687)))
 else:s+=g(min(2,steps-1),path([(705,455),(680,455),(680,765),(705,765)],'Output 검증' if kind=='P' else '기록 / 상태','state',label_xy=(590,665)))
 s+=g(min(2,steps-1),path([(584,765),(630,765),(630,445),(705,445)],'Event' if kind=='G' else '정책 / 앱 책임','state' if kind=='G' else 'risk',label_xy=(560,505),dash=True))
 for i,item in enumerate(items):
  sid,title,sub,role=item;x,y,w,h=coords[i];k=0 if i<2 else 1 if i==2 else min(2,steps-1)
  if kind=='H' and sid=='H-PROV':sub='모델 요청 전 형식 변환'
  n=node(x,y,w,h,title,sub,role,sid,('APP-OWNED' if i==0 else 'MODEL' if i==2 else 'TOOL' if i==3 else 'STATE' if role=='state' else ''))
  if highlight and sid not in highlight:n=f'<g opacity=".5">{n}</g>'
  s+=g(k,n)
 if steps>3:s+=g(3,txt(134,625,'설정·확장·운영의 접점',23,'runtime',600))
 return s

def sdk_master(steps=3):
 """Host SDK transport and CLI subprocess are explicitly separate actors."""
 b=g(0,node(134,330,350,110,'Host application','업무 요청과 결과 처리','muted','S-HOST')+node(705,330,420,110,'SDK transport','Python / TypeScript','runtime','S-SDK')+path([(484,385),(705,385)],'query / stream','runtime'))
 b+=g(1,node(1426,330,360,110,'Claude Code runtime','Agent Loop 실행','runtime','S-CLI')+path([(1125,385),(1426,385)],'프로세스 연결','runtime'))
 b+=g(1,node(1426,550,360,110,'Model provider','설정된 인증 경로','model','S-LLM')+path([(1606,440),(1606,550)],'model request','model',label_xy=(1690,503)))
 b+=g(2,node(705,550,420,110,'Built-in tools','런타임 측 실행','tool','S-TOOL')+path([(1490,440),(1490,490),(915,490),(915,550)],'dispatch','tool',label_xy=(1190,478))+node(134,550,450,110,'Host MCP callback','호스트 함수 실행','tool','S-MCP-HOST')+path([(705,420),(620,420),(620,605),(584,605)],'MCP 요청 / 반환','tool',label_xy=(410,500)))
 b+=g(2,node(134,715,720,105,'Permission / Hook','종류별 실행 정책과 이벤트','risk','S-POLICY')+node(1070,715,716,105,'Session','대화와 실행 맥락','state','S-STATE'))
 return b

def adk_master():
 b=g(0,node(134,340,300,110,'Caller','사용자 / 앱 요청','muted','G-CALLER')+node(565,340,340,110,'Runner','실행과 세션 연결','runtime','G-RUNNER')+path([(434,395),(565,395)],'요청','runtime'))
 b+=g(1,node(1036,340,300,110,'Agent / Flow','모델·Tool 단계','runtime','G-AGENT')+node(1466,340,320,110,'Model','추론과 Tool 요청','model','G-LLM')+path([(905,395),(1036,395)],'실행','runtime')+path([(1336,395),(1466,395)],'model API','model'))
 b+=g(1,node(1466,545,320,110,'Tools','함수 / 외부 실행','tool','G-TOOLS')+path([(1186,450),(1186,495),(1626,495),(1626,545)],'dispatch','tool',label_xy=(1420,481))+node(134,545,300,110,'Workflow','선택 실행 조합','runtime','G-WORKFLOW')+path([(565,430),(490,430),(490,600),(434,600)],'선택','runtime',label_xy=(485,520),dash=True))
 b+=g(2,node(1036,545,300,110,'Event','출력 / state delta','state','G-EVENT')+node(565,545,340,110,'SessionService','대화와 state 저장','state','G-SESSION')+path([(1466,600),(1336,600)],'이벤트','state')+path([(1036,600),(905,600)],'저장','state')+node(565,735,520,105,'Memory','선택: 실행 간 정보 활용','state','G-MEMORY')+node(1200,735,586,105,'Artifact','선택: 파일 등 산출물 저장','tool','G-ARTIFACT'))
 return b

def sequence(lanes,events):
 xs=[430,950,1500];s=''
 for i,(name,role) in enumerate(lanes):s+=label(xs[i]-120,322,name,role)+rule(xs[i],349,xs[i],807,'line',True)
 for k,(a,b,label_text,role,extra) in enumerate(events):
  y=390+k*91
  if a==b:chunk=box(xs[a]-155,y-20,310,60,role)+txt(xs[a],y+18,label_text,22,role,600,'middle')
  else:chunk=path([(xs[a],y),(xs[b],y)],label_text,role)
  if extra:chunk+=txt(134,y+8,extra,20,'muted')
  s+=g(k,chunk)
 return s
def fork(title_a='Tool A',title_b='Tool B',child=False,y=340,k=0,workflow=False):
 a='Child loop A' if child else title_a;b='Child loop B' if child else title_b
 s=node(134,y+55,330,100,'Workflow start' if workflow else 'Parent Loop','입력 메시지' if workflow else '요청과 결과를 소유','runtime')
 desc='해당 단계의 처리' if workflow else '독립 Context' if child else '독립적인 읽기'
 s+=node(735,y,380,95,a,desc,'runtime' if child else 'tool')+node(735,y+145,380,95,b,desc,'runtime' if child else 'tool')
 s+=node(1436,y+55,350,100,'Join / Executor C' if workflow else 'Parent 복귀','다음 superstep 실행' if workflow else 'summary' if child else 'ToolResult 수집','runtime')
 for yy in [y+48,y+193]:s+=path([(464,y+105),(620,y+105),(620,yy),(735,yy)],'위임' if child else '실행','runtime',label_xy=(614,yy-13))+path([(1115,yy),(1290,yy),(1290,y+105),(1436,y+105)],'반환','tool',label_xy=(1280,yy-13))
 return g(k,s)
def checklist(items,roles=None):
 s=''
 for i,(title,sub) in enumerate(items):
  y=340+i*155;role=(roles or ['runtime','tool','state'])[i%3]
  s+=g(i,txt(134,y+30,f'0{i+1}',44,role,600,mono=True)+txt(240,y+25,title,31,role,600)+txt(240,y+73,sub,25,'muted',limit=105)+rule(240,y+108,1786,y+108))
 return s
