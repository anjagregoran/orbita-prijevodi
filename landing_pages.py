# Google Ads landing pages, run from build_pages.py (uses its helpers and constants).
# Facts here come from Orbita's own landing pages on the old site: quote within an hour,
# one page in 2 hours for the main languages, office hours 9 to 17, phones 24 hours.

LP_PHONE = PHONES[0]  # Rijeka mobile is the main WhatsApp/Viber number on landing pages
HOURS = "U uredu smo svakim radnim danom od 8 do 16 sati, a na mobitel smo Vam dostupni u bilo koje doba dana."

QUOTES_LP = [
  ("Imali smo dosta obiman tekst za prijevod, korisničke upute i jamstvene listove. Odabrali smo ih po preporuci i jako smo zadovoljni obavljenim poslom.", "Primož Prosen", "Product Manager, Euroton d.o.o."),
  ("U prevoditeljskoj agenciji Orbita dobili smo svu potrebnu podršku. Pokazali su se vrlo fleksibilnim i pouzdanim poslovnim partnerom koji je odličan u pronalaženju rješenja za najteže i najsloženije probleme.", "Anita Satler", "direktorica, AKTA Co d.o.o."),
]
CV_QUOTES = [
  ("Obratila sam se agenciji Orbita i u vrlo kratkom roku dobila odlično napravljen životopis i motivacijsko pismo s prijevodom na njemački jezik. Djelatnica s kojom sam surađivala oduševila me fleksibilnošću i individualnim pristupom. Iskreno preporučujem svima koji trebaju brzu stručnu pomoć za pisanje i prijevod životopisa.", "AMB", "liječnica s 15 godina radnog iskustva"),
  ("Osobno sam vrlo zadovoljan temeljito izrađenim CV-jem koji mi je napravljen u agenciji Orbita. Profesionalno, detaljno, vremenski brzo i financijski pristojno.", "Milan Drenovac", "pomorac"),
  ("Trebao mi je prijevod diploma, Europass CV i molba za posao u inozemstvu. Sve su obavili kako smo se dogovorili, kao i dodatne izmjene koje nisu dodatno naplatili, što iznimno cijenim. Agenciju Orbita preporučujem svima kojima su potrebni stručno sastavljeni CV i motivacijsko pismo!", "Alen Grgić", ""),
  ("Za agenciju Orbita imam sve pohvale na uslugu pisanja i prijevoda životopisa i motivacijskog pisma. Uz ljubaznost, pristupačnost i brzinu zahvaljujem Vam i na svakom savjetu i poticaju koje dajete od srca.", "Jelena Jeremiš", ""),
]
CLIENTS = ["Petrol", "Bureau Veritas", "Trea Trade", "Euroton", "AKTA", "Inspirion", "IAPC", "Edit"]

TRUST_TR = [("1 sat", "do ponude"), ("2 sata", "za prijevod jedne stranice"), ("Dostupni", "na mobitel u bilo koje doba dana"), ("2 ureda", "u Zagrebu i Kastvu")]
STEPS_TR = [
  ("Pošaljite dokument", "Fotografirajte ili skenirajte dokument i pošaljite nam ga putem WhatsAppa, Vibera ili e-maila. Ako Vam više odgovara, posjetite nas osobno."),
  ("Primite ponudu unutar sat vremena", "Brzo i jednostavno! Najkasnije u roku od sat vremena šaljemo Vam ponudu s cijenom i rokom izrade prijevoda."),
  ("Vaš prijevod je spreman :-)", "Kraći prijevodi mogu biti gotovi već za 1 do 2 sata, a opsežniji istoga ili sljedećeg dana odmah ujutro. Gotov prijevod šaljemo Vam e-mailom, putem Vibera ili WhatsAppa (ako je potreban samo u elektroničkom obliku) ili ga preuzimate u našem uredu u fizičkom obliku. Naravno, možemo ga poslati i običnom poštom na Vašu adresu. U slučaju hitnoće i isti dan bike expressom (vrijedi za grad Zagreb)."),
]
# Diana's hero text for the four court interpreter pages (31 Oct 2026)
TR_INTRO = ("Trebate prijevod? Riješite to već danas!", [
  "Bez čekanja, nepotrebnih odlazaka i kompliciranja! Jednostavno fotografirajte ili skenirajte dokument i pošaljite nam ga putem Vibera, WhatsAppa ili e-maila.",
  "Ponudu dobivate unutar sat vremena, a kraći prijevodi mogu biti gotovi već za 1 do 2 sata! U slučaju hitnoće, opsežnije dokumente također smo u mogućnosti isporučiti istoga dana ili najkasnije sljedećeg jutra.",
  "Vi šaljete dokument, mi se brinemo za sve ostalo!"])
