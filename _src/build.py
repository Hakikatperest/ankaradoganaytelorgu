#!/usr/bin/env python3
"""Doğanay Tel Örgü — ankaradoganaytelorgu.com statik site üreticisi.

Çalıştır:  python3 _src/build.py   (herhangi bir dizinden)
Girdi:     _src/data.py (hizmetler, SSS, görseller), img/stok/*.jpg (Unsplash, temsili), images/*.webp (kullanıcı)
Çıktı:     index.html, /<hizmet>/ × 7, /hakkimizda/, /iletisim/, 404.html, sitemap.xml, robots.txt, assets/, images/g + images/k türevleri
Denetim:   yasak ifade, kırık iç link, tekrar eden title/description, uzunluk → HATA, dosya yazılmaz.
İç yollar sayfa derinliğine göre GÖRELİ (Pages alt yol önizlemesi kırılmasın); canonical/sitemap mutlak.
⛔ HTML'i elle düzenleme — buradan üret.
"""
import html, json, os, re, sys, shutil

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(KOK, "_src"))
from data import GORSEL, GERCEK, AFIS, HIZMETLER, ILCELER, SUREC, GENEL_SSS

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
SURUM = "1"
YASAK = ["en ucuz", "garanti", "1 numara", "bir numaralı", "%100", "lider", "7/24", "yılı aşkın", "yıllık tecrübe",
         "en iyi", "sigortalı", "kendi üretimimiz", "fabrikamız"]

e = html.escape
ONEK = ""
def ic(y): return (ONEK + y) if y else (ONEK or "./")
def tr_lower(s): return s.replace("I", "ı").replace("İ", "i").lower()

HSLUG = {h["slug"]: h for h in HIZMETLER}

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
        hedef = {"g": (1600, 82), "k": (640, 74)}
        for d, (w, q) in hedef.items():
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

# ------------------------------------------------------------------ ikonlar (çizgi, currentColor)
IKON = {
 "orgu": '<path d="M3 3l18 18M3 9l12 12M3 15l6 6M9 3l12 12M15 3l6 6M21 3L3 21M21 9L9 21M21 15l-6 6M15 3L3 15M9 3L3 9"/>',
 "panel": '<path d="M3 4v17M21 4v17M3 7h18M3 18h18M7.5 7v11M12 7v11M16.5 7v11"/>',
 "jilet": '<circle cx="7" cy="12" r="4"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="12" r="4"/><path d="M2 12h20"/>',
 "diken": '<path d="M2 9h20M2 15h20M7 7l2 4M9 7l-2 4M15 13l2 4M17 13l-2 4"/>',
 "kapi": '<path d="M3 21V4M21 21V4M3 5h8.5v15H3M12.5 5H21v15h-8.5M10 12.5h1M13 12.5h1"/>',
 "arsa": '<path d="M3 20l5-9 4 5 3-4 6 8zM3 20h18M17 7a2 2 0 1 0 0-.01"/>',
 "saha": '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M12 5v14M3 9h3v6H3M21 9h-3v6h3"/><circle cx="12" cy="12" r="2.2"/>',
 "tel": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1Z"/>',
 "konum": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
}
def ikon(ad, sinif="ikon"):
    return f'<svg class="{sinif}" viewBox="0 0 24 24" aria-hidden="true">{IKON[ad]}</svg>'
WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.2-.2-.5-.3Z"/></svg>')

def wa(metin="Merhaba, tel örgü için bilgi almak istiyorum."):
    return f"https://wa.me/{WA}?text={e(metin)}"

# ------------------------------------------------------------------ şema
def isletme():
    return {"@type": "HomeAndConstructionBusiness", "@id": SITE + "#isletme", "name": AD, "url": SITE,
            "telephone": TEL, "image": SITE + "images/logo-kare.jpg", "logo": SITE + "images/logo-512.png",
            "address": {"@type": "PostalAddress", "streetAddress": ADRES["sokak"], "postalCode": ADRES["pk"],
                        "addressLocality": ADRES["ilce"], "addressRegion": ADRES["il"], "addressCountry": "TR"},
            "hasMap": HARITA_URL,
            "areaServed": [{"@type": "City", "name": "Ankara"}],
            "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": h["baslik"],
                            "url": SITE + h["slug"] + "/"}} for h in HIZMETLER]}

