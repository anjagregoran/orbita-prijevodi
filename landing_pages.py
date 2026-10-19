# Google Ads landing pages, run from build_pages.py (uses its helpers and constants).
# Facts here come from Orbita's own landing pages on the old site: quote within an hour,
# one page in 2 hours for the main languages, office hours 9 to 17, phones 24 hours.

LP_PHONE = PHONES[0]  # Rijeka mobile is the main WhatsApp/Viber number on landing pages
HOURS = "U uredu smo svakim radnim danom od 9 do 17 sati, a na mobitel smo Vam dostupni 24 sata dnevno."

QUOTES_LP = [
  ("Imali smo dosta obiman tekst za prijevod, korisničke upute i jamstvene listove. Odabrali smo ih po preporuci i jako smo zadovoljni obavljenim poslom.", "Primož Prosen", "Product Manager, Euroton d.o.o."),
  ("U prevoditeljskoj agenciji Orbita dobili smo svu potrebnu podršku. Pokazali su se vrlo fleksibilnim i pouzdanim poslovnim partnerom koji je odličan u pronalaženju rješenja za najteže i najsloženije probleme.", "Anita Satler", "direktorica, AKTA Co d.o.o."),
]
CLIENTS = ["Petrol", "Bureau Veritas", "Trea Trade", "Euroton", "AKTA", "Inspirion", "IAPC", "Edit"]

TRUST_TR = [("1 sat", "do ponude"), ("2 sata", "za prijevod jedne stranice"), ("24 sata", "dostupni na mobitel"), ("2 ureda", "u Zagrebu i Kastvu")]
STEPS_TR = [
  ("Poslikajte dokument", "Mobitelom ili skenerom, pa nam ga pošaljite Viberom, WhatsAppom ili e-poštom. Možete ga donijeti i osobno."),
  ("Ponuda za sat vremena", "Unutar sat vremena od Vašeg upita šaljemo Vam cijenu i rok."),
  ("Gotov prijevod", "Šaljemo ga e-poštom ili poštom na Vašu kućnu adresu, a možete ga preuzeti i u uredu."),
]
def faq_tr(lang_same_day):
    return [
      ("Mogu li prijevod dobiti isti dan?", f"Izuzetno smo fleksibilni i trudimo se svakoj stranci osigurati prijevod u najkraćem mogućem roku. Prijevod dokumenta od jedne stranice, do jedne kartice teksta, za najtraženije jezike (engleski, njemački, talijanski, slovenski i srpski) moguć je i unutar 2 sata od Vašeg upita. {lang_same_day}"),
      ("Koliko košta prijevod?", "Cijena ovisi o broju znakova, ovjeri i zahtjevnosti teksta. Obračunava se po kartici teksta od 1800 znakova s razmacima, a ponudu s točnom cijenom šaljemo Vam unutar sat vremena od upita."),
      ("Kako Vam mogu poslati dokument?", "Skenirajte ga ili poslikajte mobitelom i pošaljite nam ga Viberom, WhatsAppom ili Messengerom, na info@orbitaprijevodi.com ili zagreb@orbitaprijevodi.com, ili ga donesite osobno u ured. Šaljemo ga i običnom poštom. Pazite da je fotografija oštra i da se vidi sav tekst."),
      ("Kako ću dobiti gotov prijevod?", "Onako kako Vam najviše odgovara: šaljemo ga e-poštom ili poštom na Vašu kućnu adresu, a možete ga preuzeti i u jednom od naših ureda."),
      ("Kada ste dostupni?", HOURS),
      ("Gdje se nalazite?", "Zagrebački ured nalazi se u Martićevoj 67 na Kvaternikovu trgu, na sjecištu tramvajskih i autobusnih linija, a ako dolazite automobilom, parkirati možete u dvorištu ili u garaži u sklopu zgrade. Riječki ured nalazi se u Kastvu, na adresi Ćikovići 109."),
    ]

def certified_section(lang_gen, lang_loc):
    return (f"Ovjereni prijevod koji priznaju institucije", [
      "Ovjerene prijevode izrađuju sudski tumači, osobe s diplomom i iznimnim poznavanjem stranog jezika te položenim ispitom za sudskog tumača, koje imenuje županijski sud Republike Hrvatske.",
      f"Sudski tumač za {lang_gen} jezik svojim pečatom potvrđuje da je prijevod na {lang_loc} jeziku istovjetan izvorniku na hrvatskom, i obrnuto. Ovjereni prijevod uvezuje se s originalom, ovjerenom ili običnom preslikom izvornog dokumenta i pred tijelima vlasti ima snagu izvornika.",
    ], [])