TR_STEPS_HEAD = ("Jednostavno do prijevoda", "U tri koraka. Bez nepotrebnih dolazaka.")
def faq_tr(lang_same_day):
    return [
      ("Mogu li prijevod dobiti isti dan?", f"Izuzetno smo fleksibilni i trudimo se svakoj stranci osigurati prijevod u najkraćem mogućem roku. Prijevod dokumenta od jedne stranice, do jedne kartice teksta, za najtraženije jezike (engleski, njemački, talijanski, slovenski i srpski) moguć je i unutar 2 sata od Vašeg upita. {lang_same_day}"),
      ("Koliko košta prijevod?", "Cijena ovisi o broju znakova, ovjeri i zahtjevnosti teksta. Obračunava se po kartici teksta od 1800 znakova s razmacima, a ponudu s točnom cijenom šaljemo Vam unutar sat vremena od upita."),
      ("Kako Vam mogu poslati dokument?", "Skenirajte ga ili fotografirajte mobitelom i pošaljite nam ga Viberom, WhatsAppom ili Messengerom, na info@orbitaprijevodi.com ili zagreb@orbitaprijevodi.com, ili ga donesite osobno u ured. Šaljemo ga i običnom poštom. Pazite da je fotografija oštra i da se vidi sav tekst."),
      ("Kako ću dobiti gotov prijevod?", "Onako kako Vam najviše odgovara: šaljemo ga e-poštom ili poštom na Vašu kućnu adresu, a možete ga preuzeti i u jednom od naših ureda."),
      ("Kada ste dostupni?", HOURS),
      ("Gdje se nalazite?", "Zagrebački ured nalazi se u Martićevoj 67 na Kvaternikovu trgu, na sjecištu tramvajskih i autobusnih linija, a ako dolazite automobilom, parkirati možete u dvorištu ili u garaži u sklopu zgrade. Riječki ured nalazi se u Kastvu, na adresi Ćikovići 109."),
    ]

def certified_section(lang_gen, lang_loc):
    return (f"Ovjereni prijevod koji priznaju institucije", [
      "Ovjerene prijevode izrađuju sudski tumači, osobe s diplomom i iznimnim poznavanjem stranog jezika te položenim ispitom za sudskog tumača, koje imenuje ministar nadležan za poslove pravosuđa u Republici Hrvatskoj.",
      f"Sudski tumač za {lang_gen} jezik svojim pečatom potvrđuje da je prijevod na {lang_loc} jeziku istovjetan izvorniku na hrvatskom, i obrnuto. Ovjereni prijevod uvezuje se s originalom, ovjerenom ili običnom preslikom izvornog dokumenta i pred tijelima vlasti ima snagu izvornika.",
    ], [])

DOCS = ["Svjedodžbe i diplome", "Rodni i vjenčani listovi", "Radne dozvole", "Izvadci iz sudskog registra", "Ugovori i punomoći", "Medicinska dokumentacija"]