def breadcrumb(adimlar):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": n + 1, "name": a, "item": SITE + y} for n, (a, y) in enumerate(adimlar)]}

def sss_sema(sss):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": s,
            "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in sss]}

# ------------------------------------------------------------------ iskelet
MENU = [("", "Anasayfa"), ("ankara-tel-orgu/", "Tel Örgü"), ("panel-cit/", "Panel Çit"),
        ("jiletli-tel/", "Jiletli Tel"), ("#hizmetler", "Tüm Hizmetler"), ("hakkimizda/", "Hakkımızda"), ("iletisim/", "İletişim")]

def bas(yol, title, desc, sema, ogimg=None, onyukle=None):
    url = SITE + yol
    og = f"{SITE}images/g/{ogimg}.webp" if ogimg else f"{SITE}images/logo-kare.jpg"
    ow, oh = OLCU[ogimg] if ogimg else (630, 630)
    pre = (f'\n<link rel="preload" as="image" href="{ic(f"images/g/{onyukle}.webp")}" imagesrcset="{ic(f"images/k/{onyukle}.webp")} 640w, '
           f'{ic(f"images/g/{onyukle}.webp")} {OLCU[onyukle][0]}w" imagesizes="100vw" fetchpriority="high">' if onyukle else "")
    ac = ' aria-current="page"'
    menu = "".join(f'<a href="{ic("") + h if h.startswith("#") else ic(h)}"{ac if h == yol else ""}>{a}</a>'
                   for h, a in MENU)
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
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": sema}, ensure_ascii=False)}</script>
</head>
<body>
<div class="ust-serit"><div class="ic">
 <span>{ikon("konum", "ikon-k")} Gölbaşı / Ankara</span>
 <a href="tel:{TEL}">{ikon("tel", "ikon-k")} {TEL_G}</a>
</div></div>
<header class="ust"><div class="ic">
 <a class="logo" href="{ic('')}" aria-label="{AD} anasayfa"><img src="{ic('images/logo-amblem.png')}" width="240" height="178" alt="" decoding="async"><span class="logo-yazi"><b>DOĞANAY</b><small>TEL ÖRGÜ</small></span></a>
 <nav class="menu" id="menu" aria-label="Ana menü">{menu}</nav>
 <a class="btn btn-tur ust-cta" href="tel:{TEL}">Teklif Al</a>
 <button class="menu-btn" type="button" aria-controls="menu" aria-expanded="false" aria-label="Menüyü aç"><span></span></button>
</div></header>
<main>
"""

def cta_bant(baslik="Metrajı söyleyin, keşfe gelelim", alt="Alanın yeri, yaklaşık uzunluğu ve ne için çevirmek istediğinizi anlatın; gerisini birlikte planlayalım."):
    return f"""<section class="cta"><div class="ic">
 <div class="cta-metin"><h2>{baslik}</h2><p>{alt}</p></div>
 <div class="dugmeler"><a class="btn btn-tur" href="tel:{TEL}">{ikon("tel", "ikon-b")} {TEL_G}</a>
 <a class="btn btn-cizgi" href="{wa()}" target="_blank" rel="noopener">{WA_SVG} WhatsApp'tan yaz</a></div>
</div></section>"""

def son():
    hz = "".join(f'<li><a href="{ic(h["slug"] + "/")}">{e(h["baslik"])}</a></li>' for h in HIZMETLER)
    return f"""</main>
<footer class="alt"><div class="ic alt-izgara">
 <div class="alt-kol">
  <img class="alt-logo" src="{ic('images/logo-tam.png')}" width="640" height="550" alt="{AD} logosu" loading="lazy" decoding="async">
 </div>
 <div class="alt-kol"><p class="alt-bas">Hizmetler</p><ul>{hz}</ul></div>
 <div class="alt-kol"><p class="alt-bas">İletişim</p>
  <p><a class="alt-tel" href="tel:{TEL}">{TEL_G}</a></p>
  <p><a href="{wa()}" target="_blank" rel="noopener">WhatsApp'tan yazın</a></p>
  <address>{ADRES_G}</address>
  <p><a href="{HARITA_URL}" target="_blank" rel="noopener">Haritada aç →</a></p>
  <p><a href="{ic('hakkimizda/')}">Hakkımızda</a> · <a href="{ic('iletisim/')}">İletişim</a></p></div>
