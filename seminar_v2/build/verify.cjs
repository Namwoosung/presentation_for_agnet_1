const {chromium}=require('C:/Users/namws/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const path=require('path');const fs=require('fs');
(async()=>{
 const root=path.resolve(__dirname,'..');const url='file:///'+path.join(root,'index.html').replaceAll('\\','/');
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage({viewport:{width:1920,height:1080}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
 for(let i=1;i<=5;i++){
  await page.goto(url+'?view=overview&slide='+i);await page.screenshot({path:path.join(root,'previews',`slide-${i}.png`)});
  const outside=await page.locator('.slide.active svg text').evaluateAll(els=>els.filter(el=>{let b=el.getBBox();return b.x<0||b.x+b.width>1920||b.y<0||b.y+b.height>1080}).map(el=>el.textContent));
  if(outside.length)throw Error('Outside stage '+outside);
 }
 await page.goto(url);let states=[];
 for(let n=0;n<23;n++) {states.push(await page.evaluate(()=>deckState));await page.keyboard.press('Space');await page.waitForTimeout(340);}
 if(states[0].slideId!=='F006'||states[21].slideId!=='F091'||states[22].stepIndex!==3)throw Error('state progression failed');
 await page.goto(url);await page.keyboard.down('Space');await page.waitForTimeout(350);await page.keyboard.down('Space');await page.waitForTimeout(350);if((await page.evaluate(()=>deckState.stepIndex))!==1)throw Error('repeat');await page.keyboard.up('Space');
 for(const [width,height] of [[1366,768],[1280,720],[390,844]]){await page.setViewportSize({width,height});await page.goto(url+'?view=overview&slide=3');const dims=await page.evaluate(()=>({w:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight}));if(dims.w!==width||dims.h!==height)throw Error('scroll');}
 if(errors.length)throw Error(errors.join('\n'));fs.writeFileSync(path.join(root,'build','qa.json'),JSON.stringify({slides:5,states,viewports:['1920x1080','1366x768','1280x720','390x844'],pageErrors:errors},null,2));await browser.close();console.log('PASS: screenshots, bounds, navigation, repeat, last page, viewport');
})();
