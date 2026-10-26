from ._ortak import kutu, liste, hesap

K = {
 "slug": "ankara-jiletli-tel", "ad": "Jiletli Tel", "baslik": "Ankara Jiletli Tel", "ikon": "jilet",
 "kisa": "Duvar, tel örgü ve panel çit üstüne spiral ya da düzlemsel jiletli tel; depo, şantiye ve fabrika güvenliği.",
 "gorsel": "jiletli-tel", "gorsel2": "tel-cit",
 "kat": {
  "title": "Ankara Jiletli Tel - Satış ve Montaj | Doğanay Tel Örgü",
  "desc": "Ankara jiletli tel: helezon (spiral), düzlemsel ve düz jiletli tel; duvar, tel örgü ve panel çit üstü montaj. Fiyat, çeşit, kullanım ve sipariş.",
  "h1": "Ankara Jiletli Tel",
  "ust": "Bir alanı sadece çevirmek değil, içeri girmeyi gerçekten zorlaştırmak istiyorsanız jiletli tel en caydırıcı çözüm. "
         "Ankara'da duvar, tel örgü ve panel çit üstüne jiletli tel takıyoruz.",
  "govde": [
   ("Jiletli tel nedir?", """
<p>Jiletli tel; galvaniz bir çekirdek telin üzerine, keskin bıçaklar halinde kesilmiş ince çelik şeridin sarılmasıyla üretilir.
Bıçak şeridi genellikle 0,5 mm civarı galvaniz ya da paslanmaz (AISI 304/430) saçtır. Spiral (helezon) olarak açılan tipine
<em>concertina</em>, NATO teli ya da helezon jiletli tel de denir.</p>"""
    + kutu("not", "Jiletli tel tek başına bir çit değildir; mevcut duvarın, [[ankara-tel-orgu|tel örgünün]] ya da "
           "[[ankara-orgu-panel-cit|panel çitin]] üstüne eklenen bir güvenlik katmanıdır."), "nedir"),
   ("Jiletli tel nasıl takılır?", """
<ol>
<li><strong>Taşıyıcı:</strong> Duvara demir kollar ya da Y/L destekler sabitlenir; çit direklerine kol takılır.</li>
<li><strong>Gergi teli:</strong> Kolların üzerinden 2–3 sıra gergi teli çekilir.</li>
<li><strong>Açma:</strong> Spiral rulo kontrollü şekilde açılır, istenen aralıkta gerilir.</li>
<li><strong>Bağlama:</strong> Spiral belirli aralıklarla gergi tellerine klipslerle bağlanır; yoksa zamanla sarkar.</li>
</ol>"""
    + kutu("dikkat", "Jiletli tel montajı kesinlikle eldivensiz, gözlüksüz yapılmaz. Rulo açılırken yay gibi davranır; deneyimsiz "
           "montajda yaralanma riski yüksek. Bu işi kendiniz yapmaya kalkmanızı tavsiye etmeyiz.."), "nasil-takilir"),
   ("Yasal durum ve komşuluk", """
<p>Araştırmamızda Türkiye'de yerleşim alanında jiletli teli açıkça yasaklayan bir hüküm bulamadık. Ancak Planlı Alanlar İmar
Yönetmeliği bahçe duvarı ve üstündeki parmaklık yüksekliğine sınır getiriyor; apartman ve sitelerde ortak alanda yapılacak
değişiklikler de kat maliklerinin kararına bağlı. Bu yüzden konut bölgesinde jiletli tel taktırmadan önce
<strong>belediyenin imar birimine ve site yönetimine danışmanızı</strong> öneriyoruz.</p>
<p>Ayrıca jiletli tel yaya yoluna ve komşu tarafına taşmayacak şekilde, içe doğru yönlendirilmelidir.</p>""", "yasal"),
   ("Fiyatı ne kadar?", "<p>Galvaniz jiletli tel Ekim 2026 piyasasında çapına göre yaklaşık 45–110 TL/metre. Kaynaklı tablo ve "
    "İngiltere/ABD karşılaştırması için [[ankara-jiletli-tel-fiyatlari|jiletli tel fiyatları]] sayfasına bakın.</p>", "fiyat"),
  ],
  "kullanim_giris": "Jiletli tel nerede kullanılır? Güvenliğin öncelikli olduğu, izinsiz girişin ciddi zarar doğurabileceği yerlerde.",
  "kullanim": [
   ("Fabrika ve depo", "Panel çit ya da duvar üstünde, Y kol ortasında helezon jiletli tel."),
   ("Şantiye", "Malzeme hırsızlığına karşı geçici çit üstünde."),
   ("Trafo, baz istasyonu, enerji tesisi", "Yetkisiz girişin tehlikeli olduğu alanlar."),
   ("Tarım deposu ve ahır", "Kırsal alanda hayvan ve ekipman güvenliği."),
   ("Duvar üstü", "Mevcut bahçe ya da çevre duvarının üstüne, demir kollarla."),
   ("Zemin bariyeri", "Gerektiğinde zemine yatay serilerek ikinci engel hattı."),
  ],
  "siparis": [
   "<strong>Yer:</strong> İşin yapılacağı ilçe ve tesis tipi.",
   "<strong>Metraj:</strong> Jiletli tel çekilecek hattın uzunluğu.",
   "<strong>Taşıyıcı:</strong> Duvar üstü mü, tel örgü / panel çit üstü mü?",
   "<strong>Tip:</strong> Helezon (spiral) mi, düzlemsel mi? Çap tercihi (45 / 60 / 90 cm).",
   "<strong>Malzeme:</strong> Galvaniz mi, paslanmaz mı?",
  ],
  "sss": [
   ("Jiletli tel ile dikenli tel farkı nedir?", "Dikenli tel aralıklı dikenleri olan düz teldir. Jiletli tel keskin bıçaklı ve genellikle spiraldir; çok daha caydırıcıdır."),
   ("Jiletli tel çapı nasıl seçilir?", "Duvar ve çit yüksekliğine göre. 45 cm duvar üstünde yaygın; 60–90 cm daha büyük ve daha caydırıcı spiral oluşturur."),
   ("Evime jiletli tel taktırabilir miyim?", "Açık bir yasak bulamadık; ancak imar yönetmeliği ve site yönetim planı nedeniyle önce belediye ve yönetimle görüşmenizi öneririz."),
   ("Mevcut tel örgümün üstüne jiletli tel eklenir mi?", "Direkler sağlamsa evet; direk başlarına kol takılarak eklenir."),
  ],
 },
 "fiyat": {
  "title": "Ankara Jiletli Tel Fiyatları 2026 - Metre ve Rulo Fiyatı",
  "desc": "Ankara jiletli tel fiyatları Ekim 2026: 45-60-90 cm helezon, düzlemsel ve paslanmaz jiletli tel metre ve rulo fiyatı; İngiltere ve ABD karşılaştırması.",
  "h1": "Ankara Jiletli Tel Fiyatları (Ekim 2026)",
  "ust": "Jiletli telin metresi kaç TL, 50 metrelik rulo ne kadar, paslanmaz ne kadar farkeder? Kaynaklarıyla tablo ve yurtdışı karşılaştırması.",
  "ozet": [
   ("Galvaniz helezon (45–90 cm)", "45–110 TL/m"),
   ("Düzlemsel jiletli tel", "45–65 TL/m"),
   ("50 m rulo", "2.250–5.500 TL"),
   ("Paslanmaz 304", "≈ +%30"),
   ("Kamu pozu (temin + gerdirme)", "546 TL/m"),
  ],
  "giris": [(None, "<p>Jiletli telde fiyatı belirleyen başlıca şeyler spiralin çapı, tipi (helezon/düzlemsel) ve malzemesi (galvaniz/paslanmaz). "
             "Aşağıdaki rakamlar montaj hariç Ekim 2026 piyasa verisidir.</p>")],
  "tr_giris": "<p>Türkiye piyasasında jiletli tel fiyatları:</p>",
  "tr": [
   ("Helezon jiletli tel, galvaniz", "Ø45 cm", "45 TL/m + KDV", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Helezon jiletli tel, galvaniz", "Ø60 cm", "65 TL/m + KDV", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Helezon jiletli tel, galvaniz", "Ø90 cm", "85 TL/m + KDV", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Helezon jiletli tel, galvaniz", "Ø60 cm · 50 m rulo", "5.500 TL (≈110 TL/m) KDV dahil", "Ankara satıcı listesi, Eki 2026", ""),
   ("Düzlemsel jiletli tel", "—", "45–65 TL/m", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Düzlemsel jiletli tel", "50 m rulo", "5.299 TL", "Cimri ilanı, 2026", "https://www.cimri.com/jiletli-tel-fiyat"),
   ("Paslanmaz 304 jiletli tel", "—", "195 TL/kg", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Helezon galvaniz (kamu pozu 10.480.1802)", "—", "115,31 TL/kg", "Bakanlık birim fiyatı, Eyl 2026", "https://herpoz.com/"),
   ("Jiletli tel temini + gerdirme (kamu pozu KTB.91.1003)", "montajlı", "546,23 TL/m", "Birim fiyat, Tem 2026", "https://herpoz.com/"),
  ],
  "tr_son": kutu("not", "Kamu birim fiyatında helezon jiletli telin kilosu bir yılda 91,41 TL'den 115,31 TL'ye çıktı (yaklaşık %26). "
                 "Çelik ürünlerinde fiyatlar hızlı değişiyor; teklifin geçerlilik süresini sorun."),
  "yd_giris": "<p>İngiltere ve ABD'de jiletli tel küçük rulolarla satılıyor:</p>",
  "yd": [
   ("İngiltere", "Concertina jiletli tel", "450 mm · 10 m", 32.47, "GBP", "rulo, KDV dahil", "Firstfence", "https://firstfence.co.uk/concertina-razor-wire-450mm"),
   ("İngiltere", "Galvaniz concertina", "455 mm · 10 m", 27.80, "GBP", "rulo + KDV", "F.H. Brundle", "https://www.fhbrundle.co.uk/"),
   ("ABD", "Çift spiral jiletli tel", "48 cm · 45 m (3 rulo)", 71.43, "USD", "kutu", "Home Depot", "https://www.homedepot.com/p/333639842"),
   ("ABD", "Concertina jiletli tel", "46 cm · 99 m", 59.99, "USD", "rulo", "Walmart", "https://www.walmart.com/"),
  ],
  "yd_yorum": "<p>Metreye çevirince İngiltere'de 45 cm'lik jiletli tel yaklaşık <strong>185–215 TL/m</strong>; Türkiye'de aynı çap 45–65 TL/m. "
   "ABD'de büyük rulolarda metre fiyatı 30–80 TL arasına iniyor; bu ürünler genelde ince bıçaklı, hafif tiplerdir. Fiyat karşılaştırırken "
   "bıçak kalınlığına ve çekirdek tele de bakmak gerekir.</p>",
  "govde": [
   ("Jiletli tel fiyatını ne değiştirir?", liste(
     "<strong>Spiral çapı:</strong> 45, 60, 90 cm; çap büyüdükçe metreye giren bıçak şeridi artar.",
     "<strong>Tip:</strong> Helezon, düzlemsel, düz hat; düz hat en ekonomik.",
     "<strong>Malzeme:</strong> Paslanmaz 304 galvanize göre yaklaşık %30 pahalı.",
     "<strong>Taşıyıcı:</strong> Duvar kolları, Y kol, gergi teli ayrı kalem.",
     "<strong>Montaj zorluğu:</strong> Yükseklik ve erişim (iskele, sepetli araç) işçiliği artırır."), "etkenler"),
   ("Örnek hesap: 100 m panel çit üstü", hesap("100 m · Ø60 cm helezon · galvaniz", [
        ("Jiletli tel: 100 m × 65–110 TL", "≈ 6.500–11.000 TL"),
        ("Y/L kollar ve gergi teli", "direk sayısına göre"),
        ("Montaj", "yüksekliğe ve erişime göre"),
       ], "Malzeme ≈ 6.500–11.000 TL + kollar ve montaj"), "ornek"),
  ],
  "sss": [
   ("Jiletli telin metresi kaç TL?", "Ekim 2026'da galvaniz helezon jiletli tel çapına göre yaklaşık 45–110 TL/m (montaj hariç)."),
   ("50 metre jiletli tel kaç TL?", "Çapa ve tipe göre yaklaşık 2.250–5.500 TL."),
   ("Paslanmaz jiletli tel ne kadar pahalı?", "Galvanize göre yaklaşık %30 daha pahalı; kilosu 195 TL civarında."),
  ],
 },
 "cesit": {
  "title": "Ankara Jiletli Tel Çeşitleri: Helezon, Düzlemsel, Paslanmaz",
  "desc": "Jiletli tel çeşitleri: helezon (spiral) concertina, çapraz tip, düzlemsel, düz hat jiletli tel; galvaniz ve paslanmaz; 45-60-90 cm çaplar.",
  "h1": "Ankara Jiletli Tel Çeşitleri",
  "gorsel": "jiletli-tel",
  "ust": "Helezon mu, düzlemsel mi, düz hat mı? 45 cm mi, 90 cm mi? Jiletli tel çeşitlerini ve nerede ne kullanıldığını anlattık.",
  "giris": [(None, "<p>Jiletli teller; şekline (helezon, düzlemsel, düz), çapına ve malzemesine göre ayrılır.</p>")],
  "cesitler": [
   ("helezon", "Helezon (spiral) jiletli tel", "<p>Spiral olarak açılan, en bilinen tip (concertina). Duvar ve çit üstünde hacimli, "
    "aşılması zor bir engel oluşturur.</p>", ["En caydırıcı", "Ø45 / 60 / 90 cm"]),
   ("capraz", "Çapraz (cross) tip", "<p>Spiraller belirli noktalardan birbirine klipslenerek çapraz bir ağ oluşturur. Daha sık ve "
    "daha zor açılan bir engel; yüksek güvenlikli alanlarda kullanılır.</p>", ["Yüksek güvenlik"]),
   ("duzlemsel", "Düzlemsel (flat) jiletli tel", "<p>Spiral yerine düz bir panel gibi açılır. Hacim kaplamaz, duvar yüzeyine ya da "
    "panel çitin önüne yakın montaj için uygundur; görüntüsü daha sadedir.</p>", ["Az yer kaplar", "Sade"]),
   ("duz", "Düz hat jiletli tel", "<p>Gergi teli gibi düz çekilen tek sıra jiletli tel. Dikenli telin daha caydırıcı versiyonu; "
    "en ekonomik jiletli tel tipi.</p>", ["Ekonomik", "Tek sıra"]),
   ("malzeme", "Galvaniz ve paslanmaz", "<p>Galvaniz standart ve ekonomik; paslanmaz (AISI 304) nemli ve uzun ömür beklenen yerlerde "
    "tercih edilir, yaklaşık %30 pahalıdır.</p>", ["Galvaniz", "Paslanmaz 304"]),
  ],
  "tablo": [
   ["Çeşit", "Caydırıcılık", "Yer kaplama", "Nereye uygun"],
   ["Helezon Ø45 cm", "Yüksek", "Orta", "Duvar üstü"],
   ["Helezon Ø60–90 cm", "Çok yüksek", "Fazla", "Fabrika, depo"],
   ["Çapraz tip", "Çok yüksek", "Fazla", "Yüksek güvenlikli alan"],
   ["Düzlemsel", "Orta-yüksek", "Az", "Cephe, panel önü"],
   ["Düz hat", "Orta", "Çok az", "Tel örgü üstü sıra"],
  ],
  "govde": [
   ("Hangi jiletli teli seçmeliyim?", "<p>Duvar üstü için Ø45 cm helezon çoğu işi görür. Fabrika ve depoda Y kol ortasında Ø60–90 cm. "
    "Görüntünün önemli olduğu yerde düzlemsel. Sadece tel örgünüzün üstüne bir sıra eklemek istiyorsanız düz hat ya da "
    "[[ankara-dikenli-tel|dikenli tel]] yeterli.</p>"
    + kutu("tavsiye", "Jiletli teli içe doğru yönlendirin; yaya yoluna ve komşuya taşan jiletli tel hem tehlikeli hem de sorun çıkarır."),
    "secim"),
  ],
  "sss": [
   ("Jiletli tel çeşitleri nelerdir?", "Helezon (spiral), çapraz tip, düzlemsel ve düz hat; malzemeye göre galvaniz ve paslanmaz."),
   ("Concertina tel ne demek?", "Spiral olarak açılan helezon jiletli telin uluslararası adıdır; NATO teli de denir."),
   ("Düzlemsel jiletli tel nerede kullanılır?", "Az yer kaplaması istenen cephelerde, duvar yüzeyinde ve panel çit önünde."),
  ],
 },
}
