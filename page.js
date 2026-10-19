// Shared behaviour for the separate pages (services, cities, FAQ, contact)
const nav = document.getElementById("nav"), burger = document.getElementById("burger"), navLinks = document.getElementById("navLinks");
const hero = document.querySelector(".page-hero");
const onScroll = () => {
  nav.classList.toggle("scrolled", scrollY > 20);
  nav.classList.toggle("on-dark", !!hero && scrollY < hero.offsetHeight - 70);
};
addEventListener("scroll", onScroll, { passive: true });
onScroll();
if (burger) burger.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  burger.classList.toggle("open", open);
  burger.setAttribute("aria-expanded", open);
});
document.getElementById("year").textContent = new Date().getFullYear();

// Testimonial slider on landing pages: one quote at a time, dots, arrows, auto-advance
document.querySelectorAll(".lp-slider").forEach((box) => {
  const slides = [...box.querySelectorAll(".lp-slide")], dots = [...box.querySelectorAll(".lp-dots button:not(.lp-prev):not(.lp-next)")];
  if (slides.length < 2) { box.querySelector(".lp-dots").hidden = true; return; }
  let i = 0, timer;
  const show = (n) => {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle("on", k === i));
    dots.forEach((d, k) => d.classList.toggle("on", k === i));
    clearInterval(timer); timer = setInterval(() => show(i + 1), 7000);
  };
  dots.forEach((d, k) => d.addEventListener("click", () => show(k)));
  box.querySelector(".lp-prev").addEventListener("click", () => show(i - 1));
  box.querySelector(".lp-next").addEventListener("click", () => show(i + 1));
  let x0 = null;
  box.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  box.addEventListener("touchend", (e) => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1)); x0 = null; });
  show(0);
});