</div>
<div class="alt-not"><div class="ic"><p>© 2026 {AD} · Ankara tel örgü, panel çit, jiletli ve dikenli tel</p></div></div>
<div class="w4"><div class="w4-bag"><span class="w4-etiket">Web Tasarım:</span> <a class="w4-ad" href="https://www.web4medya.com/" target="_blank" rel="noopener">Web<span class="w4-d">4</span>Medya</a></div></div>
</footer>
<div class="dock" id="dock"><a class="dock-tel" href="tel:{TEL}"><small>Hemen arayın</small><span>{TEL_G}</span></a>
<a class="dock-wa" href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp'tan yaz">{WA_SVG}</a></div>
<script src="{ic('assets/site.js')}?v={SURUM}" defer></script>
</body>
</html>
"""

def iz(adimlar):
    p = [f'<a href="{ic(y)}">{e(a)}</a>' for a, y in adimlar[:-1]] + [f'<span aria-current="page">{e(adimlar[-1][0])}</span>']
    return '<nav class="iz" aria-label="Konum">' + ' <span aria-hidden="true">›</span> '.join(p) + '</nav>'

def sss_html(sss):
    return '<div class="sss">' + "".join(f"<details><summary>{e(s)}</summary><p>{e(c)}</p></details>" for s, c in sss) + "</div>"

def hizmet_kartlari(haric=None):
    li = []
    for h in HIZMETLER:
        if h is haric: continue
        li.append(f'<li class="kart"><a href="{ic(h["slug"] + "/")}"><span class="kart-gorsel">'
                  f'{resim(h["gorsel"], sizes="(max-width: 600px) 100vw, (max-width: 1000px) 50vw, 380px")}</span>'
                  f'<span class="kart-govde"><span class="kart-ikon">{ikon(h["ikon"])}</span><b>{e(h["baslik"])}</b>'
                  f'<span>{e(h["kisa"])}</span><span class="kart-ok">Detaylar →</span></span></a></li>')
    return '<ul class="kartlar">' + "".join(li) + "</ul>"

def surec_html():
    return '<ol class="surec">' + "".join(f"<li><h3>{a}</h3><p>{p}</p></li>" for a, p in SUREC) + "</ol>"

def ilce_html():
    return '<ul class="ilceler">' + "".join(f"<li>{x}</li>" for x in ILCELER) + "</ul>"

def harita(baslik="Doğanay Tel Örgü konumu"):
    return (f'<div class="harita"><iframe src="{HARITA_EMBED}" title="{e(baslik)}" loading="lazy" '
            f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>')

TEMSILI = '<p class="temsili">"Uygulamamızdan" etiketli fotoğraflar kendi işlerimizdir; diğerleri uygulama türünü gösteren temsilî görsellerdir.</p>'

def altyazi(ad):
    return (f'<figcaption>{"<b>Uygulamamızdan:</b> " if ad in GERCEK else ""}{e(GORSEL[ad])}</figcaption>')

def galeri():
    return '<ul class="galeri">' + "".join(
        f'<li><a href="{ic(f"images/g/{a}.webp")}" data-buyut><figure>{resim(a, sizes="(max-width: 600px) 100vw, (max-width: 1000px) 50vw, 380px")}'
        f'{altyazi(a)}</figure></a></li>' for a in GERCEK) + "</ul>"

# ------------------------------------------------------------------ sayfalar
HERO = "beton-direk-ve-tel-orgu"

def anasayfa():
    t = f"Ankara Tel Örgü - {TEL_G} | Doğanay Tel Örgü Gölbaşı"
    d = ("Ankara tel örgü, panel çit, jiletli ve dikenli tel montajı. Gölbaşı'ndaki Doğanay Tel Örgü ile arsa, bahçe, "
         f"site ve saha çevirme. Keşif için: {TEL_G}")
    sss = [
     ("Ankara'da tel örgü yaptırmak için kime ulaşabilirim?",
      f"Doğanay Tel Örgü'ye {TEL_G} numarasından ulaşabilirsiniz. Aynı numaraya WhatsApp'tan da yazabilirsiniz."),
     ("Doğanay Tel Örgü nerede?", f"Adresimiz {ADRES_G}. Haritadaki konumumuzdan yol tarifi alabilirsiniz."),
    ] + GENEL_SSS
    sema = [isletme(), {"@type": "WebSite", "@id": SITE + "#site", "url": SITE, "name": AD, "inLanguage": "tr"}, sss_sema(sss)]
    rozet = "".join(f'<li>{ikon(h["ikon"])}<span>{e(h["ad"])}</span></li>' for h in HIZMETLER[:5])
    return bas("", t, d, sema, AFIS, onyukle=HERO) + f"""
