"""Builds the separate pages (services, cities, FAQ, contact) and sitemap.xml.

Each page lives in its own folder (e.g. ovjereni-prijevodi/index.html) so the
addresses match the old WordPress site and keep what Google already knows.
Run:  python3 build_pages.py
"""
import json, os, html, re
from urllib.parse import quote

SITE = "https://www.orbitaprijevodi.com"
V = "65"  # bump together with ?v= in index.html

BLOG_NAV = '\n    <a href="../blog/">Blog</a>'
BLOG_LI = '<li><a href="../blog/">Blog</a></li>'

PHONES = [("Rijeka", "098 163 19 30", "385981631930"), ("Zagreb", "091 612 6784", "385916126784")]
WA_TEXT = quote("Poštovani, šaljem fotografije dokumenta za ponudu prijevoda.")
AVAILABLE = "U vezi s prijevodima i ostalim našim uslugama možete s nama stupiti u kontakt u bilo koje doba pozivom ili slanjem SMS, Viber ili WhatsApp poruke ili e-pošte."
PRICE = "Cijena se obračunava po kartici teksta, a točan iznos dobit ćete u neobvezujućoj ponudi čim izvršimo uvid u dokument."
SEND_PHOTO = "Dokument možete skenirati ili fotografirati mobitelom. Ako ga fotografirate, položite ga na ravnu površinu i fotografirajte odozgo, pazeći da fotografija bude oštra i da sav tekst bude jasno vidljiv (čitljiv)."

# Questions that fit on almost every page
Q_SEND = ("Kako Vam mogu poslati dokument?", f"E-poštom na info@orbitaprijevodi.com ili na zagreb@orbitaprijevodi.com, putem obrasca na stranici, Viberom ili WhatsAppom na 098 163 19 30 ili 091 612 6784, ili ga možete donijeti osobno u jedan od naših ureda. {SEND_PHOTO}")
Q_PRICE = ("Kako se obračunava cijena?", "Cijena (ovjerenog) pisanog prijevoda obračunava se po kartici teksta, a točan iznos dobit ćete u neobvezujućoj ponudi čim izvršimo uvid u dokument. Cijena usmenog prevođenja obračunava se za svaki započeti sat, a tome se pridodaje i cijena tehničke opreme, ako je klijent zatraži. Ostale usluge obračunavaju se personalizirano, ovisno o potrebama svakog klijenta.")
Q_LANG = ("Na koje jezike prevodite?", "Prevodimo s/na više od 30 jezika, od engleskog, njemačkog, talijanskog i slovenskog do japanskog, kineskog i arapskog. Ako sudskog tumača, odnosno prevoditelja nema u Republici Hrvatskoj, osigurat ćemo ga u inozemstvu.")
Q_WHEN = ("Kada ste dostupni?", "Slobodno nas u bilo koje doba kontaktirajte u vezi s prijevodom ili nam pošaljite poruku (SMS, Viber, WhatsApp) ili e-poštu: na info@orbitaprijevodi.com ili zagreb@orbitaprijevodi.com, putem obrasca na stranici, ili Viberom i WhatsAppom na 098 163 19 30 ili 091 612 6784.")
Q_CERT = ("Što je ovjereni prijevod?", "Ovjereni prijevod izrađuje sudski tumač, osoba s diplomom, izvrsnim poznavanjem stranog jezika i položenim ispitom za sudskog tumača, koju imenuje ministar nadležan za poslove pravosuđa u Republici Hrvatskoj. Prijevod se uvezuje s izvornim dokumentom ili njegovom (ovjerenom) preslikom, a tumač pečatom i potpisom jamči da je istovjetan izvorniku.")
Q_ORIGINAL = ("Trebam li donijeti original dokumenta?", "Za ponudu je dovoljna jasna fotografija ili sken dokumenta. Prijevod se zatim uvezuje s originalom, ovjerenom ili običnom preslikom, ovisno o tome što traži institucija kojoj ga predajete.")