LANDINGS = [
  dict(slug="sudski-tumac-za-engleski-jezik",
    title="Sudski tumač za engleski jezik | Ovjereni prijevod već za 2 sata",
    desc="Ovjereni prijevodi sudskog tumača za engleski jezik u Zagrebu i Kastvu. Pošaljite fotografiju dokumenta Viberom ili WhatsAppom, a ponudu dobivate unutar sat vremena.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumač za ", "engleski jezik"),
    lead="Pošaljite nam fotografiju dokumenta i ponudu dobivate unutar sat vremena. Prijevod jedne stranice na engleski moguć je već za 2 sata, a opsežniji tekst isti dan.",
    trust=TRUST_TR, steps=STEPS_TR, intro=TR_INTRO, steps_head=TR_STEPS_HEAD, chips=("Što najčešće prevodimo", DOCS),
    sections=[certified_section("engleski", "engleskom"),
      ("Iskustvo i kod najzahtjevnijih dokumenata", ["Naši sudski tumači za engleski jezik i tim iskusnih prevoditelja različitih stručnih profila jamče visoku razinu kvalitete, preciznosti i pouzdanosti. Zahvaljujući dugogodišnjem iskustvu u izradi ovjerenih i neovjerenih prijevoda, s punim nam povjerenjem možete prepustiti i najzahtjevnije dokumente."], []),
      ("Engleski, jezik cijelog svijeta", ["Od Europe i Sjeverne Amerike do Australije i drugih krajeva svijeta, engleski jezik otvara vrata međunarodnoj komunikaciji, obrazovanju i poslovnim prilikama. Kao službeni jezik u šezdesetak država i nezaobilazan jezik globalne suradnje, ima ključnu ulogu u povezivanju ljudi i institucija. Upravo zato veleposlanstva, sveučilišta i poslodavci diljem svijeta često zahtijevaju *ovjerene prijevode na engleski jezik*, pouzdan korak prema ostvarivanju Vaših međunarodnih planova."], [])],
    faq=faq_tr("Opsežniji prijevod na engleski, slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="sudski-tumac-za-slovenski-jezik",
    title="Sudski tumač za slovenski jezik | Ovjereni prijevod već za 2 sata",
    desc="Ovjereni prijevodi sudskog tumača za slovenski jezik u Zagrebu i Kastvu. Pošaljite fotografiju dokumenta Viberom ili WhatsAppom, a ponudu dobivate unutar sat vremena.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumač za ", "slovenski jezik"),
    lead="Pošaljite nam fotografiju dokumenta i ponudu dobivate unutar sat vremena. Prijevod jedne stranice na slovenski moguć je već za 2 sata, a opsežniji tekst isti dan.",
    trust=TRUST_TR, steps=STEPS_TR, intro=TR_INTRO, steps_head=TR_STEPS_HEAD, chips=("Što najčešće prevodimo", DOCS),
    sections=[certified_section("slovenski", "slovenskom"),
      ("Slovenski, jezik naših susjeda", ["Hrvatsku i Sloveniju povezuje mnogo više od zajedničke granice: snažne gospodarske veze, uspješna poslovna suradnja te svakodnevna razmjena znanja i iskustava. Zato su kvalitetni prijevodi na slovenski i sa slovenskog jezika važni poduzetnicima, zaposlenicima i studentima s obje strane granice.", "*Naše dugogodišnje iskustvo i povjerenje slovenskih klijenata* potvrđuju našu predanost stručnosti, preciznosti i pouzdanosti u svakom prijevodu."], [])],
    faq=faq_tr("Opsežniji prijevod na slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="sudski-tumac-za-srpski-jezik",
    title="Sudski tumač za srpski jezik | Ovjereni prijevod već za 2 sata",
    desc="Ovjereni prijevodi sudskog tumača za srpski jezik u Zagrebu i Kastvu. Pošaljite fotografiju dokumenta Viberom ili WhatsAppom, a ponudu dobivate unutar sat vremena.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumač za ", "srpski jezik"),
    lead="Pošaljite nam fotografiju dokumenta i ponudu dobivate unutar sat vremena. Prijevod jedne stranice na srpski moguć je već za 2 sata, a opsežniji tekst isti dan.",
    trust=TRUST_TR, steps=STEPS_TR, intro=TR_INTRO, steps_head=TR_STEPS_HEAD, chips=("Što najčešće prevodimo", DOCS),
    sections=[certified_section("srpski", "srpskom"),
      ("Vaši dokumenti, spremni za obje strane granice", ["Bliske gospodarske, obrazovne i osobne veze Hrvatske i Srbije donose svakodnevnu potrebu za pouzdanim prijevodima službenih i osobnih dokumenata. Bilo da dokumente izdane u Srbiji predajete hrvatskim institucijama ili hrvatsku dokumentaciju trebate koristiti u Srbiji, osiguravamo *stručne i precizne ovjerene prijevode na srpski i sa srpskog jezika*.", "Od rodnih listova, svjedodžbi i diploma do radnih dozvola i poslovne dokumentacije, *Vaši su dokumenti u sigurnim rukama.*"], [])],
    faq=faq_tr("Opsežniji prijevod na slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="sudski-tumaci-za-sve-jezike",
    title="Sudski tumači za sve jezike | Ovjereni prijevodi | Orbita prijevodi",
    desc="Ovjereni prijevodi sudskih tumača za engleski, njemački, talijanski, slovenski, srpski i sve ostale jezike. Ponuda unutar sat vremena, uredi u Zagrebu i Kastvu.",
    kicker="Ovjereni prijevodi s pečatom", h1=("Sudski tumači ", "za sve jezike"),
    lead="Od engleskog, njemačkog i talijanskog do japanskog i arapskog: ovjereni prijevod na jezik koji Vam treba, uz ponudu unutar sat vremena od upita.",
    trust=TRUST_TR, steps=STEPS_TR, intro=TR_INTRO, steps_head=TR_STEPS_HEAD, chips=("Jezici koje najčešće prevodimo", ["Engleski", "Njemački", "Talijanski", "Slovenski", "Srpski", "Francuski", "Španjolski", "Ruski", "Ukrajinski", "Mađarski", "Arapski", "Kineski", "Japanski"]),
    sections=[certified_section("traženi", "traženom"),
      ("Široka mreža sudskih tumača", ["Zahvaljujući širokoj mreži iskusnih prevoditelja i ovlaštenih sudskih tumača, pružamo stručne i pouzdane prijevode s/sa i na *više od 30 svjetskih jezika*. Bilo da trebate prijevod na engleski, njemački, talijanski, francuski, španjolski, ruski, ukrajinski, slovenski, srpski ili neki drugi jezik, možete računati na našu stručnost, preciznost i profesionalnost.", "*U slučaju da u Republici Hrvatskoj nema tumača za jezik koji trebate*, osigurat ćemo tumača u inozemstvu i pobrinuti se za kvalitetan prijevod na željeni jezik."], [])],
    faq=faq_tr("Opsežniji prijevod na slovenski ili srpski jezik kod nas možete dobiti isti dan.")),
  dict(slug="profesionalno-sastavljanje-zivotopisa-cv-curriculum-vitae",
    title="Profesionalno sastavljanje životopisa (CV) i motivacijskog pisma | Orbita",
    desc="Profesionalno sastavljanje životopisa i motivacijskih pisama za posao i stipendije, u kronološkom, funkcionalnom ili kombiniranom obliku, uz prijevod na strani jezik.",
    quotes=CV_QUOTES, kicker="Profesionalno sastavljanje životopisa", micro="Pošaljite nam postojeći životopis ili osnovne podatke, bez obveze.", h1=("Životopis koji ", "otvara vrata"),
    lead="Kao što prvi dojam otvara vrata novim prilikama, profesionalno oblikovan životopis i uvjerljivo motivacijsko pismo mogu biti presudni na putu do željenog zaposlenja ili upisa na sveučilište. Prepustite nam njihovo jezično usavršavanje i prijevod kako biste se istaknuli među brojnim kandidatima, na hrvatskom ili stranom jeziku.",
    trust=[("CV", "i motivacijsko pismo"), ("3 modela", "kronološki, funkcionalni, kombinirani"), ("Prijevod", "na strani jezik"), ("Dostupni", "na mobitel u bilo koje doba dana")],
    steps_head=("Od prvog koraka do novih prilika", "Tri koraka do životopisa."),
    steps=[("Recite nam nešto o sebi", "Pošaljite nam postojeći životopis (ako ga imate) i svoje osnovne podatke (kopije potvrda o školovanju, popis poslova i radnih mjesta i osobne podatke: kontakt podaci, hobiji, vještine, interesi i sl.) putem Vibera, WhatsAppa ili e-maila. Sve počinje Vašom pričom."), ("Zajedno stvaramo najbolji dojam", "Biramo stil i strukturu životopisa koji najbolje ističu Vaše iskustvo, vještine i profesionalne ciljeve, odnosno koji se zahtijeva na poziciji za koju se prijavljujete."), ("Spremni za nove prilike", "Dobivate profesionalno oblikovan životopis i uvjerljivo motivacijsko pismo, po želji prevedene na strani jezik, spremne za Vašu prvu ili sljedeću veliku priliku.")],
    chips=("Što izrađujemo", ["Profesionalni životopis", "Akademski životopis", "Europass životopis", "Motivacijsko pismo", "Prijevod na strani jezik"]),
    sections=[
      ("Prvi dojam koji odlučuje", ["Umijeće sastavljanja dobrog životopisa jedna je od važnih stepenica na putu do željenog posla, studija ili stipendije za studij.", "Profesionalno oblikovan životopis i uvjerljivo motivacijsko pismo, koje se danas gotovo uvijek šalje uz životopis, često su prvi susret poslodavca ili obrazovne institucije s Vama.", "Dobar životopis mora zadovoljiti formalne zahtjeve, ali mora imati osobnu notu i istaknuti ono što Vas čini jedinstvenim kandidatom."], []),
      ("Životopis prilagođen Vašim ciljevima", ["Svaka karijera ima svoju priču. Uz našu pomoć ispričajte je u životopisu koji ostavlja dojam i otvara put novim prilikama.", "Ovisno o Vašem iskustvu, profesionalnom profilu i ciljevima, izrađujemo životopise u slobodnoj formi ili prema standardiziranim predlošcima, poput Europassa.", "Bilo da želite istaknuti svoj karijerni put ili predstaviti obrazovanje, znanstvene radove, istraživanja i stručna postignuća, profesionalni ili akademski životopis oblikujemo prema Vašim potrebama, ambicijama i ciljevima."], []),
    ],
    faq=[("Možete li životopis i prevesti?", "Da. Uz sastavljanje životopisa i motivacijskog pisma osiguravamo i prijevod na željeni strani jezik."), ("Što Vam trebam poslati?", "Postojeći životopis, ako ga imate, ili osnovne podatke o obrazovanju i radnom iskustvu, te natječaj ili oglas na koji se prijavljujete."), ("Kada ste dostupni?", HOURS)]),
  dict(slug="lektura",
    title="Lektura i korektura: akademski radovi, knjige, web | Orbita prijevodi",
    desc="Stručna lektura seminarskih, završnih i diplomskih radova, disertacija, knjiga, internetskih stranica i marketinških tekstova. Lektura jedne stranice već za 2 sata.",
    kicker="Lektura i korektura", micro="Pošaljite nam tekst i javljamo Vam cijenu i rok, bez obveze.", h1=("Lektura koja tekst čini ", "besprijekornim"),
    lead="Seminarski, završni i diplomski radovi, disertacije, knjige, internetske stranice ili marketinški tekstovi: pobrinut ćemo se da svaki tekst bude jezično besprijekoran i stilski dotjeran.",
    trust=[("Lekture obavljamo u vrlo kratkim rokovima", ""), ("Vrše ih profesori jezika", ""), ("Za obrazovne institucije izdajemo potvrdu o lekturi", ""), ("Dostupni na mobitel u bilo koje doba dana", "")],
    steps_head=("Put do dotjeranog teksta", "Tri koraka do lekture."),
    steps=[("Pošaljite tekst", "Na naše kontakte e-poštom, Viberom ili WhatsAppom."), ("Ponuda i rok", "Dogovaramo cijenu i rok, ovisno o vrsti i opsegu teksta. Nudimo i uslugu vrlo hitne lekture."), ("Besprijekoran tekst", "Dobivate jezično i stilski dotjeran tekst te, prema potrebi, komentare i prijedloge za pojašnjenje nejasnih dijelova.")],
    chips=("Specijalizirani smo za", ["Seminarski i maturalni radovi", "Završni i diplomski radovi", "Disertacije", "Znanstveni radovi", "Knjige i udžbenici", "Internetske stranice", "Marketinški tekstovi"]),
    sections=[
      ("Samo kod nas: stilsko-lingvistička lektura akademskih tekstova", ["U agenciji *Orbita* Vaše tekstove povjeravamo iskusnim lektorima, profesorima hrvatskog i stranih jezika, koji posebnu pozornost posvećuju svakom jezičnom i stilskom detalju. Osim ispravljanja gramatičkih, pravopisnih, interpunkcijskih i tipografskih pogrešaka, tekstove pažljivo jezično i stilski dotjeruju, pritom u potpunosti poštujući njihov izvorni sadržaj i autorovu misao. Ondje gdje je potrebno dodatno pojašnjenje, prilažu komentare i prijedloge, bez samostalnog zadiranja u sadržaj.", "Bilo da pišete *seminarski, maturalni, završni ili diplomski rad, odnosno doktorsku disertaciju*, jezična i stilska kvaliteta važan je dio njegova konačnog dojma. Pobrinut ćemo se da Vaš trud, znanje i istraživački rad budu predstavljeni jasno, stručno i besprijekornim jezikom."], []),
      ("Knjige, znanstveni radovi i internetske stranice", ["Od udžbenika, priručnika i edukativnih materijala do filozofskih djela, beletristike i znanstvenih radova, svakom tekstu pristupamo s jednakom pažnjom. Poštujemo stručnu terminologiju, autorski stil i posebnosti pojedinog područja, a prema potrebi surađujemo s autorima kako bismo postigli najbolje jezično i stilsko rješenje.", "*Prvi dojam često počinje upravo riječima.* Ako putem internetske stranice predstavljate svoje proizvode ili usluge, jasnoća, jezična ispravnost i uvjerljivost teksta mogu imati presudnu ulogu u tome kako Vas doživljavaju potencijalni klijenti. Profesionalno lektoriran tekst ulijeva povjerenje, odražava Vašu predanost kvaliteti i predstavlja Vašu ponudu u najboljem svjetlu."], []),
    ],
    faq=[("Koliko brzo možete lektorirati tekst?", "Lektura dokumenta od jedne stranice, do jedne kartice teksta od 1500 znakova bez razmaka, za najtraženije jezike (hrvatski, engleski, njemački, talijanski, slovenski i srpski) moguća je i unutar 2 sata od Vašeg upita. Opsežniji tekst, ovisno o broju kartica, vrsti teksta i jeziku, lektorirat ćemo unutar 8 dana."),
      ("Koliko košta lektura?", "Cijena ovisi o vrsti teksta, jeziku, broju kartica i roku isporuke. Jednostavniji tekstovi, poput letaka i brošura, jeftiniji su od zahtjevnih, poput diplomskih radova, a tekstovi na hrvatskom jeftiniji su od onih na stranim jezicima. Okvirno, lektura teksta na hrvatskom jeziku stoji od 3 do 6 eura po kartici od 1500 znakova bez razmaka, a hitna lektura može biti nešto skuplja."),
      ("Kako Vam mogu poslati tekst?", "E-poštom na info@orbitaprijevodi.com ili zagreb@orbitaprijevodi.com, Viberom ili WhatsAppom, ili ga donesite osobno u jedan od naših ureda."),
      ("Kada ste dostupni?", HOURS)]),
  dict(slug="medicinski-prijevodi",
    title="Medicinski prijevodi: nalazi, otpusna pisma, ovjereno | Orbita prijevodi",
    desc="Stručni i ovjereni prijevodi medicinske dokumentacije: nalazi, otpusna pisma, laboratorijska izvješća i istraživački tekstovi. Prevoditelji educirani u medicini, uz zaštitu podataka.",
    kicker="Prijevodi medicinske dokumentacije", h1=("Medicinski prijevodi: ", "stručnost i preciznost u svakoj riječi"),
    lead="Kad je zdravlje u pitanju, svaka je riječ važna. Naši prevoditelji sa stručnim znanjem iz područja medicine brinu se o preciznom prijevodu Vaših nalaza, otpusnih pisama i druge medicinske dokumentacije kako jezik ne bi bio prepreka liječenju ili traženju drugog stručnog mišljenja u inozemstvu.",
    trust=[("Medicinski", "educirani prevoditelji"), ("Ovjereno", "za nalaze i izvješća"), ("Povjerljivo", "uz zaštitu podataka"), ("1 sat", "do ponude")],
    steps=STEPS_TR, steps_head=("Vaša dokumentacija u pouzdanim rukama", "Tri koraka do prijevoda."),
    chips=("Prevodimo za Vas", ["Medicinski nalazi", "Otpusna pisma", "Medicinski dosjei", "Laboratorijska izvješća", "Medicinska osiguranja", "Istraživačka dokumentacija", "Priručnici i edukativni materijali", "Upute za medicinske proizvode"]),
    sections=[
      ("Bez jezičnih prepreka do liječenja", ["Kada je riječ o zdravlju, jasnoća i preciznost komunikacije od iznimne su važnosti. Stručnim prijevodima medicinske dokumentacije olakšavamo Vam pristup liječenju i medicinskim mišljenjima u inozemstvu. Prevodimo liječničke nalaze, medicinska izvješća, povijesti bolesti i otpusna pisma, a prema potrebi osiguravamo i *ovjeru stalnog sudskog tumača*."], []),
      ("Medicinski prijevodi u stručnim rukama", ["Medicinski prijevodi ubrajaju se među najzahtjevnije vrste stručnog prevođenja jer i najmanja terminološka pogreška može dovesti do pogrešnog tumačenja važnih zdravstvenih informacija. Zato Vašu dokumentaciju povjeravamo *iskusnim prevoditeljima s dodatnim obrazovanjem iz područja medicine*, koji izvrsno poznaju hrvatski i strane jezike te posebnu pozornost posvećuju točnosti, stručnom nazivlju i visokoj preciznosti prijevoda."], ["Interna medicina (kardiologija, hematologija, endokrinologija)", "Dermatologija", "Neurologija", "Ginekologija", "Psihijatrija", "Farmakologija", "Imunologija"]),
      ("Vaša privatnost naš je prioritet", ["Svjesni smo koliko je važna povjerljivost medicinske dokumentacije. Zato svim Vašim osobnim i zdravstvenim podacima, od informacija o bolesti i simptomima do dijagnostičkih postupaka, laboratorijskih nalaza i recepata, pristupamo s najvećom pažnjom i diskrecijom. Podatke obrađujemo i štitimo u skladu s važećim propisima o zaštiti osobnih podataka (GDPR), a pristup Vašoj dokumentaciji imaju isključivo članovi našeg prevoditeljskog tima koji sudjeluju u izradi prijevoda."], []),
    ],
    faq=[faq_tr("")[1], faq_tr("")[2], faq_tr("")[3], ("Prevodite li i stručne medicinske tekstove?", "Da. Osim dokumentacije pacijenata prevodimo istraživačke radove i tekstove iz svih područja medicine, predavanja za studente medicine, prezentacije, skripte, priručnike i konferencijske tekstove za zdravstvene djelatnike, kao i medicinsko-pravne tekstove poput diploma, licenci i dozvola za rad."), ("Kada ste dostupni?", HOURS)]),
]

