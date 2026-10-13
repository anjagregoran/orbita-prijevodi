// All editable text lists for the site live here.

const SERVICES = [
  {
    name: "Ovjereni prijevodi",
    short: "S pečatom i potpisom sudskog tumača",
    text: "Službene dokumente za Vas brzo i uredno pripremaju naši provjereni sudski tumači. Prijevod se uvezuje s izvornikom ili njegovom kopijom, a tumač pečatom i potpisom jamči da je istovjetan izvornom dokumentu.",
    items: ["Svjedodžbe i diplome", "Rodni i vjenčani listovi", "Radne dozvole", "Izvaci iz sudskog registra", "Stručna i vještačka mišljenja", "Medicinski nalazi"]
  },
  {
    name: "Pisani prijevodi",
    short: "Opći i stručni tekstovi iz svih područja",
    text: "Povjerite nam opće i stručne tekstove, rukopise, titlove, internetske stranice i programsku opremu. Na stručnim tekstovima rade prevoditelji koji poznaju područje i njegovu terminologiju, a za engleski i talijanski jezik nudimo i rad u CAT alatima.",
    items: ["Stručni i tehnički tekstovi", "Internetske stranice", "Programska oprema", "Titlovi", "Rukopisi"]
  },
  {
    name: "Usmeno prevođenje",
    short: "Simultano, konsekutivno i šaptano",
    text: "Izgovorenu riječ na Vašim događanjima prepustite prevoditeljima s velikim iskustvom i iznimnim poznavanjem jezika. Osiguravamo i sudskog tumača za javnog bilježnika ili sud, prevođenje uz pratnju te više jezika u istom danu.",
    items: ["Konferencije i seminari", "Poslovni sastanci i pregovori", "Sajmovi i prezentacije", "Sjednice i godišnje skupštine", "Javni bilježnik i sud"]
  },
  {
    name: "Lektura i korektura",
    short: "Jezična i stilska dorada prije objave",
    text: "Lektor jezično i stilski dotjeruje tekst te ispravlja pravopisne, interpunkcijske i tipografske pogreške. Preporučujemo da svaki tekst koji izlazi u javnost prije objave pregleda iskusan lektor.",
    items: ["Lektura izvornih tekstova", "Pregled prijevoda", "Korektura prije tiska"]
  },
  {
    name: "Životopisi i motivacijska pisma",
    short: "Prijava kojom se izdvajate među kandidatima",
    text: "Pomažemo Vam odabrati i sastaviti životopis i motivacijsko pismo prilagođene Vašem iskustvu, obrazovanju, interesima i ciljevima, a po želji ih i prevodimo na strani jezik.",
    items: ["Životopis (CV)", "Motivacijsko pismo", "Prijevod na strani jezik"]
  },
  {
    name: "Studij i posao u inozemstvu",
    short: "Eseji i prijavna dokumentacija",
    text: "Naši stručnjaci i sami su se školovali u inozemstvu. Kroz individualne konzultacije vode Vas u pripremi eseja i prijavne dokumentacije te u profesionalnom pisanju koje se danas očekuje na radnom mjestu.",
    items: ["Eseji za upis na sveučilište", "Prijave za stipendije", "Poslovna korespondencija", "Individualne konzultacije"]
  },
  {
    name: "Stručni tekstovi",
    short: "Pisanje prilagođeno struci",
    text: "Okupljamo stručnjake za pisanje tekstova u društvenim, tehničkim i prirodoslovnim područjima. Tekst strukturom, leksikom i stilom prilagođavamo struci, od opisa metodologije do predstavljanja rezultata.",
    items: ["Znanstveni i stručni radovi", "Opis metodologije i rezultata", "Molbe i prijave", "Mentorstvo u pisanju"]
  },
  {
    name: "Marketinški tekstovi",
    short: "Za tisak, radio, televiziju i internet",
    text: "Tekstove pišemo s pažnjom prema identitetu Vaše tvrtke i mediju u kojem se objavljuju. Tvrtkama pomažemo i u daljnjem predstavljanju na tržištu, od pisanja projekata do reklamnih tekstova.",
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
    text: "S tvrtkom Orbita surađujemo već duže vrijeme. Izuzetno su pouzdan i stručno potkovan partner koji se odmah odaziva i na kojega se uvijek možeš osloniti. Sve se odvija profesionalno i u dogovorenom roku.",
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
  hr: { name: "", label: "Prevoditeljska agencija", typed: "Vaša poruka, razumljiva svugdje.", head: ["Riječima ", "povezujemo", " svjetove."], lead: "Pisani, ovjereni i usmeni prijevodi na više od 30 jezika, uz lekturu i pisanje tekstova, sve na jednom mjestu i u roku koji Vam odgovara.", cta1: "Zatražite ponudu", cta2: "Pogledajte usluge" },
  en: { name: "English", label: "Translation agency", typed: "Your message, understood everywhere.", head: ["We ", "connect", " worlds through words."], lead: "Written, certified and spoken translation in more than 30 languages, with proofreading and copywriting, all in one place and on your deadline.", cta1: "Request a quote", cta2: "See our services" },
  ja: { name: "日本語", label: "翻訳会社", typed: "あなたのメッセージを、世界中へ。", head: ["言葉で世界を", "つなぐ", "。"], lead: "30以上の言語に対応した翻訳、公認翻訳、通訳。校正や文章作成まで、ご希望の納期でまとめてお任せください。", cta1: "お見積もりを依頼", cta2: "サービスを見る" },
  zh: { name: "中文", label: "翻译公司", typed: "您的信息，世界都能读懂。", head: ["用语言", "连接", "世界。"], lead: "提供30多种语言的笔译、认证翻译和口译服务，并提供校对与文案撰写，一站式服务，按您的时间交付。", cta1: "获取报价", cta2: "查看服务" }
};
