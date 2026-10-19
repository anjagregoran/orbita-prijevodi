"""Builds the separate pages (services, cities, FAQ, contact) and sitemap.xml.

Each page lives in its own folder (e.g. ovjereni-prijevodi/index.html) so the
addresses match the old WordPress site and keep what Google already knows.
Run:  python3 build_pages.py
"""
import json, os, html
from urllib.parse import quote

SITE = "https://www.orbitaprijevodi.com"
V = "57"  # bump together with ?v= in index.html

PHONES = [("Rijeka", "098 163 19 30", "385981631930"), ("Zagreb", "091 612 6784", "385916126784")]
WA_TEXT = quote("Poštovani, šaljem fotografije dokumenta za ponudu prijevoda.")
AVAILABLE = "Dostupni smo stalno, pa nas u vezi s prijevodom možete u bilo koje vrijeme nazvati ili nam poslati poruku ili e-poštu."
PRICE = "Cijena se obračunava po kartici teksta, a točan iznos dobit ćete u neobvezujućoj ponudi čim pogledamo dokument."
SEND_PHOTO = "Dokument možete skenirati ili poslikati mobitelom: položite ga na ravnu površinu, poslikajte odozgo i pazite da je slika oštra i da se vidi sav tekst."

# Questions that fit on almost every page
Q_SEND = ("Kako Vam mogu poslati dokument?", f"E-poštom, putem obrasca na stranici, Viberom ili WhatsAppom na 098 163 19 30 ili 091 612 6784, ili osobno u jednom od naših ureda. {SEND_PHOTO}")
Q_PRICE = ("Kako se obračunava cijena?", f"{PRICE} Ponudu ne možemo izraditi samo na temelju opisa, zato nam pošaljite sam dokument.")
Q_LANG = ("Na koje jezike prevodite?", "Prevodimo s više od 30 jezika i na više od 30 jezika, od engleskog, njemačkog, talijanskog i slovenskog do japanskog, kineskog i arapskog. Ako jezika koji Vam treba nema na popisu, osigurat ćemo Vam prijevod i na njega.")
Q_WHEN = ("Kada ste dostupni?", AVAILABLE)
Q_CERT = ("Što je ovjereni prijevod?", "Ovjereni prijevod izrađuje sudski tumač, osoba s diplomom, izvrsnim poznavanjem stranog jezika i položenim ispitom za sudskog tumača, koju imenuje županijski sud Republike Hrvatske. Prijevod se uvezuje s izvornim dokumentom ili njegovom preslikom, a tumač pečatom i potpisom jamči da je istovjetan izvorniku.")