def lp_nav(wa=None):
    n = LP_PHONE[2]; wa = wa or WA_TEXT
    return f'''<header class="nav nav-lp" id="nav">
  <a class="brand" href="../" aria-label="Orbita prijevodi, početna">
    <img src="../assets/orbita-logo.webp" alt="Orbita" width="473" height="108">
  </a>
  <div class="lp-actions">
    <a class="lp-phone" href="tel:+{PHONES[0][2]}"><span>Rijeka</span>{PHONES[0][1]}</a>
    <a class="lp-phone" href="tel:+{PHONES[1][2]}"><span>Zagreb</span>{PHONES[1][1]}</a>
    <a class="pill pill-ink" href="https://wa.me/{n}?text={wa}" target="_blank" rel="noopener">{"Pošaljite poruku" if wa != WA_TEXT else "Pošaljite dokument"}</a>
  </div>
</header>
'''

LP_IMAGES = {'sudski-tumac-za-engleski-jezik': ('1520986606214-8b456906c813', 'center 40%'), 'sudski-tumac-za-slovenski-jezik': ('1773658088032-87e28148ea1b', 'center'), 'sudski-tumac-za-srpski-jezik': ('1608816747977-4d303f476571', 'center'), 'sudski-tumaci-za-sve-jezike': ('1521295121783-8a321d551ad2', '70% center'), 'profesionalno-sastavljanje-zivotopisa-cv-curriculum-vitae': ('1499750310107-5fef28a66643', 'center'), 'lektura': ('1455390582262-044cdead277a', 'center 55%'), 'medicinski-prijevodi': ('1758691462848-ba1e929da259', 'center')}

