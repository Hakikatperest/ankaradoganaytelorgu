/* Doğanay Tel Örgü — menü, alt çubuk, ışık kutusu */
(function () {
  var btn = document.querySelector(".menu-btn"), menu = document.getElementById("menu");
  if (btn && menu) {
    btn.addEventListener("click", function () {
      var ac = menu.classList.toggle("acik");
      btn.setAttribute("aria-expanded", ac ? "true" : "false");
      btn.setAttribute("aria-label", ac ? "Menüyü kapat" : "Menüyü aç");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) { menu.classList.remove("acik"); btn.setAttribute("aria-expanded", "false"); }
    });
  }

  // alt çubuk: sayfa dibinde (imza bandı) gizlenir, imza tıklanabilir kalsın
  var dock = document.getElementById("dock");
  if (dock) {
    var bekle = false;
    var guncelle = function () {
      var kalan = document.documentElement.scrollHeight - (window.scrollY + window.innerHeight);
      dock.classList.toggle("gizli", kalan < 120);
      bekle = false;
    };
    window.addEventListener("scroll", function () { if (!bekle) { bekle = true; requestAnimationFrame(guncelle); } }, { passive: true });
    guncelle();
  }

  // ışık kutusu
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-buyut]");
    if (!a) return;
    e.preventDefault();
    var img = a.querySelector("img");
    var k = document.createElement("div");
    k.className = "isik"; k.setAttribute("role", "dialog"); k.setAttribute("aria-modal", "true");
    k.innerHTML = '<img alt=""><button type="button" aria-label="Kapat">×</button>';
    k.querySelector("img").src = a.getAttribute("href");
    k.querySelector("img").alt = img ? img.alt : "";
    var kapat = function () { k.remove(); document.removeEventListener("keydown", tus); a.focus(); };
    var tus = function (ev) { if (ev.key === "Escape") kapat(); };
    k.addEventListener("click", kapat);
    document.addEventListener("keydown", tus);
    document.body.appendChild(k);
    k.querySelector("button").focus();
  });
})();