SERVICES = [
  dict(slug="ovjereni-prijevodi", name="Ovjereni prijevodi",
    title="Ovjereni prijevodi sudskih tumača | Rijeka, Kastav i Zagreb",
    desc="Ovjereni prijevodi svjedodžbi, diploma, rodnih i vjenčanih listova, izvadaka iz sudskog registra i medicinskih nalaza. Sudski tumači za više od 30 jezika, uredi u Rijeci i Zagrebu.",
    h1=("Ovjereni prijevodi ", "sudskih tumača"),
    lead="Službene dokumente za Vas brzo i uredno pripremaju naši provjereni sudski tumači, uz pečat i potpis koje priznaju sudovi, javni bilježnici i institucije.",
    body=[
      "Ovjereni prijevodi posebna su vrsta prijevoda koje izrađuju sudski tumači. To su osobe s diplomom i iznimnim poznavanjem stranog jezika, s položenim ispitom za sudskog tumača, koje imenuje županijski sud Republike Hrvatske.",
      "Ovjereni prijevod uvezuje se s originalom, ovjerenom ili običnom preslikom izvornog dokumenta, a sudski tumač pečatom i potpisom jamči da je prevedeni tekst istovjetan izvorniku.",
      "Ovjerene prijevode svih vrsta dokumenata za Vas pripremaju naši provjereni sudski tumači, koji iza sebe imaju bogato iskustvo s najrazličitijim vrstama ovjerenih prijevoda.",
    ],
    items=["Svjedodžbe i diplome", "Rodni i vjenčani listovi", "Radne dozvole", "Izvadci iz sudskog registra", "Stručna i vještačka mišljenja", "Medicinski nalazi"],
    faq=[Q_CERT, ("Trebam li donijeti original dokumenta?", "Za ponudu je dovoljna jasna fotografija ili sken dokumenta. Prijevod se zatim uvezuje s originalom, ovjerenom ili običnom preslikom, ovisno o tome što traži institucija kojoj ga predajete, a mi ćemo Vas uputiti što je u Vašem slučaju potrebno."), Q_PRICE, Q_SEND, Q_LANG]),
  dict(slug="pisani-prijevodi", name="Pisani prijevodi",
    title="Pisani prijevodi općih i stručnih tekstova | Orbita prijevodi",
    desc="Prijevodi općih i stručnih tekstova, korisničkih uputa, internetskih stranica, programske opreme, titlova i rukopisa na više od 30 jezika. Rijeka, Kastav i Zagreb.",
    h1=("Pisani ", "prijevodi"),
    lead="Opći i stručni tekstovi iz svih područja, prevedeni tako da se čitaju kao da su izvorno napisani na tom jeziku.",
    body=[
      "Predajte nam na povjerenje prijevode svih vrsta općih i stručnih tekstova, rukopisa, titlova te internetske građe, od internetskih stranica do programske opreme.",
      "Stručni prijevodi sadrže nazivlje koje zahtijeva poznavanje predmetnog područja i namijenjeni su čitateljima iz te struke. Surađujemo sa stručnjacima iz širokog polja tehničkih i društvenih znanosti, a pri narudžbi vrlo stručnih prijevoda poželjno je da naručitelj osigura pomoćnu literaturu ili odredi svog stručnjaka za savjete u vezi s nazivljem.",
      "Za engleski i talijanski jezik nudimo i prevođenje u CAT alatima, koji osiguravaju dosljedno nazivlje u većim i ponavljajućim projektima.",
    ],
    items=["Stručni i tehnički tekstovi", "Korisničke upute i jamstveni listovi", "Medicinska dokumentacija", "Internetske stranice", "Programska oprema", "Titlovi", "Rukopisi"],
    faq=[Q_PRICE, Q_SEND, Q_LANG, Q_WHEN]),
  dict(slug="usmeni-prijevodi", name="Usmeno prevođenje",
    title="Usmeno prevođenje: simultano, konsekutivno, šaptano | Orbita",
    desc="Simultano, konsekutivno i šaptano prevođenje na sastancima, konferencijama i sajmovima, te sudski tumač kod javnog bilježnika ili na sudu. Rijeka i Zagreb.",
    h1=("Usmeno ", "prevođenje"),
    lead="Simultano, konsekutivno i šaptano prevođenje, kad je važno da Vas svi u prostoriji razumiju.",
    body=[
      "Tražite li prevoditelje za simultano ili konsekutivno prevođenje, možda i za više jezika u istom danu? Trebate li sudskog tumača za tumačenje kod javnog bilježnika ili na sudu, ili nešto posebno, poput prevođenja uz pratnju?",
      "Usmeno prevođenje iznimno je zahtjevno i mogu ga obavljati samo specijalizirane osobe s velikim iskustvom i iznimnim poznavanjem jezika.",
      "Prijevod izgovorene riječi na Vašim poslovnim sastancima, seminarima, simpozijima, međunarodnim i tiskovnim konferencijama, prezentacijama, sajmovima, sjednicama nadzornih odbora, pregovorima, državnim protokolima ili godišnjim skupštinama prepustite našim usmenim prevoditeljima.",
    ],
    items=["Konferencije i seminari", "Poslovni sastanci i pregovori", "Sajmovi i prezentacije", "Sjednice i godišnje skupštine", "Javni bilježnik i sud", "Prevođenje uz pratnju"],
    faq=[("Koja je razlika između simultanog i konsekutivnog prevođenja?", "Kod simultanog prevođenja prevoditelj prevodi istodobno s govornikom, najčešće iz kabine i uz slušalice, pa je pogodno za konferencije. Kod konsekutivnog prevođenja govornik zastaje, a prevoditelj zatim prevodi rečeno, što je uobičajeno na sastancima, pregovorima i kod javnog bilježnika. Šaptano prevođenje izvodi se tiho, uz jednu ili dvije osobe."), ("Kako rezervirati prevoditelja?", f"Javite nam datum, mjesto, trajanje, jezike i vrstu događaja, a mi ćemo Vam poslati ponudu. {AVAILABLE}"), Q_LANG]),
  dict(slug="lektoriranje", name="Lektura i korektura",
    title="Lektura i korektura tekstova | Orbita prijevodi",
    desc="Lektura i korektura tekstova i prijevoda: stilska i jezična dorada, pravopis, interpunkcija i tipografija prije objave. Rijeka, Kastav i Zagreb.",
    h1=("Lektura i ", "korektura"),
    lead="Jezična i stilska dorada, da tekst koji izlazi u javnost bude besprijekoran.",
    body=[
      "Orbita nudi i uslugu pregledavanja odnosno lektoriranja tekstova iz raznih područja i na raznim jezicima.",
      "Lektura i korektura podrazumijevaju stilsku i jezičnu obradu teksta te provjeru i ispravljanje tipografskih, interpunkcijskih i pravopisnih pogrešaka, redoslijeda riječi i drugih manjih propusta nastalih pri oblikovanju teksta ili prijevoda.",
      "Preporučujemo da svaki tekst koji izlazi u javnost prije objave pregleda iskusan lektor.",
    ],
    items=["Lektura izvornih tekstova", "Pregled prijevoda", "Korektura prije tiska"],
    faq=[("Koja je razlika između lekture i korekture?", "Lektura dotjeruje jezik i stil teksta, od izbora riječi do rečenične strukture. Korektura je završna provjera pravopisa, interpunkcije i tipografskih pogrešaka, najčešće neposredno prije tiska ili objave."), Q_PRICE, Q_SEND]),
  dict(slug="asistiranje-u-pisanju-teksta", name="Životopisi i motivacijska pisma",
    title="Profesionalno sastavljanje životopisa i motivacijskih pisama | Orbita",
    desc="Pomoć u sastavljanju životopisa (CV) i motivacijskih pisama za posao i stipendije, uz prijevod na strani jezik. Rijeka, Kastav i Zagreb.",
    h1=("Životopisi i ", "motivacijska pisma"),
    lead="Životopis kojim ćete se izdvojiti među prijavama, za posao ili stipendiju, u Hrvatskoj i u inozemstvu.",
    body=[
      "Kao jednu od usluga nudimo profesionalno sastavljanje životopisa (CV) i popratnih motivacijskih pisama, koja se danas uz životopis gotovo neizostavno prilažu prijavama za posao u svim strukama i područjima.",
      "Dobar životopis jedna je od važnih stepenica na putu do željenog posla ili stipendije, osobito u inozemnim tvrtkama i na inozemnim sveučilištima.",
      "Pomoći ćemo Vam odabrati i izraditi životopis savršeno prilagođen Vašem radnom iskustvu, obrazovanju, interesima i ciljevima, a uz to Vam osiguravamo i prijevod na željeni strani jezik.",
    ],
    items=["Životopis (CV)", "Motivacijsko pismo", "Prijevod na strani jezik"],
    faq=[("Možete li životopis i prevesti?", "Da. Uz sastavljanje životopisa i motivacijskog pisma osiguravamo i prijevod na željeni strani jezik."), Q_SEND, Q_WHEN]),
  dict(slug="pisanje-dokumentacije-za-studij-i-zaposlenje-u-inozemstvu", name="Studij i posao u inozemstvu",
    title="Dokumentacija za studij i posao u inozemstvu | Orbita prijevodi",
    desc="Pomoć u pripremi eseja i prijavne dokumentacije za inozemna sveučilišta i poslodavce, uz individualne konzultacije i prijevod. Rijeka, Kastav i Zagreb.",
    h1=("Studij i posao ", "u inozemstvu"),
    lead="Eseji i prijavna dokumentacija za inozemna sveučilišta i poslodavce, uz stručno vodstvo.",
    body=[
      "Visokoobrazovne institucije u Europi i svijetu od budućih studenata traže visoku pismenost. Naši su se stručnjaci i sami školovali u inozemstvu, pa će Vam priprema pisane dokumentacije, poput eseja za upis, uz njihovo vodstvo i individualne konzultacije biti jedan od važnih koraka na putu prema studiju u inozemstvu.",
      "Radna mjesta danas od zaposlenika traže sposobnost obavljanja brojnih i različitih poslova, a profesionalno pisanje jedan je od njihovih neizostavnih dijelova. Naši stručnjaci bit će Vaši osobni mentori u pisanju i u argumentiranom predstavljanju ideja, stavova i zaključaka.",
    ],
    items=["Eseji za upis na sveučilište", "Prijave za stipendije", "Poslovna korespondencija", "Individualne konzultacije"],
    faq=[("Pomažete li i s prijevodom dokumentacije?", "Da. Uz pripremu eseja i prijave možemo prevesti i ovjeriti prateće dokumente, poput svjedodžbi i diploma, koje sveučilišta i poslodavci traže."), Q_SEND, Q_WHEN]),
  dict(slug="pisanje-u-raznim-profesionalnim-podrucjima", name="Stručni tekstovi",
    title="Pisanje stručnih tekstova u raznim područjima | Orbita prijevodi",
    desc="Pisanje stručnih tekstova prilagođenih struci strukturom, nazivljem i stilom, od opisa metodologije do predstavljanja rezultata. Rijeka, Kastav i Zagreb.",
    h1=("Stručni ", "tekstovi"),
    lead="Pisanje prilagođeno struci strukturom, nazivljem i stilom.",
    body=[
      "Okupljamo stručnjake za pisanje svih vrsta tekstova u raznim područjima i strukama, s raznim profesionalnim svrhama, od molbi i prijava do stručnih radova.",
      "Pisanje u različitim područjima poseban je izazov za strukturu teksta, argumentaciju, nazivlje i lekturu. Visoka pismenost traži se i u tehničkim i prirodoslovnim disciplinama, od opisa metodologije istraživanja do predstavljanja rezultata.",
      "Naši stručnjaci bit će Vaši osobni mentori i u području profesionalnog pisanja.",
    ],
    items=["Znanstveni i stručni radovi", "Opis metodologije i rezultata", "Molbe i prijave", "Mentorstvo u pisanju"],
    faq=[Q_SEND, Q_PRICE, Q_WHEN]),
  dict(slug="marketinski-tekstovi", name="Marketinški tekstovi",
    title="Marketinški i reklamni tekstovi | Orbita prijevodi",
    desc="Pisanje i prijevod marketinških tekstova za tisak, radio, televiziju i internet: reklame, brošure, katalozi, pozivnice i cjenici. Rijeka, Kastav i Zagreb.",
    h1=("Marketinški ", "tekstovi"),
    lead="Tekstovi za tisak, radio, televiziju i internet, pisani s pažnjom prema identitetu Vaše tvrtke.",
    body=[
      "Specijalizirani smo za izradu marketinških tekstova u multimedijalnom okruženju. Tekstove stvaramo s osobitom pažnjom prema stilskom identitetu tvrtke i mediju u kojem će biti objavljeni, bilo da je riječ o radiju, televiziji, internetu ili tisku.",
      "Pomoći ćemo Vam da se reklamama, brošurama, katalozima, pozivnicama, cjenicima i drugim promotivnim tekstovima predstavite na nadahnut i jedinstven način.",
      "Poslovnim subjektima pomažemo i u daljnjem predstavljanju na tržištu, od pisanja projekata do reklamnih tekstova.",
    ],
    items=["Reklame", "Brošure i katalozi", "Pozivnice i cjenici", "Tekstovi za mrežne stranice"],
    faq=[("Prevodite li i marketinške tekstove?", "Da. Marketinške tekstove prevodimo i prilagođavamo tako da na stranom jeziku zvuče prirodno i zadrže ton Vaše tvrtke."), Q_SEND, Q_WHEN]),
]