SERVICES = [
  dict(slug="ovjereni-prijevodi", name="Ovjereni prijevodi",
    title="Ovjereni prijevodi sudskih tumača | Rijeka, Kastav i Zagreb",
    desc="Ovjereni prijevodi svjedodžbi, diploma, rodnih i vjenčanih listova, izvadaka iz sudskog registra i medicinskih nalaza. Sudski tumači za više od 30 jezika, uredi u Rijeci i Zagrebu.",
    h1=("Ovjereni prijevodi ", "sudskih tumača"),
    lead="Službene dokumente za Vas brzo i uredno pripremaju naši provjereni sudski tumači, uz pečat i potpis koje priznaju sudovi, javni bilježnici i institucije.",
    body=[
      "Ovjereni prijevodi posebna su vrsta prijevoda koje izrađuju sudski tumači. To su osobe s diplomom i iznimnim poznavanjem stranog jezika, s položenim ispitom za sudskog tumača, koje rješenjem imenuje ministar nadležan za poslove pravosuđa u Republici Hrvatskoj.",
      "Ovjereni prijevod uvezuje se s originalom, ovjerenom ili običnom preslikom izvornog dokumenta, a sudski tumač pečatom i potpisom jamči da je prevedeni tekst istovjetan izvorniku.",
      "Ovjerene prijevode svih vrsta dokumenata za Vas pripremaju naši provjereni sudski tumači, koji iza sebe imaju bogato iskustvo s najrazličitijim vrstama ovjerenih prijevoda.",
    ],
    items=["Svjedodžbe i diplome", "Rodni i vjenčani listovi", "Radne dozvole", "Izvadci iz sudskog registra", "Stručna i vještačka mišljenja", "Medicinski nalazi"],
    faq=[Q_CERT, Q_ORIGINAL, Q_PRICE, Q_SEND, Q_LANG]),
  dict(slug="pisani-prijevodi", name="Pisani prijevodi",
    title="Pisani prijevodi općih i stručnih tekstova | Orbita prijevodi",
    desc="Prijevodi općih i stručnih tekstova, korisničkih uputa, internetskih stranica, programske opreme, titlova i rukopisa na više od 30 jezika. Rijeka, Kastav i Zagreb.",
    h1=("Pisani ", "prijevodi"),
    lead="Opći i stručni tekstovi iz svih područja, prevedeni tako da se čitaju kao da su izvorno napisani na tom jeziku.",
    body=[
      "Unaprijedite svoje poslovanje vrhunskim prijevodom! Povjerite nam opće i stručne tekstove, rukopise, titlove i digitalne sadržaje, uključujući internetske stranice i programsku opremu.",
      "Stručni prijevodi sadrže nazivlje koje zahtijeva poznavanje predmetnog područja i namijenjeni su čitateljima iz te struke. Surađujemo sa stručnjacima iz širokog polja tehničkih i društvenih znanosti, a pri narudžbi vrlo stručnih prijevoda poželjno je da naručitelj osigura pomoćnu literaturu ili odredi svog stručnjaka za savjete u vezi s nazivljem.",
      "Za engleski i talijanski jezik nudimo i prevođenje u CAT alatima, koji osiguravaju dosljedno nazivlje u većim i ponavljajućim projektima.",
    ],
    items=["Stručni i tehnički tekstovi", "Korisničke upute i jamstveni listovi", "Medicinska dokumentacija", "Internetske stranice", "Programska oprema", "Titlovi", "Rukopisi"],
    faq=[Q_PRICE, Q_SEND, Q_LANG, Q_WHEN]),
  dict(slug="usmeni-prijevodi", name="Usmeno prevođenje",
    title="Usmeno prevođenje: simultano, konsekutivno, šaptano | Orbita",
    desc="Simultano, konsekutivno i šaptano prevođenje na sastancima, konferencijama i sajmovima, te sudski tumač kod javnog bilježnika ili na sudu. Rijeka i Zagreb.",
    h1=("Usmeno ", "prevođenje"),
    lead="Od poslovnih sastanaka do međunarodnih konferencija – simultanim, konsekutivnim i šaptanim prevođenjem osiguravamo jasno i učinkovito sporazumijevanje.",
    body=[
      "Tražite li prevoditelje za simultano ili konsekutivno prevođenje, možda i za više jezika u istom danu? Trebate li sudskog tumača za tumačenje kod javnog bilježnika ili na sudu, ili nešto posebno, poput prevođenja uz pratnju?",
      "Usmeno prevođenje iznimno je zahtjevno i mogu ga obavljati samo specijalizirane osobe s velikim iskustvom i iznimnim poznavanjem jezika.",
      "Prijevod izgovorene riječi na Vašim poslovnim sastancima, seminarima, simpozijima, međunarodnim i tiskovnim konferencijama, prezentacijama, sajmovima, sjednicama nadzornih odbora, pregovorima, državnim protokolima ili godišnjim skupštinama prepustite našim usmenim prevoditeljima.",
      "Treba Vam i oprema i stručni tim koji će je postaviti u Vašem prostoru? Nema problema!",
    ],
    price="Cijena se obračunava po svakom započetom satu prevođenja, a konačnu ponudu, kojoj možemo dodati i osiguravanje cjelokupne potrebne tehničke opreme, pripremamo nakon što se upoznamo s Vašim potrebama i zahtjevima.", photo=False,
    items=["Konferencije i seminari", "Poslovni sastanci i pregovori", "Sajmovi i prezentacije", "Sjednice i godišnje skupštine", "Javni bilježnik i sud", "Prevođenje uz pratnju"],
    faq=[("Koja je razlika između simultanog i konsekutivnog prevođenja?", "Kod *simultanog prevođenja* prevoditelj prenosi poruku na drugi jezik gotovo istodobno s govornikom, najčešće iz prevoditeljske kabine uz pomoć posebne opreme. Ova vrsta prevođenja idealna je za konferencije, kongrese i veća međunarodna događanja.\n\nKod *konsekutivnog prevođenja* govornik izlaže dio po dio, a prevoditelj prenosi njegove riječi tijekom stanki. Takav način prevođenja osobito je prikladan za poslovne sastanke, pregovore i postupke pred javnim bilježnikom.\n\n*Šaptano prevođenje* posebna je vrsta simultanog prevođenja pri kojoj prevoditelj tihim glasom prevodi izravno jednoj ili dvjema osobama, bez potrebe za posebnom opremom."), ("Kako rezervirati prevoditelja?", f"Javite nam datum, mjesto, trajanje, jezike i vrstu događaja, a mi ćemo Vam poslati ponudu. {AVAILABLE}"), Q_LANG]),
  dict(slug="lektoriranje", name="Lektura i korektura",
    title="Lektura i korektura tekstova | Orbita prijevodi",
    desc="Lektura i korektura tekstova i prijevoda: stilska i jezična dorada, pravopis, interpunkcija i tipografija prije objave. Rijeka, Kastav i Zagreb.",
    h1=("Lektura i ", "korektura"),
    lead="Vašim tekstovima dajemo završni sjaj, kako bi tekst koji izlazi u javnost bio jezično besprijekoran i stilski dotjeran.",
    body=[
      "Orbita nudi i uslugu pregledavanja odnosno lektoriranja tekstova iz raznih područja i na raznim jezicima.",
      "Lektura i korektura podrazumijevaju stilsku i jezičnu obradu teksta te provjeru i ispravljanje tipografskih, interpunkcijskih i pravopisnih pogrešaka, redoslijeda riječi i drugih manjih propusta nastalih pri oblikovanju teksta ili prijevoda.",
      "Preporučujemo da svaki tekst koji izlazi u javnost prije objave pregleda iskusan lektor.",
      "Također vršimo hitne lekture završnih, diplomskih i doktorskih radova uz priloženu službenu potvrdu o obavljenoj lekturi stručne osobe koju zahtijevaju visoka učilišta u Republici Hrvatskoj.",
    ],
    items=["Lektura izvornih tekstova", "Pregled prijevoda", "Korektura prije tiska"],
    faq=[("Koja je razlika između lekture i korekture?", "*Lektura* obuhvaća jezično i stilsko dotjerivanje teksta kako bi bio jasan, tečan i izražajno ujednačen. Pritom se posebna pozornost posvećuje izboru riječi, oblikovanju rečenica te gramatičkoj i pravopisnoj ispravnosti.\n\n*Korektura* je završna provjera teksta kojom se uklanjaju preostale pravopisne, interpunkcijske i tipografske pogreške, najčešće neposredno prije tiska ili objave."), Q_PRICE, Q_SEND]),
  dict(slug="asistiranje-u-pisanju-teksta", name="Životopisi i motivacijska pisma",
    title="Profesionalno sastavljanje životopisa i motivacijskih pisama | Orbita",
    desc="Pomoć u sastavljanju životopisa (CV) i motivacijskih pisama za posao i stipendije, uz prijevod na strani jezik. Rijeka, Kastav i Zagreb.",
    h1=("Životopisi i ", "motivacijska pisma"),
    lead="Životopis kojim ćete se izdvojiti među prijavama, za posao ili stipendiju, u Hrvatskoj i u inozemstvu.",
    body=[
      "Kao jednu od usluga nudimo i profesionalno sastavljanje životopisa (CV) i popratnih motivacijskih pisama, koja se danas uz životopis gotovo neizostavno prilažu prijavama za posao u svim strukama i područjima.",
      "Dobar životopis jedna je od važnih stepenica na putu do željenog posla ili stipendije, osobito u inozemstvu.",
      "Pomoći ćemo Vam odabrati i izraditi životopis savršeno prilagođen Vašem radnom iskustvu, obrazovanju, interesima i ciljevima, a uz to Vam osiguravamo i prijevod na željeni strani jezik.",
      "U čitavom procesu izrade životopisa i motivacijskih pisama te njihova prevođenja sudjeluju stručnjaci lingvisti specijalizirani u području akademskog i profesionalnog pisanja, pri čemu se prijevodi također izrađuju, lektoriraju i usklađuju terminološki u području akademskog pisanja, kako biste na kraju dobili kvalitetnu uslugu.",
      "Potrebno je poslati kopije potvrda o školovanju, popis poslova i radnih mjesta i osobne podatke (kontakt podaci, hobiji, vještine, interesi i sl.) na naš e-mail: info@orbitaprijevodi.com.",
      "Također trebate javiti na kojem jeziku Vam je potreban životopis (hrvatski i/ili želite li izradu/prijevod na neki jezik).",
    ],
    price=None, photo=False,
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
    price="Cjenovna ponuda priprema se nakon izvršenog detaljnog uvida u Vaše specifične potrebe.", photo=False,
    items=["Znanstveni i stručni radovi", "Opis metodologije i rezultata", "Molbe i prijave", "Mentorstvo u pisanju"],
    faq=[Q_SEND, Q_PRICE, Q_WHEN]),
  dict(slug="marketinski-tekstovi", name="Marketinški tekstovi",
    title="Marketinški i reklamni tekstovi | Orbita prijevodi",
    desc="Pisanje i prijevod marketinških tekstova za tisak, radio, televiziju i internet: reklame, brošure, katalozi, pozivnice i cjenici. Rijeka, Kastav i Zagreb.",
    h1=("Marketinški ", "tekstovi"),
    lead="Riječi koje privlače. Poruke koje se pamte. Tekstovi za sve medije, osmišljeni po Vašoj mjeri.",
    body=[
      "Specijalizirani smo za izradu marketinških tekstova u multimedijalnom okruženju. Tekstove stvaramo s osobitom pažnjom prema stilskom identitetu poslovnog subjekta i mediju u kojem će biti objavljeni, bilo da je riječ o radiju, televiziji, internetu ili tisku.",
      "Pomoći ćemo Vam da u reklamama, brošurama, katalozima, pozivnicama, cjenicima i drugim promotivnim tekstovima zablistate i predstavite se na nadahnut i jedinstven način.",
      "Poslovnim subjektima pomažemo i u daljnjem predstavljanju na tržištu, od pisanja projekata do reklamnih tekstova.",
    ],
    price="Cjenovna ponuda je personalizirana i prilagođena Vašim specifičnim potrebama.", photo=False,
    items=["Reklame", "Brošure i katalozi", "Pozivnice i cjenici", "Tekstovi za mrežne stranice"],
    faq=[("Prevodite li i marketinške tekstove?", "Da. Marketinške tekstove prevodimo i prilagođavamo tako da na stranom jeziku zvuče prirodno i zadrže ton Vaše tvrtke."), Q_SEND, Q_WHEN]),
]

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
      "Nudimo ovjerene prijevode sudskih tumača, obične pisane prijevode, sve vrste usmenog prevođenja te lekturu, s/na više od 30 jezika.",
      "Najčešće prevodimo službene dokumente, poput svjedodžbi, diploma, rodnih i vjenčanih listova, radnih dozvola, izvadaka iz sudskog registra i medicinskih nalaza, ali i ugovore, upute i stručne tekstove za poslovne subjekte.",
      "Cijena se obračunava po kartici teksta, a točan iznos dobit ćete u neobvezujućoj ponudi čim izvršimo uvid u dokument(e). U vezi s prijevodom možete u bilo koje doba stupiti s nama u kontakt telefonski ili nam poslati poruku (SMS, Viber, WhatsApp) ili e-poštu.",
      SEND_PHOTO,
      "Ako se ne nalazite u Rijeci ili bližoj okolici, odnosno ne planirate dolazak u Rijeku, sve možemo obaviti putem pošte.",
      "Ako je potreban uvez prijevoda s originalom, možete nam ga poslati običnom poštom na našu adresu, u protivnom možemo prijevod uvezati i s elektroničkom verzijom dokumenta, odnosno s kopijom te uvezani ovjereni prijevod poslati na Vašu adresu.",
    ]),
  dict(slug="prijevodi-zagreb", office="zagreb", name="Zagreb", za="za Zagreb", u="u Zagrebu", biz="Orbita prijevodi, ured u Zagrebu",
    title="Prijevodi i sudski tumači u Zagrebu | Orbita prijevodi",
    desc="Ovjereni prijevodi sudskih tumača, pisani i usmeni prijevodi te lektura u Zagrebu. Ured u Martićevoj ulici 67, na Kvatrić tržnici. Dokument pošaljite i Viberom ili WhatsAppom.",
    h1=("Prijevodi i sudski tumači ", "u Zagrebu"),
    lead="Naš zagrebački ured nalazi se u Martićevoj ulici 67, na Kvatrić tržnici, a dokumente nam možete poslati i bez dolaska, e-poštom, Viberom ili WhatsAppom.",
    body=[
      "Nudimo ovjerene prijevode sudskih tumača, obične pisane prijevode, sve vrste usmenog prevođenja te lekturu, s/na više od 30 jezika.",
      "Najčešće prevodimo službene dokumente, poput svjedodžbi, diploma, rodnih i vjenčanih listova, radnih dozvola, izvadaka iz sudskog registra i medicinskih nalaza, ali i ugovore, upute i stručne tekstove za poslovne subjekte.",
      "Cijena se obračunava po kartici teksta, a točan iznos dobit ćete u neobvezujućoj ponudi čim izvršimo uvid u dokument(e). U vezi s prijevodom možete u bilo koje doba stupiti s nama u kontakt telefonski ili nam poslati poruku (SMS, Viber, WhatsApp) ili e-poštu.",
      SEND_PHOTO,
      "Ako se ne nalazite u Zagrebu ili bližoj okolici, odnosno ne planirate dolazak u Zagreb, sve možemo obaviti putem pošte.",
      "Ako je potreban uvez prijevoda s originalom, možete nam ga poslati običnom poštom na našu adresu, u protivnom možemo prijevod uvezati i s elektroničkom verzijom dokumenta, odnosno s kopijom te uvezani ovjereni prijevod poslati na Vašu adresu.",
    ]),
]

