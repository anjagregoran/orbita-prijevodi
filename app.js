const $ = (s) => document.querySelector(s);

// Always start at the top after a refresh
history.scrollRestoration = "manual";
if (location.hash) history.replaceState(null, "", location.pathname);
scrollTo(0, 0);

// Typewriter line above the headline
const typed = $("#typed"), calm = matchMedia("(prefers-reduced-motion: reduce)").matches;
let typeTimer;
function typeLine(text) {
  clearTimeout(typeTimer);
  typed.textContent = "";
  if (calm) { typed.textContent = text; return; }
  (function type() {
    typed.textContent = text.slice(0, typed.textContent.length + 1);
    if (typed.textContent.length < text.length) typeTimer = setTimeout(type, 40 + Math.random() * 50);
  })();
}
typeTimer = setTimeout(() => typeLine(HERO_I18N.hr.typed), 700);

// The light bulb in the header: each press lights it and retypes the first screen in the next language
const bulb = $("#bulb"), hero = $(".hero"), heroLangs = Object.keys(HERO_I18N);
if (location.search.includes("warm")) hero.classList.add("warm");
let heroLang = 0;
bulb.addEventListener("click", () => {
  bulb.classList.remove("pull"); void bulb.offsetWidth; bulb.classList.add("pull");
  heroLang = (heroLang + 1) % heroLangs.length;
  const code = heroLangs[heroLang], t = HERO_I18N[code];
  bulb.classList.toggle("on", heroLang > 0);
  hero.classList.toggle("lit", heroLang > 0);
  $("#bulbLang").textContent = t.name;
  if (scrollY > 80) scrollTo({ top: 0, behavior: "smooth" });
  hero.classList.add("swap");
  typeLine(t.typed);
  setTimeout(() => {
    $("#hLabel").textContent = t.label;
    $("#hHead").innerHTML = `${t.head[0]}<wbr><em>${t.head[1]}</em>${t.head[2]}`;
    $("#hHead").lang = $("#hLead").lang = code;
    $("#hLead").textContent = t.lead;
    $("#hCta1").textContent = t.cta1;
    $("#hCta2").textContent = t.cta2;
    $("#hF1").textContent = t.f1;
    $("#hF2").textContent = t.f2;
    hero.classList.remove("swap");
  }, 260);
});

// Nav
const nav = $("#nav"), burger = $("#burger"), navLinks = $("#navLinks");
const heroEl = $(".hero");
const onScroll = () => {
  nav.classList.toggle("scrolled", scrollY > 20);
  nav.classList.toggle("on-dark", scrollY < heroEl.offsetHeight - 70);
};
addEventListener("scroll", onScroll, { passive: true });
onScroll();
burger.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  burger.classList.toggle("open", open);
  burger.setAttribute("aria-expanded", open);
});
navLinks.addEventListener("click", () => { navLinks.classList.remove("open"); burger.classList.remove("open"); });

// Services
const svcList = $("#svcList"), svcPanel = $("#svcPanel");
function showService(i) {
  const s = SERVICES[i];
  [...svcList.children].forEach((li, n) => li.classList.toggle("active", n === i));
  svcPanel.innerHTML = `
    <p class="label">${String(i + 1).padStart(2, "0")} / ${String(SERVICES.length).padStart(2, "0")}</p>
    <h3>${s.name}</h3>
    <p>${s.text}</p>
    <ul>${s.items.map((x) => `<li>${x}</li>`).join("")}</ul>
    <a class="pill pill-ink" href="#ponuda" data-svc="${s.name}">Zatražite ponudu za ovu uslugu</a>`;
  svcPanel.classList.remove("in");
  void svcPanel.offsetWidth;
  svcPanel.classList.add("in");
}
SERVICES.forEach((s, i) => {
  const li = document.createElement("li");
  li.innerHTML = `<button role="tab"><span class="svc-name">${s.name}</span><span class="svc-short">${s.short}</span></button>`;
  li.firstChild.addEventListener("click", () => {
    showService(i);
    if (innerWidth < 900) svcPanel.scrollIntoView({ behavior: "smooth", block: "nearest" });
  });
  li.firstChild.addEventListener("mouseenter", () => { if (innerWidth >= 900) showService(i); });
  svcList.appendChild(li);
});
showService(0);

