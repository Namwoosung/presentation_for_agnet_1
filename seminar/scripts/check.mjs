import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {nextPosition,parsePosition,mainIds,shortened} from '../dist/navigation.js';
import {architectures} from '../dist/architectures.js';
import {diagram} from '../dist/diagrams.js';
import {illustrative,validateTrace,redact} from '../dist/trace.js';
import {blocks} from '../dist/markdown.js';
import {appendixTabs} from '../dist/appendix.js';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const sandbox={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'dist/data.js'),'utf8'),sandbox);
const {slides,sources}=sandbox.window.SEMINAR;
assert.equal(slides.length,51);assert.equal(new Set(slides.map(x=>x.id)).size,51);
assert.equal(slides.filter(x=>x.id.startsWith('S')).length,41);assert.equal(slides.filter(x=>x.id.startsWith('X')).length,10);
for(const s of slides){assert(s.title);assert(s.buildSteps.length);if(s.id.startsWith('S')){assert(s.onScreen.length>=3,`${s.id}: copy`);assert(s.sourceRefs);assert(s.speakerNotes);if(s.id!=='S00')assert(diagram(s,99).includes('<svg'),s.id);}for(const id of s.appendixLinks)assert(slides.some(x=>x.id===id));}
for(const a of Object.values(architectures)){const ids=new Set(a.nodes.map(x=>x.id));assert.equal(ids.size,a.nodes.length);for(const [from,to] of a.edges){assert(ids.has(from));assert(ids.has(to));}}
let position={slideId:'S00',buildStep:0};let steps=0;while(position.slideId!=='S40'||position.buildStep!==slides[40].buildSteps.length-1){const next=nextPosition(position,slides);assert.notDeepEqual(next,position);position=next;if(++steps>300)throw Error('Navigation did not converge');}
let reverse=0;while(position.slideId!=='S00'||position.buildStep!==0){position=nextPosition(position,slides,-1);if(++reverse>300)throw Error('Reverse did not converge');}assert.equal(steps,reverse);
assert.equal(parsePosition('#S99/999',slides).slideId,'S00');assert.equal(parsePosition('#S03/999',slides).buildStep,3);assert.equal(shortened.length,36);
for(const f of ['hermes','pydantic'])validateTrace(illustrative(f));
assert.equal(redact({Authorization:'Bearer super-secret',nested:{api_key:'secret'}}).nested.api_key,'[REDACTED]');
assert.throws(()=>validateTrace({...illustrative('hermes'),mode:'recorded',redacted:false}));
const broken=illustrative('hermes');broken.events[1].id=broken.events[0].id;assert.throws(()=>validateTrace(broken));
const x07=slides.find(x=>x.id==='X07');assert.equal(blocks(x07.body).filter(x=>x.type==='table')[0].rows.length,24);
assert.equal(blocks(slides.find(x=>x.id==='X10').body).filter(x=>x.type==='table')[0].rows.length,30);
assert.equal(Object.keys(sources).length,7);
for(const s of slides.filter(s=>s.id.startsWith('X')))for(const tab of appendixTabs(s)){assert(tab.title);assert(tab.block,s.id);}
assert.equal(nextPosition({slideId:'S08',buildStep:slides[8].buildSteps.length-1},slides,1,shortened).slideId,'S09');
assert.equal(nextPosition({slideId:'S08',buildStep:0},slides,-1,shortened).slideId,'S07');
const portable=fs.readFileSync(path.join(root,'dist/presentation.html'),'utf8');assert(!portable.includes('type="module"'));assert(!/<script[^>]+src=/.test(portable));assert(portable.includes('window.SEMINAR='));
for(const file of ['index.html','demo.html','app.js','architectures.js','navigation.js','tokens.css','trace.js','sources/analysis.md','sources/blueprint.md','sources/design.md'])assert(fs.existsSync(path.join(root,'dist',file)),file);
console.log(JSON.stringify({status:'passed',slides:41,appendices:10,architectures:7,forwardTransitions:steps,reverseTransitions:reverse,failureQuestions:24,qaQuestions:30,limits:'Browser layout and actual framework execution require separate verification'},null,2));
