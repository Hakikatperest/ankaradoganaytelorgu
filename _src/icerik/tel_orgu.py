from ._ortak import kutu, liste, hesap

K = {
 "slug": "ankara-tel-orgu", "ad": "Tel Örgü", "baslik": "Ankara Tel Örgü", "ikon": "orgu",
 "kisa": "Galvaniz ya da PVC kaplı örgü tel; beton ya da demir direkle, gerdirilmiş halde montaj.",
 "gorsel": "beton-direk-ve-tel-orgu", "gorsel2": "tel-orgu-cesidi",
 "kat": {
  "title": "Ankara Tel Örgü - Fiyat, Çeşit ve Montaj | Doğanay Tel Örgü",
  "desc": "Ankara tel örgü: galvaniz ve PVC kaplı örgü tel, beton/demir direk, montaj. Fiyatlar, çeşitler, kullanım alanları ve sipariş hattı tek sayfada.",
  "h1": "Ankara Tel Örgü",
  "ust": "Bahçe, arsa, depo, fabrika, site çevresi… Ankara'da bir yeri çevirmenin en yaygın ve en ekonomik yolu hâlâ tel örgü. "
         "Biz Gölbaşı'ndan Ankara'nın her yerine tel örgü çekiyoruz.",
  "govde": [
   ("Tel örgü nedir?", """
<p>Tel örgü; galvaniz ya da PVC kaplı çelik telin baklava (eşkenar dörtgen) gözler oluşturacak şekilde birbirine örülmesiyle
üretilen, rulo (top) halinde satılan çit telidir. Sahada direklerin arasına gerdirilerek bağlanır. Avrupa'da bu ürünün adı
<em>chain link fencing</em>, standardı da EN 10223-6.</p>
<p>Piyasada aynı ürün için "kafes tel örgü", "bahçe teli", "örgü tel" gibi farklı adlar duyacaksınız. Hepsi aşağı yukarı
aynı şeyi anlatıyor :) Kaynaklı (puntalı) hasır teli ise [[ankara-kafes-tel|kafes tel sayfasında]] ayrıca anlattık, onu
karıştırmayın.</p>""", "tel-orgu-nedir"),
   ("Tel örgü çit nasıl kurulur?", """
<p>Bir tel örgü çitin ömrünü telden çok <strong>direk, gergi ve montaj</strong> belirler. Biz şu sırayla çalışıyoruz:</p>
<ol>
<li><strong>Hat ve kot:</strong> Köşe noktalarına kazık çakıp ip çekiyoruz. Eğimli arazide hattı kademelere bölüyoruz.</li>
<li><strong>Direk:</strong> Beton ya da demir direkler genellikle 2,5–3 metre arayla dikilir, dibi betonlanır. Köşe ve uç
direklerine payanda (destek) konur; gerilimi en çok onlar taşır.</li>
<li><strong>Gergi telleri:</strong> Alt, orta ve üst olmak üzere gergi telleri çekilir.</li>
<li><strong>Örgü tel:</strong> Rulo açılır, gerdirilir ve gergi tellerine bağlanır. Ortası göbek yapmaz.</li>
<li><strong>Üst ekler:</strong> İstenirse direk başlarına kol takılıp [[ankara-dikenli-tel|dikenli tel]] ya da
[[ankara-jiletli-tel|jiletli tel]] eklenir.</li>
</ol>""" + kutu("ipucu", "Ankara'nın kışı serttir; zemin donar, çözülür. Direğin dibini sığ betonlarsanız birkaç kış sonra direkler "
               "yatmaya başlar. Direk temelini kısa kesmiyoruz, bunu baştan söyleyelim.."), "nasil-kurulur"),
   ("Galvaniz mi, PVC kaplı mı?", """
<p>Kısaca: <strong>arsa, tarla, depo</strong> gibi görüntünün çok önemli olmadığı yerlerde galvaniz tel ekonomik ve yeterli.
<strong>Bahçe, villa, site</strong> gibi yerlerde yeşil ya da antrasit PVC kaplı tel çok daha temiz duruyor. Detaylı
karşılaştırmayı [[ankara-tel-orgu-cesitleri|tel örgü çeşitleri]] sayfasında tablo halinde verdik.</p>"""
    + kutu("tavsiye", "Fiyat sorarken sadece \"metresi kaç\" demeyin; tel kalınlığını da sorun. Aynı top, 2 mm ile 3 mm arasında "
           "neredeyse iki katı fiyat farkı yapıyor. Ucuz teklif çoğu zaman ince telden çıkıyor :)"), "galvaniz-pvc"),
   ("Fiyatı ne belirler?", """
<p>Tel kalınlığı, göz aralığı, yükseklik, direk tipi (beton/demir), toplam metraj, zemin (toprak, taşlık, beton) ve kapı sayısı.
Ekim 2026 piyasa rakamlarını, Ankara için örnek bir maliyet hesabını ve ABD, İngiltere, Almanya fiyatlarıyla karşılaştırmayı
[[ankara-tel-orgu-fiyatlari|Ankara tel örgü fiyatları]] sayfasında bulabilirsiniz.</p>""", "fiyat"),
  ],
  "kullanim_giris": "Tel örgüyü nerede kullanıyoruz? Kısa cevap: sınırı belli olsun, içerisi korunsun istenen hemen her yerde.",
  "kullanim": [
   ("Bahçe ve müstakil ev", "PVC kaplı yeşil ya da antrasit tel; 120–150 cm yükseklik çoğu bahçeye yetiyor."),
   ("Arsa ve tarla", "Galvaniz tel, beton direk; üstüne bir iki sıra dikenli tel. Bkz. [[ankara-arsa-tarla-cevirme|arsa ve tarla çevirme]]."),
   ("Fabrika, depo, sanayi parseli", "Daha kalın tel, 200 cm ve üstü yükseklik, üstte jiletli ya da dikenli tel."),
   ("Site ve apartman bahçesi", "Ortak alanda yapılacağı için önce yönetimle konuşulması gerekir; görünüm için PVC kaplı tel."),
   ("Halı saha ve okul bahçesi", "Yüksek tel ve sık göz; ayrıntısı [[ankara-saha-teli|saha teli]] sayfasında."),
   ("Hayvan barınağı, kümes, ağıl", "Hayvanın türüne göre göz aralığı seçilir; küçük hayvan için [[ankara-kafes-tel|kafes tel]] daha uygun olabilir."),
  ],
  "siparis": [
   "<strong>Yer:</strong> İşin yapılacağı ilçe ve mahalle (Gölbaşı, Çankaya, Etimesgut…).",
   "<strong>Metraj:</strong> Çevrilecek hattın yaklaşık uzunluğu (metre). Bilmiyorsanız tapudaki ölçüler de iş görür.",
   "<strong>Yükseklik:</strong> 100, 150, 200 cm gibi.",
   "<strong>Tel tipi:</strong> Galvaniz mi PVC kaplı mı? Emin değilseniz birlikte seçeriz.",
   "<strong>Ekler:</strong> Kapı, dikenli tel, jiletli tel ister misiniz?",
  ],
  "sss": [
   ("Tel örgünün metresi kaç TL?", "Ekim 2026 itibarıyla piyasada montajlı tel örgü çit yaklaşık 195–500 TL/metre aralığında. Kalınlık, yükseklik ve direğe göre değişir; ayrıntı [[ankara-tel-orgu-fiyatlari|fiyat sayfasında]]."),
   ("Tel örgü kaç yıl dayanır?", "Telin galvaniz kaplamasına, PVC kaplı olup olmamasına ve montaj kalitesine bağlı. Gerdirilmiş, sağlam direkli bir çit uzun yıllar sorunsuz durur; gevşek bağlanmış çit birkaç kışta sarkar."),
   ("Tel örgü için direk aralığı kaç metre olmalı?", "Genellikle 2,5–3 metre. Rüzgâr alan, yüksek ya da eğimli hatlarda aralık daraltılır."),
   ("Sadece tel örgü malzemesi satıyor musunuz?", "Malzemeli ya da yalnız işçilik çalışabiliyoruz. Ne kadar malzeme gerektiğini metrajınıza göre biz hesaplıyoruz."),
  ],
 },
 "fiyat": {
  "title": "Ankara Tel Örgü Fiyatları 2026 - Metre ve Top Fiyatı",
  "desc": "Ankara tel örgü fiyatları Ekim 2026: galvaniz ve PVC kaplı top/m² fiyatı, beton ve demir direk, montajlı metre fiyatı; ABD, İngiltere, Almanya ile karşılaştırma.",
  "h1": "Ankara Tel Örgü Fiyatları (Ekim 2026)",
  "ust": "Tel örgünün topu, metrekaresi, direği ve montajlı metre fiyatı… Piyasayı taradık, kaynaklarıyla tabloya döktük. "
         "Üstüne ABD, İngiltere ve Almanya'da aynı işin kaça yapıldığını da ekledik :)",
  "ozet": [
   ("Montajlı tel örgü çit", "195–500 TL/m"),
   ("Galvaniz top (150 cm × 20 m)", "1.500–3.500 TL + KDV"),
   ("PVC kaplı örgü tel", "35–90 TL/m²"),
   ("Beton direk", "140–500 TL/adet"),
   ("Demir (boru) direk", "200–900 TL/adet"),
  ],
  "giris": [
   (None, """<p>Önce şunu netleştirelim: Bu sayfadaki rakamlar <strong>bizim teklifimiz değil</strong>, Ekim 2026'da Türkiye ve
Ankara piyasasından topladığımız fiyatlar. Amacımız siz telefonu açmadan önce kafanızda bir rakam olsun. Kendi işinizin net
fiyatı için [[siparis-hatti|sipariş hattımızı]] arayın.</p>"""
    + kutu("onemli", "Tel örgü ilanlarının çoğu <strong>KDV hariç</strong> yazılıyor. Karşılaştırma yaparken %20 KDV eklemeyi unutmayın; "
           "bir de nakliye ve montajın dahil olup olmadığını sorun.")),
  ],
  "tr_giris": "<p>Galvaniz örgü tel genelde <strong>150 cm × 20 m</strong> top (rulo) halinde satılıyor; bu da 30 m² eder. "
              "Aşağıdaki fiyatlar ilan tarihinde görülen değerlerdir.</p>",
  "tr": [
   ("Galvaniz örgü tel", "2 mm · 6×6 göz · 150 cm × 20 m", "1.500 TL + KDV", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Galvaniz örgü tel", "2,5 mm · 6×6 göz · 150 cm × 20 m", "2.400 TL + KDV", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Galvaniz örgü tel", "3 mm · 5×5 göz · 150 cm × 20 m", "3.500 TL + KDV", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Galvaniz örgü tel (m²)", "2 mm · 60×60 / 50×50 göz", "40–48 TL/m²", "Ankara imalatçı listesi, Eki 2026", ""),
   ("Galvaniz örgü tel (m²)", "3 mm · 60×60 / 50×50 göz", "81–92 TL/m²", "Ankara imalatçı listesi, Eki 2026", ""),
   ("PVC kaplı örgü tel", "3–4 mm · 80×80 ile 50×50 göz", "35–57 TL/m²", "Ankara imalatçı listesi, Eki 2026", ""),
   ("PVC kaplı örgü tel", "standart / ağır hizmet", "50–140 TL/m", "Türkiye üretici listesi, 2026", ""),
   ("Beton çit direği", "2 m", "140–500 TL/adet", "Ankara ve Türkiye satıcıları, Eki 2026", ""),
   ("Demir / boru direk", "—", "200–900 TL/adet", "Ankara ve Türkiye satıcıları, Eki 2026", ""),
   ("Montaj işçiliği", "yalnız işçilik", "70–350 TL/m", "Ankara satıcı beyanları, Eki 2026", ""),
   ("Montajlı tel örgü çit", "demir direkli, 150 cm", "240–350 TL/m", "Ankara satıcı beyanı, Eki 2026", ""),
   ("Betonarme direkli kafes tel çit", "2,63 m · kamu birim fiyatı (poz 43.665.1082)", "3.034,18 TL/m", "İller Bankası birim fiyatı, Ara 2025", "https://www.birimfiyat.com/"),
  ],
  "tr_son": """<p>Gerçek iş örneklerine bakmak isterseniz: Ağustos–Ekim 2026'da hizmet platformu Armut'a Ankara'dan gelen tel örgü
taleplerinde <strong>Gölbaşı'nda 100 metre için 34.500–65.000 TL</strong>, Mamak'ta 60 metre için 30.000–43.265 TL teklif
verilmiş (<a href="https://armut.com/fiyatlari/ankara-tel-orgu-cit_28387_6" target="_blank" rel="noopener nofollow">kaynak</a>).
Aralığın bu kadar geniş olması tesadüf değil; bir sonraki bölümde nedenini anlatıyoruz.</p>"""
   + kutu("not", "Kamu birim fiyatı (3.034 TL/m) özel piyasadan çok yüksek görünüyor; çünkü 2,63 m betonarme direk, kazı, beton, "
          "nakliye ve müteahhit kârı gibi kalemlerin hepsi pozun içinde. Bu rakamı ihale işleri için referans alın, bahçeniz için değil :)"),
  "yd_giris": "<p>Aynı işi yurtdışında yaptırsaydınız? ABD, İngiltere ve Almanya'daki yapı marketlerinin ve maliyet rehberlerinin "
              "Ekim 2026'daki fiyatları:</p>",
  "yd": [
   ("ABD", "YARDGARD galvaniz örgü tel", "1,22 × 15,24 m · ~3 mm", 112.82, "USD", "rulo", "Home Depot", "https://www.homedepot.com/p/202024333"),
   ("ABD", "Montajlı chain-link çit", "metre karşılığı", (32.8, 65.6), "USD", "metre", "Angi maliyet rehberi", "https://www.angi.com/articles/how-much-does-installing-chain-link-fence-cost.htm"),
   ("İngiltere", "Galvaniz örgü tel", "1,2 × 25 m · 3 mm · 50 mm göz", 242.88, "GBP", "rulo, KDV dahil", "F.H. Brundle", "https://www.fhbrundle.co.uk/"),
   ("İngiltere", "Montajlı güvenlik çiti", "1,8–2,4 m", (35, 70), "GBP", "metre", "BestBuilders (Ağu 2026)", "https://bestbuilders.co.uk/costs/security-fencing-cost-uk"),
   ("Almanya", "PVC yeşil örgü tel", "150 cm × 25 m", 118, "EUR", "rulo", "Kaufland.de", "https://www.kaufland.de/"),
  ],
  "yd_yorum": """<p>Rakamları yan yana koyunca tablo net: ABD'de 15 metrelik bir galvaniz rulonun fiyatı, Türkiye'de 20 metrelik
2,5 mm topun iki katından fazla. Asıl fark ise <strong>işçilikte</strong>: ABD'de montajlı tel örgü çitin metresi
1.600–3.200 TL'ye, İngiltere'de 2.300–4.600 TL'ye denk geliyor. Türkiye'de montajlı metre fiyatı bunun yaklaşık
onda biri ile beşte biri arasında.</p>"""
   + kutu("not", "Bu fark Türkiye'deki tel örgünün kalitesiz olduğu anlamına gelmiyor; farkın büyük kısmı işçilik ücretlerinden "
          "geliyor. Ama ucuz işçiliğin de bir bedeli var: Aceleyle, gergi teli çekmeden yapılan montaj ilk kışta kendini belli ediyor."),
  "govde": [
   ("Tel örgü fiyatını ne değiştirir?", liste(
     "<strong>Tel kalınlığı:</strong> En büyük etken bu. Aynı göz ve top boyunda 2 mm'den 3 mm'ye geçince fiyat 2–2,3 katına çıkıyor.",
     "<strong>Göz aralığı:</strong> Göz küçüldükçe metrekareye giren tel artar; 80×80'den 50×50'ye geçince m² fiyatı %50'nin üzerinde artabiliyor.",
     "<strong>Kaplama:</strong> PVC kaplı tel galvanize göre daha pahalı ama bahçede çok daha temiz durur.",
     "<strong>Direk:</strong> Beton direk ekonomik; boyalı ya da galvaniz demir boru direk daha pahalı ama daha ince ve şık.",
     "<strong>Zemin:</strong> Taşlık, kaya ya da beton zeminde direk yeri açmak işçiliği artırır.",
     "<strong>Ekler:</strong> Kapı, dikenli tel kolu, jiletli tel her biri ayrı kalem.",
     "<strong>Çelik fiyatları:</strong> Dikenli tel gibi çelik ürünlerde son 6 ayda %17'yi aşan fiyat artışı görüldü; teklifler kısa süre geçerli oluyor."),
    "fiyat-etkenleri"),
   ("Örnek hesap: 100 metre bahçe çiti", "<p>Gölbaşı'nda 100 metrelik, 150 cm yüksekliğinde galvaniz tel örgü, beton direkli bir çit için "
    "kabaca bir malzeme hesabı yapalım. (Piyasa ortalamalarıyla, KDV hariç, tahminidir.)</p>"
    + hesap("100 m · 150 cm · galvaniz 2,5 mm · beton direk", [
        ("Örgü tel: 5 top (150 cm × 20 m)", "≈ 12.000 TL"),
        ("Beton direk: ~38 adet (2,7 m aralık + köşe payı)", "≈ 7.600 TL"),
        ("Gergi teli, bağlama teli, payanda", "≈ 1.500 TL"),
        ("Direk betonu ve işçilik", "metraja ve zemine göre"),
       ], "Malzeme ≈ 21.000 TL + işçilik")
    + "<p>Bu tablo size bir fikir versin diye. Zemin taşlıksa, köşe sayısı fazlaysa ya da kapı eklenecekse rakam değişir. "
      "Net fiyatı yerinde ölçüyle veriyoruz.</p>", "ornek-hesap"),
   ("Tel örgü alırken nelere dikkat etmeli?", liste(
     "Teklifte tel kalınlığı (mm), göz aralığı ve top ölçüsü yazılı olsun.",
     "KDV, nakliye ve montajın dahil olup olmadığını sorun.",
     "Direk aralığını ve direk temelinin nasıl yapılacağını sorun.",
     "Gergi telinin kaç sıra çekileceğini sorun; \"gerek yok\" diyen ustadan uzak durun :)")
    + kutu("tavsiye", "Farklı firmalardan teklif alıyorsanız aynı ölçüyle karşılaştırın: 2 mm telle 3 mm teli, beton direkle boru direği "
           "kıyaslamak elmayla armudu kıyaslamak gibi.."), "dikkat"),
  ],
  "sss": [
   ("Ankara'da tel örgünün metresi ne kadar?", "Ekim 2026 piyasasında montajlı tel örgü çit yaklaşık 195–500 TL/metre. Tel kalınlığı, yükseklik ve direk tipine göre değişiyor."),
   ("1 top tel örgü kaç metre?", "Yaygın top ölçüsü 150 cm yükseklik × 20 metre uzunluk, yani 30 m². Farklı yükseklik ve boyda toplar da üretiliyor."),
   ("Tel örgü fiyatlarına KDV dahil mi?", "Satıcıların çoğu KDV hariç fiyat ilan ediyor. Teklif alırken mutlaka sorun."),
   ("Yurtdışında tel örgü daha mı pahalı?", "Evet. ABD'de montajlı chain-link çitin metresi yaklaşık 1.600–3.200 TL'ye, İngiltere'de 2.300–4.600 TL'ye denk geliyor. Farkın büyük kısmı işçilikten."),
  ],
 },
 "cesit": {
  "title": "Ankara Tel Örgü Çeşitleri: Galvaniz, PVC, Göz ve Kalınlık",
  "desc": "Tel örgü çeşitleri: galvaniz ve PVC kaplı örgü tel, göz aralıkları, tel kalınlıkları, beton ve demir direk seçenekleri. Hangisi nereye uygun?",
  "h1": "Ankara Tel Örgü Çeşitleri",
  "gorsel": "tel-orgu-cesidi",
  "ust": "Galvaniz mi, PVC kaplı mı? 2 mm mi, 3 mm mi? Beton direk mi, boru mu? Tel örgü seçerken kafanızı karıştıran ne varsa tek tek anlattık.",
  "giris": [
   (None, "<p>Tel örgü dediğimiz şey aslında birkaç kararın toplamı: <strong>kaplama, tel kalınlığı, göz aralığı, yükseklik ve "
    "direk</strong>. Bu kararları doğru verirseniz çit hem bütçenize uyar hem de yıllarca dik durur.</p>"),
  ],
  "cesitler": [
   ("galvaniz", "Galvaniz tel örgü", "<p>Çelik telin üzeri çinkoyla kaplanır; çinko teli paslanmaya karşı korur. Gri, mat görünümlüdür. "
    "Arsa, tarla, depo, şantiye ve sanayi parselleri için en çok tercih edilen ve en ekonomik seçenek.</p>"
    + kutu("ipucu", "Galvaniz kaplamanın kalınlığı telin ömrünü belirler; kaplama sınıfları EN 10244-2 standardında tanımlı. "
           "Kaplama değerini satıcıdan, üreticinin belgesinden isteyebilirsiniz."),
    ["Ekonomik", "Arsa · tarla · sanayi", "Gri görünüm"]),
   ("pvc-kapli", "PVC kaplı tel örgü", "<p>Galvaniz telin üzeri bir de PVC (plastik) ile kaplanır. Genelde yeşil ya da antrasit olur. "
    "Çift katlı koruma sayesinde dış etkilere dayanıklıdır, en önemlisi de bahçede çok daha şık durur.</p>",
    ["Bahçe · villa · site", "Yeşil / antrasit", "Daha şık"]),
   ("kalinlik", "Tel kalınlığına göre: 2 mm – 3 mm", "<p>Piyasada en çok 2 mm, 2,2 mm, 2,5 mm ve 3 mm tel görürsünüz. 2 mm "
    "sınır belirlemek için yeterli; 2,5 mm genel kullanım için dengeli; 3 mm ise fabrika, saha ve zorlanacak hatlar için. "
    "PVC kaplı tellerde ölçü kaplamayla birlikte verildiği için 3–4 mm yazar, karşılaştırırken buna dikkat edin.</p>",
    ["2 mm: sınır", "2,5 mm: genel", "3 mm: ağır kullanım"]),
   ("goz", "Göz aralığına göre: 4×4, 5×5, 6×6 cm", "<p>Göz ne kadar küçükse çit o kadar sık ve dayanıklı olur, ama metrekareye "
    "giren tel de artar. Küçük hayvanların geçmemesi gereken yerde küçük göz; sadece sınır için 6×6 yeterli.</p>",
    ["Küçük göz: sık", "6×6: ekonomik"]),
   ("direk", "Direk seçenekleri: beton ve demir", "<p><strong>Beton direk</strong> ekonomik ve sağlamdır; arazide, tarlada çok "
    "kullanılır. <strong>Demir (boru) direk</strong> daha ince ve şık durur, boyalı ya da galvaniz olabilir; bahçe ve sitelerde "
    "tercih edilir. Direk başına kol takılırsa üstüne [[ankara-dikenli-tel|dikenli tel]] çekilir.</p>",
    ["Beton: ekonomik", "Demir: şık"]),
  ],
  "tablo": [
   ["Çeşit", "Görünüm", "Nereye uygun", "Bütçe"],
   ["Galvaniz 2 mm", "Gri", "Arsa, tarla sınırı", "Düşük"],
   ["Galvaniz 2,5–3 mm", "Gri", "Depo, fabrika, şantiye", "Orta"],
   ["PVC kaplı", "Yeşil / antrasit", "Bahçe, villa, site", "Orta"],
   ["Beton direk", "Kalın, beyaz-gri", "Arazi, tarla", "Düşük"],
   ["Demir (boru) direk", "İnce, boyalı", "Bahçe, site", "Orta-yüksek"],
  ],
  "govde": [
   ("Hangi tel örgüyü seçmeliyim?", "<p>Kısaca özetleyelim: Arsanızın sınırını çizecekseniz 2–2,5 mm galvaniz ve beton direk yeter. "
    "Evin bahçesiyse PVC kaplı tel ve boru direk çok daha yakışır. Fabrika ya da depoysa kalın tel, yüksek çit ve üstte "
    "[[ankara-jiletli-tel|jiletli tel]] düşünün. Daha düzgün ve rijit bir görünüm istiyorsanız tel örgü yerine "
    "[[ankara-orgu-panel-cit|panel çite]] bakın.</p>"
    + kutu("tavsiye", "Seçimde kararsız kaldıysanız alanın birkaç fotoğrafını WhatsApp'tan atın; hangi çeşidin uygun olduğunu "
           "fotoğrafa bakarak söyleyelim :)"), "secim"),
  ],
  "sss": [
   ("Tel örgü çeşitleri nelerdir?", "Kaplamaya göre galvaniz ve PVC kaplı; tel kalınlığına göre 2–3 mm; göz aralığına göre 4×4, 5×5, 6×6 cm; direğe göre beton ve demir."),
   ("PVC kaplı tel örgü daha mı dayanıklı?", "Galvaniz kaplamanın üzerine PVC eklendiği için dış etkilere karşı ek koruma sağlar. Asıl fark görünümde; bahçede çok daha temiz durur."),
   ("Bahçe için hangi tel örgü?", "Çoğu bahçe için 120–150 cm yükseklikte PVC kaplı yeşil ya da antrasit tel ve boru direk iyi bir seçim."),
  ],
 },
}
