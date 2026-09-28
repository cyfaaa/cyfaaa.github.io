#!/usr/bin/env python3
"""Build static academic pages from local content, using the reference theme DOM."""
from pathlib import Path
from html import escape as esc
import json,re,markdown
ROOT=Path(__file__).resolve().parents[1]
CONTENT=ROOT/'_site_content'
def md(name):return markdown.markdown((CONTENT/f'{name}.md').read_text(),extensions=['tables','attr_list'])
def section(label,anchor,body):return f'<h1 id="{anchor}">{label}</h1>{body}'
PAPERS=json.loads((CONTENT/'papers.json').read_text())
# Keep original publication metadata; combine all venues in a single list.
for p in PAPERS:
 if not p['year']:p['year']='2026'
PAPERS.sort(key=lambda p:p['year'],reverse=True)
def publications(selected=False):
 records=PAPERS
 if selected:
  records=[p for p in PAPERS if p.get('image') and (p.get('featured_eligible') or (p.get('award') and 'Nomination' not in p['award']))]
 out='<p>J: journal; C: conference. * Corresponding author.</p>'
 if not selected: out+='<ul class="publication-list">'
 for p in records:
  title=esc(p['title']); authors=esc(p['authors'])
  authors=re.sub(r'(Yinfeng Cao|Yin Feng Cao|YinFeng Cao)',lambda m:'<strong>'+m[0]+'</strong>',authors)
  links=p['links'];url=next((x['url'] for x in links if x['label']!='Program'),None)
  heading=f'<a class="publication-title" href="{esc(url)}">{title}</a>' if url else f'<span class="publication-title">{title}</span>'
  badge=p.get('badge') or p['venue'].strip('.').replace('International Workshop on Blockchain and Web3 for Education, Research, and Science (BERS), International Conference on Artificial Intelligence for Health and Education (ICAIHE 2026)','ICAIHE 2026 / BERS')
  if p['year'] not in badge:badge+=' '+p['year']
  visual=f'<img src="{esc(p["image"])}" alt="{title}: paper overview" width="100%" loading="lazy">' if p.get('image') else ''
  desc=f'<ul><li>{esc(p["summary"])}</li></ul>' if selected and p.get('summary') else f'<ul><li><em>{esc(p["venue"].strip(chr(46)))}</em>, {p["year"]}.</li></ul>'
  resources=' '.join(f'(<a href="{esc(x["url"])}"><strong>{esc("Paper" if x["label"].startswith(("DOI", "Preprint")) else x["label"])}</strong></a>)' for x in links)
  note=' · '.join(x for x in [p['status'],p['award']] if x)
  labels=' · '.join(f'<a href="{esc(x["source"])}">{esc(x["label"])}</a>' for x in p.get('classifications', []))
  if note: note+='.'
  classification=f'<span class="publication-classification">[{labels}]</span>' if labels else ''
  if not selected:
   award=f'<span class="publication-award">[{esc(p["award"])}]</span>' if p['award'] else ''
   status=esc(p['status'])+'.' if p['status'] else ''
   out+=f'<li><span class="publication-id">[{esc(p["id"])}]</span> {classification} {award} {authors}. {heading}. <em>{esc(p["venue"].rstrip(chr(46)))}</em>, {esc(p["year"])}. {status} {resources}</li>'
   continue
  card_class='paper-box' if visual else 'paper-box no-figure'
  out+=f'<div class="{card_class}"><div class="paper-box-image"><div><div class="badge">{esc(badge)}</div>{visual}</div></div><div class="paper-box-text"><p>{heading}</p><p>{authors}</p>{desc}<p>{esc(note)}</p><p>{classification}</p><p>{resources}</p></div></div>'
 return out if selected else out+'</ul>'
