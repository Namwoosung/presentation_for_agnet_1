const {chromium}=require('C:/Users/namws/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..');const file=name=>'file:///'+path.join(root,name).replaceAll('\\','/');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage({viewport:{width:1920,height:1080},reducedMotion:'reduce'});
 const errors=[],bounds=[],overlap=[],nodeOverflow=[];page.on('pageerror',e=>errors.push(e.message));
 for(let i=1;i<=60;i++){
  await page.goto(file('preview.html')+'?slide='+i);await page.screenshot({path:path.join(root,'evidence/screenshots',`S${String(i).padStart(2,'0')}.png`)});
  const result=await page.locator('.slide.active').evaluate(el=>{
   const text=[...el.querySelectorAll('text')].map(e=>{let b=e.getBBox();return {text:e.textContent,x:b.x,y:b.y,w:b.width,h:b.height}});
   const out=text.filter(t=>t.x<120||t.x+t.w>1800||t.y<45||t.y+t.h>1060);
   const pairs=[];for(let a=0;a<text.length;a++)for(let b=a+1;b<text.length;b++){const x=text[a],y=text[b];let ix=Math.min(x.x+x.w,y.x+y.w)-Math.max(x.x,y.x),iy=Math.min(x.y+x.h,y.y+y.h)-Math.max(x.y,y.y);if(ix>8&&iy>8)pairs.push([x.text,y.text]);}
   const nodes=[];for(const n of el.querySelectorAll('.node')){const x=+n.dataset.x,y=+n.dataset.y,w=+n.dataset.w,h=+n.dataset.h;for(const t of n.querySelectorAll('text')){if(+t.getAttribute('y')<y)continue;const b=t.getBBox();if(b.x<x+8||b.x+b.width>x+w-8||b.y+b.height>y+h-6)nodes.push({node:n.dataset.node,text:t.textContent});}}
   return {out,pairs,nodes};
  });if(result.out.length)bounds.push({slide:i,items:result.out});if(result.pairs.length)overlap.push({slide:i,pairs:result.pairs});if(result.nodes.length)nodeOverflow.push({slide:i,items:result.nodes});
 }
 // All stage dimensions must remain visible and unscrolled at required sizes.
 const viewportResults=[];
 for(const [width,height] of [[1920,1080],[1366,768],[1280,720],[390,844]]){
  await page.setViewportSize({width,height});await page.goto(file('index.html'));
  const r=await page.evaluate(()=>{const b=document.querySelector('.deck-stage').getBoundingClientRect();return {sw:document.documentElement.scrollWidth,sh:document.documentElement.scrollHeight,x:b.x,y:b.y,right:b.right,bottom:b.bottom}});
  if(r.sw!==width||r.sh!==height||r.x<-.1||r.y<-.1||r.right>width+.1||r.bottom>height+.1)throw Error('Viewport failure '+JSON.stringify(r));
  const all=await page.locator('.slide').evaluateAll(els=>els.every(el=>{let b=el.getBoundingClientRect();return b.x>=-.1&&b.y>=-.1&&b.right<=innerWidth+.1&&b.bottom<=innerHeight+.1}));if(!all)throw Error('Some slides outside viewport');
  viewportResults.push({width,height,slidesChecked:60,pass:true});
 }
 await page.goto(file('index.html'));const meta=JSON.parse(fs.readFileSync(path.join(root,'slides/slide-data.json'),'utf8'));
 // Use browser fake clock to exercise the real keyboard controller without wall-clock waits.
 await page.clock.install();let visited=0;
 for(const m of meta){for(let step=0;step<m.stepCount;step++){
  const state=await page.evaluate(()=>window.deckState);if(state.slideId!==m.id||state.stepIndex!==step)throw Error('Progression '+JSON.stringify(state));
  await page.keyboard.press('Space');await page.clock.runFor(310);visited++;
 }}
 const last=await page.evaluate(()=>deckState);await page.keyboard.press('Space');await page.clock.runFor(310);if(JSON.stringify(await page.evaluate(()=>deckState))!==JSON.stringify(last))throw Error('End wrap');
 await page.goto(file('index.html'));await page.keyboard.down('Space');await page.clock.runFor(350);await page.keyboard.down('Space');await page.clock.runFor(350);if((await page.evaluate(()=>deckState.stepIndex))!==1)throw Error('Held repeat');await page.keyboard.up('Space');
 await page.keyboard.press('ArrowRight');await page.keyboard.press('Enter');if((await page.evaluate(()=>deckState.stepIndex))!==1)throw Error('Unexpected key advances');
 await page.keyboard.press('Space');await page.keyboard.press('Space');if((await page.evaluate(()=>deckState.stepIndex))!==2)throw Error('Transition double advance');
 if(errors.length)throw Error(errors.join('\n'));
 const masterMap={S04:['H-IN','H-CORE','H-PROV','H-LLM','H-TOOLS','H-STATE','H-POLICY'],S22:['C-IN','C-CORE','C-LLM','C-TOOLS','C-RULES','C-POLICY','C-DELEGATE'],S30:['P-APP','P-CORE','P-LLM','P-HANDLER','P-OUT','P-APPSTATE','P-HARNESS'],S45:['O-APP','O-RUNNER','O-LLM','O-FUNCTOOLS','O-HANDOFF','O-GUARD','O-STATE'],S48:['S-HOST','S-SDK','S-CLI','S-LLM','S-TOOL','S-MCP-HOST','S-POLICY','S-STATE'],S51:['G-CALLER','G-RUNNER','G-AGENT','G-LLM','G-TOOLS','G-EVENT','G-SESSION','G-WORKFLOW','G-MEMORY','G-ARTIFACT'],S54:['M-APP','M-AGENT','M-MODEL','M-TOOL','M-MIDDLE','M-WORKFLOW','M-HARNESS','M-CHECKPOINT']};
 for(const [id,ids] of Object.entries(masterMap)){const got=await page.locator(`.slide[data-id="${id}"] .node`).evaluateAll(els=>els.map(el=>el.dataset.node));if(!ids.every(id=>got.includes(id)))throw Error('Missing master node '+id);}
 const external=await page.locator('script[src],link[href],img[src],iframe').count();if(external)throw Error('External dependencies');
 fs.writeFileSync(path.join(root,'evidence/browser-report.json'),JSON.stringify({slideCount:60,visitedStates:visited,viewports:viewportResults,errors,bounds,overlap,nodeOverflow,masterNodes:'PASS',externalDependencies:0,keys:'PASS'},null,2));
 await browser.close();console.log(JSON.stringify({slides:60,states:visited,bounds:bounds.length,overlap:overlap.length,nodeOverflow:nodeOverflow.length,keys:'PASS'}));
})();
