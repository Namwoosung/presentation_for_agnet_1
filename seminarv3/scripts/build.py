from pathlib import Path
import sys,json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'slides'))
from diagrams import *
from content import render,TITLES,COPY
source=json.loads((ROOT/'slide_map.json').read_text(encoding='utf-8'))
base=(ROOT/'slides/viewport-base.css').read_text(encoding='utf-8')
theme=(ROOT/'slides/theme.css').read_text(encoding='utf-8')
controller=(ROOT/'slides/controller.js').read_text(encoding='utf-8')
pages=[];metadata=[];notes=['# 발표자 원고 — Agent Framework Seminar II','', '발표 범위: 60장. 실제 데모는 수행하지 않았으며 S18/S19/S41/S42는 확인 계획입니다.','']
aliases={'H-COMPACT':'H-LOOP','H-SECURITY':'H-TOOLS','H-GATEWAY':'H-ARCH'}
for i,s in enumerate(source,1):
 sid=s['id'];title=TITLES.get(i,s['title']);steps=len(s['builds'])
 if i==18:s['builds']=['합성 질문과 스냅샷','모델 요청·Tool Call 수집 계획','Tool 결과·반환 확인 계획','실행 전 상태와 다음 검증 안내']
 if i==19:s['builds']=['요청 증거','실제 handler 증거','History 갱신 증거','저장·오류 경계의 확인 계획']
 if i==41:s['builds']=['앱 Agent 정의','Python Tool 실행 확인 계획','최종 Output 검증 계획','실행 전 상태와 기록 계획']
 if i==42:s['builds']=['Core 처리의 증거','앱 함수·DB의 증거','검산·저장·예외 검증 계획']
 body=render(i,s)
 # Match the original semantic build count. Closely related sub-elements share a build.
 body=re.sub(r'data-build="(\d+)"',lambda m:f'data-build="{min(int(m[1]),steps-1)}"',body)
 if i in [18,19,41,42]:status='실행 전 · 검증 계획'
 elif i in [1,2,3,17,26,27,28,40,43,44,50,57,58,59,60]:status='개념 / 설계'
 elif i in [7,32,48]:status='문서 / 공개 소스 확인'
 elif i==31:status='API 예시 · 실행 미검증'
 else:status='공식 문서 기준'
 sourcekeys=[aliases.get(x,x) for x in s['sources']]
 if i==36:sourcekeys=['P-OUTPUT']
 if i==7:sourcekeys+=['H-SRC']
 if i==32:sourcekeys+=['P-SRC']
 if i==48:sourcekeys+=['S-SRC']
 if i in [23,24,25,33,37,47,53,56]:sourcekeys+= {23:['C-SKILL'],24:['C-HOOK','C-SANDBOX'],25:['C-TEAM'],33:['P-DEPS'],37:['P-ADV'],47:['O-HITL'],53:['G-EVENT','G-STATE'],56:['M-CHECKPOINT']}[i]
 sourcekeys=list(dict.fromkeys(sourcekeys))
 header=txt(134,80,'AGENT FRAMEWORK  /  SEMINAR II',18,'muted',600)+txt(1786,80,f'{i:02d} / 60',20,'muted',anchor='end',mono=True)
 titlelines=wrap(title,68)
 header+=txt(134,153,'\n'.join(titlelines),48,'ink',700)
 header+=txt(134,270,s['section'].upper(),20,'runtime',600)
 for j,(label_text,role) in enumerate([('MODEL','model'),('RUNTIME','runtime'),('TOOL','tool'),('STATE','state'),('APP-OWNED','muted')]):header+=txt(1070+j*143,270,label_text,17,role,600)
 screen=COPY.get(i,[t.strip().replace('`','') for t in s['screen'].split(' · ')])
 if len(screen)>3:screen=[' / '.join(screen[:2])]+screen[2:]
 assert len(screen)<=3,(sid,screen)
 band=rule(134,878,1786,878)
 for j,claim in enumerate(screen):
  x=134+j*565;k=min(j,steps-1)
  band+=g(k,txt(x,919,f'0{j+1}',18,'runtime',600,mono=True)+txt(x+45,919,claim,24,'ink',limit=37))
 footer=rule(134,1007,1786,1007)+txt(134,1043,sid+'  /  '+status,17,'muted')+txt(705,1043,' · '.join(sourcekeys),16,'muted')+'<text class="build-counter" x="1786" y="1043" text-anchor="end" fill="#526279" font-size="18"></text>'
 marker=f'<defs><marker id="arrow-{sid}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="#526279"/></marker></defs>'
 body=body.replace('#ARROW',f'#arrow-{sid}')
 pages.append(f'<section class="slide" data-id="{sid}" data-steps="{steps}"><svg viewBox="0 0 1920 1080" role="img" aria-label="{escape(title)}">{marker}{header}{body}{band}{footer}</svg></section>')
 metadata.append(dict(id=sid,title=title,section=s['section'],stepCount=steps,builds=s['builds'],sources=sourcekeys,status=status,screen=screen,master=s['master']))
 notes.extend([f'## {sid} — {title}','',s['notes'],'','### 화면 문구','']+['- '+t for t in screen]+['','### 단계별 전개','']+[f'{k+1}. {b}' for k,b in enumerate(s['builds'])]+['','### 원문 도식 요구','',s['diagram'],'','출처: '+', '.join(sourcekeys),''])
 if i in [18,19,41,42]:notes+=['이번 전달본은 실행 전 계획이다. Viewer 이동·캡처·event_id·실제 Trace는 제공하지 않는다.','']
 if i==31:notes+=['화면의 API 형태는 공개 문서와 대조했다. model과 read_synthetic_fixture는 앱이 주입하는 이름이며 독립 실행 파일이 아니다. 실제 모델 호출은 하지 않았다.','']
 if i==36:notes+=['현재 공식 Output 문서에서 graceful이 기본값이다. 화면 표는 유효한 Output Tool이 포함된 경우이며 plain text와 Native/Prompted output의 혼합 조건에는 그대로 일반화하지 않는다. Streaming은 첫 적합 출력을 확정하는 시점이 달라진다. 실제 설치 릴리스에서는 재검증한다.','']
 if i==39:notes+=['외부 승인을 기다리는 stop-the-world 흐름은 DeferredToolRequests로 run을 끝낸 뒤, message history와 DeferredToolResults를 후속 run에 전달한다. 현재 문서에는 같은 프로세스의 handler로 inline 해결하는 선택지도 있다.','']
 if i==8:notes+=['승인 거부가 항상 전체 run 중단을 뜻하지 않는다. Tool 실패 반환과 정책에 의한 강제 run 종료를 구분한다. 화면은 세 가지 가능한 처리 범주를 설명한다.','']
htmlhead='<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Agent Framework Seminar II</title><style>'+base+theme+'</style><body>'
htmlbody='<main class="deck-viewport"><div class="deck-stage">'+''.join(pages)+'</div></main>'
for filename,overview in [('index.html',False),('preview.html',True)]:
 html=htmlhead+htmlbody+'<script>const DECK_OVERVIEW='+str(overview).lower()+';const metadata='+json.dumps(metadata,ensure_ascii=False)+';\n'+controller+'</script></body></html>'
 (ROOT/filename).write_text(html,encoding='utf-8')
(ROOT/'slides/slide-data.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'docs/presenter-notes.md').write_text('\n'.join(notes),encoding='utf-8')
(ROOT/'evidence/build.json').write_text(json.dumps({'slides':60,'steps':sum(s['stepCount'] for s in metadata),'sha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest()},indent=2),encoding='utf-8')
print('Built',len(pages),'slides with',sum(s['stepCount'] for s in metadata),'semantic states')
