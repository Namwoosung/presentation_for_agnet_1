from pathlib import Path
p=Path(__file__).with_name('create_deck.py')
s=p.read_text(encoding='utf-8')
s=s.replace("text((x1+x2)/2,(y1+y2)/2+dy,label,20,color,anchor='middle')", "text((x1+x2)/2+(20 if x1==x2 else 0),(y1+y2)/2+dy,label,20,color,anchor=('start' if x1==x2 else 'middle'))")
s=s.replace('node(650,477,260,105','node(650,477,280,105')
s=s.replace("    slides.append({'id':id", "    body=body.replace('#arr)', '#arr-'+id+')')\n    defs=defs.replace('id=\"arr\"', 'id=\"arr-'+id+'\"')\n    slides.append({'id':id")
s += "\n(ROOT/'preview.html').write_text(html.replace(\"const overview=params.get('view')==='overview'\", \"const overview=true\"),encoding='utf-8')\n"
p.write_text(s,encoding='utf-8')