LESSONS_LINK = ("individualne-poduke-stranih-jezika-hrvatskog-jezika-za-strance", "Poduka iz jezika", "Individualna poduka iz engleskog, slovenskog i talijanskog te hrvatskog za strance.")

OFFICES = {
  "rijeka": dict(label="Ured u Rijeci", street="Ćikovići 109", city="51215 Kastav", note="",
    phones=[("+385 98 163 19 30", "+385981631930"), ("+385 51 223 932", "+38551223932")], email="info@orbitaprijevodi.com",
    map="https://www.google.com/maps/search/?api=1&query=%C4%86ikovi%C4%87i+109+Kastav"),
  "zagreb": dict(label="Ured u Zagrebu", street="Martićeva ulica 67", city="10000 Zagreb",
    note="Poslovna zgrada na Kvatrić tržnici, 2. kat (na kojem se nalazi i kafić), staklena vrata preko puta lifta na kojima piše Orbita.",
    phones=[("+385 91 612 6784", "+385916126784"), ("+385 1 2018 053", "+38512018053")], email="zagreb@orbitaprijevodi.com",
    map="https://www.google.com/maps/search/?api=1&query=Marti%C4%87eva+ulica+67+Zagreb"),
}

CITIES = [
  dict(slug="prijevodi-rijeka", office="rijeka", name="Rijeka i Kastav", za="za Rijeku i Kastav", u="u Rijeci i Kastvu", biz="Orbita prijevodi, ured u Rijeci",
    title="Prijevodi i sudski tumači u Rijeci i Kastvu | Orbita prijevodi",
    desc="Ovjereni prijevodi sudskih tumača, pisani i usmeni prijevodi te lektura za Rijeku, Kastav i okolicu. Ured na adresi Ćikovići 109, Kastav. Dokument pošaljite i Viberom ili WhatsAppom.",
    h1=("Prijevodi i sudski tumači ", "u Rijeci i Kastvu"),
    lead="Naš ured za Rijeku i okolicu nalazi se u Kastvu, a dokumente nam možete poslati i bez dolaska, e-poštom, Viberom ili WhatsAppom.",
    body=[
      "Za Rijeku, Kastav, Opatiju i cijelo Primorje izrađujemo ovjerene prijevode sudskih tumača, pisane i usmene prijevode te lekturu, na više od 30 jezika.",
      "Najčešće prevodimo službene dokumente, poput svjedodžbi, diploma, rodnih i vjenčanih listova, radnih dozvola, izvadaka iz sudskog registra i medicinskih nalaza, ali i ugovore, upute i stručne tekstove za tvrtke.",
      f"{PRICE} {AVAILABLE}",
    ]),
  dict(slug="prijevodi-zagreb", office="zagreb", name="Zagreb", za="za Zagreb", u="u Zagrebu", biz="Orbita prijevodi, ured u Zagrebu",
    title="Prijevodi i sudski tumači u Zagrebu | Orbita prijevodi",
    desc="Ovjereni prijevodi sudskih tumača, pisani i usmeni prijevodi te lektura u Zagrebu. Ured u Martićevoj ulici 67, na Kvatrić tržnici. Dokument pošaljite i Viberom ili WhatsAppom.",
    h1=("Prijevodi i sudski tumači ", "u Zagrebu"),
    lead="Naš zagrebački ured nalazi se u Martićevoj ulici 67, na Kvatrić tržnici, a dokumente nam možete poslati i bez dolaska, e-poštom, Viberom ili WhatsAppom.",
    body=[
      "U Zagrebu izrađujemo ovjerene prijevode sudskih tumača, pisane i usmene prijevode te lekturu, na više od 30 jezika, za građane i za poslovne subjekte.",
      "Najčešće prevodimo službene dokumente, poput svjedodžbi, diploma, rodnih i vjenčanih listova, radnih dozvola, izvadaka iz sudskog registra i medicinskih nalaza, ali i ugovore, upute i stručne tekstove za tvrtke.",
      f"{PRICE} {AVAILABLE}",
    ]),
]

