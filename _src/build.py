#!/usr/bin/env python3
"""Doğanay Tel Örgü — ankaradoganaytelorgu.com statik site üreticisi.

Çalıştır:  python3 _src/build.py   (herhangi bir dizinden)
Girdi:     _src/data.py (görseller, ilçeler, süreç, genel SSS), _src/icerik/*.py (9 kategori: kategori + fiyat + çeşit),
           img/stok/*.jpg (Unsplash, temsili), images/*.webp (kullanıcının gerçek fotoğrafları)
Çıktı:     index.html, /<kategori>/ × 9, /<kategori>-fiyatlari/ × 9, /<kategori>-cesitleri/ × 9, /siparis-hatti/,
           /hakkimizda/, /iletisim/, 404.html, sitemap.xml, robots.txt, assets/, images/g + images/k türevleri
İlçe:      /<ilce>-<urun>/ × 60 (20 ilçe × beton direk, jiletli tel, tel örgü; fiyat + satan yerler TEK sayfada — kullanıcı
           2026-10-26 onayladı) + /ankara-ilceleri/ dizini. İlçe verisi _src/ilceler.py (kaynaklı, 2025-2026).
Yapı:      "Kullanım Alanları" ve "Sipariş Ver" ayrı sayfa DEĞİL — kategori sayfasında #kullanim-alanlari / #siparis-ver
           bölümü (ölçekli içerik riski, kullanıcı 2026-10-26 onayladı).
İçerik:    gövde metninde [[slug|yazı]] veya [[slug#capa|yazı]] = iç link; kutu("tavsiye", "...") = kutucuk.
Denetim:   yasak ifade, kırık iç link, tekrar eden title/description, uzunluk → HATA, dosya yazılmaz.
İç yollar sayfa derinliğine göre GÖRELİ (Pages alt yol önizlemesi kırılmasın); canonical/sitemap mutlak.
⛔ HTML'i elle düzenleme — buradan üret.
"""
import html, json, os, re, sys, shutil

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(KOK, "_src"))
from data import GORSEL, GERCEK, GALERI, AFIS, ILCELER, SUREC, GENEL_SSS
from icerik import KATEGORILER, KUR, FIYAT_TARIH
from ilceler import ILCE, URUNLER

SITE = "https://ankaradoganaytelorgu.com/"
AD = "Doğanay Tel Örgü"
TEL, TEL_G, WA = "+905301552927", "0530 155 29 27", "905301552927"
ADRES = {"sokak": "Gaziosmanpaşa Mah., 377. Sk. No:20 D:14", "pk": "06830", "ilce": "Gölbaşı", "il": "Ankara"}
ADRES_G = "Gaziosmanpaşa, 377. Sk. No:20 D:14, 06830 Gölbaşı/Ankara"
HARITA_CID = "11896703876323172056"
HARITA_URL = f"https://www.google.com/maps?cid={HARITA_CID}"
HARITA_EMBED = ("https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d97974.87748769506!2d32.69075416456537"
                "!3d39.88062313067494!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14d3417ef65e64f3%3A0xa5199524e2415ed8"
                "!2zRE_EnkFOQVkgVEVMIMOWUkfDnA!5e0!3m2!1str!2str!4v1792984681174!5m2!1str!2str")
BUGUN = "2026-10-26"            # yayın tarihi SABİT
BUGUN_G = "26 Ekim 2026"
SURUM = "10"
YASAK = ["en ucuz", "garanti", "1 numara", "bir numaralı", "%100", "lider", "yılı aşkın", "yıllık tecrübe",
         "en iyi", "sigortalı", "kendi üretimimiz", "fabrikamız", "lorem"]

# Google Ads etiketi (kullanıcı 2026-10-26): global gtag + "Tıkla ve ara" dönüşümü; tel: tıklaması site.js'te bağlı
ADS_ID = "AW-18538306458"
ADS_ARAMA = "AW-18538306458/KFbSCLqyuaodEJq34IdF"
ADS_ETIKET = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ADS_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{ADS_ID}');
</script>
<!-- Event snippet for Tıkla ve ara conversion page -->
<script>
function gtag_report_conversion(url) {{
  var callback = function () {{
    if (typeof(url) != 'undefined') {{
      window.location = url;
    }}
  }};
  gtag('event', 'conversion', {{
      'send_to': '{ADS_ARAMA}',
      'value': 1.0,
      'currency': 'TRY',
      'event_callback': callback
  }});
  return false;
}}
</script>"""

e = html.escape
ONEK = ""
def ic(y): return (ONEK + y) if y else (ONEK or "./")
def tr_lower(s): return s.replace("I", "ı").replace("İ", "i").lower()
def tl(n): return f"{n:,.0f}".replace(",", ".")

KSLUG = {k["slug"]: k for k in KATEGORILER}

def baglar(s):
    """[[slug|yazı]] / [[slug#capa|yazı]] → göreli iç link."""
    def r(m):
        hedef, yazi = m.group(1), m.group(2)
        yol, _, capa = hedef.partition("#")
        href = (ic(yol + "/") if yol else ic("")) + (("#" + capa) if capa else "")
        return f'<a href="{href}">{yazi}</a>'
    return re.sub(r"\[\[([a-z0-9#/-]*)\|([^\]]+)\]\]", r, s)

# ------------------------------------------------------------------ görseller
OLCU = {}
def kaynak(ad):
    for y in (f"img/stok/{ad}.jpg", f"images/{ad}.webp", f"images/{ad}.jpg"):
        if os.path.exists(os.path.join(KOK, y)): return os.path.join(KOK, y)
    raise SystemExit(f"görsel yok: {ad}")

def gorselleri_hazirla():
    from PIL import Image, ImageOps
    for d in ("images/g", "images/k"): os.makedirs(os.path.join(KOK, d), exist_ok=True)
    for ad in GORSEL:
        k = kaynak(ad)
        for d, (w, q) in {"g": (1600, 82), "k": (640, 74)}.items():
            t = os.path.join(KOK, f"images/{d}/{ad}.webp")
            if not os.path.exists(t) or os.path.getmtime(t) < os.path.getmtime(k):
                im = ImageOps.exif_transpose(Image.open(k)).convert("RGB"); im.thumbnail((w, 2400), Image.LANCZOS)
                im.save(t, "WEBP", quality=q, method=6)
        OLCU[ad] = Image.open(os.path.join(KOK, f"images/g/{ad}.webp")).size

FP = ' fetchpriority="high"'
def resim(ad, sinif="", yukle="lazy", sizes="(max-width: 760px) 100vw, 50vw"):
    w, h = OLCU[ad]
    sc = f' class="{sinif}"' if sinif else ""
    return (f'<img{sc} src="{ic(f"images/k/{ad}.webp")}" '
            f'srcset="{ic(f"images/k/{ad}.webp")} 640w, {ic(f"images/g/{ad}.webp")} {w}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{e(GORSEL[ad])}" loading="{yukle}"{FP if yukle == "eager" else ""} decoding="async">')

def altyazi(ad):
    return f'<figcaption>{"<b>Uygulamamızdan:</b> " if ad in GERCEK else ""}{e(GORSEL[ad])}</figcaption>'

def figur(ad, sizes="(max-width: 760px) 100vw, 560px"):
    return f'<figure class="cerceve">{resim(ad, sizes=sizes)}{altyazi(ad)}</figure>'

# ------------------------------------------------------------------ ikonlar (çizgi, currentColor)
IKON = {
 "orgu": '<path d="M3 3l18 18M3 9l12 12M3 15l6 6M9 3l12 12M15 3l6 6M21 3L3 21M21 9L9 21M21 15l-6 6M15 3L3 15M9 3L3 9"/>',
 "kafes": '<path d="M6 3l-3 5 3 5-3 5 3 3M12 3L9 8l3 5-3 5 3 3M18 3l-3 5 3 5-3 5 3 3M3 8h18M3 13h18M3 18h18"/>',
 "panel": '<path d="M3 4v17M21 4v17M3 7h18M3 18h18M7.5 7v11M12 7v11M16.5 7v11"/>',
 "jilet": '<circle cx="7" cy="12" r="4"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="12" r="4"/><path d="M2 12h20"/>',
 "diken": '<path d="M2 9h20M2 15h20M7 7l2 4M9 7l-2 4M15 13l2 4M17 13l-2 4"/>',
 "cim": '<path d="M3 21V9M7 21V6M11 21V8M15 21V5M19 21V7M3 21h18M3 9c1-2 2-2 4-3M11 8c1-2 2-2 4-3M15 5c2 0 3 1 4 2"/>',
 "kapi": '<path d="M3 21V4M21 21V4M3 5h8.5v15H3M12.5 5H21v15h-8.5M10 12.5h1M13 12.5h1"/>',
 "arsa": '<path d="M3 20l5-9 4 5 3-4 6 8zM3 20h18M17 7a2 2 0 1 0 0-.01"/>',
 "saha": '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M12 5v14M3 9h3v6H3M21 9h-3v6h3"/><circle cx="12" cy="12" r="2.2"/>',
 "tel": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1Z"/>',
 "konum": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "fiyat": '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
 "liste": '<path d="M9 6h12M9 12h12M9 18h12M4 6h.01M4 12h.01M4 18h.01"/>',
 "yer": '<path d="M3 7l6-3 6 3 6-3v13l-6 3-6-3-6 3zM9 4v13M15 7v13"/>',
 "direk": '<path d="M9 21V6l3-3 3 3v15M9 10h6M9 15h6M5 21h14M12 3V1"/>',
 "sepet": '<path d="M3 4h2l2.4 11.2a1 1 0 0 0 1 .8h9.2a1 1 0 0 0 1-.8L21 7H6M9 20h.01M18 20h.01"/>',
}
def ikon(ad, sinif="ikon"):
    return f'<svg class="{sinif}" viewBox="0 0 24 24" aria-hidden="true">{IKON[ad]}</svg>'
WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3Z"/></svg>')

def wa(metin="Merhaba, Doğanay Tel Örgü sipariş hattı için yazıyorum."):
    return f"https://wa.me/{WA}?text={e(metin)}"

# ------------------------------------------------------------------ şema
def isletme():
    return {"@type": "HomeAndConstructionBusiness", "@id": SITE + "#isletme", "name": AD, "url": SITE,
            "telephone": TEL, "image": SITE + "images/logo-kare.jpg", "logo": SITE + "images/logo-512.png",
            "address": {"@type": "PostalAddress", "streetAddress": ADRES["sokak"], "postalCode": ADRES["pk"],
                        "addressLocality": ADRES["ilce"], "addressRegion": ADRES["il"], "addressCountry": "TR"},
            "hasMap": HARITA_URL, "areaServed": [{"@type": "City", "name": "Ankara"}],
            "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": k["baslik"],
                            "url": SITE + k["slug"] + "/"}} for k in KATEGORILER]}