DOCS = ["Svjedodžbe i diplome", "Rodni i vjenčani listovi", "Radne dozvole", "Izvadci iz sudskog registra", "Ugovori i punomoći", "Medicinska dokumentacija"]

LANDINGS = [
  dict(slug="sudski-tumac-za-engleski-jezik",
    title="Sudski tumač za engleski jezik | Ovjereni prijevod već za 2 sata",
    desc="Ovjereni prijevodi sudskog tumača za engleski jezik u Zagrebu i Kastvu. Pošaljite fotografiju dokumenta Viberom ili WhatsAppom, a ponudu dobivate unutar sat vremena.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumač za ", "engleski jezik"),
    lead="Pošaljite nam fotografiju dokumenta i ponudu dobivate unutar sat vremena. Prijevod jedne stranice na engleski moguć je već za 2 sata, a opsežniji tekst isti dan.",
    trust=TRUST_TR, steps=STEPS_TR, chips=("Što najčešće prevodimo", DOCS),
    sections=[certified_section("engleski", "engleskom"),
      ("Iskustvo i kod najzahtjevnijih dokumenata", ["Naš sudski tumač za engleski jezik i prevoditelji različitih profila imaju dugogodišnje iskustvo s ovjerenim i neovjerenim prijevodima, pa nam se s povjerenjem možete obratiti i kad su dokumenti najzahtjevniji."], []),
      ("Engleski, jezik cijelog svijeta", ["Engleski je službeni jezik u šezdesetak država, od SAD-a, Ujedinjenog Kraljevstva i Irske do Kanade i Australije, i glavni jezik međunarodne komunikacije, znanosti i poslovanja. Zato ovjereni prijevod na engleski traže veleposlanstva, sveučilišta i poslodavci diljem svijeta."], [])],
    faq=faq_tr("Opsežniji prijevod na engleski, slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="sudski-tumac-za-slovenski-jezik",
    title="Sudski tumač za slovenski jezik | Ovjereni prijevod već za 2 sata",
    desc="Ovjereni prijevodi sudskog tumača za slovenski jezik u Zagrebu i Kastvu. Pošaljite fotografiju dokumenta Viberom ili WhatsAppom, a ponudu dobivate unutar sat vremena.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumač za ", "slovenski jezik"),
    lead="Pošaljite nam fotografiju dokumenta i ponudu dobivate unutar sat vremena. Prijevod jedne stranice na slovenski moguć je već za 2 sata, a opsežniji tekst isti dan.",
    trust=TRUST_TR, steps=STEPS_TR, chips=("Što najčešće prevodimo", DOCS),
    sections=[certified_section("slovenski", "slovenskom"),
      ("Slovenski, jezik naših susjeda", ["Slovenija je jedan od najvažnijih poslovnih partnera Hrvatske, pa slovenski prijevod često trebaju tvrtke, radnici i studenti s obje strane granice. Za slovenske klijente prevodimo godinama, od Petrola u Ljubljani do računovodstvene tvrtke AKTA."], [])],
    faq=faq_tr("Opsežniji prijevod na slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="sudski-tumac-za-srpski-jezik",
    title="Sudski tumač za srpski jezik | Ovjereni prijevod već za 2 sata",
    desc="Ovjereni prijevodi sudskog tumača za srpski jezik u Zagrebu i Kastvu. Pošaljite fotografiju dokumenta Viberom ili WhatsAppom, a ponudu dobivate unutar sat vremena.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumač za ", "srpski jezik"),
    lead="Pošaljite nam fotografiju dokumenta i ponudu dobivate unutar sat vremena. Prijevod jedne stranice na srpski moguć je već za 2 sata, a opsežniji tekst isti dan.",
    trust=TRUST_TR, steps=STEPS_TR, chips=("Što najčešće prevodimo", DOCS),
    sections=[certified_section("srpski", "srpskom"),
      ("Za dokumente iz Srbije i za Srbiju", ["Ovjereni prijevod sa srpskog ili na srpski trebaju svi koji dokumente iz Srbije predaju hrvatskim institucijama, kao i oni kojima hrvatski dokumenti trebaju u Srbiji, od svjedodžbi i diploma do rodnih listova i radnih dozvola."], [])],
    faq=faq_tr("Opsežniji prijevod na slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="sudski-tumaci-za-sve-jezike",
    title="Sudski tumači za sve jezike | Ovjereni prijevodi | Orbita prijevodi",
    desc="Ovjereni prijevodi sudskih tumača za engleski, njemački, talijanski, slovenski, srpski i sve ostale jezike. Ponuda unutar sat vremena, uredi u Zagrebu i Kastvu.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumači ", "za sve jezike"),
    lead="Od engleskog, njemačkog i talijanskog do japanskog i arapskog: ovjereni prijevod na jezik koji Vam treba, uz ponudu unutar sat vremena od upita.",
    trust=TRUST_TR, steps=STEPS_TR, chips=("Jezici koje najčešće prevodimo", ["Engleski", "Njemački", "Talijanski", "Slovenski", "Srpski", "Francuski", "Španjolski", "Ruski", "Ukrajinski", "Mađarski", "Arapski", "Kineski", "Japanski"]),
    sections=[certified_section("traženi", "traženom"),
      ("Široka mreža sudskih tumača", ["Imamo široku mrežu suradnika, ovlaštenih sudskih tumača i prevoditelja za slovenski, srpski, engleski, talijanski i njemački jezik, kao i za sve ostale tražene jezike, ukupno više od 30 jezika.", "Ako jezika koji Vam treba nema na popisu, javite nam se, osigurat ćemo Vam prijevod i na njega."], [])],
    faq=faq_tr("Opsežniji prijevod na slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="profesionalno-sastavljanje-zivotopisa-cv-curriculum-vitae",
    title="Profesionalno sastavljanje životopisa (CV) i motivacijskog pisma | Orbita",
    desc="Profesionalno sastavljanje životopisa i motivacijskih pisama za posao i stipendije, u kronološkom, funkcionalnom ili kombiniranom obliku, uz prijevod na strani jezik.",
    kicker="Profesionalno sastavljanje životopisa", micro="Pošaljite nam postojeći životopis ili osnovne podatke, bez obveze.", h1=("Životopis koji ", "otvara vrata"),
    lead="Životopis i motivacijsko pismo često su prvi dojam koji ostavljate na poslodavca ili sveučilište. Pomoći ćemo Vam da se istaknete u mnoštvu prijava, na hrvatskom ili na stranom jeziku.",
    trust=[("CV", "i motivacijsko pismo"), ("3 modela", "kronološki, funkcionalni, kombinirani"), ("Prijevod", "na strani jezik"), ("24 sata", "dostupni na mobitel")],
    steps=[("Javite nam se", "Pošaljite nam postojeći životopis ili osnovne podatke Viberom, WhatsAppom ili e-poštom."), ("Biramo pravi model", "Zajedno biramo oblik koji najbolje predstavlja Vaše iskustvo i cilj."), ("Gotov životopis", "Dobivate dotjeran životopis i motivacijsko pismo, po želji i prevedene na strani jezik.")],
    chips=("Što izrađujemo", ["Profesionalni životopis", "Akademski životopis", "Europass životopis", "Motivacijsko pismo", "Prijevod na strani jezik"]),
    sections=[
      ("Prvi dojam koji odlučuje", ["Umijeće sastavljanja dobrog životopisa jedna je od važnih stepenica na putu do željenog posla ili stipendije za studij. Uz motivacijsko pismo, koje se danas gotovo uvijek šalje uz životopis, ta dva dokumenta često predstavljaju prvi dojam koji ostavljate na poslodavca ili obrazovnu instituciju.", "Dobar životopis, uz stroge formalne zahtjeve, mora imati osobnu notu i biti dovoljno poseban da u mnoštvu prijava bude odabran baš on."], []),
      ("Koji životopis Vam treba", ["Životopis može biti napisan u slobodnoj formi ili prema obrascu, poput Europass obrasca. Profesionalni životopis donosi pregled cijele radne i akademske karijere, a akademski pregled obrazovanja i postignuća, od objavljenih radova do održanih predavanja i konferencija.", "Ovisno o cilju, birat ćemo između kronološkog, funkcionalnog i kombiniranog modela, a pomoći ćemo Vam odabrati i izraditi onaj koji je za Vas najprikladniji."], []),
    ],
    faq=[("Možete li životopis i prevesti?", "Da. Uz sastavljanje životopisa i motivacijskog pisma osiguravamo i prijevod na željeni strani jezik."), ("Što Vam trebam poslati?", "Postojeći životopis, ako ga imate, ili osnovne podatke o obrazovanju i radnom iskustvu, te natječaj ili oglas na koji se prijavljujete."), ("Kada ste dostupni?", HOURS)]),
  dict(slug="lektura",
    title="Lektura i korektura: akademski radovi, knjige, web | Orbita prijevodi",
    desc="Stručna lektura seminarskih, završnih i diplomskih radova, disertacija, knjiga, internetskih stranica i marketinških tekstova. Lektura jedne stranice već za 2 sata.",
    kicker="Lektura i korektura", micro="Pošaljite nam tekst i javljamo Vam cijenu i rok, bez obveze.", h1=("Lektura koja tekst čini ", "besprijekornim"),
    lead="Seminarski, završni i diplomski radovi, disertacije, knjige, internetske stranice i marketinški tekstovi. Lektura jedne stranice moguća je već za 2 sata.",
    trust=[("2 sata", "za lekturu jedne stranice"), ("8 dana", "za opsežnije tekstove"), ("Profesori jezika", "rade lekturu"), ("24 sata", "dostupni na mobitel")],
    steps=[("Pošaljite tekst", "E-poštom, Viberom ili WhatsAppom, u Wordu, PowerPointu ili Excelu."), ("Ponuda i rok", "Javljamo Vam cijenu i rok, ovisno o vrsti i opsegu teksta."), ("Besprijekoran tekst", "Dobivate lektorirani tekst, s komentarima ondje gdje je sadržaj nejasan.")],
    chips=("Specijalizirani smo za", ["Seminarski i maturalni radovi", "Završni i diplomski radovi", "Disertacije", "Znanstveni radovi", "Knjige i udžbenici", "Internetske stranice", "Marketinški tekstovi"]),
    sections=[
      ("Samo kod nas: stilsko-lingvistička lektura akademskih tekstova", ["Lekturu u agenciji Orbita rade stručni lektori, profesori hrvatskog i stranih jezika, s iznimno bogatim iskustvom. Ispravljaju gramatičke, pravopisne, tipografske i interpunkcijske pogreške te tekst jezično i stilski dotjeruju, a ne zadiru u sadržaj, nego prilažu komentar ondje gdje je nešto nejasno.", "Seminarski, maturalni, završni i diplomski rad te disertacija moraju biti pravopisno, gramatički i stilski ispravni, jer škole i fakulteti ne prihvaćaju radove pune pogrešaka. Naši lektori pobrinut će se da Vaš rad bude besprijekoran."], []),
      ("Knjige, znanstveni radovi i internetske stranice", ["Lektoriramo udžbenike, priručnike, radne bilježnice i edukativne materijale, filozofske i beletrističke knjige te znanstvene radove, uz poštivanje stručnog nazivlja i suradnju s autorima.", "Ako na internetskim stranicama nudite proizvode ili usluge, tekst mora biti ispravan, jer u protivnom može odbiti klijente. Dobro lektoriran tekst je poput celofana oko proizvoda: predstavlja ga u najboljem svjetlu."], []),
    ],
    faq=[("Koliko brzo možete lektorirati tekst?", "Lektura dokumenta od jedne stranice, do jedne kartice teksta od 1500 znakova bez razmaka, za najtraženije jezike (hrvatski, engleski, njemački, talijanski, slovenski i srpski) moguća je i unutar 2 sata od Vašeg upita. Opsežniji tekst, ovisno o broju kartica, vrsti teksta i jeziku, lektorirat ćemo unutar 8 dana."),
      ("Koliko košta lektura?", "Cijena ovisi o vrsti teksta, jeziku, broju kartica i roku isporuke. Jednostavniji tekstovi, poput letaka i brošura, jeftiniji su od zahtjevnih, poput diplomskih radova, a tekstovi na hrvatskom jeftiniji su od onih na stranim jezicima. Okvirno, lektura teksta na hrvatskom jeziku stoji od 3 do 6 eura po kartici od 1500 znakova bez razmaka, a hitna lektura može biti nešto skuplja."),
      ("Kako Vam mogu poslati tekst?", "E-poštom na info@orbitaprijevodi.com ili zagreb@orbitaprijevodi.com, Viberom ili WhatsAppom, ili ga donesite osobno u jedan od naših ureda."),
      ("Kada ste dostupni?", HOURS)]),
  dict(slug="medicinski-prijevodi",
    title="Medicinski prijevodi: nalazi, otpusna pisma, ovjereno | Orbita prijevodi",
    desc="Stručni i ovjereni prijevodi medicinske dokumentacije: nalazi, otpusna pisma, laboratorijska izvješća i istraživački tekstovi. Prevoditelji educirani u medicini, uz zaštitu podataka.",
    kicker="Prijevodi medicinske dokumentacije", h1=("Medicinski prijevodi, ", "stručno i ovjereno"),
    lead="Nalaze, otpusna pisma i medicinsku dokumentaciju prevode prevoditelji educirani u medicini, kako biste bez jezične barijere dobili liječenje ili mišljenje bilo gdje u svijetu.",
    trust=[("Medicinski", "educirani prevoditelji"), ("Ovjereno", "za nalaze i izvješća"), ("Povjerljivo", "uz zaštitu podataka"), ("1 sat", "do ponude")],
    steps=STEPS_TR,
    chips=("Prevodimo za Vas", ["Medicinski nalazi", "Otpusna pisma", "Medicinski dosjei", "Laboratorijska izvješća", "Medicinska osiguranja", "Istraživačka dokumentacija", "Priručnici i edukativni materijali", "Upute za medicinske proizvode"]),
    sections=[
      ("Bez jezične barijere do liječenja", ["Prijevodi medicinske dokumentacije imaju jasnu svrhu: pomoći pacijentu da zatraži medicinsko mišljenje ili liječenje u drugoj državi. Zato prevodimo i ovjereno, s pečatom sudskog tumača, liječničke nalaze, izvješća, povijesti bolesti i otpusna pisma."], []),
      ("Prevode ih medicinski educirani prevoditelji", ["Medicinski prijevodi spadaju među najzahtjevnije stručne prijevode, jer pogreška u medicinskoj dokumentaciji može značiti pogrešnu dijagnozu. Zato ih kod nas rade iskusni prevoditelji, izvrsni poznavatelji hrvatskog i stranih jezika, koji su ujedno educirani u području medicine."], ["Interna medicina (kardiologija, hematologija, endokrinologija)", "Dermatologija", "Neurologija", "Ginekologija", "Psihijatrija", "Farmakologija", "Imunologija"]),
      ("Vaši podaci ostaju povjerljivi", ["Sve osobne podatke pacijenata, uključujući podatke o bolesti, simptome, dijagnostičke postupke, laboratorijske nalaze i recepte, smatramo strogo povjerljivima, u skladu s propisima o zaštiti osobnih podataka (GDPR). U postupku prevođenja sudjeluju samo naš prevoditeljski tim i Vi."], []),
    ],
    faq=[faq_tr("")[1], faq_tr("")[2], faq_tr("")[3], ("Prevodite li i stručne medicinske tekstove?", "Da. Osim dokumentacije pacijenata prevodimo istraživačke radove i tekstove iz svih područja medicine, predavanja za studente medicine, prezentacije, skripte, priručnike i konferencijske tekstove za zdravstvene djelatnike, kao i medicinsko-pravne tekstove poput diploma, licenci i dozvola za rad."), ("Kada ste dostupni?", HOURS)]),
]