ALL_FAQ = [Q_CERT, Q_SEND, Q_PRICE, Q_LANG, Q_WHEN,
  ("Trebam li donijeti original dokumenta?", SERVICES[0]["faq"][1][1]),
  ("Koliko traje prijevod?", "Rok ovisi o opsegu i vrsti teksta te o jeziku. Napišite nam do kada Vam prijevod treba, a u ponudi ćemo navesti rok koji Vam možemo jamčiti. Dogovorenih rokova se pridržavamo i kada su vrlo kratki."),
  ("Mogu li dokument predati osobno?", "Možete, u našem uredu u Kastvu (Ćikovići 109) ili u Zagrebu (Martićeva ulica 67, na Kvatrić tržnici). Za ponudu nije potrebno dolaziti, dovoljno je poslati fotografiju ili sken dokumenta."),
  SERVICES[2]["faq"][0], SERVICES[3]["faq"][0]]

e = html.escape

def head(title, desc, path, ld):
    return f'''<!doctype html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}/{path}">
<link rel="icon" sizes="32x32" href="../assets/favicon-32x32.jpg">
<link rel="icon" sizes="192x192" href="../assets/favicon-192x192.jpg">
<link rel="apple-touch-icon" href="../assets/favicon-180x180.jpg">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:image" content="{SITE}/assets/hero-desk.jpg">
<meta property="og:locale" content="hr_HR">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&family=DM+Sans:wght@400;500&family=DM+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css?v={V}">
</head>
<body class="subpage">
'''

