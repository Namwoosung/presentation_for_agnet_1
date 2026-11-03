/* Space is the sole audience progression input. Presses during the transition
   are discarded; held keys never advance twice. No wrap after the final build. */
const slides=[...document.querySelectorAll('.slide')];
const stage=document.querySelector('.deck-stage');
const params=new URLSearchParams(location.search);
const initial=Number(params.get('slide')||1);
let index=Number.isInteger(initial)?Math.min(slides.length-1,Math.max(0,initial-1)):0;
let step=0,held=false,locked=false;
const overview=DECK_OVERVIEW;
if(overview)document.body.classList.add('overview');
function fit(){const scale=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(${(innerWidth-1920*scale)/2}px,${(innerHeight-1080*scale)/2}px) scale(${scale})`;}
function render(){
 slides.forEach((slide,i)=>{slide.classList.toggle('active',i===index);slide.setAttribute('aria-hidden',String(i!==index));});
 const slide=slides[index],count=Number(slide.dataset.steps);
 slide.querySelectorAll('[data-build]').forEach(el=>{let k=Number(el.dataset.build);el.classList.toggle('shown',k<=step);el.classList.toggle('past',k<step);});
 const finished=index===slides.length-1&&(overview||step===count-1);
 slide.querySelector('.build-counter').textContent=`${overview?'전체 화면':`build ${step+1}/${count}`}    ${finished?'END':'SPACE'}`;
 window.deckState={slideId:slide.dataset.id,slideIndex:index,stepIndex:step,stepCount:count,sourceRefs:metadata[index].sources,mode:overview?'overview':'presentation'};
 document.title=`${slide.dataset.id} · Agent Framework Seminar II`;
}
addEventListener('keydown',event=>{
 if(event.code!=='Space')return;
 if(/INPUT|TEXTAREA|SELECT/.test(event.target.tagName)||event.target.isContentEditable)return;
 event.preventDefault();if(event.repeat||held||locked)return;
 held=true;locked=true;setTimeout(()=>locked=false,300);
 if(overview){if(index<slides.length-1)index++;}
 else if(step<Number(slides[index].dataset.steps)-1)step++;
 else if(index<slides.length-1){index++;step=0;}
 render();
});
addEventListener('keyup',event=>{if(event.code==='Space')held=false;});
addEventListener('blur',()=>{held=false;});addEventListener('resize',fit);
fit();render();