NAV=[('About Me','/#about-me'),('News','/#-news'),('Publications','/publications/'),('Awards && Honors','/#-honors-and-awards'),('Education Background','/#-education-background'),('Talks','/#-talks'),('Academic Services','/#-academic-services'),('Projects','/projects/'),('Demo','/demo/'),('Teaching','/teaching/')]
def render(title,body):
 nav=''.join(f'<li class="masthead__menu-item"><a href="{u}">{esc(t)}</a></li>' for t,u in NAV)
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Yinfeng Cao (曹寅峰) — {esc(title)}</title><meta name="description" content="Yinfeng Cao, Assistant Professor at HKCT Institute of Higher Education. Blockchain, edge computing and digital twins."><link rel="stylesheet" href="/assets/css/reference-main.css"><link rel="stylesheet" href="/assets/css/academic.css?v=20260926-visitor-stats"><link rel="icon" href="/assets/favicon.svg"></head><body>
<a class="skip" href="#main">Skip to content</a><div class="masthead"><div class="masthead__inner-wrap"><div class="masthead__menu"><nav id="site-nav" class="greedy-nav"><button aria-label="Toggle navigation" aria-expanded="false"><div class="navicon"></div></button><ul class="visible-links"><li class="masthead__menu-item masthead__menu-item--lg masthead__menu-home-item"><a href="/#about-me">Homepage</a></li>{nav}</ul><ul class="hidden-links hidden"></ul></nav></div></div></div>
<div id="main" role="main"><div class="sidebar sticky"><div class="profile_box" itemscope itemtype="http://schema.org/Person"><div class="author__avatar"><div class="portrait-frame"><img src="/images/yinfeng-cao.jpg" alt="Yinfeng Cao" class="portrait"></div></div><div class="author__content"><h3 class="author__name">Yinfeng Cao</h3><h3 class="author__name">(曹寅峰)</h3></div><div class="author__urls-wrapper"><ul class="author__urls social-icons"><li><div style="white-space:normal;margin-bottom:1em">Assistant Professor at HKCT Institute of Higher Education</div></li><li><i class="fa fa-fw fa-map-marker" aria-hidden="true"></i> Hong Kong</li><li><a href="mailto:kevincao@ctihe.edu.hk"><i class="fas fa-fw fa-envelope" aria-hidden="true"></i> Email</a></li><li><a href="https://github.com/cyfaaa"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a></li><li><a href="https://scholar.google.com.hk/citations?user=xos6JXEAAAAJ&amp;hl=en"><i class="fas fa-fw fa-graduation-cap" aria-hidden="true"></i> Google Scholar</a></li></ul><div class="author__urls_sm"><a href="mailto:kevincao@ctihe.edu.hk" aria-label="Email"><i class="fas fa-fw fa-envelope"></i></a><a href="https://github.com/cyfaaa" aria-label="Github"><i class="fab fa-fw fa-github"></i></a><a href="https://scholar.google.com.hk/citations?user=xos6JXEAAAAJ" aria-label="Google Scholar"><i class="fas fa-fw fa-graduation-cap"></i></a></div></div></div></div><article class="page"><div class="page__inner-wrap"><section class="page__content">{body}</section></div></article></div>
<footer class="visitor-stats"><a href="https://librecounter.org/cyfaaa.github.io/show" target="_blank" rel="noopener noreferrer">Visitor statistics <img src="https://librecounter.org/oldStyle.svg" referrerpolicy="unsafe-url" alt="Page views — open statistics" width="110" height="30"></a><span>Powered by <a href="https://github.com/alexfernandez/librecounter">LibreCounter</a></span></footer>
<script src="/assets/js/vendor/jquery/jquery-1.12.4.min.js"></script><script src="/assets/js/reference-navigation.js"></script></body></html>'''
about='''<span class="anchor" id="about-me"></span><p>I am an Assistant Professor at the HKCT Institute of Higher Education and a part-time Postdoctoral Fellow at The Hong Kong Polytechnic University. I completed my Ph.D. in Computing at The Hong Kong Polytechnic University, supervised by <a href="https://www4.comp.polyu.edu.hk/~csjcao/">Prof. Jiannong Cao</a>. I was a visiting research student at Kanazawa University, supervised by <a href="https://sites.google.com/site/liruidong/">Prof. Ruidong Li</a>.</p><p>My research focuses on <strong>trustworthy decentralized AI</strong> for applications in education, finance, and other domains where data and computing resources are distributed across devices and organizations. I study how these participants can collaborate on AI tasks while retaining control of their data and verifying the information and computation they exchange. My work brings together blockchain for verifiable coordination, edge computing for distributed learning and inference, and digital twins for connecting AI systems with physical environments. It spans three areas:</p><ul><li><p><strong>Blockchain Infrastructure and Security</strong>: Decentralized identity, cross-chain interoperability, and verifiable data sharing to support collaboration across organizations.</p></li><li><p><strong>Edge Computing and AI</strong>: Federated learning and decentralized inference that enable devices to collaborate under data and resource constraints.</p></li><li><p><strong>Digital Twin Networks</strong>: Trustworthy digital twin generation and cross-domain sharing that provide AI systems with verifiable representations of physical environments.</p></li></ul>'''
old=(CONTENT/'about.md').read_text()
def extract(start,end=None):
 s=old.split('## '+start+'\n')[1]
 if end:s=s.split('## '+end)[0]
 return markdown.markdown(s)
news=md('news');news=re.sub(r'<h2>2026</h2>','',news)
services=md('service')
# Mirror the reference's compact service-category lists.
services=re.sub(r'<h2>(.*?)</h2>\s*<ul>(.*?)</ul>',lambda m:'<li><strong>'+m[1]+':</strong> '+', '.join(re.findall(r'<li>(.*?)</li>',m[2],re.S))+'</li>',services,flags=re.S)
services='<ul>'+services+'</ul>'
talks=md('talks') if (CONTENT/'talks.md').exists() else ''
awards=extract('Selected Honors and Awards','Scholarships')+extract('Scholarships')
awards=re.sub(r'<li>(.*?), (20[0-9]{2})</li>',r'<li><em>\2</em> \1</li>',awards)
education=markdown.markdown("""- *2020 – 2025*, **The Hong Kong Polytechnic University**.
    - Ph.D. in Computing
    - Advisor: [Prof. Jiannong Cao](https://www4.comp.polyu.edu.hk/~csjcao/)
- *2016 – 2020*, **Xidian University**.
    - B.Eng. in Information Security, Experimental Class in Cybersecurity
""")
home=about+section('News','-news',news)+section('Selected Publications <a href="/publications/">[FullList]</a>','-publications',publications(True))+section('Awards && Honors','-honors-and-awards',awards)+section('Education Background','-education-background',education)+section('Talks','-talks',talks)+section('Academic Services','-academic-services',services)
pages={'':('Homepage',home),'publications':('Publications',section('Publications','-publications',publications())),'news':('News',section('News','-news',news)),'service':('Academic Services',section('Academic Services','-academic-services',services)),'talks':('Talks',section('Talks','-talks',talks)),'projects':('Projects',section('Projects','projects',md('projects'))),'demo':('Demo',section('Demo','demo',md('demo'))),'teaching':('Teaching',section('Teaching','teaching',md('teaching'))),'cv':('CV',section('CV','cv',md('cv')))}
for key,(title,body) in pages.items():
 dest=ROOT/key/'index.html';dest.parent.mkdir(exist_ok=True);dest.write_text(render(title,body))
 if key:(ROOT/f'{key}.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=/{key}/"><title>{title}</title><a href="/{key}/">{title}</a></html>')
print(f'Built {len(pages)} pages.')
