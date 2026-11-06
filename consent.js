// Cookie notice: Google Analytics (and the Google Ads link in it) loads only after the visitor accepts
(function () {
  var KEY = "orbita-consent", GA = "G-RWXVL3SGX0";
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  function loadAnalytics() {
    if (window.gtag) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date());
    gtag("config", GA);
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA;
    document.head.appendChild(s);
  }
  window.orbitaTrack = function (name, params) { if (window.gtag) gtag("event", name, params || {}); };

  // Calls, WhatsApp, Viber and e-mail clicks count as contacts (only when analytics is on)
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a || !window.gtag) return;
    var h = a.getAttribute("href");
    if (h.indexOf("tel:") === 0) orbitaTrack("click_call", { number: h.slice(4) });
    else if (h.indexOf("wa.me") > -1) orbitaTrack("click_whatsapp");
    else if (h.indexOf("viber:") === 0) orbitaTrack("click_viber");
    else if (h.indexOf("mailto:") === 0) orbitaTrack("click_email");
  });

  var root = document.querySelector('link[href*="styles.css"]').getAttribute("href").replace(/styles\.css.*$/, "");
  function banner() {
    if (document.getElementById("cookieBar")) return;
    var d = document.createElement("div");
    d.className = "cookie-bar"; d.id = "cookieBar"; d.setAttribute("role", "dialog"); d.setAttribute("aria-label", "Kolačići");
    d.innerHTML = '<p><strong>Kolačići</strong> Pomažu nam vidjeti kako posjetitelji pronalaze stranicu i koliko su uspješni naši oglasi. Analitičke i oglasne kolačiće uključujemo samo uz Vašu privolu. <a href="' + root + 'zastita-privatnosti/">Više o tome</a></p>' +
      '<div><button type="button" class="pill pill-line" data-c="necessary">Samo nužni</button><button type="button" class="pill pill-ink" data-c="all">Prihvaćam sve</button></div>';
    d.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-c]");
      if (!b) return;
      set(b.dataset.c);
      if (b.dataset.c === "all") loadAnalytics();
      else if (window.gtag) location.reload();
      d.remove();
    });
    document.body.appendChild(d);
  }

  document.addEventListener("click", function (e) {
    if (e.target.closest("[data-cookie-settings]")) { e.preventDefault(); banner(); }
  });

  var choice = get();
  if (choice === "all") loadAnalytics();
  else if (!choice) banner();
})();