LESSON_WA = quote("Poštovani, zanima me individualna poduka iz jezika.")
LANDINGS.append(dict(slug="individualne-poduke-stranih-jezika-hrvatskog-jezika-za-strance",
    title="Individualna poduka: engleski, slovenski, talijanski i hrvatski za strance | Orbita",
    desc="Individualna poduka iz engleskog, slovenskog i talijanskog jezika te hrvatskog jezika za strance. Plan učenja po mjeri Vašeg cilja, u Zagrebu i Kastvu.",
    kicker="Individualna poduka iz jezika", h1=("Jezik koji ćete ", "stvarno govoriti"),
    lead="Individualna poduka iz engleskog, slovenskog i talijanskog jezika te hrvatskog za strance. Bez učionice i bez tuđeg tempa: učite točno ono što Vama treba, za školu, posao ili život u novoj zemlji.",
    micro="Javite nam se i dogovorit ćemo prvi sat, bez obveze.",
    wa=LESSON_WA, wa_label="Javite se na WhatsApp", aside_cta="Prijavite se", steps_title="Od prve poruke do prvog razgovora.",
    trust=[("1 na 1", "individualni sati"), ("4 jezika", "engleski, slovenski, talijanski, hrvatski"), ("Vaš cilj", "plan učenja po mjeri"), ("24 sata", "dostupni na mobitel")],
    steps=[("Javite nam se", "Recite nam koji jezik želite učiti, koliko ga već znate i što želite postići."), ("Plan po mjeri", "Dogovaramo plan učenja i termine koji Vam odgovaraju."), ("Učite i napredujete", "Na svakom satu radite upravo ono što Vama treba, od razgovora do gramatike i pisanja.")],
    chips=("Za koga je poduka", ["Učenici i maturanti", "Studenti", "Poslovni ljudi", "Radnici prije odlaska u inozemstvo", "Turistički djelatnici", "Stranci koji žive u Hrvatskoj"]),
    sections=[
      ("Zašto individualna poduka", ["U grupi se tempo prilagođava svima, a na individualnom satu samo Vama. Nema čekanja na druge ni preskakanja onoga što Vam je teško: svaki je sat posvećen Vašem cilju, bilo da je to bolja ocjena, matura, razgovor za posao ili prvi razgovor sa susjedima na novom jeziku."], []),
      ("Učite od ljudi koji jezikom žive", ["Orbita je prevoditeljska agencija, pa jezike ne poznajemo samo iz udžbenika: s njima radimo svaki dan, s dokumentima, poslovnim partnerima i klijentima iz cijele Europe. To iskustvo prenosimo i na Vas, s naglaskom na jezik koji ćete stvarno koristiti."], []),
      ("Četiri jezika, četiri nove prilike", ["Living in Croatia and want to learn Croatian? We offer one-to-one Croatian lessons for foreigners, at your own pace."], ["Engleski za školu, studij, posao i putovanja", "Slovenski za posao i život s druge strane granice", "Talijanski za turizam, posao i sve koji vole Italiju", "Hrvatski za strance, za život i posao u Hrvatskoj"]),
    ],
    faq=[("Koje jezike podučavate?", "Individualnu poduku nudimo iz engleskog, slovenskog i talijanskog jezika te hrvatskog jezika za strance."),
      ("Za koju je razinu poduka?", "Za svaku, od potpunih početnika do naprednih. Na početku procijenimo Vaše znanje i složimo plan prema Vašem cilju."),
      ("Gdje se održava poduka?", "U našim uredima u Zagrebu i Kastvu. Javite nam se, a termine ćemo dogovoriti prema Vašim mogućnostima."),
      ("Kako se mogu prijaviti?", "Nazovite nas ili nam pošaljite poruku Viberom ili WhatsAppom na 098 163 19 30 ili 091 612 6784, ili e-poštom na info@orbitaprijevodi.com."),
      ("Kada ste dostupni?", HOURS)]))