ALL_FAQ = [Q_CERT, Q_SEND, Q_PRICE, Q_LANG, Q_WHEN,
  Q_ORIGINAL,
  ("Koliko traje prijevod?", "U mogućnosti smo dostaviti veće količine prijevoda u vrlo kratkom roku."),
  ("Mogu li dokument predati osobno?", "Možete, u našem uredu u Kastvu (Ćikovići 109) ili u Zagrebu (Martićeva ulica 67, na Kvatrić tržnici). Za ponudu nije potrebno dolaziti, dovoljno je poslati fotografiju ili sken dokumenta."),
  SERVICES[2]["faq"][0], SERVICES[3]["faq"][0]]

e = html.escape

# Body text: Viber, WhatsApp, phone numbers and e-mail addresses become links; *word* is emphasis
MAIN_NO = PHONES[0][2]
LINKS = re.compile(r"\*([^*]+)\*|([\w.]+@orbitaprijevodi\.com)|(098 163 19 30|091 612 6784)|\b(Viber(?:om|a)?)\b|\b(WhatsApp(?:om|a)?)\b")
def rich(t):
    def rep(m):
        star, mail, tel, viber, wa = m.groups()
        if star: return f"<strong>{e(star)}</strong>"
        if mail: return f'<a href="mailto:{mail}">{mail}</a>'
        if tel: return f'<a href="tel:+385{tel.replace(" ", "")[1:]}">{tel}</a>'
        if viber: return f'<a href="viber://chat?number=%2B{MAIN_NO}">{viber}</a>'
        return f'<a href="https://wa.me/{MAIN_NO}" target="_blank" rel="noopener">{wa}</a>'
    out, last = [], 0
    for m in LINKS.finditer(t):
        out.append(e(t[last:m.start()])); out.append(rep(m)); last = m.end()
    return "".join(out) + e(t[last:])
