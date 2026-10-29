// All editable text lists for the site live here.

const SERVICES = [
  {
    name: "Ovjereni prijevodi",
    slug: "ovjereni-prijevodi",
    short: "S pečatom i potpisom sudskog tumača",
    text: "Službene dokumente za Vas brzo i uredno pripremaju naši provjereni sudski tumači. Prijevod se uvezuje s izvornikom ili njegovom kopijom, a tumač pečatom i potpisom jamči da je istovjetan izvornom dokumentu.",
    items: ["Svjedodžbe i diplome", "Rodni i vjenčani listovi", "Radne dozvole", "Izvaci iz sudskog registra", "Stručna i vještačka mišljenja", "Medicinski nalazi"]
  },
  {
    name: "Pisani prijevodi",
    slug: "pisani-prijevodi",
    short: "Opći i stručni tekstovi iz svih područja",
    text: "Povjerite nam opće i stručne tekstove, rukopise, titlove, internetske stranice i programsku opremu. Na stručnim tekstovima rade prevoditelji koji poznaju područje i njegovu terminologiju, a za engleski i talijanski jezik nudimo i rad u CAT alatima.",
    items: ["Stručni i tehnički tekstovi", "Internetske stranice", "Programska oprema", "Titlovi", "Rukopisi"]
  },
  {
    name: "Usmeno prevođenje",
    slug: "usmeni-prijevodi",
    short: "Simultano, konsekutivno i šaptano",
    text: "Izgovorenu riječ na Vašim događanjima prepustite prevoditeljima s velikim iskustvom i iznimnim poznavanjem jezika. Osiguravamo i sudskog tumača za javnog bilježnika ili sud, prevođenje uz pratnju te više jezika u istom danu.",
    items: ["Konferencije i seminari", "Poslovni sastanci i pregovori", "Sajmovi i prezentacije", "Sjednice i godišnje skupštine", "Javni bilježnik i sud"]
  },
  {
    name: "Lektura i korektura",
    slug: "lektoriranje",
    short: "Jezična i stilska dorada prije objave",
    text: "Lektor jezično i stilski dotjeruje tekst te ispravlja pravopisne, interpunkcijske i tipografske pogreške. Preporučujemo da svaki tekst koji izlazi u javnost prije objave pregleda iskusan lektor.",
    items: ["Lektura izvornih tekstova", "Pregled prijevoda", "Korektura prije tiska"]
  },
  {
    name: "Životopisi i motivacijska pisma",
    slug: "asistiranje-u-pisanju-teksta",
    short: "Prijava kojom se izdvajate među kandidatima",
    text: "Pomažemo Vam odabrati i sastaviti životopis i motivacijsko pismo prilagođene Vašem iskustvu, obrazovanju, interesima i ciljevima, a po želji ih i prevodimo na strani jezik.",
    items: ["Životopis (CV)", "Motivacijsko pismo", "Prijevod na strani jezik"]
  },
  {
    name: "Studij i posao u inozemstvu",
    slug: "pisanje-dokumentacije-za-studij-i-zaposlenje-u-inozemstvu",
    short: "Eseji i prijavna dokumentacija",
    text: "Naši stručnjaci i sami su se školovali u inozemstvu. Kroz individualne konzultacije vode Vas u pripremi eseja i prijavne dokumentacije te u profesionalnom pisanju koje se danas očekuje na radnom mjestu.",
    items: ["Eseji za upis na sveučilište", "Prijave za stipendije", "Poslovna korespondencija", "Individualne konzultacije"]
  },
  {
    name: "Stručni tekstovi",
    slug: "pisanje-u-raznim-profesionalnim-podrucjima",
    short: "Pisanje prilagođeno struci",
    text: "Okupljamo stručnjake za pisanje tekstova u društvenim, tehničkim i prirodoslovnim područjima. Tekst strukturom, leksikom i stilom prilagođavamo struci, od opisa metodologije do predstavljanja rezultata.",
    items: ["Znanstveni i stručni radovi", "Opis metodologije i rezultata", "Molbe i prijave", "Mentorstvo u pisanju"]
  },
  {
    name: "Marketinški tekstovi",
    slug: "marketinski-tekstovi",
    short: "Za tisak, radio, televiziju i internet",
    text: "Tekstove pišemo s pažnjom prema identitetu Vaše tvrtke i mediju u kojem se objavljuju. Poslovnim subjektima pomažemo i u daljnjem predstavljanju na tržištu, od pisanja projekata do reklamnih tekstova.",
    items: ["Reklame", "Brošure i katalozi", "Pozivnice i cjenici", "Tekstovi za mrežne stranice"]
  }
];

const LANGUAGES = [
  "Hrvatski", "Engleski", "Njemački", "Talijanski", "Francuski", "Španjolski", "Srpski", "Bosanski",
  "Slovenski", "Ruski", "Bugarski", "Makedonski", "Albanski", "Češki", "Slovački", "Poljski",
  "Mađarski", "Grčki", "Portugalski", "Ukrajinski", "Švedski", "Nizozemski", "Danski", "Litavski",
  "Turski", "Hebrejski", "Arapski", "Japanski", "Kineski", "Perzijski", "Rumunjski", "Latinski"
];

