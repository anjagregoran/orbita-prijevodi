// Hero: a huge globe seen from orbit, rising from the bottom of the first screen.
// Croatian words leave Croatia in blue and land translated in orange.
(function () {
  const el = document.getElementById("globe");
  if (!el) return;
  const ctx = el.getContext("2d");
  const INK = "35,39,46", BLUE = "65,146,197", CORAL = "214,90,61", CREAM = "246,241,231";
  const RAD = Math.PI / 180;
  const TILT = 8 * RAD, cp = Math.cos(TILT), sp = Math.sin(TILT);
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const vec = (lat, lon) => {
    const cl = Math.cos(lat * RAD);
    return [cl * Math.sin(lon * RAD), Math.sin(lat * RAD), cl * Math.cos(lon * RAD)];
  };
  const HUB = vec(45.6, 15.4);
  const SOURCE = ["hvala", "bok", "dobrodošli"];
  const CITIES = [
    [51.5, -0.1, "thank you", "hello", "welcome"], [52.5, 13.4, "danke", "hallo", "willkommen"],
    [40.4, -3.7, "gracias", "hola", "bienvenidos"], [59.3, 18.1, "tack", "hej", "välkommen"],
    [50.5, 30.5, "дякую", "привіт", "ласкаво просимо"], [38, 23.7, "ευχαριστώ", "γεια σου", "καλώς ήρθατε"],
    [39.9, 32.9, "teşekkürler", "merhaba", "hoş geldiniz"], [32.1, 34.8, "תודה", "שלום", "ברוכים הבאים"],
    [24.7, 46.7, "شكرا", "مرحبا", "أهلا وسهلا"], [35.7, 51.4, "ممنون", "سلام", "خوش آمدید"],
    [39.9, 116.4, "谢谢", "你好", "欢迎"], [35.7, 139.7, "ありがとう", "こんにちは", "ようこそ"],
    [40.7, -74, "thank you", "hello", "welcome"], [-23.5, -46.6, "obrigado", "olá", "bem-vindos"],
    [14.7, -17.4, "merci", "salut", "bienvenue"], [48.9, 2.3, "merci", "salut", "bienvenue"],
    [41.9, 12.5, "grazie", "ciao", "benvenuti"], [52.2, 21, "dziękuję", "cześć", "witamy"]
  ].map(([lat, lon, ...words]) => ({ words, v: vec(lat, lon) }));

  let W = 0, H = 0, R = 0, S = 0, cx = 0, cy = 0, dpr = 1;
  let dots = [], arcs = [], lam = 0, user = 0, vel = 0, dragging = false, lastX = 0;
  let visible = true, lastSpawn = 0, lastCity = -1, turn = 0;

  function size() {
    W = el.clientWidth;
    R = Math.min(760, Math.max(330, W * 0.5));
    H = Math.round(R * 0.95);
    S = Math.min(1.25, Math.max(0.72, R / 520));
    el.style.height = H + "px";
    dpr = Math.min(devicePixelRatio || 1, W > 900 ? 1.5 : 2);
    el.width = Math.round(W * dpr); el.height = Math.round(H * dpr);
    cx = W / 2; cy = R * 0.2 + R;
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
      dots = fibonacci(44000, (lat, lon) => {
        if (lat < -20) return false;
        const x = Math.min(mw - 1, Math.floor(((lon + 180) / 360) * mw)), y = Math.min(mh - 1, Math.floor(((90 - lat) / 180) * mh));
        return data[(y * mw + x) * 4 + 3] > 120;
      });
    } catch (e) {
      dots = fibonacci(2600, (lat) => lat > -20);
    }
    if (still) draw(0);
  }

  function slerp(a, b, t) {
    const om = Math.acos(Math.min(1, dot(a, b))), s = Math.sin(om) || 1;
    const k1 = Math.sin((1 - t) * om) / s, k2 = Math.sin(t * om) / s;
    return [a[0] * k1 + b[0] * k2, a[1] * k1 + b[1] * k2, a[2] * k1 + b[2] * k2];
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

  function word(text, x, y, color, alpha, pill) {
    ctx.font = `italic 400 ${Math.round(22 * S)}px "Fraunces", Georgia, serif`;
    ctx.textAlign = "center"; ctx.textBaseline = "middle";
    const w = ctx.measureText(text).width + 30 * S, h = 38 * S, top = y - h - 12 * S;
    ctx.globalAlpha = alpha;
    if (pill) {
      ctx.fillStyle = "#fff";
      ctx.shadowColor = `rgba(${INK},0.2)`; ctx.shadowBlur = 18; ctx.shadowOffsetY = 5;
      ctx.beginPath(); ctx.roundRect(x - w / 2, top, w, h, h / 2); ctx.fill();
      ctx.shadowColor = "transparent"; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0;
    } else {
      ctx.lineJoin = "round"; ctx.strokeStyle = "rgba(255,255,255,0.9)"; ctx.lineWidth = 6 * S;
      ctx.strokeText(text, x, top + h / 2);
    }
    ctx.fillStyle = `rgb(${color})`;
    ctx.fillText(text, x, top + h / 2 + 1);
    ctx.globalAlpha = 1;
  }

  function draw(now) {
    const t = now / 1000;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    lam = (15 + 42 * Math.sin(t * 0.09)) * RAD + user;

    ring(-0.2, 1.36, 1.17, t * 0.22 + 1, BLUE, false);
    ring(0.24, 1.3, 1.1, -t * 0.3 + 2.4, CORAL, false);

    // Atmosphere, then sphere body
    const halo = ctx.createRadialGradient(cx, cy, R * 0.96, cx, cy, R * 1.2);
    halo.addColorStop(0, `rgba(${BLUE},0.42)`); halo.addColorStop(1, `rgba(${BLUE},0)`);
    ctx.fillStyle = halo;
    ctx.beginPath(); ctx.arc(cx, cy, R * 1.2, 0, 7); ctx.fill();
    const g = ctx.createRadialGradient(cx - R * 0.3, cy - R * 0.75, R * 0.05, cx, cy, R);
    g.addColorStop(0, "#ffffff"); g.addColorStop(0.5, "#e9f3fa"); g.addColorStop(1, "#b5d6ed");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, 7); ctx.fill();

    // Land
    const ds = Math.max(1.5, R * 0.0042);
    for (let i = 0; i < dots.length; i++) {
      const p = proj(dots[i]);
      if (p[2] <= 0.02 || p[1] > H + 4 || p[0] < -4 || p[0] > W + 4) continue;
      ctx.fillStyle = `rgba(${BLUE},${0.6 + 0.4 * p[2]})`;
      ctx.beginPath(); ctx.arc(p[0], p[1], ds * (0.72 + 0.28 * p[2]), 0, 7); ctx.fill();
    }

    // Words in flight
    arcs = arcs.filter((a) => t - a.start < 5.2);
    arcs.forEach((a) => {
      const age = t - a.start, grow = Math.min(1, age / 1.7), head = 1 - Math.pow(1 - grow, 3);
      const tail = age > 3 ? Math.min(1, (age - 3) / 1.6) : 0;
      const N = 56;
      ctx.lineWidth = 2.4 * S; ctx.lineCap = "round";
      let prev = null;
      for (let i = Math.floor(tail * N); i <= Math.ceil(head * N); i++) {
        const k = Math.min(head, i / N), p = proj(slerp(HUB, a.city.v, k), 1 + a.lift * Math.sin(Math.PI * k));
        if (prev && shown(p) && shown(prev)) {
          ctx.strokeStyle = `rgba(${Math.round(65 + 149 * k)},${Math.round(146 - 56 * k)},${Math.round(197 - 136 * k)},0.95)`;
          ctx.beginPath(); ctx.moveTo(prev[0], prev[1]); ctx.lineTo(p[0], p[1]); ctx.stroke();
        }
        prev = p;
      }
      if (grow < 1) {
        if (prev && shown(prev)) word(SOURCE[a.n], prev[0], prev[1] + 6 * S, BLUE, Math.min(1, age / 0.3) * Math.min(1, (1 - grow) / 0.15), false);
      } else {
        const p = proj(a.city.v), fade = Math.min(1, (age - 1.7) / 0.3) * Math.min(1, (5.2 - age) / 0.6);
        if (p[2] > 0.05) {
          ctx.fillStyle = `rgba(${CORAL},${fade})`;
          ctx.beginPath(); ctx.arc(p[0], p[1], 4.5 * S, 0, 7); ctx.fill();
          word(a.city.words[a.n], p[0], p[1], CORAL, fade, true);
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
    }

    ring(-0.2, 1.36, 1.17, t * 0.22 + 1, BLUE, true);
    ring(0.24, 1.3, 1.1, -t * 0.3 + 2.4, CORAL, true);

    // Fade the planet into the page
    const fade = ctx.createLinearGradient(0, H * 0.8, 0, H);
    fade.addColorStop(0, `rgba(${CREAM},0)`); fade.addColorStop(1, `rgba(${CREAM},1)`);
    ctx.fillStyle = fade; ctx.fillRect(0, H * 0.8, W, H * 0.2 + 1);

    if (!still && t - lastSpawn > 1.1 && h[2] > 0.1) {
      const ok = (c) => { const p = proj(c.v); return p[2] > 0.25 && p[1] < H * 0.8 && p[0] > 60 && p[0] < W - 60; };
      const pool = CITIES.map((c, i) => i).filter((i) => i !== lastCity && ok(CITIES[i]) && !arcs.some((a) => dot(a.city.v, CITIES[i].v) > 0.975));
      if (pool.length) {
        lastCity = pool[Math.floor(Math.random() * pool.length)];
        const c = CITIES[lastCity], d = Math.acos(Math.min(1, dot(HUB, c.v)));
        arcs.push({ city: c, start: t, lift: 0.06 + d * 0.2, n: turn++ % SOURCE.length });
        lastSpawn = t;
      }
    }
  }

  function frame(now) {
    if (!dragging) { user += vel; vel *= 0.94; user *= 0.992; }
    if (visible) draw(now);
    requestAnimationFrame(frame);
  }

  el.addEventListener("pointerdown", (e) => { dragging = true; lastX = e.clientX; vel = 0; el.setPointerCapture(e.pointerId); el.classList.add("grabbing"); });
  el.addEventListener("pointermove", (e) => {
    if (!dragging) return;
    const d = ((e.clientX - lastX) / R) * -1;
    user += d; vel = d; lastX = e.clientX;
  });
  const drop = () => { dragging = false; el.classList.remove("grabbing"); };
  el.addEventListener("pointerup", drop);
  el.addEventListener("pointercancel", drop);

  new IntersectionObserver(([en]) => (visible = en.isIntersecting)).observe(el);
  addEventListener("resize", () => { size(); if (still) draw(0); });
  size();
  loadLand();
  if (still) draw(0); else requestAnimationFrame(frame);
})();
