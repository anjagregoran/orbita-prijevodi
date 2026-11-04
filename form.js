// Quote forms: send the enquiry and the attached documents straight to both offices (send.php)
document.querySelectorAll(".send-form").forEach((form) => {
  const note = form.querySelector(".form-note");
  const button = form.querySelector('button[type="submit"]');
  const MAX_FILES = 10, MAX_BYTES = 20 * 1024 * 1024;
  const say = (text, ok) => { note.textContent = text; note.classList.toggle("ok", !!ok); };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = form.elements.name.value.trim();
    const email = form.elements.email.value.trim();
    const phone = form.elements.phone.value.trim();
    if (!name) { say("Upišite ime i prezime kako bismo znali kome odgovaramo."); form.elements.name.focus(); return; }
    if (!email && !phone) { say("Upišite e-poštu ili broj telefona kako bismo Vam mogli poslati ponudu."); form.elements.email.focus(); return; }
    if (email && !form.elements.email.checkValidity()) { say("Provjerite adresu e-pošte."); form.elements.email.focus(); return; }
    const files = [...form.querySelector('input[type="file"]').files];
    if (files.length > MAX_FILES) { say(`Možete priložiti najviše ${MAX_FILES} datoteka.`); return; }
    if (files.reduce((n, f) => n + f.size, 0) > MAX_BYTES) { say("Datoteke su zajedno veće od 20 MB. Pošaljite ih u dva upita ili e-poštom."); return; }

    button.disabled = true;
    say("Šaljemo upit…");
    try {
      const res = await fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
      const data = await res.json();
      if (!res.ok || !data.ok) throw new Error(data.error || "send");
      form.reset();
      say("Hvala! Upit je poslan, a ponudu ćemo Vam poslati najkasnije unutar sat vremena.", true);
      if (window.orbitaTrack) window.orbitaTrack("generate_lead", { form: form.id || "landing" });
    } catch (err) {
      say(err.message && err.message !== "send" && !/JSON/.test(err.message) ? err.message
        : "Slanje trenutačno nije uspjelo. Pošaljite nam dokument na info@orbitaprijevodi.com ili WhatsAppom na 098 163 19 30.");
    } finally {
      button.disabled = false;
    }
  });

  // Show which files are attached
  const input = form.querySelector('input[type="file"]'), hint = form.querySelector(".file-hint");
  const base = hint.textContent;
  input.addEventListener("change", () => {
    const n = input.files.length;
    hint.textContent = n ? [...input.files].map((f) => f.name).join(", ") : base;
  });
});