// Languages
const langs = $("#langs"), langInput = $("#langInput"), langEmpty = $("#langEmpty");
const plain = (s) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d");
LANGUAGES.forEach((l) => {
  const li = document.createElement("li");
  li.innerHTML = `<button type="button"><img src="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/flags/1x1/${FLAGS[l]}.svg" alt="" width="24" height="24" loading="lazy">${l}</button>`;
  li.firstChild.addEventListener("click", () => {
    form.elements.to.value = l;
    $("#ponuda").scrollIntoView({ behavior: "smooth" });
  });
  langs.appendChild(li);
  $("#langList").insertAdjacentHTML("beforeend", `<option value="${l}">`);
});
langInput.addEventListener("input", () => {
  const q = plain(langInput.value.trim());
  let shown = 0;
  [...langs.children].forEach((li) => {
    const hit = plain(li.textContent).includes(q);
    li.hidden = !hit;
    if (hit) shown++;
  });
  langEmpty.hidden = shown > 0;
});

// Testimonials
const stage = $("#quoteStage");
let q = 0, qTimer;
function showQuote(i) {
  q = (i + QUOTES.length) % QUOTES.length;
  const t = QUOTES[q];
  stage.classList.remove("in");
  setTimeout(() => {
    stage.innerHTML = `<blockquote>${t.text}</blockquote><p class="who"><strong>${t.who}</strong>${t.role}</p>`;
    $("#qCount").textContent = `${q + 1} / ${QUOTES.length}`;
    stage.classList.add("in");
  }, 250);
  clearInterval(qTimer);
  qTimer = setInterval(() => showQuote(q + 1), 8000);
}
$("#qPrev").addEventListener("click", () => showQuote(q - 1));
$("#qNext").addEventListener("click", () => showQuote(q + 1));
showQuote(0);

// Quote form
const form = $("#quoteForm"), chips = $("#svcChips"), note = $("#formNote");
SERVICES.forEach((s) => {
  chips.insertAdjacentHTML("beforeend", `<label class="chip"><input type="checkbox" name="svc" value="${s.name}"><span>${s.name}</span></label>`);
});
document.addEventListener("click", (e) => {
  const a = e.target.closest("[data-svc]");
  if (!a) return;
  chips.querySelectorAll("input").forEach((c) => (c.checked = c.value === a.dataset.svc));
  if (a.dataset.doc) form.elements.msg.value = `Dokument: ${a.dataset.doc}`;
});
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const d = new FormData(form);
  if (!d.get("name").trim()) {
    note.textContent = "Upišite ime i prezime kako bismo znali kome odgovaramo.";
    form.elements.name.focus();
    return;
  }
  const svc = d.getAll("svc");
  const lines = [
    "Poštovani,",
    "",
    "molim Vas ponudu za sljedeće:",
    "",
    `Usluga: ${svc.length ? svc.join(", ") : "nije odabrano"}`,
    `S jezika: ${d.get("from") || "/"}`,
    `Na jezik: ${d.get("to") || "/"}`,
    `Rok: ${d.get("deadline") || "po dogovoru"}`,
    `Ured: ${d.get("office")}`,
    "",
    d.get("msg") || "",
    "",
    "Dokument šaljem u privitku.",
    "",
    "Srdačan pozdrav,",
    d.get("name")
  ];
  const subject = `Upit za ponudu${svc.length ? ": " + svc[0] : ""}`;
  // Every enquiry goes to both offices
  location.href = `mailto:info@orbitaprijevodi.com,zagreb@orbitaprijevodi.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join("\n"))}`;
  note.textContent = "Upit se otvorio u Vašem programu za e-poštu. Priložite dokument i pošaljite poruku.";
});

// Reveal on scroll
const io = new IntersectionObserver((entries) => {
  entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("shown"); io.unobserve(en.target); } });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

// Floating button hides once the form is on screen
const floatCta = $(".float-cta");
new IntersectionObserver(([en]) => floatCta.classList.toggle("hide", en.isIntersecting), { threshold: 0.05 }).observe($("#ponuda"));

// Decorative letters drift a little as the page scrolls
const glyphs = [...document.querySelectorAll(".glyph")];
if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const drift = () => glyphs.forEach((gl) => {
    const r = gl.parentElement.getBoundingClientRect();
    gl.style.transform = `translateY(${(r.top - innerHeight / 2) * gl.dataset.speed}px)`;
  });
  addEventListener("scroll", drift, { passive: true });
  drift();
}

// The photo behind the first screen drifts with scrolling and with the mouse
const heroBg = $("#heroBg");
if (!calm) {
  let bx = 0, by = 0, tx = 0, ty = 0;
  addEventListener("pointermove", (e) => { tx = e.clientX / innerWidth - 0.5; ty = e.clientY / innerHeight - 0.5; }, { passive: true });
  (function drift() {
    bx += (tx - bx) * 0.06; by += (ty - by) * 0.06;
    if (scrollY < innerHeight * 1.2) heroBg.style.transform = `translate3d(${bx * -46}px, ${by * -30 + scrollY * 0.32}px, 0) scale(1.04)`;
    requestAnimationFrame(drift);
  })();
}

$("#year").textContent = new Date().getFullYear();
