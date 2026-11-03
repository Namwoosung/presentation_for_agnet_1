from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
doc=(root/'agent_framework_seminar_ii_codex_revised_blueprint.md').read_text(encoding='utf-8')
chunks=re.split(r'^### (S\d{2}) · (.+?)\s*$',doc,flags=re.M)
slides=[]
for i in range(1,len(chunks),3):
    sid,title,body=chunks[i:i+3]
    if sid=='S60':body=body.split('## 5.')[0]
    def field(name):
        m=re.search(r'\*\*'+re.escape(name)+r':\*\*\s*(.*?)(?=\n\*\*|\Z)',body,re.S)
        return m[1].strip() if m else ''
    section=re.search(r'\*섹션: (.*?) /',body)[1]
    master=re.search(r'기준 도식: (.*?)\*',body)[1]
    sources=re.findall(r'`([^`]+)`',field('출처 키'))
    sources=[{'CC':'C','P':'P-AGENT'}.get(x,x) for x in sources]
    slides.append(dict(id=sid,title=title,section=section,master=master,screen=field('화면'),diagram=field('구조도'),builds=field('Space 전개').split(' → '),notes=field('발표자'),code=field('코드/발췌 원칙'),sources=sources))
assert len(slides)==60
assert [s['id'] for s in slides]==[f'S{i:02}' for i in range(1,61)]
for d in ['docs','slides','tests','evidence/screenshots','evidence/sources']: (root/d).mkdir(parents=True,exist_ok=True)
(root/'slide_map.json').write_text(json.dumps(slides,ensure_ascii=False,indent=2),encoding='utf-8')
(root/'docs/implementation-plan.md').write_text('''# 제작 범위\n\n60장 원고를 순서대로 구현합니다. 도식·본문·전개·발표자 설명·출처를 slide_map.json에 먼저 보존했습니다. CC와 P 출처 키는 C와 P-AGENT로 정규화했습니다.\n\n1. 원고 데이터화 및 60개 ID 검사\n2. 공식 문서 및 공개 소스 확인, claims.md 기록\n3. 밝은 16:9 HTML/SVG 도식과 7개 재사용 마스터 구현\n4. Space 진행 및 완성 화면 검토용 별도 HTML\n5. 전체 60장 렌더·시각 검수·다중 화면 크기 검수\n\n사용자 요청에 따라 데모, relay, fixture 실행기, 모델 API 호출은 제작하지 않습니다. S18/S19/S41/S42는 실행 전 확인 계획으로 보존합니다. 기존 seminar_v2와 archive는 변경하지 않습니다.\n''',encoding='utf-8')
print('PASS: 60 unique ordered slides mapped before implementation')
