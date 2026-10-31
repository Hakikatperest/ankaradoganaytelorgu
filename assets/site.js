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

  // ürünler mega menüsü: dokunmatik ve mobilde tıklayınca aç/kapa
  var mb = document.querySelector(".mega-btn");
  if (mb) {
    mb.addEventListener("click", function () {
      var k = mb.parentNode, ac = k.classList.toggle("acik");
      mb.setAttribute("aria-expanded", ac ? "true" : "false");
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".menu-urun")) { mb.parentNode.classList.remove("acik"); mb.setAttribute("aria-expanded", "false"); }
    });
  }

  // sipariş formu → hazır WhatsApp mesajı (hiçbir yere kaydedilmez)
  var sf = document.getElementById("siparis-form");
  if (sf) {
    sf.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = sf.elements, sat = ["Merhaba, Doğanay Tel Örgü sipariş hattı için yazıyorum."];
      sat.push("Ürün: " + f.urun.value);
      if (f.metraj.value) sat.push("Metraj: " + f.metraj.value);
      if (f.yukseklik.value) sat.push("Yükseklik: " + f.yukseklik.value);
      sat.push("İlçe: " + f.ilce.value);
      sat.push("Montaj: " + f.montaj.value);
      if (f.not.value) sat.push("Not: " + f.not.value);
      window.open("https://wa.me/" + sf.getAttribute("data-wa") + "?text=" + encodeURIComponent(sat.join("\n")), "_blank", "noopener");
    });
  }

  // alt çubuk: üstteki arama/WhatsApp butonları görünürken ve sayfa dibinde (imza bandı) gizlenir
  var dock = document.getElementById("dock");
  if (dock) {
    var bekle = false, ustBtn = document.querySelector(".hero .dugmeler, .sayfa-bas .dugmeler, .sayfa-bas .hero-tel");
    var guncelle = function () {
      var kalan = document.documentElement.scrollHeight - (window.scrollY + window.innerHeight);
      var ustGorunur = ustBtn && ustBtn.getBoundingClientRect().bottom > 0;
      dock.classList.toggle("gizli", kalan < 120 || !!ustGorunur);
      bekle = false;
    };
    window.addEventListener("scroll", function () { if (!bekle) { bekle = true; requestAnimationFrame(guncelle); } }, { passive: true });
    guncelle();
  }

  // Google Ads "Tıkla ve ara" dönüşümü: sitedeki her tel: bağlantısı (üst şerit, butonlar, alt çubuk, alt bilgi).
  // url verilmiyor → arama tarayıcının kendi akışıyla hemen başlar, dönüşüm arka planda gönderilir.
  document.addEventListener("click", function (e) {
    var a = e.target.closest('a[href^="tel:"]');
    if (a && typeof window.gtag_report_conversion === "function") {
      try { window.gtag_report_conversion(); } catch (_) {}
    }
  }, true);

  // danışma hattı bildirimi: 5. saniyede tüm ziyaretçilere; kapatılınca ya da arayınca oturum boyunca gelmez
  var dn = document.getElementById("danisma"), DN_ANAHTAR = "dt-danisma-kapandi-v1";
  if (dn) {
    var dnKapali = function () { try { return sessionStorage.getItem(DN_ANAHTAR) === "1"; } catch (_) { return false; } };
    var dnKapat = function () {
      try { sessionStorage.setItem(DN_ANAHTAR, "1"); } catch (_) {}
      dn.classList.remove("acik");
      setTimeout(function () { dn.hidden = true; }, 400);
    };
    dn.querySelector(".danisma-kapat").addEventListener("click", dnKapat);
    dn.querySelector(".danisma-btn").addEventListener("click", function () { try { sessionStorage.setItem(DN_ANAHTAR, "1"); } catch (_) {} setTimeout(dnKapat, 300); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !dn.hidden) dnKapat(); });
    if (!dnKapali()) setTimeout(function () {
      if (dnKapali()) return;
      dn.hidden = false;
      requestAnimationFrame(function () { requestAnimationFrame(function () { dn.classList.add("acik"); }); });
    }, 5000);
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
