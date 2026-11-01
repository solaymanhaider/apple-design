#!/usr/bin/env python3
"""Refresh references/ from Apple's Human Interface Guidelines.

Apple renders the HIG from DocC JSON. This script downloads the navigator
index, every page's JSON, and converts each page to Markdown under references/,
mirroring Apple's section hierarchy.

Usage:  python3 scripts/update.py
"""
import collections, json, os, re, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'references')
BASE = 'https://developer.apple.com/tutorials/data'
HIG = '/design/human-interface-guidelines'
UA = {'User-Agent': 'Mozilla/5.0'}


def get_json(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except Exception as e:  # noqa
            err = e
            time.sleep(2 * (i + 1))
    raise SystemExit(f'failed {url}: {err}')


# ---- 1. navigator (section hierarchy) -------------------------------------
navigator = get_json(BASE + '/index/design--human-interface-guidelines')
nav = navigator['interfaceLanguages']['swift'][0]['children']
loc = {'index': {'file': 'README.md', 'title': 'Human Interface Guidelines'}}


def walk_nav(nodes, dirs):
    for n in nodes:
        slug = n['path'].replace(HIG, '').strip('/')
        kids = n.get('children', [])
        d = dirs + [slug] if kids else dirs
        loc[slug] = {'title': n['title'],
                     'file': ('/'.join(d) + '/README.md') if kids else ('/'.join(dirs + [slug]) + '.md')}
        walk_nav(kids, d)


walk_nav(nav, [])

# ---- 2. crawl every page ---------------------------------------------------
pages = {}
seen = set()
q = collections.deque([HIG])
while q:
    path = q.popleft()
    if path in seen:
        continue
    seen.add(path)
    slug = path[len(HIG):].strip('/') or 'index'
    d = get_json(BASE + path + '.json')
    pages[slug] = d
    print('fetched', slug, file=sys.stderr)
    for v in d.get('references', {}).values():
        u = v.get('url', '')
        if u.startswith(HIG):
            u = u.split('#')[0].rstrip('/')
            if u not in seen:
                q.append(u)

missing = set(pages) - set(loc)
for slug in missing:  # page not in navigator: file it at top level
    loc[slug] = {'title': pages[slug]['metadata']['title'], 'file': slug + '.md'}

def relpath(frm, to):
    return os.path.relpath(to, os.path.dirname(frm) or '.')

class Conv:
    def __init__(s,d,slug):
        s.d=d; s.refs=d['references']; s.slug=slug; s.file=loc[slug]['file']
    def ref_url(s,ident):
        r=s.refs.get(ident,{})
        url=r.get('url','') or (ident if ident.startswith('http') else '')
        url=url.replace('https://developer.apple.com'+HIG, HIG)
        if url.startswith(HIG):
            tslug=url.replace(HIG,'').split('#')[0].strip('/').split('/')[-1] or 'index'
            anchor=('#'+url.split('#')[1]) if '#' in url else ''
            if tslug in loc: return relpath(s.file, loc[tslug]['file'])+anchor.lower()
        if url.startswith('/'): return 'https://developer.apple.com'+url
        if url: return url
        if ident.startswith('http'): return ident
        return ''
    def ref_title(s,ident):
        r=s.refs.get(ident,{})
        t=r.get('title')
        if not t and r.get('fragments'): t=''.join(f.get('text','') for f in r['fragments'])
        return t or ident
    def inline(s,items):
        out=[]
        for it in items:
            t=it.get('type')
            if t=='text': out.append(it['text'])
            elif t=='strong': out.append('**'+s.inline(it['inlineContent']).strip()+'**')
            elif t=='emphasis': out.append('*'+s.inline(it['inlineContent']).strip()+'*')
            elif t=='codeVoice': out.append('`'+it['code']+'`')
            elif t=='reference':
                title=it.get('overridingTitle') or s.ref_title(it['identifier'])
                url=s.ref_url(it['identifier'])
                out.append(f'[{title}]({url})' if url else title)
            elif t=='link': out.append(f"[{it.get('title',it['destination'])}]({it['destination']})")
            elif t=='image':
                r=s.refs.get(it['identifier'],{})
                cap=''
                md=it.get('metadata',{})
                if md.get('abstract'): cap=s.inline(md['abstract']).strip()
                alt=r.get('alt','').strip()
                txt=cap or alt
                out.append(f'\n\n> **Image:** {txt}\n\n' if txt else '')
            elif t=='newTerm': out.append('*'+s.inline(it['inlineContent'])+'*')
            elif t=='inlineHead': out.append('**'+s.inline(it['inlineContent'])+'**')
            elif t in('superscript','subscript','strikethrough'): out.append(s.inline(it['inlineContent']))
            elif 'inlineContent' in it: out.append(s.inline(it['inlineContent']))
            elif 'text' in it: out.append(it['text'])
        return ''.join(out)
    def blocks(s,items,indent=''):
        out=[]
        for b in items:
            t=b.get('type')
            if t=='heading':
                out.append('\n'+'#'*max(2,b.get('level',2))+' '+b['text']+'\n')
            elif t=='paragraph':
                txt=s.inline(b['inlineContent']).strip()
                if txt: out.append(indent+txt+'\n')
            elif t=='small':
                txt=s.inline(b['inlineContent']).strip()
                if txt: out.append(indent+'*'+txt+'*\n')
            elif t in('unorderedList','orderedList'):
                for i,li in enumerate(b['items']):
                    inner=s.blocks(li['content'],indent+'  ').strip('\n')
                    lines=inner.split('\n')
                    bullet=(f'{i+1}. ' if t=='orderedList' else '- ')
                    first=lines[0].lstrip()
                    rest='\n'.join(lines[1:])
                    out.append(indent+bullet+first+('\n'+rest if rest.strip() else '')+'\n')
            elif t=='aside':
                name=b.get('name') or b.get('style','Note').capitalize()
                inner=s.blocks(b['content']).strip('\n')
                q='\n'.join('> '+l if l else '>' for l in inner.split('\n'))
                out.append(f'\n> **{name}:**\n{q}\n')
            elif t=='table':
                rows=b['rows']
                def cell(c): 
                    t=s.blocks(c).strip().replace('> **Image:** ','').replace('> **Video:** ','')
                    return t.replace('\n\n','<br>').replace('\n','<br>').replace('|','\\|')
                md=[]
                for ri,row in enumerate(rows):
                    md.append('| '+' | '.join(cell(c) for c in row)+' |')
                    if ri==0: md.append('|'+'---|'*len(row))
                out.append('\n'+'\n'.join(md)+'\n')
            elif t=='row':
                for col in b['columns']:
                    out.append(s.blocks(col['content'],indent))
            elif t=='tabNavigator':
                for tab in b['tabs']:
                    c=tab['content']
                    if c and c[0].get('type')=='heading' and c[0].get('text','').strip().lower()==tab['title'].strip().lower():
                        out.append(s.blocks(c,indent))
                    else:
                        out.append(f"\n**{tab['title']}**\n\n"+s.blocks(c,indent))
            elif t=='video':
                r=s.refs.get(b['identifier'],{})
                alt=r.get('alt','') or b['identifier']
                out.append(f'\n> **Video:** {alt}\n')
            elif t=='links':
                for ident in b['items']:
                    r=s.refs.get(ident,{})
                    title=r.get('title',ident); url=s.ref_url(ident)
                    ab=s.inline(r.get('abstract',[])).strip()
                    out.append(f'- [{title}]({url})'+(f' — {ab}' if ab else '')+'\n')
            elif t=='codeListing':
                out.append('\n```'+(b.get('syntax') or '')+'\n'+'\n'.join(b['code'])+'\n```\n')
            elif t=='termList':
                for item in b['items']:
                    out.append('- **'+s.inline(item['term']['inlineContent']).strip()+'**: '+s.blocks(item['definition']['content']).strip()+'\n')
            elif t=='image':
                r=s.refs.get(b['identifier'],{}); alt=r.get('alt','').strip()
                if alt: out.append(f'\n> **Image:** {alt}\n')
            elif 'content' in b: out.append(s.blocks(b['content'],indent))
            elif 'inlineContent' in b: out.append(indent+s.inline(b['inlineContent'])+'\n')
        return '\n'.join(out)
    def render(s):
        d=s.d; md=d['metadata']; title=md['title']
        url='https://developer.apple.com'+(HIG if s.slug=='index' else f'{HIG}/{s.slug}')
        head=[f'# {title}\n']
        ab=s.inline(d.get('abstract',[])).strip()
        if ab: head.append(f'*{ab}*\n')
        cm=md.get('customMetadata',{})
        meta=[f'Source: {url}']
        if cm.get('supported-platforms'): meta.append('Platforms: '+', '.join(cm['supported-platforms'].split(',')))
        if cm.get('alert-text'): meta.append(f"Latest change ({cm.get('alert-date','')}): {cm['alert-text']}")
        head.append('\n'.join(meta)+'\n')
        body=''.join(s.blocks(sec['content']) for sec in d.get('primaryContentSections',[]))
        topics=''
        for ts in d.get('topicSections',[]):
            sec=''
            for ident in ts['identifiers']:
                if s.ref_url(ident) and f"]({s.ref_url(ident)})" in body: continue
                r=s.refs.get(ident,{}); ab=s.inline(r.get('abstract',[])).strip()
                sec+=f"- [{r.get('title',ident)}]({s.ref_url(ident)})"+(f' — {ab}' if ab else '')+'\n'
            if sec: topics+=f"\n## {ts.get('title') or ts.get('anchor','Topics')}\n\n"+sec
        txt='\n'.join(head)+'\n'+body+topics
        txt=re.sub(r'\n{3,}','\n\n',txt).strip()+'\n'
        return txt

import shutil
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
for slug, d in pages.items():
    out = os.path.join(OUT, loc[slug]['file'])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(Conv(d, slug).render())
print(f'wrote {len(pages)} pages to {OUT}')