const QUOTES = [
  {
    text: "S prevoditeljskom agencijom Orbita surađujemo već duže vrijeme. Izuzetno su pouzdan i stručno potkovan partner koji se odmah odaziva i na kojega se uvijek možeš osloniti. Sve se odvija profesionalno i u dogovorenom roku.",
    who: "Robert Šefman", role: "IT, Petrol d.d., Ljubljana"
  },
  {
    text: "Imali smo dosta obiman tekst za prijevod, korisničke upute i jamstvene listove. Odabrali smo ih po preporuci i jako smo zadovoljni obavljenim poslom.",
    who: "Primož Prosen", role: "Product Manager, Euroton d.o.o."
  },
  {
    text: "U prevoditeljskoj agenciji Orbita dobili smo svu potrebnu podršku. Pokazali su se vrlo fleksibilnim i pouzdanim poslovnim partnerom koji je odličan u pronalaženju rješenja za najteže i najsloženije probleme.",
    who: "Anita Satler", role: "direktorica, AKTA Co d.o.o."
  },
  {
    text: "Ne samo da su odmah riješili zadatak, cijelom poslu dodali su i jednu dublju dimenziju. Svojim osobnim pristupom posao pretvaraju u suradnju. Izuzetno mi je zadovoljstvo raditi s Orbitom.",
    who: "Zoran Mandić", role: "tehnički direktor, Inspirion d.o.o."
  },
  {
    text: "Obratila sam se agenciji Orbita i u vrlo kratkom roku dobila odlično napravljen životopis i motivacijsko pismo s prijevodom na njemački jezik. Oduševila me fleksibilnost i individualni pristup mojim potrebama.",
    who: "AMB", role: "liječnica"
  },
  {
    text: "Osobno sam vrlo zadovoljan temeljito izrađenim CV-jem koji mi je napravljen u agenciji Orbita. Profesionalno, detaljno, vremenski brzo i financijski pristojno.",
    who: "Milan Drenovac", role: "pomorac"
  }
];

// Country flag shown next to each language
const FLAGS = {
  Hrvatski: "hr", Engleski: "gb", Njemački: "de", Talijanski: "it", Francuski: "fr", Španjolski: "es",
  Srpski: "rs", Bosanski: "ba", Slovenski: "si", Ruski: "ru", Bugarski: "bg", Makedonski: "mk",
  Albanski: "al", Češki: "cz", Slovački: "sk", Poljski: "pl", Mađarski: "hu", Grčki: "gr",
  Portugalski: "pt", Ukrajinski: "ua", Švedski: "se", Nizozemski: "nl", Danski: "dk", Litavski: "lt",
  Turski: "tr", Hebrejski: "il", Arapski: "sa", Japanski: "jp", Kineski: "cn", Perzijski: "ir",
  Rumunjski: "ro", Latinski: "va"
};

// First-screen text in other languages (the light bulb in the header steps through them)
const HERO_I18N = {
  hr: { f1: "jezika", f2: "vrsta usluga", name: "", label: "Prevoditeljska agencija", typed: "Vaša poruka, razumljiva svugdje.", head: ["Riječima ", "povezujemo", " svjetove."], lead: "Pisani, ovjereni i usmeni prijevodi na više od 30 jezika, uz lekturu i pisanje tekstova, sve na jednom mjestu i u roku koji Vam odgovara.", cta1: "Zatražite ponudu", cta2: "Pogledajte usluge" },
  sl: { f1: "jezikov", f2: "vrst storitev", name: "Slovenščina", label: "Prevajalska agencija", typed: "Vaše sporočilo, razumljivo povsod.", head: ["Z besedami ", "povezujemo", " svetove."], lead: "Pisni, sodni in ustni prevodi v več kot 30 jezikov, z lektoriranjem in pisanjem besedil, vse na enem mestu in v roku, ki vam ustreza.", cta1: "Zahtevajte ponudbo", cta2: "Oglejte si storitve" },
  de: { f1: "Sprachen", f2: "Leistungen", name: "Deutsch", label: "Übersetzungsbüro", typed: "Ihre Botschaft, überall verstanden.", head: ["Worte ", "verbinden", " Welten."], lead: "Fachübersetzungen, beglaubigte Übersetzungen und Dolmetschen in über 30 Sprachen, dazu Lektorat und Texte, alles aus einer Hand und termingerecht.", cta1: "Angebot anfordern", cta2: "Leistungen ansehen" },
  sr: { f1: "jezika", f2: "vrsta usluga", name: "Srpski", label: "Prevodilačka agencija", typed: "Vaša poruka, razumljiva svuda.", head: ["Rečima ", "povezujemo", " svetove."], lead: "Pisani, overeni i usmeni prevodi na više od 30 jezika, uz lekturu i pisanje tekstova, sve na jednom mestu i u roku koji Vam odgovara.", cta1: "Zatražite ponudu", cta2: "Pogledajte usluge" }
};