def plain(t):
    return t.replace("*", "")
def paras(t):
    return "".join(f"<p>{rich(p)}</p>" for p in t.split("\n\n"))

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

NAV = f'''<header class="nav" id="nav">
  <a class="brand" href="../" aria-label="Orbita prijevodi, početna">
    <img src="../assets/orbita-logo.webp" alt="Orbita" width="473" height="108">
  </a>
  <nav class="nav-links" id="navLinks">
    <a href="../usluge/">Usluge</a>
    <a href="../#jezici">Jezici</a>
    <a href="../cesta-pitanja/">Česta pitanja</a>{BLOG_NAV}
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

def cta_band(price=PRICE, photo=True):
    first = " ".join(rich(t) for t in (price, SEND_PHOTO if photo else "") if t)
    first_p = f'<p class="sub">{first}</p>' if first else ""
    return f'''<section class="section dark">
    <div class="offer">
      <div class="offer-intro">
        <p class="label">Ponuda</p>
        <h2>Pošaljite dokument, a mi šaljemo ponudu.</h2>
        {first_p}
        <p class="sub">{rich(AVAILABLE)}</p>
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
      <details class="faq-item"><summary>{e(q)}</summary>{paras(a)}</details>''' for q, a in items)
    return f'''<section class="section">
    <div class="section-head"><p class="label">Pitanja</p><h2>{e(title)}</h2></div>
    <div class="faq">{qs}
    </div>
  </section>