def lp_intro(d):
    if "intro" not in d:
        return f'<p class="lead">{rich(d["lead"])}</p>'
    head_line, ps = d["intro"]
    return f'<p class="lead lp-hook">{e(head_line)}</p>' + "".join(f'<p class="lead lp-lead">{rich(p)}</p>' for p in ps)

def lp_form(d):
    svc = d["kicker"]
    return f'''<section class="section dark" id="upit">
    <div class="offer">
      <div class="offer-intro">
        <p class="label">Upit za ponudu</p>
        <h2>Pošaljite dokument i zatražite ponudu.</h2>
        <p class="sub">{rich(SEND_PHOTO)}</p>
        <p class="sub">Ponudu dobivate unutar sat vremena.</p>
      </div>
      {form_html(svc, "../send.php")}
    </div>
  </section>
'''

def lp_hero(d):
    n = LP_PHONE[2]; wa = d.get("wa", WA_TEXT)
    return f'''<section class="hero page-hero lp-hero">
    <div class="hero-bg lp-photo" aria-hidden="true" style="background-image:url(https://images.unsplash.com/photo-{LP_IMAGES[d["slug"]][0]}?auto=format&fit=crop&w=2000&q=70);background-position:{LP_IMAGES[d["slug"]][1]}"></div>
    <div class="hero-text">
      {offices_strip()}
      <p class="label lp-kicker">{e(d["kicker"])}</p>
      <h1>{e(d["h1"][0])}<em>{e(d["h1"][1])}</em></h1>
      {lp_intro(d)}
      <div class="hero-cta">
        <a class="pill pill-ink" href="https://wa.me/{n}?text={wa}" target="_blank" rel="noopener">{d.get("wa_label", "Pošaljite na WhatsApp")}</a>
        <a class="pill pill-line" href="viber://chat?number=%2B{n}">Viber</a>
        <a class="pill pill-line" href="tel:+{n}">Nazovite {LP_PHONE[1]}</a>
        <a class="pill pill-accent lp-formbtn" href="#upit">Pošaljite dokument putem kontakt obrasca i zatražite ponudu!</a>
      </div>
      <p class="lp-micro">{e(d.get("micro", "Fotografirajte dokument mobitelom i pošaljite ga, bez obveze."))}</p>
    </div>
  </section>
'''

