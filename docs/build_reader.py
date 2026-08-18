import markdown, json, html, re, os

DOCS = [
    ("START-HERE.md",     "Start Here",     "The whole project in one document. Read this first."),
    ("the-game.md",       "The Game",       "Plain terms. What it is and how it plays. Start here."),
    ("orientation.md",    "Orientation",    "Everything explained at length, straight through."),
    ("architecture.md",   "Architecture",   "The reasoning and the engineering."),
    ("entity-catalog.md", "Entity Catalog", "What ~90 games actually track, with real numbers."),
    ("categorization-and-action.md","Categorization & Action","How to represent everything, and what actions really are."),
    ("tabletop-history.md", "History",        "The hobby as history: people, money, panics, fights."),
    ("dictionary.md",     "Dictionary",     "Every term, every list, every decision."),
    ("substrate-checklist.md","Substrate Checklist","What has to exist, and what to decide about each."),
    ("field-survey.md",   "Field Survey",   "The state of the tabletop world, Aug 2026."),
    ("issues-and-ideas.md","Issues & Ideas", "23 ranked problems with the design, and 20 things it makes possible."),
    ("branding-research.md","Branding",      "Naming, trademark, identity, positioning, community. Aug 2026."),
    ("phase-map.md",      "Phase Map",      "Every phase to release, what gets done, and the gates."),
    ("open-questions.md", "Open Questions", "Everything undecided, by when it has to be answered."),
    ("work-repair.md",    "Work · Repair",  "The record of Phase 0. What was decided and why."),
    ("list-log.md",       "List Log",       "The conversation that made each list. The argument, not just the answer."),
    ("worked-builds.md",  "Worked Builds",  "Twenty things built from the model — the evaluation, not the description."),
    ("lists-research.md", "Lists · Research","What the field does, for every list still open. The digest."),
    ("research-timing.md","Research · Timing","Full report: naming when an ability may be used."),
    ("research-listeners.md","Research · Listeners","Full report: triggers, cascades, deterministic ordering."),
    ("research-states.md","Research · States","Full report: condition and status systems."),
    ("research-entities.md","Research · Entities","Full report: ships, factions, places and relationships as Entities."),
    ("tags-tabletop.md",  "Tags · Tabletop","Every tag, keyword, trait and property found across ~26 tabletop systems."),
    ("tags-digital.md",   "Tags · Digital", "The same, from digital games — PoE, Minecraft, RimWorld, Dwarf Fortress, Bethesda."),
    ("work-lists.md",     "Work · Lists",   "Phase 1 guide. Companion to the workbook."),
    ("work-tracks.md",    "Work · Tracks",  "Brand, legal and audience. Startable today."),
    ("repo-and-sync.md",  "Repo & Sync",    "Where everything lives, how git works here, and the traps."),
    ("README.md",         "Index",          "What each document is for."),
]

md = markdown.Markdown(extensions=["tables","fenced_code","toc","sane_lists","attr_list"])

missing = [fn for fn, _, _ in DOCS if not os.path.exists(fn)]
if missing:
    raise SystemExit(f"build_reader: missing source documents {missing} — "
                     "a renamed doc must be renamed here too, never silently dropped")

sections, nav = [], []
for i,(fn,title,blurb) in enumerate(DOCS):
    md.reset()
    body = md.convert(open(fn, encoding="utf-8").read())
    did = f"doc{i}"
    # collect h1/h2 for the nav
    heads = re.findall(r'<h([12]) id="([^"]+)">(.*?)</h[12]>', body)
    items = "".join(
        f'<a class="lvl{l}" href="#{did}--{hid}">{re.sub("<[^>]+>","",txt)}</a>'
        for l,hid,txt in heads
    )
    body = re.sub(r'(<h[1-6]) id="([^"]+)"', lambda m: f'{m.group(1)} id="{did}--{m.group(2)}"', body)
    nav.append(f'<div class="navdoc"><button class="navtitle" data-doc="{did}">{title}</button>'
               f'<div class="navblurb">{blurb}</div><div class="navitems">{items}</div></div>')
    sections.append(f'<section id="{did}" class="doc{" active" if i==0 else ""}">{body}</section>')

HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Game Platform — Design Documents</title>
<style>
:root{--bg:#faf9f7;--fg:#1b1a18;--mut:#6b6862;--line:#e2ded7;--accent:#8a5a2b;--code:#f2efe9;--head:#fff}
@media(prefers-color-scheme:dark){:root{--bg:#16151a;--fg:#e8e6e1;--mut:#9d9a93;--line:#2e2c33;--accent:#d99b5a;--code:#211f26;--head:#1d1c22}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);
 font:16px/1.65 ui-serif,Georgia,'Iowan Old Style',serif;-webkit-font-smoothing:antialiased}
#wrap{display:flex;min-height:100vh}
#side{width:290px;flex:0 0 290px;border-right:1px solid var(--line);height:100vh;position:sticky;top:0;
 overflow-y:auto;padding:22px 0 60px;background:var(--head)}
#side h1{font-size:14px;letter-spacing:.09em;text-transform:uppercase;color:var(--mut);
 margin:0 0 18px;padding:0 20px;font-weight:600;font-family:ui-sans-serif,system-ui,sans-serif}