'''

# Quote form that sends the message and the documents straight to both offices (send.php on the host)
def form_html(service, action):
    return f'''<form class="form send-form" action="{action}" method="post" enctype="multipart/form-data" novalidate>
        <input type="hidden" name="service" value="{e(service)}">
        <div class="row">
          <label>Ime i prezime<input name="name" required autocomplete="name"></label>
          <label>Telefon<input name="phone" type="tel" autocomplete="tel" placeholder="Npr. 091 234 5678"></label>
        </div>
        <label>E-pošta<input name="email" type="email" autocomplete="email" placeholder="ime@primjer.hr"></label>
        <div class="row">
          <label>S jezika<input name="from" placeholder="Hrvatski"></label>
          <label>Na jezik<input name="to" placeholder="Engleski"></label>
        </div>
        <label>Poruka<textarea name="msg" rows="3" placeholder="Vrsta dokumenta, rok i sve što nam može pomoći."></textarea></label>
        <label>Kako ste saznali za nas?<select name="source">
          <option value="">Odaberite</option>
          <option>Google oglas</option>
          <option>Google pretraživanje</option>
          <option>Google karte</option>
          <option>Preporuka</option>
          <option>Facebook</option>
          <option>Već sam bio/la klijent</option>
          <option>Umjetna inteligencija (AI)</option>
          <option>Drugo</option>
        </select></label>
        <label class="file-drop">Dokumenti za ponudu<input type="file" name="files[]" multiple accept=".pdf,.jpg,.jpeg,.png,.heic,.webp,.doc,.docx,.odt,.rtf,.txt,.xls,.xlsx,.ppt,.pptx"><span class="file-hint">Fotografije ili skenovi, do 10 datoteka i ukupno 20 MB</span></label>
        <fieldset>
          <legend>Koji Vam je ured bliži?</legend>
          <div class="chips">
            <label class="chip"><input type="radio" name="office" value="Rijeka" checked><span>Rijeka</span></label>
            <label class="chip"><input type="radio" name="office" value="Zagreb"><span>Zagreb</span></label>
          </div>
        </fieldset>
        <label class="hp" aria-hidden="true">Web stranica<input name="website" tabindex="-1" autocomplete="off"></label>
        <button class="pill pill-accent" type="submit">Pošaljite upit</button>
        <p class="form-small">Slanjem upita prihvaćate da Vaše podatke i dokumente koristimo samo za izradu ponude, kako je opisano u <a href="../zastita-privatnosti/">zaštiti privatnosti</a>.</p>
        <p class="form-note" role="status"></p>
      </form>'''

def aside_contacts():
    rows = ""
    for key in ("rijeka", "zagreb"):
        o = OFFICES[key]; mob, tel = o["phones"][0]; no = tel.lstrip("+")
        rows += f'''<div class="ac-office">
          <strong>{o["label"]}</strong>
          <span>{o["street"]}, {o["city"]}</span>
          <a href="tel:{tel}">{mob}</a>
          <span class="ac-msg"><a href="https://wa.me/{no}?text={WA_TEXT}" target="_blank" rel="noopener">WhatsApp</a><a href="viber://chat?number=%2B{no}">Viber</a></span>
          <a href="mailto:{o["email"]}">{o["email"]}</a>
        </div>'''
    return f'<div class="aside-contacts"><p class="label">Kontakt</p>{rows}</div>'

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
    links = ''.join(f'<li><a href="../{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES if s["slug"] != exclude)
    return f'''<section class="section">
    <div class="section-head"><p class="label">Usluge</p><h2>{title}</h2></div>
    <ul class="related">{links}</ul>
  </section>