NAV = '''<header class="nav" id="nav">
  <a class="brand" href="../" aria-label="Orbita prijevodi, početna">
    <img src="../assets/orbita-logo.webp" alt="Orbita" width="473" height="108">
  </a>
  <nav class="nav-links" id="navLinks">
    <a href="../usluge/">Usluge</a>
    <a href="../#jezici">Jezici</a>
    <a href="../cesta-pitanja/">Česta pitanja</a>
    <a href="../#o-nama">O nama</a>
    <a href="../kontakt/">Kontakt</a>
  </nav>
  <a class="pill pill-ink nav-cta" href="../#ponuda">Zatražite ponudu</a>
  <button class="burger" id="burger" aria-label="Izbornik" aria-expanded="false"><span></span><span></span></button>
</header>
'''

def page_hero(crumbs, h1, lead, extra=""):
    trail = ' <span>/</span> '.join(f'<a href="{href}">{e(t)}</a>' if href else f'<span aria-current="page">{e(t)}</span>' for t, href in crumbs)
    return f'''<section class="hero page-hero">
    <div class="hero-bg" aria-hidden="true"></div>
    <div class="hero-text">
      <nav class="crumbs" aria-label="Putanja">{trail}</nav>
      <h1>{e(h1[0])}<em>{e(h1[1])}</em></h1>
      <p class="lead">{e(lead)}</p>
      <div class="hero-cta">
        <a class="pill pill-ink" href="../#ponuda">Zatražite ponudu</a>
        <a class="pill pill-line" href="https://wa.me/{PHONES[0][2]}?text={WA_TEXT}" target="_blank" rel="noopener">Pošaljite dokument na WhatsApp</a>
      </div>{extra}
    </div>
  </section>
'''

