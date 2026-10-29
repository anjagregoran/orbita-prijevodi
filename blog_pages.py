# Blog: approved articles live in _blog/ as Markdown (GitHub Pages and the upload zip skip folders starting with _).
# Run by build_pages.py, so head(), NAV, page_hero() and the rest are already defined.
import re

def md_inline(t):
    t = e(t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)

def md_html(text):
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = block.strip().split("\n")
        if lines[0].startswith("## "):
            out.append(f"<h2>{md_inline(lines[0][3:])}</h2>")
            lines = lines[1:]
            if not lines:
                continue
        if all(re.match(r"\d+\. ", l) for l in lines):
            out.append("<ol>" + "".join("<li>" + md_inline(re.sub(r"^\d+\. ", "", l)) + "</li>" for l in lines) + "</ol>")
        elif all(l.startswith("- ") for l in lines):
            out.append("<ul>" + "".join("<li>" + md_inline(l[2:]) + "</li>" for l in lines) + "</ul>")
        elif len(lines) == 1 and re.fullmatch(r"\*[^*].*\*", lines[0]):
            out.append('<p class="post-note">' + md_inline(lines[0][1:-1]) + "</p>")
        else:
            out.append("<p>" + "<br>".join(md_inline(l) for l in lines) + "</p>")
    return "\n".join(out)

MONTHS = ["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja", "kolovoza", "rujna", "listopada", "studenoga", "prosinca"]
posts = []
for fn in sorted(os.listdir("_blog"), reverse=True):
    if not fn.endswith(".md"):
        continue
    raw = open(os.path.join("_blog", fn)).read()
    meta_part, body = raw.split("\n---\n")[:2]
    meta = dict(l.split(": ", 1) for l in meta_part.strip().split("\n") if ": " in l)
    lines = body.strip().split("\n")
    y, m, d = map(int, fn[:10].split("-"))
    posts.append(dict(slug=meta["Adresa (slug)"], title=lines[0].lstrip("# ").strip(), seo=meta["SEO naslov"], desc=meta["Meta opis"],
        date=fn[:10], date_hr=f"{d}. {MONTHS[m - 1]} {y}.", body=md_html("\n".join(lines[1:]))))

for p in posts:
    path = f"blog/{p['slug']}/"
    ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Blog", "blog/"), (p["title"], path)]),
        {"@type": "BlogPosting", "headline": p["title"], "description": p["desc"], "datePublished": p["date"], "inLanguage": "hr",
         "mainEntityOfPage": f"{SITE}/{path}", "author": {"@type": "Organization", "name": "Orbita prijevodi"},
         "publisher": {"@type": "Organization", "name": "Orbita prijevodi", "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/orbita-logo.png"}}}]}
    html_out = (head(p["seo"] + " | Orbita", p["desc"], path, ld).replace('content="website"', 'content="article"') + NAV + "<main>\n  "
        + page_hero([("Početna", "../"), ("Blog", "../blog/"), (p["title"], None)], (p["title"], ""), f"Objavljeno {p['date_hr']}")
        + f'''  <section class="section">
    <article class="prose blog-prose">{p["body"]}</article>
  </section>
  ''' + cta_band() + "</main>\n" + footer())
    # Article pages sit two folders deep, so every relative link needs one more step up
    write(path, html_out.replace('"../', '"../../').replace('"../../blog/"', '"../"'))
    pages.append(path)

path = "blog/"
cards = "".join(f'''<a class="svc-card" href="{p["slug"]}/"><p class="post-date">{p["date_hr"]}</p><h3>{e(p["title"])}</h3><p>{e(p["desc"])}</p><span>Pročitajte</span></a>''' for p in posts)
ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Blog", path)])]}
html_out = (head("Blog: savjeti o prijevodima, ovjerama i dokumentima | Orbita prijevodi", "Praktični savjeti o ovjerenim prijevodima, apostilleu i dokumentima za inozemstvo te zanimljivosti o jezicima, iz svakodnevnog rada prevoditeljske agencije Orbita.", path, ld)
    + NAV + "<main>\n  " + page_hero([("Početna", "../"), ("Blog", None)], ("Savjeti iz ", "prevoditeljskog ureda"), "Praktični vodiči za dokumente, prijevode i ovjere, i ponešto o jezicima, iz našeg svakodnevnog rada.")
    + f'''  <section class="section">
    <div class="svc-cards">{cards}</div>
  </section>
  ''' + cta_band() + "</main>\n" + footer())
write("blog", html_out)
pages.append(path)