def lp_page(d):
    path = f'{d["slug"]}/'
    sh = d.get("steps_head") or ("Kako to ide", d.get("steps_title", "Tri koraka do prijevoda."))
    trust = ''.join(f'<div><strong>{e(v)}</strong><span>{e(l)}</span></div>' if l else f'<div class="t-line"><strong>{e(v)}</strong></div>' for v, l in d["trust"])
    steps = ''.join(f'<li><span class="n">0{i+1}</span><h3>{e(t)}</h3><p>{e(p)}</p></li>' for i, (t, p) in enumerate(d["steps"]))
    secs = ''
    for h, paras, bullets in d["sections"]:
        secs += f'<h2>{e(h)}</h2>' + ''.join(f'<p>{rich(p)}</p>' for p in paras)
        if bullets: secs += '<ul class="lp-bullets">' + ''.join(f'<li>{e(b)}</li>' for b in bullets) + '</ul>'
    chips = ''.join(f'<li>{e(c)}</li>' for c in d["chips"][1])
    qs = d.get("quotes", QUOTES_LP)
    slides = ''.join(f'<figure class="lp-slide{" on" if i == 0 else ""}"><blockquote>{e(q)}</blockquote><figcaption><strong>{e(w)}</strong>{(" · " + e(r)) if r else ""}</figcaption></figure>' for i, (q, w, r) in enumerate(qs))
    on_cls = ' class="on"'
    dots = ''.join(f'<button type="button" aria-label="Preporuka {i+1}"{on_cls if i == 0 else ""}></button>' for i in range(len(qs)))
    quotes = f'<div class="lp-slider"><div class="lp-slides">{slides}</div><div class="lp-dots"><button type="button" class="lp-prev" aria-label="Prethodna">←</button>{dots}<button type="button" class="lp-next" aria-label="Sljedeća">→</button></div></div>'
    clients = ''.join(f'<span>{c}</span>' for c in CLIENTS)
    n = LP_PHONE[2]; wa = d.get("wa", WA_TEXT)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": d["h1"][0] + d["h1"][1], "description": d["desc"], "areaServed": ["Zagreb", "Rijeka", "Kastav", "Hrvatska"],
         "provider": {"@type": "ProfessionalService", "name": "Orbita prijevodi", "url": SITE + "/", "telephone": "+385981631930"}},
        faq_ld(d["faq"])]}
    body = f'''<section class="lp-trust" aria-label="Zašto Orbita">{trust}</section>
  <section class="section">
    <div class="section-head"><p class="label">{e(sh[0])}</p><h2>{e(sh[1])}</h2></div>
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
    <p class="label lp-proof-label">Što kažu klijenti</p>
    {quotes}
    <div class="lp-clients">{clients}</div>
  </section>
  ''' + faq_block(d["faq"]) + lp_form(d) + f'''  <section class="section">
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
