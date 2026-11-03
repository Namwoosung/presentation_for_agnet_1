import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const blueprint=fs.readFileSync(path.join(root,'..','agent_framework_seminar_2_slide_blueprint.md'),'utf8');
fs.mkdirSync(path.join(root,'dist','sources'),{recursive:true});
const sections=[...blueprint.matchAll(/^## ([SX]\d{2}) — (.+)\r?\n([\s\S]*?)(?=^## |^# |$(?![\s\S]))/gm)];
const field=(body,key)=>body.match(new RegExp('^- \\*\\*'+key+':\\*\\* (.+)$','m'))?.[1]||'';
const groupFor=id=>id.startsWith('X')?'부록':Number(id.slice(1))<3?'Opening':Number(id.slice(1))<12?'Hermes':Number(id.slice(1))<14?'Claude Code':Number(id.slice(1))<22?'PydanticAI':Number(id.slice(1))<25?'OpenAI Agents SDK':Number(id.slice(1))<27?'Claude Agent SDK':Number(id.slice(1))<29?'Google ADK':Number(id.slice(1))<32?'Microsoft Agent Framework':'개발·운영 판단';
const sources={};
for(const m of blueprint.matchAll(/^### G-([HPOGMCS])\. (.+)\r?\n([\s\S]*?)(?=^### |^# |$(?![\s\S]))/gm))sources[m[1]]={name:m[2],links:[...m[3].matchAll(/\[([^\]]+)\]\((https:\/\/[^)]+)\)/g)].map(x=>({label:x[1],url:x[2]}))};
const versions={Hermes:'v0.22.5','Claude Code':'CLI v2.1.314',PydanticAI:'Core v2.61.0','OpenAI Agents SDK':'Python v0.24.0','Claude Agent SDK':'Python v0.2.176 / CLI v2.1.316','Google ADK':'Python v2.13.0','Microsoft Agent Framework':'Python python-1.24.0'};
const slides=sections.map(([all,id,title,body])=>{
 const visual=field(body,'그림·단계');const screen=field(body,'화면');
 const links=[...new Set([...body.matchAll(/X\d{2}/g)].map(x=>x[0]).filter(x=>x!==id))];
 const digits=[...visual.matchAll(/[①②③④⑤⑥⑦⑧⑨⑩]([^①②③④⑤⑥⑦⑧⑨⑩]+)/g)].map(x=>x[1].trim().split(/\. /)[0]);
 return {id,section:groupFor(id),priority:['S08','S10','S26','S31','S34'].includes(id)?'확장':['S11','S21'].includes(id)?'연결':'핵심',title,onScreen:[...screen.matchAll(/`([^`]+)`/g)].map(x=>x[1]),visual,buildSteps:digits.length?digits:['전체 관계','주 경로','경계와 판단'],speakerNotes:field(body,'노트·연결'),sourceRefs:field(body,'근거')||body.match(/\*\*근거:\*\* (.+)/)?.[1]||(id==='X10'?'C §38 · 발표자 Q&A':id.startsWith('X')?'C 고정 분석 · 상세 부록':''),appendixLinks:links,body:id.startsWith('X')?body:'',version:versions[groupFor(id)]||'2026-10-31 분석 기준'};
});
const supplemental=blueprint.slice(blueprint.indexOf('# E.'),blueprint.indexOf('# F.'));
fs.writeFileSync(path.join(root,'dist','data.js'),'window.SEMINAR='+JSON.stringify({slides,sources,versions,supplemental,scope:'고정 버전 분석 · 실제 실행 기록 미연결'})+';\n');
fs.copyFileSync(path.join(root,'..','agent_framework_seminar_2_slide_blueprint.md'),path.join(root,'dist','sources','blueprint.md'));
const sourceRoot='C:/Users/namws/OneDrive/Desktop/study_for_agent_framework';
for(const [from,to] of [['Agent_Framework_7종_최종_종합_비교_분석.md','analysis.md'],['agent_framework_seminar_1_slide_blueprint.md','design.md']]){
 const src=path.join(sourceRoot,from); if(fs.existsSync(src))fs.copyFileSync(src,path.join(root,'dist','sources',to));
}
const traceability=blueprint.slice(blueprint.indexOf('# D.'),blueprint.indexOf('# E.'));
fs.writeFileSync(path.join(root,'dist','sources','traceability.md'),traceability);
console.log(`Built ${slides.filter(s=>s.id.startsWith('S')).length} slides + ${slides.filter(s=>s.id.startsWith('X')).length} appendices`);
// Dependency-free classic bundles also work under file:// without module CORS.
function bundle(entry){const ids=new Map(),chunks=[];function visit(file){if(ids.has(file))return ids.get(file);const id='__m'+ids.size;ids.set(file,id);let code=fs.readFileSync(path.join(root,'dist',file),'utf8');const exported=[...code.matchAll(/export\s+(?:const|function|class)\s+(\w+)/g)].map(x=>x[1]);code=code.replace(/import\s+\{([^}]+)\}\s+from\s+['"]\.\/([^'"]+)['"];?/g,(_,names,dependency)=>{const dep=visit(dependency);return 'const {'+names.replace(/\s+as\s+/g,':')+'}='+dep+';';});code=code.replace(/export\s+(?=(?:const|function|class)\s)/g,'');chunks.push(`const ${id}=(()=>{\n${code}\nreturn {${exported.join(',')}};\n})();`);return id;}visit(entry);return chunks.join('\n');}
for(const entry of ['app','demo'])fs.writeFileSync(path.join(root,'dist',entry+'.bundle.js'),bundle(entry+'.js'));
for(const file of ['index.html','demo.html']){const p=path.join(root,'dist',file);const html=fs.readFileSync(p,'utf8').replace(/<script type="module" src="(app|demo)\.js"><\/script>/g,'<script src="$1.bundle.js"></script>');fs.writeFileSync(p,html);}
let portable=fs.readFileSync(path.join(root,'dist','index.html'),'utf8');
portable=portable.replace('<link rel="stylesheet" href="tokens.css">','<style>'+fs.readFileSync(path.join(root,'dist','tokens.css'),'utf8')+'</style>');
for(const file of ['data.js','app.bundle.js'])portable=portable.replace(`<script src="${file}"></script>`,'<script>'+fs.readFileSync(path.join(root,'dist',file),'utf8').replace(/<\/script/gi,'<\\/script')+'</script>');
fs.writeFileSync(path.join(root,'dist','presentation.html'),portable);
