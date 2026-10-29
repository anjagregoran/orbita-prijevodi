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

# Short contact line above every article, so a reader can get in touch without scrolling
POST_CONTACT = '''<aside class="post-contact" aria-label="Kontakt">
      <p>Trebate prijevod ili savjet oko dokumenata? Javite nam se:</p>
      <ul>
        <li><span>Rijeka i Kastav</span><a href="tel:+385981631930">098 163 19 30</a><a href="mailto:info@orbitaprijevodi.com">info@orbitaprijevodi.com</a></li>
        <li><span>Zagreb</span><a href="tel:+385916126784">091 612 6784</a><a href="mailto:zagreb@orbitaprijevodi.com">zagreb@orbitaprijevodi.com</a></li>
      </ul>
    </aside>'''

for p in posts:
    path = f"blog/{p['slug']}/"
    ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Blog", "blog/"), (p["title"], path)]),
        {"@type": "BlogPosting", "headline": p["title"], "description": p["desc"], "datePublished": p["date"], "inLanguage": "hr",
         "mainEntityOfPage": f"{SITE}/{path}", "author": {"@type": "Organization", "name": "Orbita prijevodi"},
         "publisher": {"@type": "Organization", "name": "Orbita prijevodi", "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/orbita-logo.png"}}}]}
    html_out = (head(p["seo"] + " | Orbita", p["desc"], path, ld).replace('content="website"', 'content="article"') + NAV + "<main>\n  "
        + page_hero([("Početna", "../"), ("Blog", "../blog/"), (p["title"], None)], (p["title"], ""), f"Objavljeno {p['date_hr']}")
        + f'''  <section class="section">
    {POST_CONTACT}
    <article class="prose blog-prose">{p["body"]}</article>
  </section>
  <section class="section">
    <div class="section-head"><p class="label">Kontakt</p><h2>Javite nam se, <em>rado ćemo pomoći</em></h2></div>
    <div class="offices">
      {office_card("rijeka")}
      {office_card("zagreb")}
    </div>
  </section>
  ''' + cta_band() + "</main>\n" + footer())
    # Article pages sit two folders deep, so every relative link needs one more step up
    write(path, html_out.replace('"../', '"../../').replace('"../../blog/"', '"../"'))
    pages.append(path)

path = "blog/"
cards = "".join(f'''<a class="svc-card" href="{p["slug"]}/"><p class="post-date">{p["date_hr"]}</p><h3>{e(p["title"])}</h3><p>{e(p["desc"])}</p><span>Pročitajte</span></a>''' for p in posts)
if posts:
    listing = f'<div class="svc-cards">{cards}</div>'
else:
    listing = '''<div class="blog-empty">
      <h2>Prvi članci stižu uskoro</h2>
      <p>Pripremamo praktične vodiče o ovjerenim prijevodima, apostilleu i dokumentima za inozemstvo, i ponešto o jezicima. Dok ih ne objavimo, odgovore na najčešća pitanja pronaći ćete na stranici Česta pitanja.</p>
      <a class="pill pill-line" href="../cesta-pitanja/">Česta pitanja</a>
    </div>'''
ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Blog", path)])]}
html_out = (head("Blog: savjeti o prijevodima, ovjerama i dokumentima | Orbita prijevodi", "Praktični savjeti o ovjerenim prijevodima, apostilleu i dokumentima za inozemstvo te zanimljivosti o jezicima, iz svakodnevnog rada prevoditeljske agencije Orbita.", path, ld)
    + NAV + "<main>\n  " + page_hero([("Početna", "../"), ("Blog", None)], ("Savjeti iz ", "prevoditeljskog ureda"), "Praktični vodiči za dokumente, prijevode i ovjere, i ponešto o jezicima, iz našeg svakodnevnog rada.")
    + f'''  <section class="section">
    {listing}
  </section>
  ''' + cta_band() + "</main>\n" + footer())
if not posts:  # keep an empty listing out of Google until the first article is up
    html_out = html_out.replace("<head>", '<head>\n<meta name="robots" content="noindex">', 1)
write("blog", html_out)
if posts:
    pages.append(path)

# Home page: the three newest articles, shown only once there is at least one
home_cards = "".join(f'''<a class="svc-card" href="blog/{p["slug"]}/"><p class="post-date">{p["date_hr"]}</p><h3>{e(p["title"])}</h3><p>{e(p["desc"])}</p><span>Pročitajte</span></a>''' for p in posts[:3])
home_section = f'''
  <section class="section" id="blog">
    <div class="section-head reveal"><p class="label">Blog</p><h2>Savjeti iz <em>prevoditeljskog ureda</em></h2></div>
    <div class="svc-cards">{home_cards}</div>
    <p class="blog-more"><a class="pill pill-line" href="blog/">Svi članci</a></p>
  </section>
  ''' if posts else ""
home = open("index.html").read()
home = re.sub(r"<!--BLOG-->.*?<!--/BLOG-->", lambda m: "<!--BLOG-->" + home_section + "<!--/BLOG-->", home, flags=re.S)
open("index.html", "w").write(home)