def lp_nav(wa=None):
    n = LP_PHONE[2]; wa = wa or WA_TEXT
    return f'''<header class="nav nav-lp" id="nav">
  <a class="brand" href="../" aria-label="Orbita prijevodi, početna">
    <img src="../assets/orbita-logo.webp" alt="Orbita" width="473" height="108">
  </a>
  <div class="lp-actions">
    <a class="lp-phone" href="tel:+{n}">{LP_PHONE[1]}</a>
    <a class="pill pill-ink" href="https://wa.me/{n}?text={wa}" target="_blank" rel="noopener">{"Pošaljite poruku" if wa != WA_TEXT else "Pošaljite dokument"}</a>
  </div>
</header>
'''

def lp_hero(d):
    n = LP_PHONE[2]; wa = d.get("wa", WA_TEXT)
    return f'''<section class="hero page-hero lp-hero">
    <div class="hero-bg" aria-hidden="true"></div>
    <div class="hero-text">
      <p class="label lp-kicker">{e(d["kicker"])}</p>
      <h1>{e(d["h1"][0])}<em>{e(d["h1"][1])}</em></h1>
      <p class="lead">{e(d["lead"])}</p>
      <div class="hero-cta">
        <a class="pill pill-ink" href="https://wa.me/{n}?text={wa}" target="_blank" rel="noopener">{d.get("wa_label", "Pošaljite na WhatsApp")}</a>
        <a class="pill pill-line" href="viber://chat?number=%2B{n}">Viber</a>
        <a class="pill pill-line" href="tel:+{n}">Nazovite {LP_PHONE[1]}</a>
      </div>
      <p class="lp-micro">{e(d.get("micro", "Poslikajte dokument mobitelom i pošaljite ga, bez obveze."))}</p>
    </div>
  </section>
'''

