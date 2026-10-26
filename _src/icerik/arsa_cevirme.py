from ._ortak import kutu, liste, hesap

K = {
 "slug": "ankara-arsa-tarla-cevirme", "ad": "Arsa ve Tarla Çevirme", "baslik": "Ankara Arsa ve Tarla Çevirme", "ikon": "arsa",
 "kisa": "Arsa, tarla, bağ-bahçe ve şantiye çevresini tel örgü, dikenli tel ya da panel çitle çeviriyoruz.",
 "gorsel": "tel-orgu-resmi2", "gorsel2": "arsa-cevirme",
 "kat": {
  "title": "Ankara Arsa ve Tarla Çevirme - Tel Çit | Doğanay Tel Örgü",
  "desc": "Ankara arsa ve tarla çevirme: tel örgü, dikenli tel ve panel çit ile arsa, tarla, bağ-bahçe çevirme. Dönüm maliyeti, çeşitler, yasal notlar ve sipariş.",
  "h1": "Ankara Arsa ve Tarla Çevirme",
  "ust": "Arsanızı, tarlanızı ya da bağ evinizin bahçesini çevirmek istiyorsunuz ama nereden başlayacağınızı bilmiyorsanız doğru "
         "yerdesiniz. Ankara'da arsa ve tarla çevirme işinin tamamını yapıyoruz.",
  "govde": [
   ("Arsa çevirmeye nereden başlamalı?", """
<p>Çevirme işi telden önce <strong>sınırla</strong> başlar. Çiti nereye çekeceğinizden emin olmadan direk dikmek, sonradan
komşuyla sorun yaşamanın en kısa yolu.</p>"""
    + liste("<strong>Sınır noktaları:</strong> Tapu ve kadastro bilgisine göre köşe noktalarının belli olması gerekir. Emin "
            "değilseniz bir lisanslı harita bürosundan aplikasyon (yerinde sınır gösterimi) yaptırmanızı öneririz.",
            "<strong>Hisseli tapu:</strong> Paylı mülkiyette olağan kullanımı aşan işler kural olarak paydaşların kabulüne bağlıdır "
            "(TMK md. 692). Hisseli bir arsayı tek başınıza çevirmeden önce diğer hissedarlarla konuşun.",
            "<strong>İmar durumu:</strong> İmar alanında bahçe duvarı ve parmaklık yükseklikleri yönetmelikle sınırlı. Kalıcı beton "
            "hatıl ya da duvar yapacaksanız belediyeye danışın.")
    + kutu("onemli", "Bu bölüm hukuki tavsiye değildir; genel bilgi olarak yazıldı. Sınır ve izin konusunda kesin cevap için "
           "tapu müdürlüğü, harita bürosu ya da belediyenin imar birimine danışın."), "baslangic"),
   ("Hangi çit, nereye?", """
<p>Arsa ve tarla çevirmede tek bir doğru yok; bütçe, arazinin eğimi ve amaç belirliyor:</p>"""
    + liste("<strong>Tarla ve mera:</strong> [[ankara-dikenli-tel|Dikenli tel]] ya da galvaniz [[ankara-tel-orgu|tel örgü]] + beton direk.",
            "<strong>Arsa:</strong> Beton direkli galvaniz tel örgü, üstte 1–2 sıra dikenli tel.",
            "<strong>Bağ-bahçe:</strong> PVC kaplı tel örgü ya da [[ankara-orgu-panel-cit|panel çit]].",
            "<strong>Yol cephesi:</strong> Görünür taraf panel, arka taraf tel örgü; bütçeyi dengelemenin en mantıklı yolu.")
    + "<p>Seçenekleri karşılaştırmalı olarak [[ankara-arsa-tarla-cevirme-cesitleri|arsa çevirme çeşitleri]] sayfasında anlattık.</p>",
    "hangi-cit"),
   ("Ankara'da arazide direk temeli", """
<p>Ankara'da kayıtlara geçen en düşük sıcaklık -24,9 °C ve ocak ayının ortalama en düşüğü -3,1 °C (MGM, 1927–2025). Kışın
toprak donuyor, baharda çözülüyor; sığ betonlanmış direkler bu döngüde yerinden oynuyor. Ankara'da don derinliği için tek bir
resmi değer yok; zemin etütlerinde 80–100 cm civarı görülüyor. Kalıcı bir çitte direk temelini bu gerçeğe göre yapıyoruz.</p>""",
    "iklim"),
   ("Bir dönüm arsayı çevirmek ne kadar tutar?", "<p>1 dönüm (1.000 m²) kare bir arsanın çevresi yaklaşık 126 metre. Ankara'da tel örgü ile "
    "çevrilmesinin Ekim 2026 piyasasında kapı dahil yaklaşık 35.000–65.000 TL tuttuğunu görüyoruz. Hesabın detayları "
    "[[ankara-arsa-tarla-cevirme-fiyatlari|arsa çevirme fiyatları]] sayfasında.</p>", "fiyat"),
  ],
  "kullanim_giris": "Arsa ve tarla çevirme hangi durumlarda yapılır? En sık karşılaştığımız ihtiyaçlar:",
  "kullanim": [
   ("Boş imarlı arsa", "Sınırı belli etmek, izinsiz park ve moloz dökülmesini önlemek."),
   ("Tarla ve mera", "Hayvanı içeride tutmak ya da dışarıda bırakmak; dikenli tel ya da tel örgü."),
   ("Bağ evi ve hobi bahçesi", "Görünüm ve güvenlik birlikte; PVC kaplı tel ya da panel."),
   ("Meyve bahçesi", "Yabani hayvan ve izinsiz toplamaya karşı."),
   ("Şantiye", "Malzeme güvenliği; gerekirse [[ankara-jiletli-tel|jiletli tel]]."),
   ("Sanayi ve depo arsası", "Yüksek çit, üstte dikenli ya da jiletli tel."),
  ],
  "siparis": [
   "<strong>Konum:</strong> Arsa/tarlanın ilçe ve mahalle/köy bilgisi (konum atabilirsiniz).",
   "<strong>Ölçü:</strong> Çevre uzunluğu ya da tapudaki alan (m², dönüm).",
   "<strong>Amaç:</strong> Sınır mı, hayvan mı, güvenlik mi?",
   "<strong>Kapı:</strong> Kaç kapı, araç kapısı genişliği.",
   "<strong>Arazi:</strong> Eğim, taşlık, ulaşım durumu.",
  ],
  "sss": [
   ("Arsa çevirmek için izin gerekir mi?", "Beton direkli tel çit için durum, arsanın imar durumuna ve yapılacak işe göre değişebilir. Kalıcı duvar ya da beton hatıl yapılacaksa mutlaka belediyeye danışın."),
   ("Hisseli tarlayı çevirebilir miyim?", "Paylı mülkiyette olağan kullanımı aşan işler kural olarak tüm paydaşların kabulüne bağlıdır; önce diğer hissedarlarla anlaşmanız gerekir."),
   ("1 dönüm arsanın çevresi kaç metre?", "Kare bir arsada yaklaşık 126 metre; arsanın şekli uzadıkça çevre artar."),
   ("Sınırı siz mi belirliyorsunuz?", "Hayır; çiti sizin gösterdiğiniz, tapu ve kadastroya göre belli olan noktalara çekiyoruz. Emin değilseniz önce aplikasyon yaptırın."),
  ],
 },
 "fiyat": {
  "title": "Ankara Arsa ve Tarla Çevirme Fiyatları 2026 - Dönüm Maliyeti",
  "desc": "Ankara arsa ve tarla çevirme fiyatları Ekim 2026: 1 dönüm tel örgü maliyeti, gerçek Ankara talepleri, metre fiyatı; ABD, İngiltere ve Almanya karşılaştırması.",
  "h1": "Ankara Arsa ve Tarla Çevirme Fiyatları (Ekim 2026)",
  "ust": "Bir dönüm arsayı tel örgüyle çevirmek ne tutar? Ankara'dan gerçek talepler, satıcı rehberleri ve yurtdışı karşılaştırması tek sayfada.",
  "ozet": [
   ("1 dönüm (≈126 m), kapı dahil", "35.000–65.000 TL"),
   ("Montajlı tel örgü", "290–450 TL/m"),
   ("Beton direkli, nakliye dahil", "290 TL/m'den"),
   ("Dikenli tel (sadece tel)", "≈ 3–4 TL/m"),
  ],
  "giris": [(None, "<p>Arsa çevirme fiyatı çit tipinden çok <strong>çevre uzunluğuna ve araziye</strong> bağlı. Aynı alan, şekli uzadıkça "
             "daha fazla metre çit ister. Rakamlar Ekim 2026 piyasa verisidir.</p>"
             + kutu("ipucu", "Arsanızın alanını değil çevresini bilin. 1 dönüm kare arsa ≈126 m çevre; aynı alan 20 × 50 m olursa çevre 140 m olur."))],
  "tr_giris": "<p>Ankara'dan gerçek iş talepleri ve piyasa fiyatları (Armut rakamları müşteri talebine verilen teklif aralıklarıdır):</p>",
  "tr": [
   ("Gölbaşı · 100 m, 180 cm, ≈1 dönüm, 1 kapı", "Armut talebi, 6 Eki 2026", "34.500–65.000 TL (orta: 50.000)", "Armut", "https://armut.com/fiyatlari/ankara-tel-orgu-cit_28387_6"),
   ("Mamak · 60 m, 150 cm, beton direk, 4 m kapı", "Armut talebi, 15 Eki 2026", "30.000–43.265 TL", "Armut", "https://armut.com/fiyatlari/ankara-tel-orgu-cit_28387_6"),
   ("Polatlı · 150 m, 150 cm, 1.000 m², 1 kapı", "Armut talebi, 13 Eki 2026", "35.000–147.500 TL", "Armut", "https://armut.com/fiyatlari/ankara-tel-orgu-cit_28387_6"),
   ("Kızılcahamam · 100 m, 150 cm, 4 m kapı", "Armut talebi, 16 Eyl 2026", "29.000–111.111 TL", "Armut", "https://armut.com/fiyatlari/ankara-tel-orgu-cit_28387_6"),
   ("Elmadağ · 80 m, 180 cm, 4 m kapı", "Armut talebi, 24 Ağu 2026", "38.000–111.111 TL", "Armut", "https://armut.com/fiyatlari/ankara-tel-orgu-cit_28387_6"),
   ("1 dönüm çevre, montaj + 4 m kapı", "≈120–130 m", "35.000–55.000 TL", "Ankara satıcı rehberi, Eki 2026", ""),
   ("Beton direkli tel örgü", "montaj + nakliye dahil", "290 TL/m'den", "Ankara satıcı rehberi, Eki 2026", ""),
   ("Standart tel örgü", "montaj dahil", "290–450 TL/m", "Ankara satıcı rehberi, Eki 2026", ""),
  ],
  "tr_son": "<p>Aynı ölçüdeki iş için bile tekliflerin 3–4 kat farklı olabildiğini görüyorsunuz. Farkın nedeni genelde tel kalınlığı, direk tipi "
            "ve temel, kapı kalitesi ve nakliye. Teklifleri bu kalemleri yan yana koyarak karşılaştırın.</p>"
            + kutu("dikkat", "En düşük teklif çoğu zaman ince tel ve sığ direk demek. Arazide çit bir kez yapılır; iki kez yapmak her zaman daha pahalı.."),
  "yd_giris": "<p>Yurtdışında arazi çevirme maliyeti (montajlı, metre başına):</p>",
  "yd": [
   ("ABD", "Montajlı chain-link çit", "metre karşılığı", (32.8, 131), "USD", "metre", "HomeGuide (2026)", "https://homeguide.com/costs/chain-link-fence-cost"),
   ("İngiltere", "Chain-link malzeme", "1,8 m yükseklik", 34.75, "GBP", "metre", "Checkatrade", "https://www.checkatrade.com/blog/cost-guides/chain-link-fence-cost/"),
   ("İngiltere", "Çit işçiliği", "günlük", 220, "GBP", "gün", "Checkatrade", "https://www.checkatrade.com/blog/cost-guides/chain-link-fence-cost/"),
   ("Almanya", "Tel örgü çit (Maschendrahtzaun), montajlı", "direk + temel dahil", (35, 70), "EUR", "metre", "Clean-Invoice (2026)", "https://www.clean-invoice.com/wissen/allgemein/zaun-bauen-kosten"),
  ],
  "yd_yorum": "<p>Bir dönüm (≈126 m) arsayı tel örgüyle çevirmek Almanya'da montajlı fiyatla yaklaşık <strong>245.000–490.000 TL</strong>, "
   "ABD'de 205.000 TL'nin üzerinde tutuyor. Türkiye'de aynı iş 35.000–65.000 TL. Fark büyük ölçüde işçilik ve yan maliyetlerden geliyor.</p>",
  "govde": [
   ("Arsa çevirme fiyatını ne değiştirir?", liste(
     "<strong>Çevre uzunluğu ve şekil:</strong> Uzun ve dar arsa daha fazla metre ister.",
     "<strong>Çit tipi:</strong> Dikenli tel &lt; galvaniz tel örgü &lt; PVC kaplı &lt; panel çit.",
     "<strong>Yükseklik:</strong> 150'den 180–200 cm'ye çıkınca tel ve direk maliyeti artar.",
     "<strong>Kapı:</strong> 4 m arazi kapısı tek başına toplamın ciddi bir kısmı.",
     "<strong>Arazi:</strong> Eğim, taşlık ve ulaşım (malzeme taşıma) işçiliği artırır.",
     "<strong>Mesafe:</strong> Şehir dışı ve köy arazilerinde nakliye ayrı kalem olabilir.",
     "<strong>Maliyet artışı:</strong> TÜİK'e göre inşaat maliyetleri Ağustos 2026'da yıllık %29,6 arttı; teklifler kısa süre geçerli."), "etkenler"),
   ("Örnek hesap: 1 dönüm, Gölbaşı", hesap("≈126 m · 150 cm · galvaniz tel örgü · beton direk · 4 m kapı", [
        ("Montajlı tel örgü: 122 m × 290–450 TL", "≈ 35.400–54.900 TL"),
        ("4 m çift kanat arazi kapısı", "≈ 4.500–8.500 TL"),
        ("Üstte 2 sıra dikenli tel (opsiyonel)", "≈ 2.500–5.000 TL"),
       ], "≈ 40.000–68.000 TL")
    + "<p>Rakamlar piyasa ortalamasıyla yapılmış kaba bir hesaptır; arsanızın net fiyatını yerinde ölçüyle veriyoruz.</p>", "ornek"),
  ],
  "sss": [
   ("1 dönüm arsa çevirmek kaç TL?", "Ekim 2026'da Ankara'da kapı dahil tel örgü ile yaklaşık 35.000–65.000 TL; çit tipi, yükseklik ve araziye göre değişiyor."),
   ("Tarla çevirmenin en ekonomik yolu nedir?", "Dikenli tel. Ama küçük hayvanların geçmemesi gerekiyorsa tel örgü gerekir."),
   ("Arsa çevirme fiyatına kapı dahil mi?", "Tekliflere göre değişiyor; 4 m arazi kapısı çoğu zaman ayrı kalem olarak yazılıyor. Mutlaka sorun."),
  ],
 },
 "cesit": {
  "title": "Ankara Arsa ve Tarla Çevirme Çeşitleri: Hangi Çit Nereye?",
  "desc": "Arsa ve tarla çevirme çeşitleri: dikenli tel, galvaniz ve PVC tel örgü, panel çit, karma çözümler. Arazi tipine göre doğru çit seçimi.",
  "h1": "Arsa ve Tarla Çevirme Çeşitleri",
  "gorsel": "arsa-cevirme",
  "ust": "Dikenli tel mi, tel örgü mü, panel mi? Arazinizi hangi çitle çevirmeniz gerektiğini, artı ve eksileriyle anlattık.",
  "giris": [(None, "<p>Arazi çevirmede beş yaygın çözüm var. Doğru seçim; bütçeye, amaca ve arazinin görünür olup olmamasına bağlı.</p>")],
  "cesitler": [
   ("dikenli", "Dikenli tel ile çevirme", "<p>Direkler arasında 3–5 sıra [[ankara-dikenli-tel|dikenli tel]]. En ekonomik çözüm; tarla ve mera "
    "için ideal. Küçük hayvanları durdurmaz, içerisi görünür.</p>", ["En ekonomik", "Tarla · mera"]),
   ("galvaniz-orgu", "Galvaniz tel örgü ile çevirme", "<p>Beton direkli galvaniz [[ankara-tel-orgu|tel örgü]], üstte 1–2 sıra dikenli tel. Arsa "
    "çevirmenin en yaygın yolu; fiyat ve dayanım dengesi iyi.</p>", ["En yaygın", "Arsa"]),
   ("pvc-orgu", "PVC kaplı tel örgü ile çevirme", "<p>Bağ evi ve hobi bahçeleri için daha şık bir tel örgü. Yeşil kaplama bahçede kaybolur.</p>",
    ["Bağ-bahçe", "Şık"]),
   ("panel", "Panel çit ile çevirme", "<p>[[ankara-orgu-panel-cit|Panel çit]] düzgün ve rijit bir sınır verir; yol cephesi ve görünür "
    "alanlar için. Büyük arazide tamamını panelle çevirmek pahalıya gelir.</p>", ["Görünür cephe", "Rijit"]),
   ("karma", "Karma çözüm", "<p>Yol cephesi panel, yanlar ve arka tel örgü; köşelerde dikenli tel. Bütçeyi dengelerken görünen tarafı "
    "düzgün tutmanın en mantıklı yolu.</p>", ["Bütçe dengesi"]),
  ],
  "tablo": [
   ["Çözüm", "Maliyet", "Görünüm", "Küçük hayvan", "Uygun arazi"],
   ["Dikenli tel", "Düşük", "Açık", "Durdurmaz", "Tarla, mera"],
   ["Galvaniz tel örgü", "Orta", "Gri", "Durdurur", "Arsa"],
   ["PVC tel örgü", "Orta", "Yeşil", "Durdurur", "Bağ-bahçe"],
   ["Panel çit", "Yüksek", "Düzgün", "Durdurur", "Yol cephesi"],
   ["Karma", "Orta", "Önü düzgün", "Durdurur", "Her tip"],
  ],
  "govde": [
   ("Arazime hangisi uygun?", "<p>Büyükbaş mera ise dikenli tel; boş arsa ise galvaniz tel örgü; bağ evi ise PVC kaplı tel ya da panel; yol "
    "kenarındaki görünür arsa ise karma çözüm. Kararsız kalırsanız arazinin konumunu ve birkaç fotoğrafını gönderin, birlikte bakalım.</p>"
    + kutu("tavsiye", "Kapıyı unutmayın :) Arazi çevirmede en çok yapılan hata kapıyı sonradan düşünmek. Araç kapısının yerini ve "
           "genişliğini baştan planlayın; bkz. [[ankara-cit-kapisi|çit kapısı]]."), "secim"),
  ],
  "sss": [
   ("Arsa çevirmede en çok hangi çit kullanılıyor?", "Beton direkli galvaniz tel örgü ve üstte 1–2 sıra dikenli tel."),
   ("Tarla için tel örgü mü dikenli tel mi?", "Büyük tarla ve merada dikenli tel daha ekonomik; küçük hayvan söz konusuysa tel örgü gerekir."),
   ("Panel çit arazide kullanılır mı?", "Kullanılır ama büyük arazide maliyet yüksek olur; genellikle yalnız yol cephesinde tercih ediliyor."),
  ],
 },
}