'''

def footer():
    svc = ''.join(f'<li><a href="../{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    return f'''<footer class="footer">
  <div class="footer-top">
    <a class="brand" href="../"><img src="../assets/orbita-logo.webp" alt="Orbita" width="473" height="108"></a>
    <p>Riječima povezujemo svjetove.</p>
  </div>
  <div class="footer-links">
    <div><p class="label">Usluge</p><ul>{svc}</ul></div>
    <div><p class="label">Gradovi</p><ul><li><a href="../prijevodi-rijeka/">Prijevodi Rijeka i Kastav</a></li><li><a href="../prijevodi-zagreb/">Prijevodi Zagreb</a></li></ul></div>
    <div><p class="label">Orbita</p><ul><li><a href="../cesta-pitanja/">Česta pitanja</a></li>{BLOG_LI}<li><a href="../kontakt/">Kontakt</a></li><li><a href="../#o-nama">O nama</a></li><li><a href="../#ponuda">Zatražite ponudu</a></li></ul></div>
  </div>
  <div class="footer-bottom">
    <span>© <span id="year"></span> Orbita prijevodi · OMNIA d.o.o., OIB 42140363484</span>
    <nav><a href="../kontakt/">Kontakt</a><a href="../pravne-informacije/">Pravne informacije</a><a href="../zastita-privatnosti/">Zaštita privatnosti</a><a href="#" data-cookie-settings>Postavke kolačića</a></nav>
  </div>