def breadcrumb(adimlar):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": n + 1, "name": a, "item": SITE + y} for n, (a, y) in enumerate(adimlar)]}

def sss_sema(sss):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": s,
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", baglar(c).replace("[[", ""))}} for s, c in sss]}

def makale(t, yol, gorsel):
    return {"@type": "Article", "headline": t, "datePublished": BUGUN, "dateModified": BUGUN, "inLanguage": "tr",
            "author": {"@id": SITE + "#isletme"}, "publisher": {"@id": SITE + "#isletme"},
            "image": SITE + f"images/g/{gorsel}.webp", "mainEntityOfPage": SITE + yol}

# ------------------------------------------------------------------ iskelet
def mega():
    kol = []
    for k in KATEGORILER:
        s = k["slug"]
        kol.append(f'<div class="mega-kol"><a class="mega-bas" href="{ic(s + "/")}">{ikon(k["ikon"])}<span>{e(k["baslik"])}</span></a>'
                   f'<a href="{ic(s + "-fiyatlari/")}">{e(k["baslik"])} Fiyatları</a>'
                   f'<a href="{ic(s + "-cesitleri/")}">{e(k["baslik"])} Çeşitleri</a>'
                   f'<a href="{ic(s + "/")}#kullanim-alanlari">Kullanım Alanları</a>'
                   f'<a href="{ic(s + "/")}#siparis-ver">Sipariş Ver</a></div>')
    return '<div class="mega" id="mega">' + "".join(kol) + "</div>"

def bas(yol, title, desc, sema, ogimg=None, onyukle=None, aktif=""):
    url = SITE + yol
    og = f"{SITE}images/g/{ogimg}.webp" if ogimg else f"{SITE}images/logo-kare.jpg"
    ow, oh = OLCU[ogimg] if ogimg else (630, 630)
    pre = (f'\n<link rel="preload" as="image" href="{ic(f"images/g/{onyukle}.webp")}" imagesrcset="{ic(f"images/k/{onyukle}.webp")} 640w, '
           f'{ic(f"images/g/{onyukle}.webp")} {OLCU[onyukle][0]}w" imagesizes="100vw" fetchpriority="high">' if onyukle else "")
    ac = ' aria-current="page"'
    def m(h, a): return f'<a href="{ic(h)}"{ac if h == yol else ""}>{a}</a>'
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{AD}"><meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{og}"><meta property="og:image:width" content="{ow}"><meta property="og:image:height" content="{oh}">
<meta property="og:image:alt" content="{e(GORSEL.get(ogimg, AD + ' logosu'))}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#061D3D">{pre}
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="192x192" href="/images/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{ic('assets/site.css')}?v={SURUM}">
{ADS_ETIKET}
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": sema}, ensure_ascii=False)}</script>
</head>
<body>
<div class="ust-serit"><div class="ic">
 <span>{ikon("konum", "ikon-k")} Gölbaşı / Ankara</span>
 <a href="tel:{TEL}">{ikon("tel", "ikon-k")} Sipariş hattı: {TEL_G}</a>
</div></div>
<header class="ust"><div class="ic">
 <a class="logo" href="{ic('')}" aria-label="{AD} anasayfa"><img src="{ic('images/logo-amblem.png')}" width="240" height="178" alt="" decoding="async"><span class="logo-yazi"><b>DOĞANAY</b><small>TEL ÖRGÜ</small></span></a>
 <nav class="menu" id="menu" aria-label="Ana menü">
  {m("", "Anasayfa")}
  <div class="menu-urun{" aktif" if aktif == "urun" else ""}"><button type="button" class="mega-btn" aria-expanded="false" aria-controls="mega">Ürünler</button>{mega()}</div>
  {m("ankara-ilceleri/", "İlçeler")}{m("siparis-hatti/", "Sipariş Hattı")}{m("hakkimizda/", "Hakkımızda")}{m("iletisim/", "İletişim")}
 </nav>
 <a class="btn btn-tur ust-cta" href="tel:{TEL}">Teklif Al</a>
 <button class="menu-btn" type="button" aria-controls="menu" aria-expanded="false" aria-label="Menüyü aç"><span></span></button>
</div></header>
<main>
"""

def cta_bant(baslik="Sipariş ve keşif için Doğanay Tel Örgü sipariş hattı",
             alt="Ürünü, metrajı ve yüksekliği söyleyin; Ankara'da net fiyatı ve teslim gününü birlikte belirleyelim."):
    return f"""<section class="cta"><div class="ic">
 <div class="cta-metin"><h2>{baslik}</h2><p>{alt}</p></div>
 <div class="dugmeler"><a class="btn btn-tur" href="tel:{TEL}">{ikon("tel", "ikon-b")} {TEL_G}</a>
 <a class="btn btn-cizgi" href="{wa()}" target="_blank" rel="noopener">{WA_SVG} WhatsApp'tan sipariş</a></div>
</div></section>"""

def son():
    kat = "".join(f'<li><a href="{ic(k["slug"] + "/")}">{e(k["baslik"])}</a></li>' for k in KATEGORILER)
    fiy = "".join(f'<li><a href="{ic(k["slug"] + "-fiyatlari/")}">{e(k["baslik"])} Fiyatları</a></li>' for k in KATEGORILER)
    return f"""</main>
<footer class="alt"><div class="ic alt-izgara">
 <div class="alt-kol">
  <img class="alt-logo" src="{ic('images/logo-tam.png')}" width="640" height="550" alt="{AD} logosu" loading="lazy" decoding="async">
  <p class="alt-kisa">Gölbaşı'nda tel örgü, dikenli tel, kafes tel, panel çit, jiletli tel ve çim çit satışı ve montajı.</p>
 </div>
 <div class="alt-kol"><p class="alt-bas">Ürünler</p><ul>{kat}</ul></div>
 <div class="alt-kol"><p class="alt-bas">Fiyatlar {FIYAT_TARIH}</p><ul>{fiy}</ul></div>
 <div class="alt-kol"><p class="alt-bas">Sipariş Hattı</p>
  <p><a class="alt-tel" href="tel:{TEL}">{TEL_G}</a></p>
  <p><a href="{wa()}" target="_blank" rel="noopener">WhatsApp'tan yazın</a></p>
  <address>{ADRES_G}</address>
  <p><a href="{HARITA_URL}" target="_blank" rel="noopener">Haritada aç →</a></p>
  <p><a href="{ic('ankara-ilceleri/')}">Ankara ilçeleri</a> · <a href="{ic('siparis-hatti/')}">Sipariş hattı</a> · <a href="{ic('hakkimizda/')}">Hakkımızda</a> · <a href="{ic('iletisim/')}">İletişim</a></p></div>
</div>
<div class="alt-not"><div class="ic"><p>© 2026 {AD} · Fiyat bilgileri {FIYAT_TARIH} piyasa araştırmasıdır, bağlayıcı teklif değildir.</p></div></div>
<div class="w4"><div class="w4-bag"><span class="w4-etiket">Web Tasarım:</span> <a class="w4-ad" href="https://www.web4medya.com/" target="_blank" rel="noopener">Web<span class="w4-d">4</span>Medya</a></div></div>
</footer>
<div class="dock" id="dock"><a class="dock-tel" href="tel:{TEL}"><small>Sipariş hattı</small><span>{TEL_G}</span></a>
<a class="dock-wa" href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp'tan yaz">{WA_SVG}</a></div>
<aside class="danisma" id="danisma" role="dialog" aria-labelledby="danisma-bas" hidden>
 <button class="danisma-kapat" type="button" aria-label="Bildirimi kapat">×</button>
 <span class="danisma-ikon">{ikon("tel")}</span>
 <p class="danisma-bas" id="danisma-bas">Ücretsiz danışma hattımızı arayın:</p>
 <a class="btn btn-mavi nabiz danisma-btn" href="tel:{TEL}">{ikon("tel", "ikon-b")} {TEL_G}</a>
</aside>
<script src="{ic('assets/site.js')}?v={SURUM}" defer></script>
</body>
</html>
"""

def iz(adimlar):
    p = [f'<a href="{ic(y)}">{e(a)}</a>' for a, y in adimlar[:-1]] + [f'<span aria-current="page">{e(adimlar[-1][0])}</span>']
    return '<nav class="iz" aria-label="Konum">' + ' <span aria-hidden="true">›</span> '.join(p) + '</nav>'

def sss_html(sss):
    return '<div class="sss">' + "".join(f"<details><summary>{e(s)}</summary><p>{baglar(c)}</p></details>" for s, c in sss) + "</div>"

def kategori_kartlari(haric=None):
    li = []
    for k in KATEGORILER:
        if k is haric: continue
        li.append(f'<li class="kart"><a href="{ic(k["slug"] + "/")}"><span class="kart-gorsel">'
                  f'{resim(k["gorsel"], sizes="(max-width: 600px) 100vw, (max-width: 1000px) 50vw, 300px")}</span>'
                  f'<span class="kart-govde"><span class="kart-ikon">{ikon(k["ikon"])}</span><b>{e(k["baslik"])}</b>'
                  f'<span>{e(k["kisa"])}</span><span class="kart-ok">İncele →</span></span></a></li>')
    return '<ul class="kartlar">' + "".join(li) + "</ul>"

def ilce_html(urun=None, n0=0):
    """İlçe çipleri → ilçe sayfalarına bağlantı (ürün verilmezse ürünler sırayla döner: örümcek ağı)."""
    li = []
    for j, i in enumerate(ILCE):
        u = urun or URUNLER[(n0 + j) % len(URUNLER)]
        li.append(f'<li><a href="{ic(i["slug"] + "-" + u["ek"] + "/")}">{e(i["ad"])} {e(u["kisa"])}</a></li>')
    return '<ul class="ilceler">' + "".join(li) + "</ul>"

def harita(baslik="Doğanay Tel Örgü konumu"):
    return (f'<div class="harita"><iframe src="{HARITA_EMBED}" title="{e(baslik)}" loading="lazy" '
            f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>')

def galeri():
    return '<ul class="galeri">' + "".join(
        f'<li><a href="{ic(f"images/g/{a}.webp")}" data-buyut><figure>{resim(a, sizes="(max-width: 600px) 100vw, (max-width: 1000px) 50vw, 380px")}'
        f'{altyazi(a)}</figure></a></li>' for a in GALERI) + "</ul>"

def bolumler(govde):
    """[(h2, html), ...] → içerik bölümleri; h2 None ise düz blok."""
    out = []
    for b in govde:
        h2, icerik = b[0], b[1]
        kimlik = f' id="{b[2]}"' if len(b) > 2 else ""
        out.append(f'<section class="yazi-bol"{kimlik}>' + (f"<h2>{h2}</h2>" if h2 else "") + baglar(icerik) + "</section>")
    return "".join(out)

def icindekiler(govde, ek=(), on=()):
    li = list(on) + [(b[0], b[2]) for b in govde if b[0] and len(b) > 2] + list(ek)
    if len(li) < 3: return ""
    return ('<nav class="icindekiler" aria-label="İçindekiler"><p class="ic-bas">Bu sayfada</p><ol>' +
            "".join(f'<li><a href="#{c}">{re.sub(r"<[^>]+>", "", h)}</a></li>' for h, c in li) + "</ol></nav>")

def alt_sekme(k, aktif):
    s = k["slug"]
    sek = [("kategori", f"{s}/", k["baslik"], k["ikon"]), ("fiyat", f"{s}-fiyatlari/", "Fiyatları", "fiyat"),
           ("cesit", f"{s}-cesitleri/", "Çeşitleri", "liste"), ("kullanim", f"{s}/#kullanim-alanlari", "Kullanım Alanları", "yer"),
           ("siparis", f"{s}/#siparis-ver", "Sipariş Ver", "sepet")]
    out = []
    for kod, yol, ad, ik in sek:
        y, _, c = yol.partition("#")
        href = ic(y) + (("#" + c) if c else "")
        ac = ' aria-current="page"' if kod == aktif else ""
        out.append(f'<a href="{href}"{ac}>{ikon(ik)}<span>{e(ad)}</span></a>')
    return '<nav class="sekme" aria-label="' + e(k["baslik"]) + ' sayfaları">' + "".join(out) + "</nav>"

def sayfa_bas(adim, h1, giris, gorsel, wa_metin, ek=""):
    return f"""<section class="sayfa-bas"><div class="sb-fon" aria-hidden="true">{resim(gorsel, "kb", "eager", "100vw")}</div>
<div class="desen" aria-hidden="true"></div>
<div class="ic">
 {iz(adim)}
 <h1>{h1}</h1>
 <p class="giris">{giris}</p>
 <div class="dugmeler"><a class="btn btn-mavi nabiz" href="tel:{TEL}">{ikon("tel", "ikon-b")} {TEL_G}</a>
 <a class="btn btn-cizgi" href="{wa(wa_metin)}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
 {ek}
</div></section>"""

def siparis_kutu(k):
    return f"""<aside class="siparis-kutu">
 <div><p class="ust-etiket koyu">Doğanay Tel Örgü sipariş hattı</p>
 <p class="sk-bas">{e(k["baslik"])} için net fiyat ve teslim günü</p>
 <p>Piyasa rakamları fikir versin diye burada. Sizin işinizin fiyatı metraja, yüksekliğe ve zemine göre çıkıyor; telefonda
 birkaç soruyla netleştiriyoruz.</p></div>
 <div class="dugmeler"><a class="btn btn-tur" href="tel:{TEL}">{ikon("tel", "ikon-b")} {TEL_G}</a>
 <a class="btn btn-wa" href="{wa(f'Merhaba, {k["baslik"]} için fiyat almak istiyorum.')}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
</aside>"""

# ------------------------------------------------------------------ fiyat tabloları
def tr_tablo(satirlar):
    def kay(ka, url):
        return f'<a href="{url}" target="_blank" rel="noopener nofollow">{e(ka)}</a>' if url else e(ka)
    g = "".join(f'<tr><th scope="row">{e(u)}</th><td data-l="Ölçü">{e(o)}</td><td class="tutar" data-l="Fiyat">{e(f)}</td>'
                f'<td class="kaynak" data-l="Kaynak">{kay(ka, url)}</td></tr>' for u, o, f, ka, url in satirlar)
    return (f'<div class="tablo-sar"><table class="fiyat-tbl kartli"><thead><tr><th scope="col">Ürün</th><th scope="col">Ölçü / özellik</th>'
            f'<th scope="col">Fiyat</th><th scope="col">Kaynak</th></tr></thead><tbody>{g}</tbody></table></div>')

def yd_tablo(satirlar):
    g = []
    for ulke, u, o, tutar, para, birim, ka, url in satirlar:
        isaret = {"USD": "$", "EUR": "€", "GBP": "£"}[para]
        if isinstance(tutar, tuple):
            yerel = f"{isaret}{tutar[0]:,.2f}–{isaret}{tutar[1]:,.2f}"
            tlk = f"≈ {tl(tutar[0] * KUR[para][0])}–{tl(tutar[1] * KUR[para][0])} TL"
        else:
            yerel = f"{isaret}{tutar:,.2f}"; tlk = f"≈ {tl(tutar * KUR[para][0])} TL"
        g.append(f'<tr><th scope="row">{e(ulke)}</th><td data-l="Ürün">{e(u)}<small>{e(o)}</small></td><td class="tutar" data-l="Yerel">{yerel}<small>{e(birim)}</small></td>'
                 f'<td class="tutar tl" data-l="TL">{tlk}</td><td class="kaynak" data-l="Kaynak"><a href="{url}" target="_blank" rel="noopener nofollow">{e(ka)}</a></td></tr>')
    return (f'<div class="tablo-sar"><table class="fiyat-tbl kartli"><thead><tr><th scope="col">Ülke</th><th scope="col">Ürün</th>'
            f'<th scope="col">Yerel fiyat</th><th scope="col">TL karşılığı</th><th scope="col">Kaynak</th></tr></thead>'
            f'<tbody>{"".join(g)}</tbody></table></div>')

def kur_notu():
    return ('<p class="kur-not">TL karşılıkları ' + ", ".join(f"1 {p} = {v:.2f} TL" for p, (v, _) in KUR.items()) +
            f' kuruyla hesaplandı ({KUR["USD"][1]}). Yurtdışı fiyatlarına KDV/satış vergisi ülkeye göre dahil ya da hariç olabilir.</p>')

def ozet_kart(ozet, baslik):
    g = "".join(f'<li><span>{e(a)}</span><b>{e(b)}</b></li>' for a, b in ozet)
    return f'<div class="ozet-kart"><p class="ozet-bas">{baslik}</p><ul>{g}</ul><p class="ozet-not">Ankara, {FIYAT_TARIH} · KDV dahil perakende/piyasa aralığı</p></div>'

def karsilastirma(tablo):
    bas_, *sat = tablo
    th = "".join(f'<th scope="col">{e(x)}</th>' for x in bas_)
    tr = "".join("<tr>" + f'<th scope="row">{e(r[0])}</th>' + "".join(f"<td>{e(x)}</td>" for x in r[1:]) + "</tr>" for r in sat)
    return f'<div class="tablo-sar"><table class="kars-tbl"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

# ------------------------------------------------------------------ sayfalar
HERO = "beton-direk-ve-tel-orgu"

def anasayfa():
    t = f"Ankara Tel Örgü - {TEL_G} | Doğanay Tel Örgü Gölbaşı"
    d = ("Ankara tel örgü, dikenli tel, kafes tel, panel çit, jiletli tel ve çim çit: 2026 fiyatları, çeşitleri ve montaj. "
         f"Doğanay Tel Örgü sipariş hattı: {TEL_G}")
    sss = [
     ("Ankara'da tel örgü siparişi için kime ulaşabilirim?",
      f"Doğanay Tel Örgü sipariş hattı {TEL_G}. Aynı numaraya WhatsApp'tan da yazabilirsiniz; ürün, metraj ve yüksekliği söylemeniz yeterli."),
     ("Doğanay Tel Örgü nerede?", f"Adresimiz {ADRES_G}. Haritadaki konumumuzdan yol tarifi alabilirsiniz."),
    ] + GENEL_SSS
    sema = [isletme(), {"@type": "WebSite", "@id": SITE + "#site", "url": SITE, "name": AD, "inLanguage": "tr"}, sss_sema(sss)]
    rozet = "".join(f'<li><a href="{ic(k["slug"] + "/")}">{ikon(k["ikon"])}<span>{e(k["ad"])}</span></a></li>' for k in KATEGORILER[:6])
    fiyat_sat = "".join(
        f'<tr><th scope="row"><a href="{ic(k["slug"] + "-fiyatlari/")}">{e(k["baslik"])} fiyatları</a></th>'
        f'<td>{e(k["fiyat"]["ozet"][0][0])}</td><td class="tutar">{e(k["fiyat"]["ozet"][0][1])}</td></tr>' for k in KATEGORILER)
    return bas("", t, d, sema, AFIS, onyukle=HERO) + f"""
<section class="hero"><div class="hero-fon" aria-hidden="true">{resim(HERO, "kb", "eager", "100vw")}</div>
<div class="desen" aria-hidden="true"></div>
<div class="ic hero-ic">
  <p class="ust-etiket">Gölbaşı · Ankara</p>
  <h1>Ankara Tel Örgü <span>ve Çit Sistemleri</span></h1>
  <p class="giris">Tel örgü, dikenli tel, kafes tel, panel çit, jiletli tel, çim çit… Hepsini burada; fiyatıyla, çeşidiyle,
  nerede işe yarayıp nerede yaramadığıyla anlattık. Tüm sorularınız için 7/24 arayabilirsiniz.</p>
  <div class="dugmeler"><a class="btn btn-mavi nabiz" href="tel:{TEL}">{ikon("tel", "ikon-b")} {TEL_G}</a>
  <a class="btn btn-cizgi" href="{wa('Merhaba, tel örgü için teklif almak istiyorum.')}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
  <ul class="hero-rozet">{rozet}</ul>
</div></section>

<section class="blok" id="urunler"><div class="ic">
 <p class="ust-etiket koyu">Ürünler ve hizmetler</p>
 <h2>Ankara'da tel örgü ve çit ürünleri</h2>
 <p class="bolum-giris">Bahçe için başka, fabrika için başka, tarla için başka bir çit doğru olur. Ürüne tıklayın; fiyatını,
 çeşitlerini, kullanım alanlarını ve nasıl sipariş vereceğinizi tek tek anlattık.</p>
 {kategori_kartlari()}
</div></section>

<section class="blok acik" id="fiyatlar"><div class="ic iki">
 <div class="kol">
  <p class="ust-etiket koyu">{FIYAT_TARIH} fiyatları</p>
  <h2>Ankara tel örgü fiyatları özet</h2>
  <p>Aşağıdaki rakamlar {FIYAT_TARIH} itibarıyla Türkiye piyasasından topladığımız başlangıç aralıkları. Her ürünün sayfasında
  kaynaklarıyla birlikte ayrıntılı tabloyu, yurtdışı fiyatlarıyla karşılaştırmayı ve fiyatı neyin değiştirdiğini bulacaksınız.</p>
  {kutu_html("onemli", "Bunlar piyasa rakamları, bizim teklifimiz değil. Net fiyat için metraj ve yükseklikle sipariş hattımızı arayın.")}
 </div>
 <div class="kol"><div class="tablo-sar"><table class="fiyat-tbl ozet-tbl"><thead><tr><th scope="col">Sayfa</th><th scope="col">Kalem</th><th scope="col">Piyasa</th></tr></thead>
 <tbody>{fiyat_sat}</tbody></table></div></div>
</div></section>

<section class="blok koyu"><div class="desen" aria-hidden="true"></div><div class="ic iki">
 <div class="kol">
  <p class="ust-etiket">Neden Doğanay?</p>
  <h2>Çitin ömrünü direk belirler</h2>
  <p>Tel ne kadar iyi olursa olsun, direk sağlam oturmamışsa ve tel gerdirilmeden bağlanmışsa çit birkaç kışta sarkar.
  Bu yüzden işe her zaman direkten başlıyoruz: hattı ip ile çekiyor, köşe ve uç direklerini payandalıyor, betonun
  oturmasını bekliyoruz.</p>
  <ul class="tik">
   <li>Yerinde keşif ve ölçü</li><li>Malzeme ve işçilik ayrı ayrı, açık fiyat</li>
   <li>Malzemeli ya da yalnız işçilik</li><li>Gölbaşı merkezli, Ankara genelinde</li></ul>
 </div>
 <div class="kol"><a class="afis" href="{ic('hakkimizda/')}">{resim(AFIS, sizes="(max-width: 760px) 100vw, 600px")}</a>
  <p><a class="ok-link acik-ok" href="{ic('hakkimizda/')}">Doğanay Tel Örgü'yü tanıyın →</a></p></div>
</div></section>

<section class="blok"><div class="ic">
 <p class="ust-etiket koyu">Uygulamalarımızdan</p>
 <h2>Sahada yaptığımız tel örgü işleri</h2>
 <p class="bolum-giris">Beton direkli galvaniz tel örgü, panel çit üstü jiletli tel, tarla ve sanayi parseli çevirme.
 Fotoğrafların hepsi kendi işlerimiz.</p>
 {galeri()}
</div></section>

<section class="blok acik"><div class="ic">
 <p class="ust-etiket koyu">Nasıl çalışıyoruz?</p>
 <h2>Telefondan teslime 5 adım</h2>
 <ol class="surec">{"".join(f"<li><h3>{a}</h3><p>{p}</p></li>" for a, p in SUREC)}</ol>
</div></section>

<section class="blok"><div class="ic iki">
 <div class="kol">
  <p class="ust-etiket koyu">Hizmet bölgesi</p>
  <h2>Gölbaşı'ndan Ankara'nın ilçelerine</h2>
  <p>Atölyemiz Gölbaşı Gaziosmanpaşa'da. Gölbaşı ve çevresinin yanında Ankara'nın ilçelerinde de tel örgü ve çit
  işi yapıyoruz. İlçenize tıklayın; o ilçenin arazisine göre hazırladığımız fiyat ve uygulama sayfasına gidin.</p>
  {ilce_html()}
  <p><a class="ok-link" href="{ic('ankara-ilceleri/')}">20 ilçede beton direk, jiletli tel ve tel örgü →</a></p>
 </div>
 <div class="kol">{harita()}
  <p class="adres">{ikon("konum", "ikon-k")} <span>{ADRES_G}</span> · <a href="{HARITA_URL}" target="_blank" rel="noopener">Yol tarifi al</a></p></div>
</div></section>

<section class="blok acik"><div class="ic iki">
 <div class="kol"><p class="ust-etiket koyu">Merak edilenler</p><h2>Sık sorulan sorular</h2>
  <p>Aklınızdaki soru burada yoksa çekinmeden arayın; telefonda kısa bir konuşma çoğu zaman yeterli oluyor.</p>
  <p><a class="btn btn-lac" href="tel:{TEL}">{ikon("tel", "ikon-b")} {TEL_G}</a></p></div>
 <div class="kol">{sss_html(sss)}</div>
</div>
<div class="ic">{TEMSILI}</div></section>
""" + cta_bant("Ankara'da tel örgü siparişi mi vereceksiniz?") + son()

URUN_KAT = {u["kat"]: u for u in URUNLER}

def ilce_bas(k):
    u = URUN_KAT.get(k["slug"])
    return f"İlçelere göre {u['ad'].lower()} fiyatları" if u else "Ankara'da hizmet verdiğimiz ilçeler"

def ilce_fiyat_blok(k):
    u = URUN_KAT.get(k["slug"])
    if not u: return ""
    li = "".join(f'<li><a href="{ic(i["slug"] + "-" + u["ek"] + "/")}">{e(i["ad"])} {e(u["ad"].lower())} fiyatları</a></li>' for i in ILCE)
    return (f'<section class="blok acik"><div class="ic"><h2>İlçe ilçe {e(u["ad"].lower())} fiyatları ve satan yerler</h2>'
            f'<p class="bolum-giris">Gölbaşı\'ndan Ankara\'nın 20 ilçesine sevkiyat yapıyoruz. İlçenize özel mesafe, uygulama ve fiyat notları için seçin.</p>'
            f'<ul class="link-bulut">{li}</ul></div></section>')

TEMSILI = '<p class="temsili">"Uygulamamızdan" etiketli fotoğraflar kendi işlerimizdir; diğerleri ürün türünü gösteren temsilî görsellerdir.</p>'

def kutu_html(tur, metin):
    ad = {"tavsiye": "Tavsiyemiz", "dikkat": "Dikkat", "onemli": "Önemli", "not": "Bizden not", "ipucu": "Usta ipucu"}[tur]
    return f'<div class="kutu kutu-{tur}"><b>{ad}:</b> {baglar(metin)}</div>'


def kategori_sayfasi(k):
    yol = k["slug"] + "/"
    c = k["kat"]
    adim = [("Anasayfa", ""), (k["baslik"], yol)]
    sema = [isletme(), breadcrumb(adim), sss_sema(c["sss"]),
            {"@type": "Service", "name": k["baslik"], "serviceType": k["ad"], "description": k["kisa"],
             "provider": {"@id": SITE + "#isletme"}, "areaServed": {"@type": "City", "name": "Ankara"}, "url": SITE + yol}]
    kul = "".join(f'<li><b>{e(a)}</b><span>{baglar(b)}</span></li>' for a, b in c["kullanim"])
    sip = "".join(f"<li>{baglar(x)}</li>" for x in c["siparis"])
    ek = [("Kullanım alanları", "kullanim-alanlari"), ("Sipariş ver", "siparis-ver"), ("Sık sorulanlar", "sss")]
    return bas(yol, c["title"], c["desc"], sema, k["gorsel"], onyukle=k["gorsel"], aktif="urun") + sayfa_bas(
        adim, e(c["h1"]), baglar(c["ust"]), k["gorsel"], f'Merhaba, {k["baslik"]} siparişi vermek istiyorum.') + f"""
<div class="sekme-sar"><div class="ic">{alt_sekme(k, "kategori")}</div></div>

<section class="blok"><div class="ic yazi-izgara">
 <article class="yazi">
  {icindekiler(c["govde"], ek)}
  {bolumler(c["govde"])}
 </article>
 <aside class="yan">
  {figur(k["gorsel2"], "(max-width: 960px) 100vw, 360px")}
  <div class="yan-kutu"><p class="yk-bas">{e(k["baslik"])} rehberi</p>
   <a href="{ic(k['slug'] + '-fiyatlari/')}">{ikon("fiyat")} {e(k["baslik"])} Fiyatları {FIYAT_TARIH[-4:]}</a>
   <a href="{ic(k['slug'] + '-cesitleri/')}">{ikon("liste")} {e(k["baslik"])} Çeşitleri</a>
   <a href="#kullanim-alanlari">{ikon("yer")} Kullanım Alanları</a>
   <a href="#siparis-ver">{ikon("sepet")} Sipariş Ver</a></div>
  {ozet_kart(k["fiyat"]["ozet"][:3], k["baslik"] + " piyasa fiyatı")}
 </aside>
</div></section>

<section class="blok acik" id="kullanim-alanlari"><div class="ic">
 <p class="ust-etiket koyu">Kullanım alanları</p>
 <h2>{e(k["baslik"])} kullanım alanları</h2>
 <p class="bolum-giris">{baglar(c["kullanim_giris"])}</p>
 <ul class="secenek">{kul}</ul>
</div></section>

<section class="blok" id="siparis-ver"><div class="ic iki">
 <div class="kol">
  <p class="ust-etiket koyu">Sipariş ver</p>
  <h2>{e(k["baslik"])} sipariş ver</h2>
  <p>Sipariş için Doğanay Tel Örgü sipariş hattını arayın ya da WhatsApp'tan yazın. Doğru fiyatı hemen verebilmemiz için
  şunları söylemeniz yeterli:</p>
  <ol class="kisa-adim">{sip}</ol>
  <p>Formu doldurup mesajı hazır göndermek isterseniz [[siparis-hatti|sipariş hattı sayfamızı]] kullanabilirsiniz.</p>
 </div>
 <div class="kol">{siparis_kutu(k)}</div>
</div></section>

<section class="blok acik" id="sss"><div class="ic iki">
 <div class="kol"><h2>{e(k["baslik"])} hakkında sık sorulanlar</h2>{sss_html(c["sss"])}</div>
 <div class="kol"><h2>{ilce_bas(k)}</h2>
  <p>Gölbaşı merkezli olarak Ankara'nın ilçelerinde çalışıyoruz. İlçenizi seçin; o ilçeye özel fiyat, sevkiyat ve uygulama
  notlarını görün. Tümü için <a href="{ic('ankara-ilceleri/')}">Ankara ilçeleri</a> sayfasına bakın.</p>{ilce_html(URUN_KAT.get(k["slug"]), KATEGORILER.index(k))}</div>
</div></section>

<section class="blok"><div class="ic">
 <h2>Diğer ürünlerimiz</h2>
 {kategori_kartlari(k)}
 {TEMSILI}
</div></section>
""".replace("[[siparis-hatti|sipariş hattı sayfamızı]]", f'<a href="{ic("siparis-hatti/")}">sipariş hattı sayfamızı</a>') + cta_bant(
        f"{e(k['baslik'])} siparişi için arayın") + son()


def fiyat_sayfasi(k):
    yol = k["slug"] + "-fiyatlari/"
    f = k["fiyat"]
    adim = [("Anasayfa", ""), (k["baslik"], k["slug"] + "/"), ("Fiyatları", yol)]
    sema = [isletme(), breadcrumb(adim), sss_sema(f["sss"]), makale(f["h1"], yol, k["gorsel"])]
    on = [("Türkiye fiyatları", "turkiye-fiyatlari"), ("Yurtdışı karşılaştırması", "yurtdisi-fiyatlari")]
    ek = [("Sık sorulanlar", "sss")]
    return bas(yol, f["title"], f["desc"], sema, k["gorsel"], onyukle=k["gorsel"], aktif="urun") + sayfa_bas(
        adim, e(f["h1"]), baglar(f["ust"]), k["gorsel"], f'Merhaba, {k["baslik"]} fiyatı almak istiyorum.',
        f'<p class="tarih">Güncelleme: <time datetime="{BUGUN}">{BUGUN_G}</time> · Fiyatlar {FIYAT_TARIH} piyasa verisidir</p>') + f"""
<div class="sekme-sar"><div class="ic">{alt_sekme(k, "fiyat")}</div></div>

<section class="blok"><div class="ic yazi-izgara">
 <article class="yazi">
  {icindekiler(f["govde"], ek, on)}
  {bolumler(f["giris"])}
  <section class="yazi-bol" id="turkiye-fiyatlari"><h2>{e(k["baslik"])} fiyatları: Türkiye piyasası ({FIYAT_TARIH})</h2>
   {baglar(f["tr_giris"])}
   {tr_tablo(f["tr"])}
   {baglar(f.get("tr_son", ""))}
  </section>
  <section class="yazi-bol" id="yurtdisi-fiyatlari"><h2>Yurtdışı fiyatlarıyla karşılaştırma</h2>
   {baglar(f["yd_giris"])}
   {yd_tablo(f["yd"])}
   {kur_notu()}
   {baglar(f["yd_yorum"])}
  </section>
  {bolumler(f["govde"])}
  {siparis_kutu(k)}
 </article>
 <aside class="yan">
  {ozet_kart(f["ozet"], k["baslik"] + " fiyatları özet")}
  <div class="yan-kutu"><p class="yk-bas">{e(k["baslik"])} rehberi</p>
   <a href="{ic(k['slug'] + '/')}">{ikon(k["ikon"])} {e(k["baslik"])}</a>
   <a href="{ic(k['slug'] + '-cesitleri/')}">{ikon("liste")} {e(k["baslik"])} Çeşitleri</a>
   <a href="{ic(k['slug'] + '/')}#kullanim-alanlari">{ikon("yer")} Kullanım Alanları</a>
   <a href="{ic(k['slug'] + '/')}#siparis-ver">{ikon("sepet")} Sipariş Ver</a></div>
 </aside>
</div></section>

<section class="blok acik" id="sss"><div class="ic dar-ic">
 <h2>{e(k["baslik"])} fiyatları hakkında sık sorulanlar</h2>{sss_html(f["sss"])}
</div></section>

{ilce_fiyat_blok(k)}
<section class="blok"><div class="ic">
 <h2>Diğer ürünlerin fiyatları</h2>
 <ul class="link-bulut">{"".join(f'<li><a href="{ic(x["slug"] + "-fiyatlari/")}">{e(x["baslik"])} fiyatları</a></li>' for x in KATEGORILER if x is not k)}</ul>
</div></section>
""" + cta_bant(f"{e(k['baslik'])} için net fiyat alın") + son()


def cesit_sayfasi(k):
    yol = k["slug"] + "-cesitleri/"
    c = k["cesit"]
    adim = [("Anasayfa", ""), (k["baslik"], k["slug"] + "/"), ("Çeşitleri", yol)]
    sema = [isletme(), breadcrumb(adim), sss_sema(c["sss"]), makale(c["h1"], yol, c.get("gorsel", k["gorsel2"]))]
    ces = "".join(
        f'<section class="cesit" id="{cid}"><div class="cesit-bas"><span class="cesit-no">{n + 1:02d}</span><h3>{e(ad)}</h3></div>'
        f'{baglar(govde)}' + (f'<ul class="etiketler">{"".join(f"<li>{e(x)}</li>" for x in etk)}</ul>' if etk else "") + "</section>"
        for n, (cid, ad, govde, etk) in enumerate(c["cesitler"]))
    ek = [("Karşılaştırma tablosu", "karsilastirma"), ("Sık sorulanlar", "sss")]
    return bas(yol, c["title"], c["desc"], sema, c.get("gorsel", k["gorsel2"]), onyukle=c.get("gorsel", k["gorsel2"]), aktif="urun") + sayfa_bas(
        adim, e(c["h1"]), baglar(c["ust"]), c.get("gorsel", k["gorsel2"]), f'Merhaba, {k["baslik"]} çeşitleri hakkında bilgi almak istiyorum.') + f"""
<div class="sekme-sar"><div class="ic">{alt_sekme(k, "cesit")}</div></div>

<section class="blok"><div class="ic yazi-izgara">
 <article class="yazi">
  {icindekiler([(None, "", "")] + [(ad, "", cid) for cid, ad, _, _ in c["cesitler"]], ek)}
  {bolumler(c["giris"])}
  <div class="cesitler">{ces}</div>
  <section class="yazi-bol" id="karsilastirma"><h2>{e(k["baslik"])} çeşitleri karşılaştırma</h2>
   {karsilastirma(c["tablo"])}</section>
  {bolumler(c["govde"])}
  {siparis_kutu(k)}
 </article>
 <aside class="yan">
  {figur(k["gorsel"], "(max-width: 960px) 100vw, 360px")}
  <div class="yan-kutu"><p class="yk-bas">{e(k["baslik"])} rehberi</p>
   <a href="{ic(k['slug'] + '/')}">{ikon(k["ikon"])} {e(k["baslik"])}</a>
   <a href="{ic(k['slug'] + '-fiyatlari/')}">{ikon("fiyat")} {e(k["baslik"])} Fiyatları</a>
   <a href="{ic(k['slug'] + '/')}#kullanim-alanlari">{ikon("yer")} Kullanım Alanları</a>
   <a href="{ic(k['slug'] + '/')}#siparis-ver">{ikon("sepet")} Sipariş Ver</a></div>
 </aside>
</div></section>

<section class="blok acik" id="sss"><div class="ic dar-ic">
 <h2>{e(k["baslik"])} çeşitleri hakkında sık sorulanlar</h2>{sss_html(c["sss"])}
</div></section>

<section class="blok"><div class="ic">
 <h2>Diğer ürünler</h2>
 {kategori_kartlari(k)}
 {TEMSILI}
</div></section>
""" + cta_bant() + son()


def siparis_hatti():
    yol = "siparis-hatti/"
    t = f"Sipariş Hattı {TEL_G} | Doğanay Tel Örgü Ankara"
    d = (f"Ankara Doğanay Tel Örgü sipariş hattı: {TEL_G}. Tel örgü, dikenli tel, kafes tel, panel çit, jiletli tel ve "
         "çim çit siparişi için arayın ya da yazın.")
    adim = [("Anasayfa", ""), ("Sipariş Hattı", yol)]
    sss = [
     ("Sipariş verirken ne söylemeliyim?", "Ürün, yaklaşık metraj (metre ya da m²), yükseklik, kapı olup olmayacağı ve işin yapılacağı ilçe yeterli. Fotoğraf atarsanız daha da iyi."),
     ("Sadece malzeme alabilir miyim?", "Evet, malzemeli ya da yalnız işçilik çalışabiliyoruz; ihtiyacınızı söyleyin, birlikte netleştirelim."),
     ("Siparişten sonra ne oluyor?", "Gerekiyorsa keşfe gelip ölçüyü yerinde alıyoruz, net fiyat ve iş gününü veriyoruz, montajı yapıp teslim ediyoruz."),
    ]
    sema = [isletme(), breadcrumb(adim), sss_sema(sss), {"@type": "ContactPage", "url": SITE + yol, "about": {"@id": SITE + "#isletme"}}]
    sec = "".join(f'<option>{e(k["baslik"])}</option>' for k in KATEGORILER)
    ilc = "".join(f"<option>{i['ad']}</option>" for i in ILCE) + "<option>Diğer</option>"
    return bas(yol, t, d, sema) + f"""
<section class="sayfa-bas sade"><div class="desen" aria-hidden="true"></div><div class="ic">
 {iz(adim)}
 <h1>Doğanay Tel Örgü Sipariş Hattı</h1>
 <p class="giris">Ankara'da tel örgü, dikenli tel, kafes tel, panel çit, jiletli tel ya da çim çit siparişi vermek için
 doğru yerdesiniz. Arayın ya da aşağıdaki formu doldurun; mesajınız WhatsApp'ta hazır açılsın.</p>
 <a class="hero-tel" href="tel:{TEL}"><small>Sipariş hattı</small>{TEL_G}</a>
</div></section>

<section class="blok"><div class="ic iki">
 <div class="kol">
  <h2>WhatsApp sipariş formu</h2>
  <p>Formdaki bilgiler hiçbir yere kaydedilmez; yalnızca WhatsApp mesajınızı hazırlar. Gönder dediğinizde WhatsApp açılır.</p>
  <form class="siparis-form" id="siparis-form" data-wa="{WA}">
   <label>Ürün<select name="urun" required>{sec}</select></label>
   <div class="form-iki"><label>Yaklaşık metraj<input name="metraj" inputmode="decimal" placeholder="Örn. 120 metre"></label>
   <label>Yükseklik<input name="yukseklik" placeholder="Örn. 150 cm"></label></div>
   <div class="form-iki"><label>İlçe<select name="ilce">{ilc}</select></label>
   <label>Montaj<select name="montaj"><option>Montajlı istiyorum</option><option>Sadece malzeme</option><option>Emin değilim</option></select></label></div>
   <label>Not<textarea name="not" rows="3" placeholder="Kapı, zemin, eğim gibi eklemek istedikleriniz"></textarea></label>
   <button class="btn btn-tur" type="submit">{WA_SVG} WhatsApp'tan gönder</button>
  </form>
 </div>
 <div class="kol">
  <ul class="ilet">
   <li>{ikon("tel")}<div><small>Sipariş hattı</small><a href="tel:{TEL}">{TEL_G}</a></div></li>
   <li><span class="ikon wa-ikon">{WA_SVG}</span><div><small>WhatsApp</small><a href="{wa()}" target="_blank" rel="noopener">{TEL_G}</a></div></li>
   <li>{ikon("konum")}<div><small>Adres</small><address>{ADRES_G}</address><a href="{HARITA_URL}" target="_blank" rel="noopener">Haritada aç →</a></div></li>
  </ul>
  <h2>Sık sorulanlar</h2>{sss_html(sss)}
 </div>
</div></section>

<section class="blok acik"><div class="ic">
 <h2>Ürünlerimiz</h2>
 {kategori_kartlari()}
</div></section>
""" + son()


def hakkimizda():
    yol = "hakkimizda/"
    t = "Hakkımızda | Doğanay Tel Örgü - Gölbaşı Ankara"
    d = ("Doğanay Tel Örgü, Gölbaşı'nda tel örgü, panel çit, jiletli ve dikenli tel işleri yapan ekip. Nasıl "
         "çalıştığımızı ve sahadaki işlerimizi görün.")
    adim = [("Anasayfa", ""), ("Hakkımızda", yol)]
    sema = [isletme(), breadcrumb(adim), {"@type": "AboutPage", "url": SITE + yol, "about": {"@id": SITE + "#isletme"}}]
    return bas(yol, t, d, sema, AFIS) + f"""
<section class="sayfa-bas sade"><div class="desen" aria-hidden="true"></div><div class="ic">
 {iz(adim)}
 <h1>Doğanay Tel Örgü</h1>
 <p class="giris">Gölbaşı'nda, Ankara'nın tel örgü ve çit işlerini yapan bir ekibiz. Konut bahçesinden fabrika
 çevresine, tarladan spor sahasına kadar alanları çeviriyoruz.</p>
</div></section>

<section class="blok"><div class="ic iki">
 <div class="kol"><figure class="afis-fig">{resim(AFIS, "", "eager", "(max-width: 760px) 100vw, 640px")}</figure></div>
 <div class="kol">
  <h2>Ne yapıyoruz?</h2>
  <p>Tel örgü, dikenli tel, kafes tel, panel çit, jiletli tel, çim çit ve çit kapısı. Kısacası bir alanın sınırını çizmek ve
  korumak için gereken işlerin hepsi. Alanı yerinde görüp ölçüyor, ihtiyaca uygun çiti birlikte seçiyor ve montajını yapıyoruz.</p>
  <h2>Nasıl çalışıyoruz?</h2>
  <p>Bir çitin ömrünü telden çok direk ve montaj belirler. Hattı ip ile çekiyor, köşe ve uç direklerini
  payandalıyor, betonun oturmasını bekleyip teli gerdirerek bağlıyoruz. Fiyatı da malzeme ve işçilik ayrı ayrı
  görünecek şekilde konuşuyoruz.</p>
  <ul class="tik koyu-tik"><li>Yerinde keşif ve ölçü</li><li>Malzemeli ya da yalnız işçilik</li>
   <li>Konut, sanayi, tarım ve spor alanları</li><li>Gölbaşı merkezli, Ankara genelinde</li></ul>
 </div>
</div></section>

<section class="blok acik"><div class="ic">
 <h2>Uygulamalarımızdan</h2>
 {galeri()}
</div></section>

<section class="blok"><div class="ic">
 <h2>Ürünlerimiz</h2>
 {kategori_kartlari()}
</div></section>
""" + cta_bant() + son()


def iletisim():
    yol = "iletisim/"
    t = f"İletişim - {TEL_G} | Doğanay Tel Örgü Gölbaşı Ankara"
    d = f"Doğanay Tel Örgü iletişim: {TEL_G}, WhatsApp ve adres: {ADRES_G}. Haritadan yol tarifi alın."
    adim = [("Anasayfa", ""), ("İletişim", yol)]
    sema = [isletme(), breadcrumb(adim), {"@type": "ContactPage", "url": SITE + yol, "about": {"@id": SITE + "#isletme"}}]
    return bas(yol, t, d, sema) + f"""
<section class="sayfa-bas sade"><div class="desen" aria-hidden="true"></div><div class="ic">
 {iz(adim)}
 <h1>İletişim</h1>
 <p class="giris">Tel örgü, panel çit ya da çit kapısı için arayın, WhatsApp'tan yazın ya da Gölbaşı'ndaki adresimize uğrayın.</p>
</div></section>

<section class="blok"><div class="ic iki">
 <div class="kol">
  <ul class="ilet">
   <li>{ikon("tel")}<div><small>Telefon</small><a href="tel:{TEL}">{TEL_G}</a></div></li>
   <li><span class="ikon wa-ikon">{WA_SVG}</span><div><small>WhatsApp</small><a href="{wa()}" target="_blank" rel="noopener">{TEL_G}</a></div></li>
   <li>{ikon("konum")}<div><small>Adres</small><address>{ADRES_G}</address><a href="{HARITA_URL}" target="_blank" rel="noopener">Haritada aç →</a></div></li>
  </ul>
  <p>Arayınca şunları söylemeniz yeterli: alanın yeri, yaklaşık uzunluğu (metre), istediğiniz yükseklik ve kapı
  olup olmayacağı. Fotoğraf atarsanız keşiften önce fikir verebiliriz. Hazır mesajla yazmak için
  <a href="{ic('siparis-hatti/')}">sipariş hattı formunu</a> kullanabilirsiniz.</p>
 </div>
 <div class="kol">{harita()}</div>
</div></section>
""" + cta_bant() + son()


# ------------------------------------------------------------------ ilçe × ürün sayfaları
ISLUG = {i["slug"]: i for i in ILCE}
ANA_CAPA = ["Ankara tel örgü", "Doğanay Tel Örgü", "Gölbaşı tel örgü", "Ankara beton direk ve tel örgü",
            "Ankara jiletli tel ve tel örgü", "Ankara tel örgü sipariş hattı"]

def ilce_yol(i, u): return f'{i["slug"]}-{u["ek"]}/'

def ilce_capa(i, u, n):
    """Aynı hedefe giden linklerde çapa metni dönsün (örümcek ağı, tekrar eden çapa yok)."""
    k = [f'{i["ad"]} {u["ad"].lower()}', f'{i["ad"]} {u["ad"].lower()} fiyatları', f'{i["de"]} {u["ad"].lower()} satan yer',
         f'{i["ad"]} {u["ad"].lower()} satış ve montaj']
    return k[n % len(k)]

def ilce_sayfasi(i, u):
    yol = ilce_yol(i, u)
    k = KSLUG[u["kat"]]
    n = ILCE.index(i) * 3 + URUNLER.index(u)
    t = u["title"][n % len(u["title"])].format(**i)
    d = u["desc"].format(**i)
    h1 = f'Ankara {i["ad"]} {u["ad"]} Fiyatları ve Satan Yerler'
    adim = [("Anasayfa", ""), ("Ankara İlçeleri", "ankara-ilceleri/"), (f'{i["ad"]} {u["ad"]}', yol)]
    ozel = i[u["k"]]                                     # ilçeye + ürüne özel paragraflar (ilceler.py)
    sss = [(q.format(**i), a.format(**i)) for q, a in u["sss"]] + i.get("sss_" + u["k"], [])
    sema = [isletme(), breadcrumb(adim), sss_sema(sss),
            {"@type": "Service", "name": f'{i["ad"]} {u["ad"].lower()} satışı ve montajı', "serviceType": u["ad"],
             "provider": {"@id": SITE + "#isletme"}, "url": SITE + yol,
             "areaServed": {"@type": "AdministrativeArea", "name": f'{i["ad"]}, Ankara'}}]
    gorsel = u["gorsel"][ILCE.index(i) % len(u["gorsel"])]
    # aynı ilçedeki diğer ürünler + komşu ilçelerde aynı ürün + kategori kümesi + anasayfa
    diger = "".join(f'<li><a href="{ic(ilce_yol(i, x))}">{e(ilce_capa(i, x, n + j))}</a></li>'
                    for j, x in enumerate(URUNLER) if x is not u)
    komsu = "".join(f'<li><a href="{ic(ilce_yol(ISLUG[s_], u))}">{e(ilce_capa(ISLUG[s_], u, n + j + 1))}</a></li>'
                    for j, s_ in enumerate(i["komsu"]))
    kume = (f'<li><a href="{ic(k["slug"] + "/")}">{e(k["baslik"])}</a></li>'
            f'<li><a href="{ic(k["slug"] + "-fiyatlari/")}">{e(k["baslik"])} fiyatları {FIYAT_TARIH[-4:]}</a></li>'
            f'<li><a href="{ic(k["slug"] + "-cesitleri/")}">{e(k["baslik"])} çeşitleri</a></li>')
    ana = f'<a href="{ic("")}">{ANA_CAPA[n % len(ANA_CAPA)]}</a>'
    mah = i["mahalleler"]
    mh = "".join(f"<li>{e(m)}</li>" for m in mah)
    veri = "".join(f"<li><b>{e(a)}:</b> {b}</li>" for a, b in i["veri"])
    kay = " · ".join(f'<a href="{url}" target="_blank" rel="noopener nofollow">{e(ad)}</a>' for ad, url in i["kaynak"])
    fiyat = ozet_kart(k["fiyat"]["ozet"], f'{i["ad"]} {u["ad"].lower()} fiyatları')
    sira = u["bolum_sira"][ILCE.index(i) % len(u["bolum_sira"])]     # bölüm sırası ilçeden ilçeye değişir
    bol = {
     "satan": f"""<section class="yazi-bol" id="satan-yer"><h2>{e(i["de"])} {e(u["ad"].lower())} satan yer</h2>
  {baglar(ozel["satan"])}
  <p>Atölyemiz Gölbaşı Gaziosmanpaşa'da; {e(i["ad"])} merkezine karayoluyla yaklaşık <strong>{i["km"]}</strong>. Siparişi
  {ana} sipariş hattından alıyor, malzemeyi kendi aracımızla getiriyoruz.</p></section>""",
     "arazi": f"""<section class="yazi-bol" id="uygulama"><h2>{e(i["ad"])} arazisine göre {e(u["ad"].lower())} seçimi</h2>
  {baglar(ozel["uygulama"])}</section>""",
     "fiyat": f"""<section class="yazi-bol" id="fiyat"><h2>{e(i["ad"])} {e(u["ad"].lower())} fiyatları ({FIYAT_TARIH})</h2>
  {baglar(ozel["fiyat"])}
  <p>Kaynaklı tam tablo ve yurtdışı karşılaştırması: <a href="{ic(k['slug'] + '-fiyatlari/')}">{e(k["baslik"])} fiyatları</a>.</p></section>""",
    }
    govde = "".join(bol[x] for x in sira)
    return bas(yol, t, d, sema, gorsel, onyukle=gorsel, aktif="urun") + sayfa_bas(
        adim, e(h1), baglar(ozel["giris"]), gorsel, f'Merhaba, {i["ad"]} için {u["ad"].lower()} fiyatı almak istiyorum.') + f"""
<div class="sekme-sar"><div class="ic"><nav class="sekme" aria-label="{e(i['ad'])} ürünleri">{"".join(
    f'<a href="{ic(ilce_yol(i, x))}"{" aria-current=" + chr(34) + "page" + chr(34) if x is u else ""}>{ikon(x["ikon"])}<span>{e(i["ad"])} {e(x["ad"])}</span></a>'
    for x in URUNLER)}<a href="{ic('ankara-ilceleri/')}">{ikon("yer")}<span>Diğer ilçeler</span></a></nav></div></div>

<section class="blok"><div class="ic yazi-izgara">
 <article class="yazi">
  {govde}
  <section class="yazi-bol" id="ilce"><h2>{e(i["ad"])} hakkında bilmeniz gerekenler</h2>
   <ul class="ilce-veri">{veri}</ul>
   <p class="kur-not">Kaynaklar: {kay}</p></section>
  {siparis_kutu(k).replace(e(k["baslik"]) + " için net fiyat", e(i["ad"]) + " " + e(u["ad"].lower()) + " için net fiyat")}
 </article>
 <aside class="yan">
  {fiyat}
  <div class="yan-kutu"><p class="yk-bas">{e(i["ad"])} için diğer ürünler</p>
   {"".join(f'<a href="{ic(ilce_yol(i, x))}">{ikon(x["ikon"])} {e(i["ad"])} {e(x["ad"])}</a>' for x in URUNLER if x is not u)}
   <a href="{ic(k['slug'] + '/')}">{ikon(u["ikon"])} {e(k["baslik"])}</a>
   <a href="{ic('siparis-hatti/')}">{ikon("sepet")} Sipariş hattı</a></div>
 </aside>
</div></section>

<section class="blok acik" id="mahalleler"><div class="ic">
 <h2>{e(i["ad"])} mahallelerine {e(u["ad"].lower())} sevkiyatı</h2>
 <p class="bolum-giris">{e(i["ad"])} ilçesinde aşağıdaki mahallelerin hepsine malzeme getiriyor, istenirse montajını yapıyoruz.</p>
 <ul class="mahalle">{mh}</ul>
</div></section>

<section class="blok" id="sss"><div class="ic iki">
 <div class="kol"><h2>{e(i["ad"])} {e(u["ad"].lower())} hakkında sık sorulanlar</h2>{sss_html(sss)}</div>
 <div class="kol">
  <h2>Yakın ilçelerde {e(u["ad"].lower())}</h2><ul class="link-bulut">{komsu}</ul>
  <h3 class="ag-bas">{e(i["ad"])} için diğer ürünler</h3><ul class="link-bulut">{diger}</ul>
  <h3 class="ag-bas">{e(u["ad"])} rehberi</h3><ul class="link-bulut">{kume}</ul>
 </div>
</div></section>
""" + cta_bant(f'{e(i["ad"])} {e(u["ad"].lower())} siparişi için arayın',
               f'{e(i["ad"])} adresinizi, metrajı ya da adedi söyleyin; Gölbaşı\'ndan sevkiyat gününü ve net fiyatı hemen verelim.') + son()


def ilceler_sayfasi():
    yol = "ankara-ilceleri/"
    t = "Ankara İlçelerinde Beton Direk, Jiletli Tel ve Tel Örgü"
    d = ("Ankara'nın 20 ilçesinde beton direk, jiletli tel ve tel örgü fiyatları ve satan yer: ilçeye özel mesafe, arazi ve "
         f"uygulama notları. Sipariş hattı {TEL_G}")
    adim = [("Anasayfa", ""), ("Ankara İlçeleri", yol)]
    sema = [isletme(), breadcrumb(adim)]
    sat = "".join(
        f'<tr><th scope="row">{e(i["ad"])}</th><td>{i["km"]}</td>'
        + "".join(f'<td><a href="{ic(ilce_yol(i, u))}">{e(i["ad"])} {e(u["ad"].lower())}</a></td>' for u in URUNLER) + "</tr>"
        for i in ILCE)
    return bas(yol, t, d, sema) + f"""
<section class="sayfa-bas sade"><div class="desen" aria-hidden="true"></div><div class="ic">
 {iz(adim)}
 <h1>Ankara İlçelerinde Beton Direk, Jiletli Tel ve Tel Örgü</h1>
 <p class="giris">Gölbaşı'ndaki atölyemizden Ankara'nın 20 ilçesine beton direk, jiletli tel ve tel örgü getiriyor, montajını
 yapıyoruz. İlçenizi ve ürünü seçin; o ilçenin arazisine, sanayisine ve iklimine göre hazırladığımız sayfaya gidin.</p>
</div></section>

<section class="blok"><div class="ic">
 <div class="tablo-sar"><table class="kars-tbl ilce-tbl"><thead><tr><th scope="col">İlçe</th><th scope="col">Gölbaşı'ndan</th>
 {"".join(f'<th scope="col">{e(u["ad"])}</th>' for u in URUNLER)}</tr></thead><tbody>{sat}</tbody></table></div>
 <p class="kur-not">Mesafeler ilçe merkezleri arasındaki yaklaşık karayolu mesafesidir. Kızılcahamam, Çamlıdere, Elmadağ, Çubuk ve
 Beypazarı için sipariş hattımızı arayın.</p>
</div></section>

<section class="blok acik"><div class="ic">
 <h2>Ürünlerimiz</h2>
 {kategori_kartlari()}
</div></section>
""" + cta_bant() + son()


def sayfa_404():
    global ONEK
    ONEK = "/"
    s = bas("404", f"Sayfa bulunamadı | {AD}", "Aradığınız sayfa bulunamadı.", [isletme()]).replace(
        f'<link rel="canonical" href="{SITE}404">', '<meta name="robots" content="noindex">')
    s += f"""<section class="sayfa-bas sade"><div class="desen" aria-hidden="true"></div><div class="ic"><h1>Sayfa bulunamadı</h1>
<p class="giris">Aradığınız sayfa taşınmış ya da hiç olmamış olabilir.</p>
<div class="dugmeler"><a class="btn btn-tur" href="/">Anasayfaya dönün</a></div></div></section>
<section class="blok"><div class="ic">{kategori_kartlari()}</div></section>""" + son()
    return s

# ------------------------------------------------------------------ denetim + yazım
def denetle(sayfalar):
    h, tt, dd = [], {}, {}
    for yol, s in sayfalar.items():
        t = re.search(r"<title>(.*?)</title>", s).group(1); d = re.search(r'name="description" content="(.*?)"', s).group(1)
        if yol != "404.html":
            if t in tt: h.append(f"tekrar title: {yol} = {tt[t]}")
            if d in dd: h.append(f"tekrar description: {yol} = {dd[d]}")
            tt[t] = yol; dd[d] = yol
            if len(html.unescape(t)) > 65: h.append(f"title uzun ({len(html.unescape(t))}): {yol}")
            if len(html.unescape(d)) > 165: h.append(f"description uzun ({len(html.unescape(d))}): {yol}")
        if s.count("<h1") != 1: h.append(f"h1 sayısı {s.count('<h1')}: {yol}")
        if "[[" in s: h.append(f"çözülmemiş link işareti: {yol}")
        metin = tr_lower(html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r'<ul class="mahalle">.*?</ul>', "", s, flags=re.S))))  # mahalle adları (Bademlidere…) yanlış alarm
        h += [f"yasak '{y}': {yol}" for y in YASAK if y in metin]
        kimlik = set(re.findall(r'id="([^"]+)"', s))
        for href in re.findall(r'(?:href|src)="([^"]+)"', s):
            if href.startswith("#") and href[1:] not in kimlik and href != "#": h.append(f"kırık çapa {href} ({yol})")
            href = re.split(r"[?#]", href)[0]
            if yol == "404.html" or href.startswith("/") or ":" in href or not href: continue
            hedef = os.path.normpath(os.path.join(os.path.dirname(yol) or ".", href))
            ok = (hedef in {os.path.normpath(p) for p in sayfalar} or
                  os.path.normpath(os.path.join(hedef, "index.html")) in {os.path.normpath(p) for p in sayfalar} or
                  os.path.exists(os.path.join(KOK, hedef)) or hedef.startswith("assets"))
            if not ok: h.append(f"kırık iç link {href} ({yol})")
    return h

def sema_ekle(s, yol):
    """WebPage + birincil görsel şemasını @graph'a ekler."""
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s)
    g = json.loads(m.group(1)); og = re.search(r'property="og:image" content="([^"]+)"', s).group(1)
    g["@graph"].append({"@type": "WebPage", "@id": SITE + yol + "#sayfa", "url": SITE + yol, "inLanguage": "tr",
        "name": html.unescape(re.search(r"<title>(.*?)</title>", s).group(1)),
        "description": html.unescape(re.search(r'name="description" content="(.*?)"', s).group(1)),
        "isPartOf": {"@id": SITE + "#site"}, "about": {"@id": SITE + "#isletme"}, "datePublished": BUGUN, "dateModified": BUGUN,
        "primaryImageOfPage": {"@type": "ImageObject", "url": og}})
    if not any(x.get("@type") == "WebSite" for x in g["@graph"]):
        g["@graph"].append({"@type": "WebSite", "@id": SITE + "#site", "url": SITE, "name": AD, "inLanguage": "tr"})
    return s[:m.start(1)] + json.dumps(g, ensure_ascii=False) + s[m.end(1):]

ESKI = ["panel-cit", "jiletli-tel", "dikenli-tel", "tel-orgu-kapi", "arsa-tarla-cevirme", "spor-sahasi-teli"]

def main():
    global ONEK
    gorselleri_hazirla()
    if not os.path.exists(os.path.join(KOK, "images/logo-amblem.png")):
        import logo; logo.main()
    S = {}
    def yaz(yol, fn, *a):
        global ONEK
        ONEK = "../" * yol.count("/") if yol else ""
        S[(yol + "index.html") if yol else "index.html"] = sema_ekle(fn(*a), yol)
    yaz("", anasayfa)
    for k in KATEGORILER:
        yaz(k["slug"] + "/", kategori_sayfasi, k)
        yaz(k["slug"] + "-fiyatlari/", fiyat_sayfasi, k)
        yaz(k["slug"] + "-cesitleri/", cesit_sayfasi, k)
    for i in ILCE:
        for u in URUNLER: yaz(ilce_yol(i, u), ilce_sayfasi, i, u)
    yaz("ankara-ilceleri/", ilceler_sayfasi)
    yaz("siparis-hatti/", siparis_hatti); yaz("hakkimizda/", hakkimizda); yaz("iletisim/", iletisim)
    S["404.html"] = sayfa_404()
    hata = denetle(S)
    if hata: print("\n".join(hata)); sys.exit(1)
    for d in ESKI:                                  # yayından önce kaldırılan eski hizmet klasörleri
        p = os.path.join(KOK, d)
        if os.path.isdir(p) and not any(d + "/" == y[:len(d) + 1] for y in S): shutil.rmtree(p)
    for yol, s in S.items():
        p = os.path.join(KOK, yol); os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w", encoding="utf-8").write(s)
    os.makedirs(os.path.join(KOK, "assets"), exist_ok=True)
    for f in ("site.css", "site.js"): shutil.copy(os.path.join(KOK, "_src", f), os.path.join(KOK, "assets", f))
    def gorsel_xml(y):
        adlar = list(dict.fromkeys(re.findall(r'images/[gk]/([a-z0-9-]+)\.webp', S[y])))
        return "".join(f"<image:image><image:loc>{SITE}images/g/{a}.webp</image:loc></image:image>" for a in adlar)
    url = [y for y in S if y != "404.html"]
    open(os.path.join(KOK, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' +
        "".join(f"<url><loc>{SITE}{y.replace('index.html', '')}</loc><lastmod>{BUGUN}</lastmod>{gorsel_xml(y)}</url>\n"
                for y in url) + "</urlset>\n")
    open(os.path.join(KOK, "robots.txt"), "w").write(f"User-agent: *\nDisallow: /_src/\nDisallow: /img/\n\nSitemap: {SITE}sitemap.xml\n")
    print(f"tamam: {len(S)} sayfa, sitemap {len(url)} URL")

if __name__ == "__main__":
    main()