def contact_rows():
    rows = ''.join(f'''
          <div class="contact-row">
            <p><span>{c}</span>{d}</p>
            <div>
              <a class="pill pill-msg" href="https://wa.me/{n}?text={WA_TEXT}" target="_blank" rel="noopener">WhatsApp</a>
              <a class="pill pill-msg" href="viber://chat?number=%2B{n}">Viber</a>
              <a class="pill pill-cream" href="tel:+{n}">Nazovite</a>
            </div>
          </div>''' for c, d, n in PHONES)
    return f'<div class="quick">{rows}\n        </div>'

def cta_band():
    return f'''<section class="section dark">
    <div class="offer">
      <div class="offer-intro">
        <p class="label">Ponuda</p>
        <h2>Pošaljite dokument, a mi šaljemo ponudu.</h2>
        <p class="sub">{e(PRICE)} {e(SEND_PHOTO)}</p>
        <p class="sub">{e(AVAILABLE)}</p>
      </div>
      <div>
        {contact_rows()}
        <p class="cta-more"><a class="pill pill-accent" href="../#ponuda">Ispunite upit za ponudu</a></p>
      </div>
    </div>
  </section>
'''

def faq_block(items, title="Česta pitanja"):
    qs = ''.join(f'''
      <details class="faq-item"><summary>{e(q)}</summary><p>{e(a)}</p></details>''' for q, a in items)
    return f'''<section class="section">
    <div class="section-head"><p class="label">Pitanja</p><h2>{e(title)}</h2></div>
    <div class="faq">{qs}
    </div>
  </section>
'''

def office_card(key):
    o = OFFICES[key]
    note = f'\n        <p class="office-note">{e(o["note"])}</p>' if o["note"] else ""
    phones = ''.join(f'<li><a href="tel:{t}">{d}</a></li>' for d, t in o["phones"])
    return f'''<article class="office">
        <p class="label">{o["label"]}</p>
        <h3>{o["street"]}<br>{o["city"]}</h3>{note}
        <ul>{phones}<li><a href="mailto:{o["email"]}">{o["email"]}</a></li></ul>
        <a class="pill pill-line" target="_blank" rel="noopener" href="{o["map"]}"><svg class="pin" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.800 7 12 7 12Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6" fill="currentColor"/></svg>Otvorite kartu</a>
      </article>'''