<section class="hero"><div class="hero-fon" aria-hidden="true">{resim(HERO, "kb", "eager", "100vw")}</div>
<div class="desen" aria-hidden="true"></div>
<div class="ic hero-ic">
  <p class="ust-etiket">Gölbaşı · Ankara</p>
  <h1>Ankara Tel Örgü <span>ve Çit Sistemleri</span></h1>
  <p class="giris">Bahçenizi, arsanızı, sitenizi ya da deponuzu çevirmek mi istiyorsunuz? Tel örgü, panel çit, jiletli ve
  dikenli tel, çit kapısı… Ölçüyü yerinde alıyor, direği sağlam dikiyor, teli gergin bağlıyoruz.</p>
  <div class="dugmeler"><a class="btn btn-tur" href="tel:{TEL}">{ikon("tel", "ikon-b")} Teklif Al: {TEL_G}</a>
  <a class="btn btn-cizgi" href="{wa('Merhaba, tel örgü için teklif almak istiyorum.')}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
  <ul class="hero-rozet">{rozet}</ul>
</div></section>

<section class="blok" id="hizmetler"><div class="ic">
 <p class="ust-etiket koyu">Hizmetlerimiz</p>
 <h2>Tel örgüden panel çite, Ankara'da çit işleri</h2>
 <p class="bolum-giris">Her alanın ihtiyacı farklı. Bahçe için başka, fabrika için başka, tarla için başka bir çit doğru olur.
 Hizmete tıklayın; nerede kullanıldığını ve nelere dikkat ettiğimizi anlatıyoruz.</p>
 {hizmet_kartlari()}
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

<section class="blok acik"><div class="ic">
 <p class="ust-etiket koyu">Uygulamalarımızdan</p>
 <h2>Sahada yaptığımız tel örgü işleri</h2>
 <p class="bolum-giris">Beton direkli galvaniz tel örgü, panel çit üstü jiletli tel, tarla ve sanayi parseli çevirme.
 Fotoğrafların hepsi kendi işlerimiz.</p>
 {galeri()}
</div></section>

<section class="blok"><div class="ic">
 <p class="ust-etiket koyu">Nasıl çalışıyoruz?</p>
 <h2>Telefondan teslime 5 adım</h2>
 {surec_html()}
</div></section>

<section class="blok"><div class="ic iki">
 <div class="kol">
  <p class="ust-etiket koyu">Hizmet bölgesi</p>
  <h2>Gölbaşı'ndan Ankara'nın ilçelerine</h2>
  <p>Atölyemiz Gölbaşı Gaziosmanpaşa'da. Gölbaşı ve çevresinin yanında Ankara'nın ilçelerinde de tel örgü ve çit
  işi yapıyoruz. İlçenizi listede göremediyseniz arayıp sorun.</p>
  {ilce_html()}
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
""" + cta_bant("Ankara'da tel örgü mü yaptıracaksınız?") + son()


def hizmet_sayfasi(h):
    yol = h["slug"] + "/"
    adim = [("Anasayfa", ""), (h["baslik"], yol)]
    sema = [isletme(), breadcrumb(adim), sss_sema(h["sss"]),
            {"@type": "Service", "name": h["baslik"], "serviceType": h["ad"], "description": h["kisa"],
             "provider": {"@id": SITE + "#isletme"}, "areaServed": {"@type": "City", "name": "Ankara"}, "url": SITE + yol}]
    giris = "".join(f"<p>{p}</p>" for p in h["giris"])
    sec = "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in h["secenek"])
    dk = "".join(f"<li>{e(x)}</li>" for x in h["dikkat"])
    n = HIZMETLER.index(h)
    ana = ["Ankara tel örgü", "Doğanay Tel Örgü", "Gölbaşı tel örgü"][n % 3]
    return bas(yol, h["title"], h["desc"], sema, h["gorsel"], onyukle=h["gorsel"]) + f"""