</footer>
<script src="../page.js?v={V}"></script>
<script src="../consent.js?v={V}"></script>
<script src="../form.js?v={V}"></script>
</body>
</html>
'''

def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}/{p}"} for i, (n, p) in enumerate(items)]}

def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a).replace("\n\n", " ")}} for q, a in items]}

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
    body_paras = ''.join(f'<p>{rich(p)}</p>' for p in s["body"])
    price = s.get("price", PRICE)
    price_p = f'<p>{rich(price)}</p>' if price else ''
    note = f'<p class="aside-note">{rich(SEND_PHOTO)}</p>' if s.get("photo", True) else ''
    items = ''.join(f'<li>{e(i)}</li>' for i in s["items"])
    body = f'''<section class="section">
    <div class="page-body">
      <div class="prose">
        <p class="label">O usluzi</p>
        <h2>{e(s["name"])}</h2>
        {body_paras}
        {price_p}
      </div>
      <aside class="page-aside">
        <p class="label">Što obuhvaća</p>
        <ul class="chips-list">{items}</ul>
        {note}
        <a class="pill pill-ink" href="../#ponuda" data-svc="{e(s["name"])}">Zatražite ponudu</a>
        {aside_contacts()}
      </aside>
    </div>
  </section>
'''
    html_out = head(s["title"], s["desc"], path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), ("Usluge", "../usluge/"), (s["name"], None)], s["h1"], s["lead"]) + '  ' + body + '  ' + faq_block(s["faq"]) + '  ' + cta_band(price, s.get("photo", True)) + '  ' + related(s["slug"]) + '</main>\n' + footer()
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
    city_paras = ''.join(f'<p>{rich(p)}</p>' for p in c["body"])
    svc_links = ''.join(f'<li><a href="../{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    body = f'''<section class="section">
    <div class="page-body">
      <div class="prose">
        <p class="label">{e(c["name"])}</p>
        <h2>Prevoditeljska agencija {e(c["za"])}</h2>
        {city_paras}
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
cards = ''.join(f'''<a class="svc-card" href="../{s["slug"]}/"><h3>{e(s["name"])}</h3><p>{e(s["lead"])}</p><span>Saznajte više</span></a>''' for s in SERVICES)
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


# Legal pages: company details (Zakon o trgovačkim društvima, Zakon o elektroničkoj trgovini) and privacy (GDPR)
COMPANY_ROWS = [
  ("Tvrtka", "OMNIA d.o.o."),
  ("Robna marka", "Orbita prijevodi"),
  ("Sjedište", "Ćikovići 109, 51215 Kastav"),
  ("Sudski registar", "Trgovački sud u Rijeci, MBS 040366010"),
  ("Matični broj", "4630327"),
  ("OIB", "42140363484"),
  ("Uprava", "Diana Jenul, zastupa društvo samostalno i pojedinačno"),
  ("Temeljni kapital", "2.655 € (20.000 kn), uplaćen u cijelosti"),
  ("Banka", "Erste&amp;Steiermärkische Bank d.d., Jadranski trg 3A, 51000 Rijeka"),
  ("IBAN", "HR47 2402 0061 1008 0465 2"),
  ("SWIFT/BIC", "ESBCHR22"),
  ("E-pošta", '<a href="mailto:info@orbitaprijevodi.com">info@orbitaprijevodi.com</a>'),
  ("Telefon", '<a href="tel:+385981631930">+385 98 163 19 30</a>'),
]
rows = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in COMPANY_ROWS)
path = "pravne-informacije/"
ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Pravne informacije", path)])]}
html_out = head("Pravne informacije | Orbita prijevodi, OMNIA d.o.o.", "Podaci o tvrtki OMNIA d.o.o., koja pruža usluge pod nazivom Orbita prijevodi: sjedište, sudski registar, OIB i kontakt.", path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), ("Pravne informacije", None)], ("Pravne ", "informacije"), "Orbita prijevodi usluga je tvrtke OMNIA d.o.o. iz Kastva.") + f'''  <section class="section">
    <dl class="legal-list">{rows}</dl>
  </section>
''' + '</main>\n' + footer()
write("pravne-informacije", html_out); pages.append(path)

