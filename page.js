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
