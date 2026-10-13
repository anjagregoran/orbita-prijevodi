// Hero: the logo's infinity loop. Croatian words travel round the blue side
// and come back translated on the orange side.
(function () {
  const el = document.getElementById("loop");
  if (!el) return;
  const ctx = el.getContext("2d");
  const BLUE = [65, 146, 197], ORANGE = [214, 90, 61], CREAM = "#f6f1e7";
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const PAIRS = [
    ["hvala", "thank you"], ["dobar dan", "guten Tag"], ["riječ", "parola"], ["svijet", "le monde"],
    ["ugovor", "contrato"], ["dobrodošli", "ようこそ"], ["ljubav", "αγάπη"], ["prijevod", "prevod"],
    ["jezik", "语言"], ["diploma", "диплом"]
  ];
  const LINES = [0.84, 0.92, 1, 1.08, 1.16];
  const DOTS = Array.from({ length: 46 }, (_, i) => ({
    t: (i / 46) * Math.PI * 2 + Math.random() * 0.1,
    line: LINES[i % LINES.length],
    r: 1.2 + Math.random() * 2.2,
    speed: 0.16 + Math.random() * 0.08
  }));

  let W = 0, H = 0, A = 0, cx = 0, cy = 0, dpr = 1;
  let mx = 0, my = 0, tx = 0, ty = 0, visible = true;

  function size() {
    dpr = Math.min(devicePixelRatio || 1, 2);
    W = el.clientWidth; H = el.clientHeight;
    el.width = Math.round(W * dpr); el.height = Math.round(H * dpr);
    A = W * 0.43; cx = W / 2; cy = H / 2;
  }

  // Point on the loop. Returns [x, y, side] where side runs -1 (blue tip) to 1 (orange tip).
  function pt(t, scale) {
    const s = Math.sin(t), c = Math.cos(t), d = 1 + s * s;
    const x = (A * scale * c) / d, y = ((A * scale * s * c) / d) * 1.5;
    const a = -0.3 + mx * 0.05, ca = Math.cos(a), sa = Math.sin(a);
    return [cx + x * ca - y * sa + mx * 14, cy + x * sa + y * ca + my * 14, c / d];
  }
  const ease = (k) => k * k * (3 - 2 * k);
  function colour(side, alpha) {
    const k = ease(Math.min(1, Math.max(0, (side + 0.25) / 0.5)));
    const c = BLUE.map((b, i) => Math.round(b + (ORANGE[i] - b) * k));
    return `rgba(${c[0]},${c[1]},${c[2]},${alpha})`;
  }

  function draw(now) {
    const t = now / 1000;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);

    const left = pt(Math.PI, 1), right = pt(0, 1);
    const grad = ctx.createLinearGradient(left[0], left[1], right[0], right[1]);
    grad.addColorStop(0, "rgba(65,146,197,0.15)");
    grad.addColorStop(0.3, "rgba(65,146,197,1)");
    grad.addColorStop(0.5, "rgba(140,118,129,1)");
    grad.addColorStop(0.7, "rgba(214,90,61,1)");
    grad.addColorStop(1, "rgba(214,90,61,0.85)");

    LINES.forEach((scale) => {
      ctx.beginPath();
      for (let i = 0; i <= 240; i++) {
        const p = pt((i / 240) * Math.PI * 2, scale);
        i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1]);
      }
      ctx.strokeStyle = grad;
      ctx.globalAlpha = scale === 1 ? 0.9 : 0.28;
      ctx.lineWidth = scale === 1 ? Math.max(1.5, W * 0.0026) : 1;
      ctx.stroke();
    });
    ctx.globalAlpha = 1;

    DOTS.forEach((d) => {
      const p = pt(d.t + t * d.speed, d.line);
      ctx.fillStyle = colour(p[2], 0.75);
      ctx.beginPath(); ctx.arc(p[0], p[1], d.r * (W / 800), 0, 7); ctx.fill();
    });

    ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.lineJoin = "round";
    PAIRS.forEach((pair, i) => {
      const p = pt(t * 0.1 + (i / PAIRS.length) * Math.PI * 2, 1), far = Math.abs(p[2]);
      const alpha = ease(Math.min(1, Math.max(0, (far - 0.1) / 0.3)));
      if (alpha <= 0) return;
      const word = p[2] < 0 ? pair[0] : pair[1];
      ctx.font = `italic 400 ${Math.max(15, W * 0.036 * (0.8 + 0.35 * far))}px "Fraunces", Georgia, serif`;
      ctx.globalAlpha = alpha;
      ctx.strokeStyle = CREAM; ctx.lineWidth = Math.max(8, W * 0.016);
      ctx.strokeText(word, p[0], p[1]);
      ctx.fillStyle = colour(p[2], 1);
      ctx.fillText(word, p[0], p[1]);
    });
    ctx.globalAlpha = 1;
  }

  function frame(now) {
    mx += (tx - mx) * 0.05; my += (ty - my) * 0.05;
    if (visible) draw(now);
    requestAnimationFrame(frame);
  }

  addEventListener("pointermove", (e) => {
    tx = (e.clientX / innerWidth) * 2 - 1;
    ty = (e.clientY / innerHeight) * 2 - 1;
  }, { passive: true });
  new IntersectionObserver(([en]) => (visible = en.isIntersecting)).observe(el);
  addEventListener("resize", () => { size(); if (still) draw(0); });
  size();
  if (still) { draw(0); document.fonts.ready.then(() => draw(0)); } else requestAnimationFrame(frame);
})();