PRIVACY = [
  ("Tko je voditelj obrade", ["Voditelj obrade Vaših osobnih podataka je OMNIA d.o.o., Ćikovići 109, 51215 Kastav, OIB 42140363484, koja pruža usluge pod nazivom Orbita prijevodi. Za sva pitanja o zaštiti podataka možete nam se obratiti na info@orbitaprijevodi.com."]),
  ("Koje podatke prikupljamo", ["Kada nam se obratite putem obrasca na stranici, e-poštom, telefonom, Viberom ili WhatsAppom, obrađujemo podatke koje nam sami pošaljete: ime i prezime, adresu e-pošte, broj telefona, sadržaj poruke te dokumente koje nam dostavite na prijevod ili lekturu. Dokumenti mogu sadržavati i osobne podatke drugih osoba ili osjetljive podatke, primjerice medicinsku dokumentaciju."]),
  ("Zašto ih obrađujemo", ["Podatke koristimo samo kako bismo Vam izradili ponudu, obavili naručenu uslugu, dostavili Vam gotov prijevod i izdali račun. Pravna osnova je izvršavanje ugovora i radnje prije sklapanja ugovora na Vaš zahtjev, te zakonske obveze, primjerice u računovodstvu."]),
  ("Tko ih vidi", ["Vašim podacima i dokumentima pristupaju samo naši djelatnici i suradnici, prevoditelji, sudski tumači i lektori koji rade na Vašem zahtjevu i obvezani su na povjerljivost. Podatke ne prodajemo i ne ustupamo trećima u marketinške svrhe. Stranica se poslužuje putem pružatelja usluge smještaja (hostinga), a e-pošta putem našeg pružatelja usluge e-pošte. Dokumente poslane putem obrasca na stranici primamo izravno na adrese info@orbitaprijevodi.com i zagreb@orbitaprijevodi.com."]),
  ("Koliko ih čuvamo", ["Podatke čuvamo onoliko dugo koliko je potrebno za obavljanje usluge, a nakon toga samo onoliko koliko nam to nalažu propisi, primjerice za račune i računovodstvene isprave. Dokumente dostavljene na prijevod ne čuvamo dulje nego što je potrebno."]),
  ("Vaša prava", ["Imate pravo zatražiti pristup svojim podacima, njihov ispravak ili brisanje, ograničenje obrade i prijenos podataka te uložiti prigovor na obradu. Zahtjev nam možete poslati na info@orbitaprijevodi.com. Ako smatrate da su Vaša prava povrijeđena, možete podnijeti pritužbu Agenciji za zaštitu osobnih podataka (azop.hr)."]),
  ("Kolačići", ["Kako bismo znali kako posjetitelji pronalaze stranicu i koriste je te koliko su uspješni naši oglasi, koristimo Google Analytics i Google Ads tvrtke Google Ireland Limited. Oni postavljaju kolačiće i bilježe, primjerice, koje ste stranice posjetili, s kojeg ste oglasa došli te jeste li nam poslali upit ili nas nazvali.", "Te kolačiće koristimo samo ako ih prihvatite u obavijesti o kolačićima pri prvom posjetu. Ako odaberete samo nužne, analitika i oglasni kolačići ostaju isključeni, a stranica radi jednako. Svoj izbor u svakom trenutku možete promijeniti putem poveznice Postavke kolačića na dnu svake stranice."]),
]
secs = ''.join(f'<h2>{e(h)}</h2>' + ''.join(f'<p>{e(p)}</p>' for p in ps) for h, ps in PRIVACY)
path = "zastita-privatnosti/"
ld = {"@context": "https://schema.org", "@graph": [crumbs_ld([("Početna", ""), ("Zaštita privatnosti", path)])]}
html_out = head("Zaštita privatnosti | Orbita prijevodi", "Kako Orbita prijevodi (OMNIA d.o.o.) obrađuje i štiti Vaše osobne podatke i dokumente.", path, ld) + NAV + '<main>\n  ' + page_hero([("Početna", "../"), ("Zaštita privatnosti", None)], ("Zaštita ", "privatnosti"), "Vaši podaci i dokumenti u sigurnim su rukama. Otkrijte kako brinemo o njihovoj povjerljivosti i zaštiti.") + f'''  <section class="section">
    <div class="prose legal-prose">{secs}<p class="legal-date">Zadnja izmjena: listopad 2026.</p></div>
  </section>
''' + '</main>\n' + footer()
write("zastita-privatnosti", html_out); pages.append(path)

exec(open("blog_pages.py").read())

# Old addresses that now live elsewhere: send people (and Google) to the right place
REDIRECTS = {"o-nama": "../#o-nama", "novosti": "../", "individualne-poduke-stranih-jezika-hrvatskog-jezika-za-strance": "../usluge/"}
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
