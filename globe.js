// Hero: a huge globe seen from orbit, rising from the bottom of the first screen.
// Croatian words leave Croatia in blue and land translated in orange.
(function () {
  const el = document.getElementById("globe");
  if (!el) return;
  const ctx = el.getContext("2d");
  const INK = "35,39,46", BLUE = "65,146,197", CORAL = "214,90,61", CREAM = "250,248,244";
  const RAD = Math.PI / 180;
  const TILT = 28 * RAD, cp = Math.cos(TILT), sp = Math.sin(TILT);
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const vec = (lat, lon) => {
    const cl = Math.cos(lat * RAD);
    return [cl * Math.sin(lon * RAD), Math.sin(lat * RAD), cl * Math.cos(lon * RAD)];
  };
  const HUB = vec(45.6, 15.4);
  function flagImage(cc) {
    const img = new Image();
    img.src = `https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/flags/1x1/${cc}.svg`;
    return img;
  }

  // Each language: thank you, hi, welcome, love, peace
  const SOURCE = ["hvala", "bok", "dobrodošli", "ljubav", "mir"];
  const LANG = {
    en: ["thank you", "hello", "welcome", "love", "peace"],
    de: ["danke", "hallo", "willkommen", "Liebe", "Frieden"],
    es: ["gracias", "hola", "bienvenidos", "amor", "paz"],
    fr: ["merci", "salut", "bienvenue", "amour", "paix"],
    it: ["grazie", "ciao", "benvenuti", "amore", "pace"],
    pt: ["obrigado", "olá", "bem-vindos", "amor", "paz"],
    nl: ["dank je", "hallo", "welkom", "liefde", "vrede"],
    sv: ["tack", "hej", "välkommen", "kärlek", "fred"],
    da: ["tak", "hej", "velkommen", "kærlighed", "fred"],
    pl: ["dziękuję", "cześć", "witamy", "miłość", "pokój"],
    cs: ["děkuji", "ahoj", "vítejte", "láska", "mír"],
    hu: ["köszönöm", "szia", "üdvözöljük", "szerelem", "béke"],
    ro: ["mulțumesc", "salut", "bun venit", "dragoste", "pace"],
    bg: ["благодаря", "здравей", "добре дошли", "любов", "мир"],
    sq: ["faleminderit", "tungjatjeta", "mirë se vini", "dashuri", "paqe"],
    lt: ["ačiū", "labas", "sveiki atvykę", "meilė", "taika"],
    uk: ["дякую", "привіт", "ласкаво просимо", "любов", "мир"],
    ru: ["спасибо", "привет", "добро пожаловать", "любовь", "мир"],
    el: ["ευχαριστώ", "γεια σου", "καλώς ήρθατε", "αγάπη", "ειρήνη"],
    tr: ["teşekkürler", "merhaba", "hoş geldiniz", "aşk", "barış"],
    he: ["תודה", "שלום", "ברוכים הבאים", "אהבה", "שלום"],
    ar: ["شكرا", "مرحبا", "أهلا وسهلا", "حب", "سلام"],
    fa: ["ممنون", "سلام", "خوش آمدید", "عشق", "صلح"],
    zh: ["谢谢", "你好", "欢迎", "爱", "和平"],
    ja: ["ありがとう", "こんにちは", "ようこそ", "愛", "平和"]
  };
  const CITIES = [
    [51.5, -0.1, "en", "gb"], [52.5, 13.4, "de", "de"], [40.4, -3.7, "es", "es"], [48.9, 2.3, "fr", "fr"], [41.9, 12.5, "it", "it"],
    [38.7, -9.1, "pt", "pt"], [52.4, 4.9, "nl", "nl"], [59.3, 18.1, "sv", "se"], [55.7, 12.6, "da", "dk"], [52.2, 21, "pl", "pl"],
    [50.1, 14.4, "cs", "cz"], [47.5, 19, "hu", "hu"], [44.4, 26.1, "ro", "ro"], [42.7, 23.3, "bg", "bg"], [41.3, 19.8, "sq", "al"],
    [54.7, 25.3, "lt", "lt"], [50.5, 30.5, "uk", "ua"], [55.8, 37.6, "ru", "ru"], [38, 23.7, "el", "gr"], [39.9, 32.9, "tr", "tr"],
    [32.1, 34.8, "he", "il"], [30, 31.2, "ar", "eg"], [24.7, 46.7, "ar", "sa"], [35.7, 51.4, "fa", "ir"], [39.9, 116.4, "zh", "cn"],
    [35.7, 139.7, "ja", "jp"], [40.7, -74, "en", "us"], [45.5, -73.6, "fr", "ca"], [19.4, -99.1, "es", "mx"], [-34.6, -58.4, "es", "ar"],
    [-23.5, -46.6, "pt", "br"], [14.7, -17.4, "fr", "sn"], [-33.9, 18.4, "en", "za"], [-33.9, 151.2, "en", "au"], [1.35, 103.8, "zh", "sg"],
    [25.2, 55.3, "ar", "ae"]
  ].map(([lat, lon, lang, cc]) => ({ lang, words: LANG[lang], v: vec(lat, lon), flag: flagImage(cc) }));

  const HR = flagImage("hr");

  let W = 0, H = 0, R = 0, S = 0, cx = 0, cy = 0, dpr = 1;
  let dots = [], arcs = [], lam = 0, user = 0, vel = 0, dragging = false, lastX = 0;
  let visible = true, lastSpawn = 0, turn = 0, now_t = 0, moved = 0;
  const used = new Set();

  function size() {
    W = el.clientWidth; H = W;
    R = W * 0.41;
    S = Math.min(1.1, Math.max(0.6, R / 330));
    dpr = Math.min(devicePixelRatio || 1, W > 900 ? 1.5 : 2);
    el.width = Math.round(W * dpr); el.height = Math.round(H * dpr);
    cx = W / 2; cy = H * 0.475;
  }

  // Rotate a geo vector into view space, then project it flat.
  function proj(v, alt) {
    const cl = Math.cos(lam), sl = Math.sin(lam);
    const x = v[0] * cl - v[2] * sl, z = v[0] * sl + v[2] * cl;
    const y = v[1] * cp - z * sp, z2 = v[1] * sp + z * cp;
    const a = alt || 1;
    return [cx + R * a * x, cy - R * a * y, z2 * a];
  }
  const shown = (p) => p[2] > 0 || Math.hypot(p[0] - cx, p[1] - cy) > R;
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

  function fibonacci(n, keep) {
    const out = [], ga = Math.PI * (3 - Math.sqrt(5));
    for (let i = 0; i < n; i++) {
      const y = 1 - (2 * (i + 0.5)) / n, lat = Math.asin(y) / RAD;
      let lon = ((i * ga) / RAD) % 360; if (lon > 180) lon -= 360;
      if (keep(lat, lon, i)) out.push(vec(lat, lon));
    }
    return out;
  }

  async function loadLand() {
    try {
      const topo = await fetch("https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/land-110m.json").then((r) => r.json());
      const land = topojson.feature(topo, topo.objects.land);
      const mw = 720, mh = 360, m = document.createElement("canvas");
      m.width = mw; m.height = mh;
      const c = m.getContext("2d");
      c.beginPath();
      const polys = land.features ? land.features.flatMap((f) => f.geometry.coordinates) : land.geometry.coordinates;
      polys.forEach((poly) => poly.forEach((ring) => {
        ring.forEach(([lon, lat], i) => {
          const x = ((lon + 180) / 360) * mw, y = ((90 - lat) / 180) * mh;
          i ? c.lineTo(x, y) : c.moveTo(x, y);
        });
        c.closePath();
      }));
      c.fill("evenodd");
      const data = c.getImageData(0, 0, mw, mh).data;
      dots = fibonacci(46000, (lat, lon) => {
        if (lat < -60) return false;
        const x = Math.min(mw - 1, Math.floor(((lon + 180) / 360) * mw)), y = Math.min(mh - 1, Math.floor(((90 - lat) / 180) * mh));
        return data[(y * mw + x) * 4 + 3] > 120;
      });
    } catch (e) {
      dots = fibonacci(2000, () => true);
    }
    if (still) draw(0);
  }

  function slerp(a, b, t) {
    const om = Math.acos(Math.min(1, dot(a, b))), s = Math.sin(om) || 1;
    const k1 = Math.sin((1 - t) * om) / s, k2 = Math.sin(t * om) / s;
    return [a[0] * k1 + b[0] * k2, a[1] * k1 + b[1] * k2, a[2] * k1 + b[2] * k2];
  }

  function line(f, n) {
    let pen = false;
    for (let i = 0; i <= n; i++) {
      const p = proj(f(i));
      if (p[2] > 0.02) { pen ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]); pen = true; } else pen = false;
    }
  }

  function ring(tiltZ, tiltX, r, t, color, front) {
    const cz = Math.cos(tiltZ), sz = Math.sin(tiltZ), cxr = Math.cos(tiltX), sxr = Math.sin(tiltX);
    const pt = (a) => {
      const x = Math.cos(a) * r, z = Math.sin(a) * r;
      const x1 = x * cz, y1 = x * sz;
      return [cx + R * x1, cy - R * (y1 * cxr - z * sxr), y1 * sxr + z * cxr];
    };
    ctx.lineWidth = 1.2;
    ctx.strokeStyle = `rgba(${color},${front ? 0.6 : 0.25})`;
    ctx.beginPath();
    let pen = false;
    for (let i = 0; i <= 240; i++) {
      const p = pt((i / 240) * Math.PI * 2);
      if (p[2] > 0 === front) { pen ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]); pen = true; } else pen = false;
    }
    ctx.stroke();
    const s = pt(t);
    if (s[2] > 0 === front) {
      ctx.fillStyle = `rgb(${color})`;
      ctx.beginPath(); ctx.arc(s[0], s[1], 5 * S, 0, 7); ctx.fill();
    }
  }

  function word(text, x, y, color, alpha, flag) {
    ctx.font = `italic 400 ${Math.round(22 * S)}px "Fraunces", Georgia, serif`;
    ctx.textBaseline = "middle";
    const h = 40 * S, top = y - h - 12 * S, tw = ctx.measureText(text).width;
    ctx.globalAlpha = alpha;
    if (!flag) {
      ctx.textAlign = "center"; ctx.lineJoin = "round"; ctx.strokeStyle = "rgba(255,255,255,0.9)"; ctx.lineWidth = 6 * S;
      ctx.strokeText(text, x, top + h / 2);
      ctx.fillStyle = `rgb(${color})`;
      ctx.fillText(text, x, top + h / 2 + 1);
    } else {
      const fr = h * 0.34, ready = flag.complete && flag.naturalWidth > 0;
      const w = tw + 32 * S + (ready ? fr * 2 + 8 * S : 0), left = x - w / 2;
      ctx.fillStyle = "#fff";
      ctx.shadowColor = `rgba(${INK},0.2)`; ctx.shadowBlur = 18; ctx.shadowOffsetY = 5;
      ctx.beginPath(); ctx.roundRect(left, top, w, h, h / 2); ctx.fill();
      ctx.shadowColor = "transparent"; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0;
      let tx = left + 16 * S;
      if (ready) {
        const fx = left + 8 * S + fr, fy = top + h / 2;
        ctx.save();
        ctx.beginPath(); ctx.arc(fx, fy, fr, 0, 7); ctx.clip();
        ctx.drawImage(flag, fx - fr, fy - fr, fr * 2, fr * 2);
        ctx.restore();
        ctx.strokeStyle = `rgba(${INK},0.14)`; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.arc(fx, fy, fr, 0, 7); ctx.stroke();
        tx = fx + fr + 8 * S;
      }
      ctx.textAlign = "left";
      ctx.fillStyle = `rgb(${color})`;
      ctx.fillText(text, tx, top + h / 2 + 1);
    }
    ctx.globalAlpha = 1;
  }

  function draw(now) {
    const t = now / 1000;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    lam = (15 + 82 * Math.sin(t * 0.13)) * RAD + user;

    ring(-0.42, 1.25, 1.2, t * 0.22 + 1, BLUE, false);
    ring(0.5, 1.12, 1.11, -t * 0.3 + 2.4, CORAL, false);

    // Soft shadow under the globe
    ctx.save();
    ctx.translate(cx, cy + R * 1.1); ctx.scale(1, 0.1);
    const sh = ctx.createRadialGradient(0, 0, 0, 0, 0, R * 0.85);
    sh.addColorStop(0, `rgba(${INK},0.22)`); sh.addColorStop(1, `rgba(${INK},0)`);
    ctx.fillStyle = sh;
    ctx.beginPath(); ctx.arc(0, 0, R * 0.85, 0, 7); ctx.fill();
    ctx.restore();

    // Atmosphere, then sphere body
    const halo = ctx.createRadialGradient(cx, cy, R * 0.97, cx, cy, R * 1.17);
    halo.addColorStop(0, `rgba(${BLUE},0.5)`); halo.addColorStop(0.4, `rgba(${BLUE},0.16)`); halo.addColorStop(1, `rgba(${BLUE},0)`);
    ctx.fillStyle = halo;
    ctx.beginPath(); ctx.arc(cx, cy, R * 1.17, 0, 7); ctx.fill();
    const g = ctx.createRadialGradient(cx - R * 0.42, cy - R * 0.48, R * 0.02, cx, cy, R);
    g.addColorStop(0, "#ffffff"); g.addColorStop(0.45, "#eef6fb"); g.addColorStop(1, "#cfe4f3");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, 7); ctx.fill();

    // Latitude and longitude lines
    ctx.strokeStyle = "rgba(255,255,255,0.9)"; ctx.lineWidth = 1;
    ctx.beginPath();
    for (let lon = -180; lon < 180; lon += 20) line((i) => vec(-80 + (i * 160) / 40, lon), 40);
    for (let lat = -60; lat <= 80; lat += 20) line((i) => vec(lat, -180 + (i * 360) / 90), 90);
    ctx.stroke();

    // Land
    const ds = Math.max(1.1, R * 0.0066);
    for (let i = 0; i < dots.length; i++) {
      const p = proj(dots[i]);
      if (p[2] <= 0.02) continue;
      ctx.fillStyle = `rgba(${BLUE},${0.55 + 0.45 * p[2]})`;
      ctx.beginPath(); ctx.arc(p[0], p[1], ds * (0.6 + 0.4 * p[2]), 0, 7); ctx.fill();
    }

    // Light from the top left, shade towards the bottom right
    ctx.save();
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, 7); ctx.clip();
    const shade = ctx.createRadialGradient(cx - R * 0.35, cy - R * 0.4, R * 0.5, cx - R * 0.1, cy - R * 0.1, R * 1.25);
    shade.addColorStop(0, "rgba(40,105,155,0)"); shade.addColorStop(1, "rgba(40,105,155,0.42)");
    ctx.fillStyle = shade; ctx.fillRect(cx - R, cy - R, R * 2, R * 2);
    const shine = ctx.createRadialGradient(cx - R * 0.45, cy - R * 0.5, 0, cx - R * 0.45, cy - R * 0.5, R * 0.75);
    shine.addColorStop(0, "rgba(255,255,255,0.55)"); shine.addColorStop(1, "rgba(255,255,255,0)");
    ctx.fillStyle = shine; ctx.fillRect(cx - R, cy - R, R * 2, R * 2);
    ctx.restore();
    ctx.strokeStyle = "rgba(255,255,255,0.9)"; ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.arc(cx, cy, R - 0.5, 0, 7); ctx.stroke();

    // Words in flight
    arcs = arcs.filter((a) => t - a.start < 3.5);
    arcs.forEach((a) => {
      const age = t - a.start, grow = Math.min(1, age / 1.5), head = 1 - Math.pow(1 - grow, 3);
      const tail = age > 2.2 ? Math.min(1, (age - 2.2) / 1.2) : 0;
      const N = 56;
      ctx.lineWidth = 2.6 * S; ctx.lineCap = "round";
      ctx.shadowColor = `rgba(${CORAL},0.55)`; ctx.shadowBlur = 10;
      let prev = null;
      for (let i = Math.floor(tail * N); i <= Math.ceil(head * N); i++) {
        const k = Math.min(head, i / N), p = proj(slerp(HUB, a.city.v, k), 1 + a.lift * Math.sin(Math.PI * k));
        if (prev && shown(p) && shown(prev)) {
          ctx.strokeStyle = `rgba(${Math.round(65 + 149 * k)},${Math.round(146 - 56 * k)},${Math.round(197 - 136 * k)},0.95)`;
          ctx.beginPath(); ctx.moveTo(prev[0], prev[1]); ctx.lineTo(p[0], p[1]); ctx.stroke();
        }
        prev = p;
      }
      ctx.shadowColor = "transparent"; ctx.shadowBlur = 0;
      if (grow >= 1) {
        const p = proj(a.city.v), fade = Math.min(1, (age - 1.5) / 0.2) * Math.min(1, (3.5 - age) / 0.4);
        if (p[2] > 0.05) {
          ctx.fillStyle = `rgba(${CORAL},${fade})`;
          ctx.beginPath(); ctx.arc(p[0], p[1], 4.5 * S, 0, 7); ctx.fill();
          word(a.city.words[a.n], p[0], p[1], CORAL, fade, a.city.flag);
        }
      }
    });

    // Croatia
    const h = proj(HUB);
    if (h[2] > 0) {
      const pulse = (t % 2.4) / 2.4;
      ctx.strokeStyle = `rgba(${CORAL},${1 - pulse})`; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(h[0], h[1], 7 * S + pulse * 26 * S, 0, 7); ctx.stroke();
      ctx.fillStyle = `rgb(${CORAL})`;
      ctx.beginPath(); ctx.arc(h[0], h[1], 7 * S, 0, 7); ctx.fill();
      if (arcs.length) word(SOURCE[arcs[arcs.length - 1].n], h[0], h[1] + 66 * S, BLUE, Math.min(1, (t - arcs[arcs.length - 1].start) / 0.12), HR);
    }

    ring(-0.42, 1.25, 1.2, t * 0.22 + 1, BLUE, true);
    ring(0.5, 1.12, 1.11, -t * 0.3 + 2.4, CORAL, true);

    if (!still && t - lastSpawn > 0.9 && h[2] > 0.1) {
      const near = CITIES.map((c, i) => i).filter((i) => proj(CITIES[i].v)[2] > 0.2 && !arcs.some((a) => dot(a.city.v, CITIES[i].v) > 0.975));
      let pool = near.filter((i) => !used.has(CITIES[i].lang));
      if (!pool.length && near.length) { used.clear(); arcs.forEach((a) => used.add(a.city.lang)); pool = near.filter((i) => !used.has(CITIES[i].lang)); }
      if (pool.length) launch(CITIES[pool[Math.floor(Math.random() * pool.length)]], t);
    }
    now_t = t;
  }

  function launch(c, t) {
    used.add(c.lang);
    const d = Math.acos(Math.min(1, dot(HUB, c.v)));
    arcs.push({ city: c, start: t, lift: 0.1 + d * 0.26, n: turn++ % SOURCE.length });
    lastSpawn = t;
  }

  function frame(now) {
    if (!dragging) { user += vel; vel *= 0.94; user *= 0.992; }
    if (visible) draw(now);
    requestAnimationFrame(frame);
  }

  el.addEventListener("pointerdown", (e) => { dragging = true; lastX = e.clientX; vel = 0; moved = 0; el.setPointerCapture(e.pointerId); el.classList.add("grabbing"); });
  el.addEventListener("pointermove", (e) => {
    if (!dragging) return;
    const d = ((e.clientX - lastX) / R) * -1;
    user += d; vel = d; moved += Math.abs(e.clientX - lastX); lastX = e.clientX;
  });
  const drop = () => { dragging = false; el.classList.remove("grabbing"); };
  el.addEventListener("pointerup", (e) => {
    drop();
    if (moved > 6) return;
    const r = el.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
    let best = null, bd = 1e9;
    CITIES.forEach((c) => {
      const p = proj(c.v), dd = Math.hypot(p[0] - x, p[1] - y);
      if (p[2] > 0.1 && dd < bd && !arcs.some((a) => a.city === c)) { bd = dd; best = c; }
    });
    if (best && bd < R * 0.5) launch(best, now_t);
  });
  el.addEventListener("pointercancel", drop);

  new IntersectionObserver(([en]) => (visible = en.isIntersecting)).observe(el);
  addEventListener("resize", () => { size(); if (still) draw(0); });
  size();
  loadLand();
  if (still) draw(0); else requestAnimationFrame(frame);
})();