def related(exclude=None, title="Ostale usluge"):
    links = ''.join(f'<li><a href="../{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES if s["slug"] != exclude) + f'<li><a href="../{LESSONS_LINK[0]}/">{LESSONS_LINK[1]}</a></li>'
    return f'''<section class="section">
    <div class="section-head"><p class="label">Usluge</p><h2>{title}</h2></div>
    <ul class="related">{links}</ul>
  </section>
'''

def footer():
    svc = ''.join(f'<li><a href="../{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES) + f'<li><a href="../{LESSONS_LINK[0]}/">{LESSONS_LINK[1]}</a></li>'
    return f'''<footer class="footer">
  <div class="footer-top">
    <a class="brand" href="../"><img src="../assets/orbita-logo.webp" alt="Orbita" width="473" height="108"></a>
    <p>Riječima povezujemo svjetove.</p>
  </div>
  <div class="footer-links">
    <div><p class="label">Usluge</p><ul>{svc}</ul></div>
    <div><p class="label">Gradovi</p><ul><li><a href="../prijevodi-rijeka/">Prijevodi Rijeka i Kastav</a></li><li><a href="../prijevodi-zagreb/">Prijevodi Zagreb</a></li></ul></div>
    <div><p class="label">Orbita</p><ul><li><a href="../cesta-pitanja/">Česta pitanja</a></li><li><a href="../kontakt/">Kontakt</a></li><li><a href="../#o-nama">O nama</a></li><li><a href="../#ponuda">Zatražite ponudu</a></li></ul></div>
  </div>
  <div class="footer-bottom">
    <span>© <span id="year"></span> Orbita prijevodi</span>
    <nav><a href="../usluge/">Usluge</a><a href="../cesta-pitanja/">Česta pitanja</a><a href="../kontakt/">Kontakt</a></nav>
  </div>
</footer>
<script src="../page.js?v={V}"></script>
</body>
</html>
'''

def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}/{p}"} for i, (n, p) in enumerate(items)]}

def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def write(path, content):
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(content)

pages = []

for s in SERVICES:
    path = f'{s["slug"]}/'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": s["name"], "serviceType": s["name"], "description": s["desc"], "areaServed": ["Rijeka", "Kastav", "Zagreb", "Hrvatska"],
         "provider": {"@type": "ProfessionalService", "name": "Orbita prijevodi", "url": SITE + "/", "telephone": "+385981631930"}},
        crumbs_ld([("Početna", ""), ("Usluge", "usluge/"), (s["name"], path)]), faq_ld(s["faq"])]}
    paras = ''.join(f'<p>{e(p)}</p>' for p in s["body"])
    items = ''.join(f'<li>{e(i)}</li>' for i in s["items"])
    body = f'''<section class="section">
    <div class="page-body">
      <div class="prose">
        <p class="label">O usluzi</p>
        <h2>{e(s["name"])}</h2>
        {paras}
        <p>{e(PRICE)}</p>
      </div>
      <aside class="page-aside">
        <p class="label">Što obuhvaća</p>
        <ul class="chips-list">{items}</ul>
        <p class="aside-note">{e(SEND_PHOTO)}</p>
        <a class="pill pill-ink" href="../#ponuda" data-svc="{e(s["name"])}">Zatražite ponudu</a>
      </aside>
    </div>
  </section>
'''
    html_out = head(s["title"], s["desc"], path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), ("Usluge", "../usluge/"), (s["name"], None)], s["h1"], s["lead"]) + '  ' + body + '  ' + faq_block(s["faq"]) + '  ' + cta_band() + '  ' + related(s["slug"]) + '</main>\n' + footer()
    write(s["slug"], html_out); pages.append(path)

