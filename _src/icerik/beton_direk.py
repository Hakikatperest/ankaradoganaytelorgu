from ._ortak import kutu, liste, hesap

K = {
 "slug": "ankara-beton-direk", "ad": "Beton Direk", "baslik": "Ankara Beton Direk", "ikon": "direk",
 "kisa": "Düz, eğik başlı (L), Y kollu ve payanda beton çit direği satışı; istenirse dikimi ve tel örgü montajı.",
 "gorsel": "beton-direk-tel", "gorsel2": "beton-direk",
 "kat": {
  "title": "Ankara Beton Direk Satışı ve Montajı | Doğanay Tel Örgü",
  "desc": "Ankara beton direk: düz, eğik başlı, Y kollu ve payanda beton çit direği satışı, sevkiyatı ve dikimi. Fiyatlar, çeşitler, kullanım alanları ve sipariş.",
  "h1": "Ankara Beton Direk",
  "ust": "Tel örgü çitin iskeleti beton direk. Gölbaşı'ndan Ankara'nın ilçelerine beton çit direği satıyor, getiriyor ve "
         "istenirse dikip tel örgüsünü de çekiyoruz.",
  "govde": [
   ("Beton direk nedir?", """
<p>Beton çit direği; içine çelik donatı (genelde 4 adet 8–10 mm demir) yerleştirilmiş kalıba beton dökülüp titreşimle sıkıştırılarak
üretilen, tel örgü ve dikenli teli taşıyan direktir. Üzerinde gergi teli için delikler bulunur. Dibi tepesinden kalındır; 2 metrelik
düz bir direk yaklaşık 40 kg, 3 metrelik ağır (NATO tipi) direk 115 kg civarındadır.</p>
<p>Avantajı basit: <strong>paslanmaz, boya ve bakım istemez</strong>, geniş arazide metal direkten ekonomik kalır. Dezavantajı da
ağırlığı ve kalın görüntüsü; bahçede daha ince bir görünüm istenirse demir boru direk tercih ediliyor.</p>""", "nedir"),
   ("Beton direk nasıl dikilir?", """
<ol>
<li><strong>Hat ve aralık:</strong> Hat ip ile çekilir; direkler genelde 2,5–3 metre arayla işaretlenir. 100 metrelik hatta yaklaşık
35–40 direk gider.</li>
<li><strong>Çukur:</strong> Kamu şartnamelerinde temel çukuru 50×50×60 cm; direğin 50–60 cm'si toprağa gömülür.</li>
<li><strong>Beton:</strong> Direk şakülüne alınıp dibi betonlanır. Köşe, uç ve uzun hatlarda ara gergi noktalarına payanda konur.</li>
<li><strong>Bekleme:</strong> Beton oturmadan tel gerdirilmez; aceleyle gerilen tel direği yatırır.</li>
</ol>"""
    + kutu("ipucu", "Ankara'da kışın toprak donup kalkıyor; Ankara için tek bir resmi don derinliği yok ama zemin etütlerinde 80–100 cm "
           "civarı görülüyor. Bu yüzden direği \"nasılsa beton\" diye sığ dikmiyoruz; özellikle köşe direklerini derin ve payandalı kuruyoruz.."),
    "nasil-dikilir"),
   ("Direk boyu nasıl seçilir?", """
<p>Basit kural: <strong>2 metrelik direkle 1,5 metre tel, 2,5 metrelik direkle 2 metre tel</strong> çekilir; aradaki fark toprağa
gömülen kısımdır. Üstüne [[ankara-dikenli-tel|dikenli tel]] ya da [[ankara-jiletli-tel|jiletli tel]] eklenecekse eğik başlı ya da
Y kollu direk seçilir. Çeşitlerin hepsini [[ankara-beton-direk-cesitleri|beton direk çeşitleri]] sayfasında anlattık.</p>""", "boy"),
   ("Fiyatı ne kadar?", "<p>Ekim 2026 piyasasında 2 metrelik düz beton direk yaklaşık 132–265 TL, 3 metrelik direk 240–350 TL, ağır NATO tipi "
    "350–600 TL/adet. Ayrıntılı tablo ve İngiltere/Almanya karşılaştırması [[ankara-beton-direk-fiyatlari|beton direk fiyatları]] sayfasında.</p>",
    "fiyat"),
  ],
  "kullanim_giris": "Beton direk nerede kullanılır? Tel örgü, dikenli tel ve jiletli tel taşıyan her çitte; özellikle geniş arazide.",
  "kullanim": [
   ("Arsa ve tarla çevirme", "Galvaniz tel örgü ya da dikenli tel için en ekonomik direk. Bkz. [[ankara-arsa-tarla-cevirme|arsa ve tarla çevirme]]."),
   ("Fabrika ve depo", "Eğik başlı ya da Y kollu direk, üstte jiletli tel."),
   ("Bağ, bahçe, hobi bahçesi", "2–2,4 m düz direk ve [[ankara-tel-orgu|tel örgü]]."),
   ("Şantiye ve inşaat sahası", "Hızlı kurulan, sökülüp taşınabilen çevirme."),
   ("Hayvancılık, ağıl", "Sık direk ve payandalı köşelerle dayanıklı çit."),
   ("Kamu ve altyapı alanları", "Trafo, depo, su deposu gibi tesislerde şartnameye uygun direk."),
  ],
  "siparis": [
   "<strong>Adet ve boy:</strong> Kaç direk, kaç metrelik (2 / 2,4 / 2,5 / 3 m)?",
   "<strong>Tip:</strong> Düz, eğik başlı, Y kollu, payanda (köşe sayısı kadar).",
   "<strong>Teslim yeri:</strong> İlçe ve araç yanaşabiliyor mu?",
   "<strong>Montaj:</strong> Sadece direk mi, dikim ve tel örgü de mi?",
  ],
  "sss": [
   ("Beton direk kaç kilo?", "2 metrelik düz direk yaklaşık 40 kg, 2,5 metrelik eğik başlı direk 49 kg, 3 metrelik ağır direk 115 kg civarında."),
   ("Beton direk kaç metre arayla dikilir?", "Genellikle 2,5–3 metre. Kamu şartnamelerinde 2,5 metre esas alınıyor."),
   ("Beton direk ne kadar gömülür?", "Genelde 50–60 cm; köşe ve payanda direklerinde temel daha geniş tutulur."),
   ("Sadece beton direk satıyor musunuz?", "Evet; yalnız direk de satıyoruz, dikim ve tel örgü montajını da yapıyoruz."),
  ],
 },
 "fiyat": {
  "title": "Ankara Beton Direk Fiyatları 2026 - Adet Fiyatı",
  "desc": "Ankara beton direk fiyatları Ekim 2026: 2-3 m düz, eğik başlı, payanda ve NATO tipi beton çit direği adet fiyatı; İngiltere ve Almanya karşılaştırması.",
  "h1": "Ankara Beton Direk Fiyatları (Ekim 2026)",
  "ust": "2 metrelik düz direkten 3 metrelik ağır direğe, payandadan eğik başlıya; beton çit direği fiyatlarını kaynaklarıyla topladık.",
  "ozet": [
   ("2 m düz beton direk", "132–265 TL/adet"),
   ("2,2–2,5 m direk", "143–320 TL/adet"),
   ("2,7–3 m direk", "240–350 TL/adet"),
   ("Payanda", "217–270 TL/adet"),
   ("Ağır (NATO tipi) 3 m", "350–600 TL/adet"),
  ],
  "giris": [(None, "<p>Beton direk fiyatını en çok <strong>boy ve tip</strong> belirliyor. Aynı boyda bile satıcıdan satıcıya iki katına varan fark "
             "var; çünkü kesit, donatı ve beton kalitesi farklı. Rakamlar Ekim 2026 piyasa verisidir, teklifimiz değildir.</p>"
             + kutu("onemli", "Fiyat sorarken direğin ağırlığını ve içindeki demiri de sorun. Hafif ve ince direk ucuzdur ama Ankara kışında "
                    "köşede çatlayan da genelde odur."))],
  "tr_giris": "<p>Türkiye piyasasında beton çit direği fiyatları (adet):</p>",
  "tr": [
   ("Düz beton direk", "200 cm", "132 TL + KDV", "Ankara imalatçı listesi, 2026", ""),
   ("Eğik başlı beton direk", "240 cm / 290 cm", "143 / 253 TL + KDV", "Ankara imalatçı listesi, 2026", ""),
   ("Düz beton direk", "200 / 240 cm", "165 / 190 TL", "Ankara satıcı listesi, Eki 2026", ""),
   ("Düz beton çit direği", "200 / 240 / 300 cm", "245–265 / 250–275 / 325–350 TL", "Keklik Panel Çit, 2026", "https://keklikpanelcit.com/urun/beton-cit-diregi/"),
   ("Eğik başlı beton direk", "240 / 300 cm", "275–300 / 320–350 TL", "Keklik Panel Çit, 2026", "https://keklikpanelcit.com/urun/beton-cit-diregi/"),
   ("Payanda", "200 / 270 cm", "217–240 / 250–270 TL", "Keklik Panel Çit, 2026", "https://keklikpanelcit.com/urun/beton-cit-diregi/"),
   ("Ara direk, temin + montaj", "—", "350 TL'den", "Gaziantep uygulayıcı, 2026", "https://www.gazianteptelcit.com/blog/beton-cit-diregi-fiyatlari-cesitleri-2026"),
   ("Köşe direği (payandalı), temin + montaj", "—", "450 TL'den", "Gaziantep uygulayıcı, 2026", "https://www.gazianteptelcit.com/blog/beton-cit-diregi-fiyatlari-cesitleri-2026"),
   ("Beton çit direğinin yerleştirilmesi", "kamu pozu KGM/51.104/B", "568,99 TL/adet", "KGM birim fiyatı, Ara 2025", "https://herpoz.com/detay/kgm-51-104-b-beton-cit-direginin-yerlestirilmesi"),
  ],
  "tr_son": kutu("not", "Beton direğin iki ana girdisi demir ve çimento. Ekim 2026'da inşaat demiri İstanbul'da 38.500–40.500 TL/ton, 50 kg torba "
                 "çimento 450–650 TL bandında; çimentoda son 6 ayda %19'u aşan artış görüldü. Yılın başında verilen direk fiyatları bu yüzden "
                 "güncelleniyor; teklifin geçerlilik süresini sorun."),
  "yd_giris": "<p>İngiltere ve Almanya'da beton çit direği yapı marketlerinde tek tek satılıyor:</p>",
  "yd": [
   ("İngiltere", "FP McCann yarıklı beton direk", "100×100×2440 mm", 30.67, "GBP", "adet, KDV dahil", "Jewson", "https://jewson.co.uk/p/fp-mccann-slotted-post-2440mm-grey-LSFPMSP8"),
   ("İngiltere", "Supreme ara direk", "2440×109×94 mm", 38.88, "GBP", "adet", "Travis Perkins", "https://www.travisperkins.co.uk/2440mm-x-109mm-x-94mm-supreme-concrete-intermediate-slotted-fence-post/p/700243"),
   ("İngiltere", "Forest Garden yarıklı direk", "2,44 m × 104 mm", 27, "GBP", "adet", "B&Q", "https://www.diy.com/departments/forest-garden-grey-slotted-rectangular-concrete-fence-post-h-2-44m-w-104mm/5013053204757_BQ.prd"),
   ("Almanya", "Betonpfosten (beton direk)", "10×10×280 cm", 33.95, "EUR", "adet", "zaunonline.de", "https://www.zaunonline.de/zaunpfosten/beton"),
   ("Almanya", "Eckpfosten (köşe direği)", "10×10×280 cm", 38.95, "EUR", "adet", "zaunonline.de", "https://www.zaunonline.de/zaunpfosten/beton"),
   ("ABD", "Galvaniz chain-link ara direk (beton yerine)", "1-7/8\" × 8 ft", 18.52, "USD", "adet", "Home Depot", "https://www.homedepot.com/p/Everbilt-1-7-8-in-Dia-x-8-ft-16-Gauge-Galvanized-Steel-Chain-Link-Fence-Line-Post-328934DPTSEB/312373073"),
  ],
  "yd_yorum": "<p>İngiltere'de 2,4 metrelik beton direk <strong>1.800–2.600 TL</strong>, Almanya'da 2,8 metrelik direk yaklaşık <strong>1.900 TL</strong>. "
   "Türkiye'de aynı boydaki direk 250–350 TL. Yani beton direk Avrupa'da Türkiye'nin 6–8 katı. ABD'de beton direk yaygın değil; "
   "tel örgü çitlerde galvaniz boru direk kullanılıyor.</p>",
  "govde": [
   ("Beton direk fiyatını ne değiştirir?", liste(
     "<strong>Boy:</strong> 1,5 m'den 3 m'ye fiyat 3 katına çıkabiliyor.",
     "<strong>Tip:</strong> Düz < eğik başlı < Y kollu / NATO tipi.",
     "<strong>Kesit ve donatı:</strong> 8×8 ile 10×13 cm arası kesit; içindeki demir sayısı ve çapı.",
     "<strong>Adet:</strong> Kamyon bazlı alımda adet fiyatı düşer.",
     "<strong>Nakliye:</strong> Direk ağırdır (40–120 kg); uzak ve yolu zor arazide taşıma ayrı kalem.",
     "<strong>Montaj:</strong> Çukur, beton ve payanda işçiliği."), "etkenler"),
   ("Beton direk mi, demir boru direk mi?", "<p>Ekim 2026'da 2 metrelik galvaniz boru direk 130–200 TL, 2,4 metrelik eğri boru direk 180–380 TL "
    "bandında; yani fiyat olarak beton direğe yakın. Fark kullanımda: beton direk paslanmaz ve bakım istemez, geniş arazide sağlamdır; "
    "boru direk daha ince ve şıktır, bahçe ve sitede tercih edilir.</p>"
    + kutu("tavsiye", "Arazi, tarla ve fabrika için beton; villa bahçesi ve site için boru direk. İkisini aynı çitte birleştirmek de mümkün :)"),
    "beton-mu-boru-mu"),
   ("Örnek hesap: 100 metre arsa çiti", hesap("100 m · 2,4 m düz beton direk · 4 köşe", [
        ("Ara direk: 36 adet × 190–275 TL", "≈ 6.800–9.900 TL"),
        ("Köşe direği + payanda: 4 köşe × 2 payanda", "≈ 2.800–4.000 TL"),
        ("Çukur, beton ve dikim", "zemine göre"),
       ], "Direk malzemesi ≈ 9.600–13.900 TL"), "ornek"),
  ],
  "sss": [
   ("Beton direk fiyatları ne kadar?", "Ekim 2026'da 2 m düz beton direk yaklaşık 132–265 TL, 2,7–3 m direk 240–350 TL, ağır NATO tipi 350–600 TL/adet."),
   ("Payanda fiyatı ne kadar?", "200–270 cm payanda yaklaşık 217–270 TL/adet."),
   ("Beton direk mi daha ucuz, boru direk mi?", "2 metrelik boyda fiyatlar birbirine yakın; beton direk bakım istemediği için geniş arazide uzun vadede daha ekonomik kalıyor."),
  ],
 },
 "cesit": {
  "title": "Ankara Beton Direk Çeşitleri: Düz, Eğik, Y Kollu, Payanda",
  "desc": "Beton direk çeşitleri: düz, eğik başlı (L), Y kollu, NATO tipi ağır direk, payanda ve köşe direği; boyları, ağırlıkları ve kullanım yerleri.",
  "h1": "Ankara Beton Direk Çeşitleri",
  "gorsel": "beton-direk6",
  "ust": "Düz mü, eğik başlı mı, Y kollu mu? Hangi boy, hangi köşe direği? Beton direk çeşitlerini ve nerede kullanıldığını anlattık.",
  "giris": [(None, "<p>Beton direkler başlık şekline, boyuna ve görevine (ara, köşe, payanda) göre ayrılır.</p>")],
  "cesitler": [
   ("duz", "Düz beton direk", "<p>En yaygın tip; tepesi düz. Tel örgü ve gergi telini taşır. 1,5–3 m boylarında, 2 metrelik direk yaklaşık 40 kg.</p>",
    ["Ara direk", "Ekonomik"]),
   ("egik", "Eğik başlı (L) beton direk", "<p>Tepesi dışa doğru eğik; eğik kısma 2–3 sıra [[ankara-dikenli-tel|dikenli tel]] çekilir. Arsa ve fabrika "
    "çevresinde standart.</p>", ["Dikenli tel", "240–300 cm"]),
   ("y-kollu", "Y kollu beton direk", "<p>Tepesi iki yana açılır; ortasına [[ankara-jiletli-tel|helezon jiletli tel]] yerleştirilir, kollara dikenli tel "
    "çekilir. Yüksek güvenlik isteyen alanlar için.</p>", ["Jiletli tel", "Güvenlik"]),
   ("nato", "NATO tipi ağır direk", "<p>3–3,4 m boyunda, dibi 14×20 cm'ye varan kalın kesitli ağır direk (115–135 kg). Askeri ve kamu tesislerinde, "
    "yüksek çitlerde kullanılır.</p>", ["3–3,4 m", "Ağır"]),
   ("payanda", "Payanda ve köşe direği", "<p>Payanda, köşe ve uç direklerini çapraz destekleyen yardımcı direktir. Tel gerildiğinde yükün çoğunu "
    "köşe direkleri taşır; payandasız köşe zamanla içe yatar. Kamu şartnamelerinde her 30 metrede çift payanda isteniyor.</p>",
    ["Köşe", "Gergi noktası"]),
  ],
  "tablo": [
   ["Çeşit", "Boy", "Yaklaşık ağırlık", "Nereye uygun"],
   ["Düz", "1,5–3 m", "≈ 40 kg (2 m)", "Bahçe, tarla, arsa"],
   ["Eğik başlı (L)", "2,4–3 m", "≈ 42–49 kg", "Arsa, depo"],
   ["Y kollu", "2,5–3 m", "—", "Fabrika, güvenlik"],
   ["NATO tipi", "3–3,4 m", "≈ 115–135 kg", "Kamu, askeri"],
   ["Payanda", "2–2,8 m", "—", "Köşe ve uç"],
  ],
  "govde": [
   ("Hangi beton direği seçmeliyim?", "<p>Bahçe ve tarla için 2–2,4 m düz direk; üstüne dikenli tel isteniyorsa eğik başlı; fabrika ve depo için Y kollu. "
    "Her köşeye ve her uca payanda. Tel yüksekliğinin üstüne yaklaşık 50 cm gömme payı ekleyerek boyu seçin.</p>"
    + kutu("tavsiye", "Köşe direklerinde tasarruf etmeyin :) Çitin bütün gerilimi oraya biniyor; köşe direği yatarsa hat boyunca tel gevşer."),
    "secim"),
  ],
  "sss": [
   ("Beton direk çeşitleri nelerdir?", "Düz, eğik başlı (L), Y kollu, NATO tipi ağır direk ve payanda/köşe direği."),
   ("Eğik başlı direk ne işe yarar?", "Eğik kısmına 2–3 sıra dikenli tel çekilir; çitin üstünden geçişi zorlaştırır."),
   ("Y kollu direğe jiletli tel takılır mı?", "Evet; Y'nin ortasına helezon jiletli tel, kollara dikenli tel yerleştirilir."),
  ],
 },
}