def lp_page(d):
    path = f'{d["slug"]}/'
    trust = ''.join(f'<div><strong>{e(v)}</strong><span>{e(l)}</span></div>' for v, l in d["trust"])
    steps = ''.join(f'<li><span class="n">0{i+1}</span><h3>{e(t)}</h3><p>{e(p)}</p></li>' for i, (t, p) in enumerate(d["steps"]))
    secs = ''
    for h, paras, bullets in d["sections"]:
        secs += f'<h2>{e(h)}</h2>' + ''.join(f'<p>{e(p)}</p>' for p in paras)
        if bullets: secs += '<ul class="lp-bullets">' + ''.join(f'<li>{e(b)}</li>' for b in bullets) + '</ul>'
    chips = ''.join(f'<li>{e(c)}</li>' for c in d["chips"][1])
    quotes = ''.join(f'<figure><blockquote>{e(q)}</blockquote><figcaption><strong>{e(w)}</strong>{e(r)}</figcaption></figure>' for q, w, r in QUOTES_LP)
    clients = ''.join(f'<span>{c}</span>' for c in CLIENTS)
    n = LP_PHONE[2]; wa = d.get("wa", WA_TEXT)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": d["h1"][0] + d["h1"][1], "description": d["desc"], "areaServed": ["Zagreb", "Rijeka", "Kastav", "Hrvatska"],
         "provider": {"@type": "ProfessionalService", "name": "Orbita prijevodi", "url": SITE + "/", "telephone": "+385981631930"}},
        faq_ld(d["faq"])]}
    body = f'''<section class="lp-trust" aria-label="Zašto Orbita">{trust}</section>
  <section class="section">
    <div class="section-head"><p class="label">Kako to ide</p><h2>{e(d.get("steps_title", "Tri koraka do prijevoda."))}</h2></div>
    <ol class="steps lp-steps">{steps}</ol>
  </section>
  <section class="section lp-detail">
    <div class="page-body">
      <div class="prose">{secs}</div>
      <aside class="page-aside">
        <p class="label">{e(d["chips"][0])}</p>
        <ul class="chips-list">{chips}</ul>
        <a class="pill pill-ink" href="https://wa.me/{n}?text={wa}" target="_blank" rel="noopener">{d.get("aside_cta", "Pošaljite dokument")}</a>
      </aside>
    </div>
  </section>
  <section class="section lp-proof">
    <div class="section-head"><p class="label">Vjeruju nam</p></div>
    <div class="lp-quotes">{quotes}</div>
    <div class="lp-clients">{clients}</div>
  </section>
  ''' + faq_block(d["faq"]) + f'''  <section class="section">
    <div class="offices">
      {office_card("zagreb")}
      {office_card("rijeka")}
    </div>
  </section>
  ''' + cta_band()
    bar = f'''<div class="lp-bar">
  <a href="https://wa.me/{n}?text={wa}" target="_blank" rel="noopener">WhatsApp</a>
  <a href="viber://chat?number=%2B{n}">Viber</a>
  <a href="tel:+{n}">Nazovite</a>
</div>
'''
    out = head(d["title"], d["desc"], path, ld).replace('<body class="subpage">', '<body class="subpage landing">') + lp_nav(d.get("wa")) + '<main>\n  ' + lp_hero(d) + '  ' + body + '</main>\n' + bar + footer()
    write(d["slug"], out)
    pages.append(path)

for d in LANDINGS:
    lp_page(d)