.navdoc{margin-bottom:6px}
.navtitle{display:block;width:100%;text-align:left;background:none;border:0;cursor:pointer;
 font:600 15px/1.3 ui-sans-serif,system-ui,sans-serif;color:var(--fg);padding:9px 20px 2px}
.navtitle:hover{color:var(--accent)}
.navblurb{font:12px/1.45 ui-sans-serif,system-ui,sans-serif;color:var(--mut);padding:0 20px 8px}
.navitems{display:none;padding-bottom:10px;border-left:2px solid var(--line);margin-left:20px}
.navitems.open{display:block}
.navitems a{display:block;font:13px/1.4 ui-sans-serif,system-ui,sans-serif;color:var(--mut);
 text-decoration:none;padding:4px 14px 4px 12px}
.navitems a:hover{color:var(--accent);background:var(--code)}
.navitems a.lvl2{padding-left:24px;font-size:12.5px}
#main{flex:1;min-width:0;padding:52px 6vw 140px;max-width:1180px}
.doc{display:none}.doc.active{display:block}
h1,h2,h3,h4{font-family:ui-sans-serif,system-ui,sans-serif;line-height:1.25;font-weight:650}
h1{font-size:2.05em;margin:0 0 .55em;letter-spacing:-.02em}
h2{font-size:1.42em;margin:2.4em 0 .6em;padding-top:.9em;border-top:1px solid var(--line)}
h3{font-size:1.13em;margin:1.9em 0 .5em}
h4{font-size:1em;margin:1.5em 0 .4em;color:var(--mut)}
p,li{max-width:74ch}
blockquote{border-left:3px solid var(--accent);margin:1.4em 0;padding:.3em 0 .3em 1.2em;color:var(--mut)}
blockquote strong{color:var(--fg)}
code{background:var(--code);padding:.14em .38em;border-radius:3px;
 font:.88em ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:var(--code);padding:15px 18px;border-radius:7px;overflow-x:auto;
 border:1px solid var(--line);line-height:1.5}
pre code{background:none;padding:0;font-size:13px}
hr{border:0;border-top:1px solid var(--line);margin:3em 0}
a{color:var(--accent)}
.tw{overflow-x:auto;margin:1.5em 0;border:1px solid var(--line);border-radius:7px;background:var(--head)}
table{border-collapse:collapse;width:100%;font:14px/1.5 ui-sans-serif,system-ui,sans-serif}
th,td{padding:8px 13px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--code);font-weight:640;position:sticky;top:0;z-index:2;white-space:nowrap;
 border-bottom:2px solid var(--line)}
tbody tr:hover{background:var(--code)}
tbody tr:last-child td{border-bottom:0}
td code{font-size:12.5px;white-space:nowrap}
#top{position:fixed;right:22px;bottom:22px;background:var(--head);border:1px solid var(--line);
 color:var(--mut);border-radius:50%;width:42px;height:42px;cursor:pointer;font-size:17px;display:none}
@media(max-width:900px){#side{display:none}#main{padding:28px 20px 90px}}
</style></head><body><div id="wrap">
<nav id="side"><h1>Game Platform</h1>__NAV__</nav>
<main id="main">__SECTIONS__</main></div>
<button id="top" title="Back to top">&uarr;</button>
<script>
document.querySelectorAll('table').forEach(t=>{const w=document.createElement('div');
 w.className='tw';t.parentNode.insertBefore(w,t);w.appendChild(t);});
const docs=[...document.querySelectorAll('.doc')],titles=[...document.querySelectorAll('.navtitle')];
function show(id,scroll){docs.forEach(d=>d.classList.toggle('active',d.id===id));
 titles.forEach(b=>{const on=b.dataset.doc===id;b.style.color=on?'var(--accent)':'';
  b.nextElementSibling.nextElementSibling.classList.toggle('open',on);});
 if(scroll!==false)window.scrollTo(0,0);
 try{history.replaceState(null,'','#'+id);}catch(e){}}
titles.forEach(b=>b.onclick=()=>show(b.dataset.doc));
document.querySelectorAll('.navitems a').forEach(a=>a.onclick=e=>{
 show(a.getAttribute('href').slice(1).split('--')[0],false);});
let h='';try{h=location.hash.slice(1);}catch(e){}
show(h?h.split('--')[0]:docs[0].id,false);
if(h)setTimeout(()=>document.getElementById(h)?.scrollIntoView(),40);
const btnTop=document.getElementById('top');
btnTop.onclick=()=>window.scrollTo({top:0,behavior:'smooth'});
onscroll=()=>btnTop.style.display=scrollY>700?'block':'none';
</script></body></html>"""

out = HTML.replace("__NAV__","\n".join(nav)).replace("__SECTIONS__","\n".join(sections))
open("design-docs.html","w",encoding="utf-8").write(out)
print("built", len(out)//1024, "KB,", len(sections), "docs")