for c in CITIES:
    path = f'{c["slug"]}/'
    o = OFFICES[c["office"]]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ProfessionalService", "name": c["biz"], "url": SITE + "/" + path,
         "telephone": o["phones"][0][1], "email": o["email"],
         "address": {"@type": "PostalAddress", "streetAddress": o["street"], "addressLocality": o["city"].split(" ", 1)[1], "postalCode": o["city"].split(" ", 1)[0], "addressCountry": "HR"},
         "contactPoint": {"@type": "ContactPoint", "telephone": o["phones"][0][1], "contactType": "customer service", "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}}},
        crumbs_ld([("Početna", ""), (c["name"], path)]), faq_ld(ALL_FAQ[:5])]}
    paras = ''.join(f'<p>{e(p)}</p>' for p in c["body"])
    svc_links = ''.join(f'<li><a href="../{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    body = f'''<section class="section">
    <div class="page-body">
      <div class="prose">
        <p class="label">{e(c["name"])}</p>
        <h2>Prevoditeljska agencija {e(c["za"])}</h2>
        {paras}
        <p>{e(SEND_PHOTO)}</p>
      </div>
      <aside class="page-aside page-aside-office">
        {office_card(c["office"])}
      </aside>
    </div>
  </section>
  <section class="section">
    <div class="section-head"><p class="label">Usluge</p><h2>Naše usluge {e(c["u"])}</h2></div>
    <ul class="related">{svc_links}</ul>
  </section>
'''
    html_out = head(c["title"], c["desc"], path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), (c["name"], None)], c["h1"], c["lead"]) + '  ' + body + '  ' + faq_block(ALL_FAQ[:5]) + '  ' + cta_band() + '</main>\n' + footer()
    write(c["slug"], html_out); pages.append(path)

# FAQ page
path = "cesta-pitanja/"
ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Česta pitanja", path)]), faq_ld(ALL_FAQ)]}
html_out = head("Česta pitanja o prijevodima i ovjerenim prijevodima | Orbita prijevodi", "Odgovori na najčešća pitanja: što je ovjereni prijevod, kako poslati dokument, kako se obračunava cijena, koliko traje prijevod i na koje jezike prevodimo.", path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), ("Česta pitanja", None)], ("Česta ", "pitanja"), "Sve što Vas najčešće zanima o prijevodima, ovjerenim prijevodima, cijeni i slanju dokumenata.") + '  ' + faq_block(ALL_FAQ, "Odgovori na Vaša pitanja") + '  ' + cta_band() + '  ' + related(None, "Naše usluge") + '</main>\n' + footer()
write("cesta-pitanja", html_out); pages.append(path)

# Services overview
path = "usluge/"
cards = ''.join(f'''<a class="svc-card" href="../{s["slug"]}/"><h3>{e(s["name"])}</h3><p>{e(s["lead"])}</p><span>Saznajte više</span></a>''' for s in SERVICES) + f'''<a class="svc-card" href="../{LESSONS_LINK[0]}/"><h3>{LESSONS_LINK[1]}</h3><p>{LESSONS_LINK[2]}</p><span>Saznajte više</span></a>'''
ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Usluge", path)])]}
html_out = head("Usluge: ovjereni, pisani i usmeni prijevodi, lektura | Orbita prijevodi", "Ovjereni prijevodi sudskih tumača, pisani i usmeni prijevodi, lektura, životopisi, dokumentacija za studij u inozemstvu, stručni i marketinški tekstovi. Rijeka, Kastav i Zagreb.", path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), ("Usluge", None)], ("Naše ", "usluge"), "Sve što Vašem tekstu treba, od prijevoda do objave.") + f'''  <section class="section">
    <div class="svc-cards">{cards}</div>
  </section>
  ''' + cta_band() + '</main>\n' + footer()
write("usluge", html_out); pages.append(path)

# Contact
path = "kontakt/"
ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Kontakt", path)])]}
html_out = head("Kontakt | Orbita prijevodi, Kastav i Zagreb", "Uredi Orbita prijevoda u Kastvu (Ćikovići 109) i Zagrebu (Martićeva ulica 67). Telefon, e-pošta, Viber i WhatsApp. Dostupni smo stalno.", path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), ("Kontakt", None)], ("Dva ureda, ", "jedan tim"), AVAILABLE) + f'''  <section class="section">
    <div class="offices">
      {office_card("rijeka")}
      {office_card("zagreb")}
    </div>
  </section>
  ''' + cta_band() + '</main>\n' + footer()
write("kontakt", html_out); pages.append(path)

# Old addresses that now live elsewhere: send people (and Google) to the right place
REDIRECTS = {"o-nama": "../#o-nama", "blog": "../", "novosti": "../"}
for slug, target in REDIRECTS.items():
    final = SITE + "/" + (target.replace("../", "") or "")
    write(slug, f'''<!doctype html><html lang="hr"><head><meta charset="utf-8"><title>Orbita prijevodi</title>
<link rel="canonical" href="{final}"><meta http-equiv="refresh" content="0; url={target}"><meta name="robots" content="noindex"></head>
<body><p><a href="{target}">Orbita prijevodi</a></p></body></html>
''')

exec(open("landing_pages.py").read())

# Sitemap for Google
urls = [""] + pages
with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        f.write(f"  <url><loc>{SITE}/{u}</loc></url>\n")
    f.write("</urlset>\n")
with open("robots.txt", "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print("built", len(pages), "pages")
