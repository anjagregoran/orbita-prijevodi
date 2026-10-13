// Hero globe: dotted continents, greetings travelling out from Croatia, two orbit rings.
(function () {
  const el = document.getElementById("globe");
  if (!el) return;
  const ctx = el.getContext("2d");
  const INK = "35,39,46", DEEP = "65,146,197", BLUE = "65,146,197", CORAL = "214,90,61";
  const RAD = Math.PI / 180;
  const TILT = 30 * RAD, cp = Math.cos(TILT), sp = Math.sin(TILT);
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const vec = (lat, lon) => {
    const cl = Math.cos(lat * RAD);
    return [cl * Math.sin(lon * RAD), Math.sin(lat * RAD), cl * Math.cos(lon * RAD)];
  };
  const HUB = vec(45.6, 15.4);
  const CITIES = [
    ["Hello", 51.5, -0.1], ["Hallo", 52.5, 13.4], ["Hola", 40.4, -3.7], ["Hej", 59.3, 18.1],
    ["Привіт", 50.5, 30.5], ["Γεια σας", 38, 23.7], ["Merhaba", 39.9, 32.9], ["שלום", 32.1, 34.8],
    ["مرحبا", 24.7, 46.7], ["سلام", 35.7, 51.4], ["你好", 39.9, 116.4], ["こんにちは", 35.7, 139.7],
    ["Hello", 40.7, -74], ["Olá", -23.5, -46.6], ["Bonjour", 14.7, -17.4], ["Bonjour", 45.5, -73.6]
  ].map(([word, lat, lon]) => ({ word, v: vec(lat, lon) }));

  let W = 0, R = 0, cx = 0, cy = 0, dpr = 1;
  let dots = [], arcs = [], lam = 0, user = 0, vel = 0, dragging = false, lastX = 0;
  let visible = true, lastSpawn = 0, lastCity = -1;

  function size() {
    dpr = Math.min(devicePixelRatio || 1, 2);
    W = el.clientWidth;
    el.width = el.height = Math.round(W * dpr);
    R = W * 0.37; cx = W / 2; cy = W / 2;
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
      dots = fibonacci(30000, (lat, lon) => {
        if (lat < -60) return false;
        const x = Math.min(mw - 1, Math.floor(((lon + 180) / 360) * mw)), y = Math.min(mh - 1, Math.floor(((90 - lat) / 180) * mh));
        return data[(y * mw + x) * 4 + 3] > 120;
      });
    } catch (e) {
      dots = fibonacci(1800, () => true);
    }
    if (still) draw(0);
  }

  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

  function slerp(a, b, t) {
    const d = Math.min(1, a[0] * b[0] + a[1] * b[1] + a[2] * b[2]), om = Math.acos(d), s = Math.sin(om) || 1;
    const k1 = Math.sin((1 - t) * om) / s, k2 = Math.sin(t * om) / s;
    return [a[0] * k1 + b[0] * k2, a[1] * k1 + b[1] * k2, a[2] * k1 + b[2] * k2];
  }

  function ring(tiltZ, tiltX, r, t, color, front) {
    const cz = Math.cos(tiltZ), sz = Math.sin(tiltZ), cxr = Math.cos(tiltX), sxr = Math.sin(tiltX);
    const pt = (a) => {
      let x = Math.cos(a) * r, y = 0, z = Math.sin(a) * r;
      const x1 = x * cz - y * sz, y1 = x * sz + y * cz;
      const y2 = y1 * cxr - z * sxr, z2 = y1 * sxr + z * cxr;
      return [cx + R * x1, cy - R * y2, z2];
    };
    ctx.lineWidth = 1;
    ctx.strokeStyle = `rgba(${BLUE},${front ? 0.55 : 0.22})`;
    ctx.beginPath();
    let pen = false;
    for (let i = 0; i <= 180; i++) {
      const p = pt((i / 180) * Math.PI * 2);
      if (p[2] > 0 === front) { pen ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]); pen = true; } else pen = false;
    }
    ctx.stroke();
    const s = pt(t);
    if (s[2] > 0 === front) {
      ctx.fillStyle = `rgb(${color})`;
      ctx.beginPath(); ctx.arc(s[0], s[1], W * 0.008, 0, 7); ctx.fill();
    }
  }

  function pill(text, x, y, alpha) {
    ctx.font = `500 ${Math.max(11, W * 0.019)}px "DM Sans", sans-serif`;
    const w = ctx.measureText(text).width + 22, h = Math.max(24, W * 0.04);
    ctx.globalAlpha = alpha;
    ctx.fillStyle = "#ffffff";
    ctx.shadowColor = `rgba(${INK},0.18)`; ctx.shadowBlur = 14; ctx.shadowOffsetY = 4;
    ctx.beginPath(); ctx.roundRect(x - w / 2, y - h - 10, w, h, h / 2); ctx.fill();
    ctx.shadowColor = "transparent"; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0;
    ctx.fillStyle = `rgb(${INK})`;
    ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.fillText(text, x, y - h / 2 - 9);
    ctx.globalAlpha = 1;
  }

  function draw(now) {
    const t = now / 1000;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, W);
    lam = (15 + 55 * Math.sin(t * 0.11)) * RAD + user;

    ring(-0.42, 1.25, 1.36, t * 0.35, BLUE, false);
    ring(0.5, 1.12, 1.2, -t * 0.5 + 2, CORAL, false);

    // Glow, then sphere body
    const halo = ctx.createRadialGradient(cx, cy, R * 0.9, cx, cy, R * 1.32);
    halo.addColorStop(0, `rgba(${BLUE},0.3)`); halo.addColorStop(1, `rgba(${BLUE},0)`);
    ctx.fillStyle = halo;
    ctx.beginPath(); ctx.arc(cx, cy, R * 1.32, 0, 7); ctx.fill();
    const g = ctx.createRadialGradient(cx - R * 0.4, cy - R * 0.45, R * 0.05, cx, cy, R);
    g.addColorStop(0, "#ffffff"); g.addColorStop(0.55, "#e6f1f9"); g.addColorStop(1, "#bfdcf0");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, 7); ctx.fill();

    // Land
    const ds = Math.max(1, W * 0.0026);
    for (let i = 0; i < dots.length; i++) {
      const p = proj(dots[i]);
      if (p[2] <= 0.02) continue;
      ctx.fillStyle = `rgba(${DEEP},${0.35 + 0.65 * p[2]})`;
      ctx.beginPath(); ctx.arc(p[0], p[1], ds * (0.55 + 0.45 * p[2]), 0, 7); ctx.fill();
    }

    // Travelling greetings
    arcs = arcs.filter((a) => t - a.start < 4.6);
    arcs.forEach((a) => {
      const age = t - a.start, grow = Math.min(1, age / 1.5), head = 1 - Math.pow(1 - grow, 3);
      const tail = age > 2.6 ? Math.min(1, (age - 2.6) / 1.4) : 0;
      const N = 44;
      ctx.lineWidth = Math.max(1.4, W * 0.0028); ctx.lineCap = "round";
      let prev = null;
      for (let i = Math.floor(tail * N); i <= Math.ceil(head * N); i++) {
        const k = Math.min(head, i / N), p = proj(slerp(HUB, a.city.v, k), 1 + a.lift * Math.sin(Math.PI * k));
        if (prev && shown(p) && shown(prev)) {
          const mix = k;
          ctx.strokeStyle = `rgba(${Math.round(65 + (214 - 65) * mix)},${Math.round(146 + (90 - 146) * mix)},${Math.round(197 + (61 - 197) * mix)},0.95)`;
          ctx.beginPath(); ctx.moveTo(prev[0], prev[1]); ctx.lineTo(p[0], p[1]); ctx.stroke();
        }
        prev = p;
      }
      if (grow >= 1) {
        const p = proj(a.city.v), fade = Math.min(1, (age - 1.5) / 0.3) * Math.min(1, (4.6 - age) / 0.5);
        if (p[2] > 0.05) {
          ctx.fillStyle = `rgba(${CORAL},${fade})`;
          ctx.beginPath(); ctx.arc(p[0], p[1], W * 0.006, 0, 7); ctx.fill();
          pill(a.city.word, p[0], p[1], fade);
        }
      }
    });

    // Croatia
    const h = proj(HUB);
    if (h[2] > 0) {
      const pulse = (t % 2.4) / 2.4;
      ctx.strokeStyle = `rgba(${CORAL},${1 - pulse})`; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(h[0], h[1], W * 0.009 + pulse * W * 0.035, 0, 7); ctx.stroke();
      ctx.fillStyle = `rgb(${CORAL})`;
      ctx.beginPath(); ctx.arc(h[0], h[1], W * 0.009, 0, 7); ctx.fill();
    }

    ring(-0.42, 1.25, 1.36, t * 0.35, BLUE, true);
    ring(0.5, 1.12, 1.2, -t * 0.5 + 2, CORAL, true);

    if (!still && t - lastSpawn > 0.85 && h[2] > 0.1) {
      const pool = CITIES.map((c, i) => i).filter((i) => i !== lastCity && proj(CITIES[i].v)[2] > 0.2 && !arcs.some((a) => dot(a.city.v, CITIES[i].v) > 0.955));
      if (pool.length) {
        lastCity = pool[Math.floor(Math.random() * pool.length)];
        const c = CITIES[lastCity], d = Math.acos(Math.min(1, HUB[0] * c.v[0] + HUB[1] * c.v[1] + HUB[2] * c.v[2]));
        arcs.push({ city: c, start: t, lift: 0.1 + d * 0.28 });
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