<section class="sayfa-bas"><div class="sb-fon" aria-hidden="true">{resim(h["gorsel"], "kb", "eager", "100vw")}</div>
<div class="desen" aria-hidden="true"></div>
<div class="ic">
 {iz(adim)}
 <h1>{e(h["baslik"])}</h1>
 <p class="giris">{e(h["kisa"])}</p>
 <div class="dugmeler"><a class="btn btn-tur" href="tel:{TEL}">{ikon("tel", "ikon-b")} Teklif Al: {TEL_G}</a>
 <a class="btn btn-cizgi" href="{wa(f'Merhaba, {h["ad"].lower()} için teklif almak istiyorum.')}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a></div>
</div></section>

<section class="blok"><div class="ic iki">
 <div class="kol"><h2>{e(h["ad"])} nedir, nerede kullanılır?</h2>{giris}
  <p>Gölbaşı'ndaki <a href="{ic('')}">{ana}</a> ekibi olarak keşfe gelip ölçüyü yerinde alıyoruz.</p></div>
 <div class="kol"><figure class="cerceve">{resim(h["gorsel2"], sizes="(max-width: 760px) 100vw, 560px")}{altyazi(h["gorsel2"])}</figure></div>
</div></section>

<section class="blok acik"><div class="ic">
 <h2>Seçenekler</h2>
 <ul class="secenek">{sec}</ul>
</div></section>

<section class="blok"><div class="ic iki">
 <div class="kol"><h2>Montajda dikkat ettiklerimiz</h2><ul class="tik koyu-tik">{dk}</ul></div>
 <div class="kol"><h2>Nasıl ilerliyoruz?</h2>
  <ol class="kisa-adim">{"".join(f"<li><b>{a}:</b> {p}</li>" for a, p in SUREC[:4])}</ol></div>
</div></section>

<section class="blok acik"><div class="ic iki">
 <div class="kol"><h2>Sık sorulan sorular</h2>{sss_html(h["sss"])}</div>
 <div class="kol"><h2>Hizmet bölgesi</h2>
  <p>Gölbaşı merkezli olarak Ankara'nın ilçelerinde çalışıyoruz.</p>{ilce_html()}</div>
</div></section>

<section class="blok"><div class="ic">
 <h2>Diğer hizmetlerimiz</h2>
 {hizmet_kartlari(h)}
 {TEMSILI}
</div></section>
""" + cta_bant(f"{e(h['ad'])} için keşif isteyin") + son()


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
  olup olmayacağı. Fotoğraf atarsanız keşiften önce fikir verebiliriz.</p>
 </div>
 <div class="kol">{harita()}</div>
</div></section>
""" + cta_bant() + son()


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
  <p>Tel örgü, panel çit, jiletli tel, dikenli tel ve çit kapısı. Kısacası bir alanın sınırını çizmek ve korumak
  için gereken işlerin hepsi. Alanı yerinde görüp ölçüyor, ihtiyaca uygun çiti birlikte seçiyor ve montajını yapıyoruz.</p>
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
 <h2>Hizmetlerimiz</h2>
 {hizmet_kartlari()}
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
<section class="blok"><div class="ic">{hizmet_kartlari()}</div></section>""" + son()
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
        metin = tr_lower(html.unescape(re.sub(r"<[^>]+>", " ", s)))
        h += [f"yasak '{y}': {yol}" for y in YASAK if y in metin]
        for href in re.findall(r'(?:href|src)="([^"]+)"', s):
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
    for h in HIZMETLER: yaz(h["slug"] + "/", hizmet_sayfasi, h)
    yaz("hakkimizda/", hakkimizda); yaz("iletisim/", iletisim)
    S["404.html"] = sayfa_404()
    hata = denetle(S)
    if hata: print("\n".join(hata)); sys.exit(1)
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
