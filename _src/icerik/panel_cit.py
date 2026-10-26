from ._ortak import kutu, liste, hesap

K = {
 "slug": "ankara-orgu-panel-cit", "ad": "Örgü Panel Çit", "baslik": "Ankara Örgü Panel Çit", "ikon": "panel",
 "kisa": "Kaynaklı, V katlamalı, boyalı hazır panellerle düzgün ve rijit çit; site, fabrika, okul ve müstakil ev için.",
 "gorsel": "tel-orgu-sistemi", "gorsel2": "panelcit",
 "kat": {
  "title": "Ankara Örgü Panel Çit - Panel Çit Montajı | Doğanay Tel Örgü",
  "desc": "Ankara örgü panel çit ve panel çit montajı: 2D/3D kaynaklı panel, yeşil ve antrasit, direk ve kelepçe. Fiyat, çeşit, kullanım ve sipariş.",
  "h1": "Ankara Örgü Panel Çit",
  "ust": "Uzun hatta bile cetvelle çizilmiş gibi duran, rijit ve şık bir çit istiyorsanız panel çit tam size göre. "
         "Ankara'da site, fabrika, okul ve müstakil ev çevresine panel çit kuruyoruz.",
  "govde": [
   ("Örgü panel çit nedir?", """
<p>Piyasada "örgü panel çit", "tel örgü panel çit" ya da kısaca "panel çit" diye anılan ürün aynı: Galvaniz telin kare ya da
dikdörtgen gözler oluşturacak şekilde <strong>kaynaklanmasıyla</strong> üretilen hazır panel. Panellerde çoğunlukla V şeklinde
katlamalar (3D) bulunur, yüzeyi elektrostatik toz boyayla kaplanır. Sahada direklere kelepçeyle bağlanır.</p>
<p>Yaygın ölçüler 250 cm genişlik, 100–200 cm yükseklik; tel kalınlığı 4–6 mm, göz 50×150 mm civarı. Renkte en çok
<strong>RAL 6005 yeşil</strong> ve <strong>RAL 7016 antrasit</strong> kullanılıyor.</p>"""
    + kutu("not", "Adı \"örgü\" olsa da panel çitin teli örülmez, kaynaklanır. Örgü tel istiyorsanız [[ankara-tel-orgu|tel örgü]] "
           "sayfasına bakın; ikisinin farkını aşağıda anlattık :)"), "nedir"),
   ("Panel çit mi, tel örgü mü?", """
<p>İkisi de iyi; ama farklı işler için:</p>"""
    + liste("<strong>Panel çit:</strong> Rijit, düz, şık; uzun hatta dalgalanmaz. Montajı hızlıdır. Fiyatı tel örgüden yüksektir.",
            "<strong>Tel örgü:</strong> Ekonomik, engebeli araziye kolay uyar. Doğru gerdirilmezse zamanla sarkabilir.")
    + "<p>Görünür cepheler, siteler ve okullar için panel; tarla ve büyük arazi için tel örgü öneriyoruz. Çoğu zaman ikisini "
      "birlikte kullanıyoruz: yol cephesi panel, arka taraf tel örgü.</p>", "panel-mi-orgu-mu"),
   ("Panel çit nasıl kurulur?", """
<ol>
<li>Hat ip ile çekilir; panel genişliğine göre (250 cm) direk yerleri işaretlenir.</li>
<li>Direkler (genelde 50×50 ya da 60×40 kutu profil) betonlanır ya da beton zemine flanşla dübellenir.</li>
<li>Paneller kelepçeyle direklere bağlanır; eğimde basamaklı yerleştirilir.</li>
<li>Kesilen panel uçları ve kesim yerleri boyayla kapatılır.</li>
<li>İstenirse üstüne [[ankara-jiletli-tel|jiletli tel]] ya da panele [[ankara-cim-cit|çim çit]] eklenir.</li>
</ol>"""
    + kutu("ipucu", "Panel çitte bir direk 2 cm kaçarsa sonraki panel oturmaz; hatayı hat boyunca taşırsınız. Bu yüzden direkleri "
           "tek tek değil, ip ve lazerle kontrol ederek dikiyoruz.."), "nasil-kurulur"),
   ("Fiyatı ne kadar?", "<p>Ekim 2026 piyasasında panel çit malzemesi yaklaşık 190–400 TL/m² (+KDV); montajlı metre fiyatı 290–450 TL "
    "civarında. Ayrıntı ve yurtdışı karşılaştırması [[ankara-orgu-panel-cit-fiyatlari|panel çit fiyatları]] sayfasında.</p>", "fiyat"),
  ],
  "kullanim_giris": "Panel çit nerede kullanılır? Görünüşün de önemli olduğu, düzgün ve sağlam bir sınır istenen her yerde.",
  "kullanim": [
   ("Site ve apartman çevresi", "Düzgün görünüm ve uzun ömür; ortak alan olduğu için yönetim kararı gerekir."),
   ("Fabrika, depo, OSB parseli", "200 cm ve üstü panel, üstte jiletli tel. Bkz. [[ankara-jiletli-tel|jiletli tel]]."),
   ("Okul, kreş, hastane", "Rijit, tırmanması zor ve temiz görünümlü sınır."),
   ("Müstakil ev ve villa", "Antrasit panel, istenirse [[ankara-cim-cit|çim çit]] ile gizlilik."),
   ("Otopark ve trafo alanı", "Hızlı kurulum, düşük bakım."),
   ("Spor alanı", "Alt kısımda panel, üstte yüksek tel; bkz. [[ankara-saha-teli|saha teli]]."),
  ],
  "siparis": [
   "<strong>Yer ve metraj:</strong> İlçe ve yaklaşık hat uzunluğu.",
   "<strong>Yükseklik:</strong> 100, 150, 200 cm…",
   "<strong>Renk:</strong> Yeşil (RAL 6005) mi, antrasit (RAL 7016) mi?",
   "<strong>Zemin:</strong> Toprak mı, beton / duvar üstü mü? (Direk tipi buna göre değişir.)",
   "<strong>Ekler:</strong> Kapı, jiletli tel, çim çit.",
  ],
  "sss": [
   ("Panel çit kaç metre?", "Paneller genelde 250 cm genişliğinde üretilir; yükseklik 100–200 cm arasında değişir."),
   ("Panel çit duvar üstüne takılır mı?", "Evet. Direkler flanşlı olarak duvar ya da beton zemine dübellenir."),
   ("Panel çit paslanır mı?", "Galvaniz tel üzerine elektrostatik boya uygulandığı için paslanmaya karşı korunur; kesim yerlerinin boyayla kapatılması önemlidir."),
   ("2D ve 3D panel farkı nedir?", "3D panelde V şeklinde katlamalar bulunur, daha rijittir. 2D daha düz ve ekonomiktir. Ayrıntısı [[ankara-orgu-panel-cit-cesitleri|çeşitler sayfasında]]."),
  ],
 },
 "fiyat": {
  "title": "Ankara Panel Çit Fiyatları 2026 - m² ve Metre Fiyatı",
  "desc": "Ankara örgü panel çit fiyatları Ekim 2026: 2D/3D panel m² fiyatı, panel takım, montajlı metre fiyatı; Almanya Doppelstabmatte fiyatlarıyla karşılaştırma.",
  "h1": "Ankara Örgü Panel Çit Fiyatları (Ekim 2026)",
  "ust": "2D mi 3D mi, 4 mm mi 5 mm mi, yeşil mi antrasit mi? Panel çit fiyatlarını kaynaklarıyla topladık, Almanya'daki karşılığıyla kıyasladık.",
  "ozet": [
   ("Montajlı panel çit", "290–450 TL/m"),
   ("2D panel (100–150 cm, 4 mm)", "210–280 TL/m² + KDV"),
   ("3D panel (150 cm, 5 mm)", "290–340 TL/m² + KDV"),
   ("Panel takım 150 × 250 cm", "≈ 940–2.900 TL"),
   ("Kamu birim fiyatı (1,5 m)", "859 TL/m"),
  ],
  "giris": [(None, "<p>Panel çitte fiyat iki şekilde konuşulur: <strong>m² (malzeme)</strong> ya da <strong>montajlı metre</strong>. "
             "Teklifleri karşılaştırırken aynı birimle konuştuğunuzdan emin olun. Rakamlar Ekim 2026 piyasa verisidir.</p>"
             + kutu("onemli", "Bir firmanın m² fiyatını diğerinin metre fiyatıyla kıyaslamayın. 150 cm yüksekliğinde 1 metre çit, 1,5 m² panel demek :)"))],
  "tr_giris": "<p>Türkiye piyasasında panel çit fiyatları (KDV durumu satırda belirtilmiştir):</p>",
  "tr": [
   ("2D panel", "100 cm · 4 mm", "210–250 TL/m² + KDV", "Karekod panel çit rehberi, Ağu 2026", "https://www.karekod.org/blog/panel-cit-fiyatlari/"),
   ("2D panel", "150 cm · 4 mm", "240–280 TL/m² + KDV", "Karekod panel çit rehberi, Ağu 2026", "https://www.karekod.org/blog/panel-cit-fiyatlari/"),
   ("3D panel", "150 cm · 5 mm", "290–340 TL/m² + KDV", "Karekod panel çit rehberi, Ağu 2026", "https://www.karekod.org/blog/panel-cit-fiyatlari/"),
   ("3D panel", "200 cm · 6 mm", "330–400 TL/m² + KDV", "Karekod panel çit rehberi, Ağu 2026", "https://www.karekod.org/blog/panel-cit-fiyatlari/"),
   ("PVC kaplı panel", "150 cm · 5 mm", "320–400 TL/m² + KDV", "Karekod panel çit rehberi, Ağu 2026", "https://www.karekod.org/blog/panel-cit-fiyatlari/"),
   ("Panel takım (imalatçı)", "100 / 150 / 200 × 250 cm", "625 / 938 / 1.250 TL", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Telfence panel takım, yeşil", "150 × 250 cm", "2.698 TL", "Koçtaş", "https://www.koctas.com.tr/telfence-150x250-cm-panel-cit-takim-yesil/p/5000703752"),
   ("Telfence panel takım, antrasit", "150 × 250 cm", "2.890 TL", "Koçtaş", "https://www.koctas.com.tr/telfence-150x250-cm-panel-cit-takim-antrasit/p/5000703856"),
   ("Montajlı panel çit", "—", "290–450 TL/m", "Karekod panel çit rehberi, Ağu 2026", "https://www.karekod.org/blog/panel-cit-fiyatlari/"),
   ("Galvaniz panel çit (kamu pozu)", "1,50 m · Ø4,5 mm", "859,49 TL/m", "Bakanlık birim fiyatı, Ara 2025", "https://www.birimfiyat.com/"),
  ],
  "tr_son": "<p>Dikkat ettiyseniz aynı ölçüdeki panel takımı yapı marketinde imalatçı fiyatının yaklaşık 3 katı. Market fiyatına kargo, "
            "raf ve marka payı biniyor; büyük metrajda doğrudan uygulayıcıyla çalışmak belirgin şekilde daha ekonomik.</p>",
  "yd_giris": "<p>Almanya'da panel çitin adı <em>Doppelstabmattenzaun</em> (çift çubuklu panel). Fiyatlar:</p>",
  "yd": [
   ("Almanya", "Doppelstabmatte 8/6/8, antrasit", "250 × 123 cm", 75.95, "EUR", "panel", "Hornbach.de", "https://www.hornbach.de/p/fa-bausysteme-doppelstabmatte-anthrazit-breite-2500-mm-hoehe-1230-draht-8-6-8-mm-gartenzaun-gitterzaun-metallzaun/12715664/"),
   ("Almanya", "Doppelstabmattenzaun, antrasit", "201 × 163 cm", 71.99, "EUR", "panel, direk hariç", "OBI.de", "https://www.obi.de/p/4172284/doppelstabmattenzaun-metall-163-cm-x-201-cm-anthrazit"),
   ("Avusturya", "Doppelstabmatte 6/5/6, antrasit", "251 × 163 cm", 89.99, "EUR", "panel", "OBI.at", "https://www.obi.at/p/7677131/doppelstabmattenzaun-staerke-6-5-6-anthrazit-163-x-251-cm"),
   ("Almanya", "Montajlı panel çit", "metre", (60, 140), "EUR", "metre", "Clean-Invoice maliyet rehberi (2026)", "https://www.clean-invoice.com/wissen/allgemein/zaun-bauen-kosten"),
  ],
  "yd_yorum": "<p>Almanya'da tek bir 250 cm'lik panel 4.000 TL'nin üzerinde; montajlı metre fiyatı ise <strong>3.300–7.800 TL</strong> "
   "aralığına denk geliyor. Türkiye'de montajlı metre 290–450 TL. Yani Almanya'da aynı işin metresi kabaca 10–17 katı. Paneller "
   "Avrupa'da genelde daha kalın tel (6/5/6, 8/6/8 mm çift çubuk) ile satılıyor; karşılaştırırken bunu da hesaba katın.</p>"
   + kutu("not", "Almanya'daki rehbere göre 200 cm'nin üzerindeki çitlerde fiyat %20–35 artıyor. Türkiye'de de yükseklik arttıkça "
          "hem panel hem direk maliyeti benzer şekilde yükseliyor."),
  "govde": [
   ("Panel çit fiyatını ne değiştirir?", liste(
     "<strong>2D / 3D:</strong> 3D (V katlamalı) panel daha rijit ve daha pahalı.",
     "<strong>Tel kalınlığı:</strong> 4, 5, 6 mm; kalınlık arttıkça ağırlık ve fiyat artar.",
     "<strong>Yükseklik:</strong> 200 cm üstünde panel ve direk maliyeti belirgin yükselir.",
     "<strong>Kaplama:</strong> Galvaniz + toz boya standart; PVC kaplı panel daha pahalı.",
     "<strong>Zemin:</strong> Beton zeminde flanşlı direk, toprakta betonlanan direk.",
     "<strong>Metraj:</strong> 500 m² üzeri işlerde m² fiyatı düşebiliyor."), "etkenler"),
   ("Örnek hesap: 50 metre bahçe, 150 cm", hesap("50 m · 150 cm · 3D 5 mm · antrasit", [
        ("Panel: 20 adet (250 cm)", "≈ 75 m² × 290–340 TL"),
        ("Direk + kelepçe: 21 adet", "direk tipine göre"),
        ("Montaj", "metraj ve zemine göre"),
       ], "Montajlı ≈ 14.500–22.500 TL + KDV")
    + "<p>Montajlı metre fiyatı (290–450 TL) üzerinden kaba hesap. Kapı ve köşe sayısı rakamı değiştirir.</p>", "ornek"),
  ],
  "sss": [
   ("Panel çitin metresi ne kadar?", "Ekim 2026 piyasasında montajlı panel çit yaklaşık 290–450 TL/metre."),
   ("Panel çit m² fiyatı ne kadar?", "2D panelde 210–280, 3D panelde 260–400 TL/m² (+KDV) aralığında; tel kalınlığı ve yüksekliğe göre değişiyor."),
   ("Panel çiti yapı marketinden almak mantıklı mı?", "Küçük işlerde olabilir. Ancak marketteki takım fiyatı imalatçı fiyatının yaklaşık 3 katı; büyük metrajda doğrudan uygulayıcıyla çalışmak daha ekonomik."),
  ],
 },
 "cesit": {
  "title": "Ankara Panel Çit Çeşitleri: 2D, 3D, Renk ve Yükseklik",
  "desc": "Örgü panel çit çeşitleri: 2D ve 3D panel, tel kalınlıkları, yeşil ve antrasit renkler, yükseklikler, direk ve kelepçe sistemleri.",
  "h1": "Ankara Örgü Panel Çit Çeşitleri",
  "gorsel": "panel-tel3",
  "ust": "2D, 3D, 4 mm, 5 mm, yeşil, antrasit… Panel çit seçeneklerini ve hangisinin nereye uyduğunu anlattık.",
  "giris": [(None, "<p>Panel çitte seçim beş başlıkta yapılır: panel tipi, tel kalınlığı, yükseklik, renk ve direk sistemi.</p>")],
  "cesitler": [
   ("3d", "3D (V katlamalı) panel", "<p>Panel yüzeyinde yatay V katlamalar bulunur; bu katlamalar paneli rijitleştirir. Site, ev ve okul "
    "çevresinde en çok kullanılan tip.</p>", ["En yaygın", "Rijit"]),
   ("2d", "2D (çift çubuklu) panel", "<p>Katlaması olmayan, yatayda çift tel kullanılan düz panel. Avrupa'da Doppelstabmatte adıyla "
    "bilinir. Büyük arazilerde ekonomik, ağır tipleri ise çok sağlam.</p>", ["Düz", "Çift yatay tel"]),
   ("kalinlik", "Tel kalınlığına göre: 4 – 6 mm", "<p>Konut için 4–5 mm yeterli; fabrika ve güvenlik alanı için 5–6 mm. Kalınlık "
    "arttıkça panel ağırlaşır, direk de güçlendirilmelidir.</p>", ["4 mm", "5 mm", "6 mm"]),
   ("renk", "Renge göre: yeşil ve antrasit", "<p>RAL 6005 yeşil bahçeyle bütünleşir; RAL 7016 antrasit modern cephelerle uyumludur. "
    "Farklı RAL renkleri sipariş üzerine yapılabilir.</p>", ["RAL 6005", "RAL 7016"]),
   ("direk", "Direk ve bağlantı", "<p>Kutu profil direk (50×50, 60×40) betonlanır ya da flanşla zemine dübellenir; panel kelepçe ile "
    "bağlanır. Kapı için daha güçlü direk kullanılır, bkz. [[ankara-cit-kapisi|çit kapısı]].</p>", ["Gömme", "Flanşlı"]),
   ("pvc", "PVC kaplı panel", "<p>Toz boya yerine PVC kaplanan panel; dış etkilere karşı ek koruma sağlar, fiyatı daha yüksektir.</p>",
    ["Ek koruma"]),
  ],
  "tablo": [
   ["Çeşit", "Görünüm", "Dayanım", "Nereye uygun"],
   ["3D · 4 mm", "V katlamalı", "Orta", "Bahçe, villa"],
   ["3D · 5 mm", "V katlamalı", "Yüksek", "Site, okul"],
   ["2D · 6/5/6 mm", "Düz, çift tel", "Çok yüksek", "Fabrika, güvenlik"],
   ["Antrasit", "Modern", "—", "Yeni cepheler"],
   ["Yeşil", "Doğal", "—", "Bahçe, park"],
  ],
  "govde": [
   ("Hangi panel çiti seçmeliyim?", "<p>Ev ve site için 3D, 4–5 mm, 150 cm yükseklik çoğu zaman doğru seçim. Fabrika ve güvenlik "
    "alanında 200 cm ve üstü, kalın tel ve üstte jiletli tel. Gizlilik istiyorsanız panelin içinden [[ankara-cim-cit|çim çit]] geçirilebilir.</p>"
    + kutu("tavsiye", "Antrasit panel tozda daha az kirli görünür; yeşil panel ise bahçede kaybolur. Karar veremiyorsanız binanın "
           "doğrama rengine bakın :)"), "secim"),
  ],
  "sss": [
   ("Panel çit çeşitleri nelerdir?", "Panel tipine göre 2D ve 3D; tel kalınlığına göre 4–6 mm; renge göre yeşil, antrasit ve diğer RAL renkleri; yükseklik 100–200 cm ve üstü."),
   ("En çok hangi panel çit kullanılıyor?", "Konut ve sitelerde 3D V katlamalı, 4–5 mm, yeşil ya da antrasit panel."),
   ("Panel çite kapı yapılır mı?", "Evet, aynı panel dolgulu yaya ve araç kapıları yapılır. Bkz. [[ankara-cit-kapisi|çit kapısı]]."),
  ],
 },
}
