const $ = (s) => document.querySelector(s);

// Nav
const nav = $("#nav"), burger = $("#burger"), navLinks = $("#navLinks");
addEventListener("scroll", () => nav.classList.toggle("scrolled", scrollY > 20), { passive: true });
burger.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  burger.classList.toggle("open", open);
  burger.setAttribute("aria-expanded", open);
});
navLinks.addEventListener("click", () => { navLinks.classList.remove("open"); burger.classList.remove("open"); });

// Hero greeting
const greeting = $("#greeting");
let g = 0;
setInterval(() => {
  greeting.classList.add("out");
  setTimeout(() => {
    g = (g + 1) % GREETINGS.length;
    greeting.textContent = GREETINGS[g];
    greeting.classList.remove("out");
  }, 400);
}, 2600);

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
  li.innerHTML = `<button type="button">${l}</button>`;
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
    "",
    d.get("msg") || "",
    "",
    "Dokument šaljem u privitku.",
    "",
    "Srdačan pozdrav,",
    d.get("name")
  ];
  const subject = `Upit za ponudu${svc.length ? ": " + svc[0] : ""}`;
  location.href = `mailto:${d.get("office")}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join("\n"))}`;
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

$("#year").textContent = new Date().getFullYear();
