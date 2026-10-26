"""20 ilçenin kaynaklı verisi + ilçe × ürün için ayrı yazılmış paragraflar (2026-10-26 araştırması).

Kaynaklar: ATO "Rakamlarla Ankara" Tem 2026 (TÜİK ADNKS 2025 nüfus, OSBÜK OSB listesi), Wikipedia "Ankara'nın ilçeleri"
(HGM yüzölçümü, mahalle sayısı), ilçe maddeleri (rakım), OSRM/OpenStreetMap (Gölbaşı Kaymakamlığı'ndan karayolu mesafesi).
⛔ Nüfusu Wikipedia listesinden alma (Gölbaşı↔Pursaklar vb. yer değiştirmiş). Akyurt'ta OSB YOK. Temelli Polatlı'ya bağlı.
"Yakacık" ilçesi belirsiz — kullanma. Fotoğraflar ilçeye ait değil.
Paragraflarda [[slug|yazı]] iç link işaretidir (build.py çözer).
"""

ATO = ("ATO Rakamlarla Ankara 2026 (TÜİK ADNKS 2025)",
       "https://www.atonet.org.tr/Uploads/Birimler/Internet/Flash%20Tan%C4%B1t%C4%B1m%20Alan%C4%B1/2026-07-03-RakamlarlaAnkara/2026-07-03-Rakamlarla-Ankara.pdf")
WIKI = ("Ankara'nın ilçeleri (HGM yüzölçümü)", "https://tr.wikipedia.org/wiki/Ankara%27n%C4%B1n_il%C3%A7eleri")
OSRM = ("OpenStreetMap / OSRM mesafe hesabı", "https://router.project-osrm.org")


def V(ad, slug, de, km, komsu, nufus, alan, mahalle, rakim, sanayi, ek, kaynak, beton, jilet, orgu):
    veri = [("Nüfus (2025, TÜİK)", nufus), ("Yüzölçümü", alan), ("Mahalle sayısı", mahalle), ("Rakım", rakim),
            ("Sanayi", sanayi), ("Gölbaşı'ndaki atölyemize uzaklık", f"yaklaşık {km} (karayolu)")] + ek
    veri = [(a, b) for a, b in veri if b != "—"]
    return {"ad": ad, "slug": slug, "de": de, "km": km, "komsu": komsu, "veri": veri,
            "kaynak": [ATO, WIKI, OSRM] + kaynak, "beton": beton, "jilet": jilet, "orgu": orgu}


def P(giris, satan, uygulama, fiyat):
    return {"giris": giris, "satan": satan, "uygulama": uygulama, "fiyat": fiyat}


VERI = [
 V("Gölbaşı", "golbasi", "Gölbaşı'nda", "birkaç km", ["cankaya", "mamak", "bala", "haymana", "etimesgut"],
   "168.881", "1.364 km²", "54", "977 m", "OSB yok (OSBÜK)",
   [("Özel durum", "İlçe 1990'dan beri Özel Çevre Koruma Bölgesi; Mogan ve Eymir gölleri ilçe sınırında.")],
   [("Gölbaşı (Vikipedi)", "https://tr.wikipedia.org/wiki/G%C3%B6lba%C5%9F%C4%B1,_Ankara"),
    ("ÇŞİDB Gölbaşı plan raporu, May 2026", "https://webdosya.csb.gov.tr/v2/ankara/2026/05/Plan-A-klama-Raporu-20260506144057.pdf")],
   P("Atölyemiz zaten Gölbaşı'nda, Gaziosmanpaşa'da :) Gölbaşı'nda beton direk arıyorsanız bundan yakını yok; direği aynı gün "
     "getirip istenirse aynı gün dikiyoruz.",
     "<p>Gölbaşı'nda beton direk satan yer olarak en büyük avantajımız mesafe: sipariş verdiğiniz direk İncek'e, Taşpınar'a ya da "
     "Hacılar'a çoğu zaman aynı gün ulaşıyor. Nakliyeyi ayrıca hesaplamaya gerek kalmıyor.</p>",
     "<p>Gölbaşı geniş bir ilçe: 1.364 km²'lik alanın bir kısmı göl çevresi ve yerleşim, büyük kısmı tarla ve mera. Göl kıyısına yakın, "
     "nemli ve killi yerlerde direk dibini daha geniş betonluyoruz; tarlada ise 2,4 m düz direk ve köşelerde payanda yeterli oluyor.</p>"
     "<p>İlçe Özel Çevre Koruma Bölgesi'nde olduğu için kalıcı duvar ya da beton hatıl yapmadan önce plan durumunu sormanızı öneririz; "
     "beton direkli tel örgü çoğu zaman en sade çözüm.</p>",
     "<p>Gölbaşı içi siparişlerde direk fiyatına uzak ilçelerdeki gibi nakliye payı binmiyor. Ekim 2026 piyasasında 2 m düz direk "
     "132–265 TL, 2,4 m direk 190–275 TL bandında; köşe sayınızı söyleyin, payandayla birlikte net adet çıkaralım.</p>"),
   P("Gölbaşı'nda jiletli tel için uzağa gitmeyin; atölyemiz ilçenin içinde. Duvar üstü, panel ya da tel örgü üstü jiletli teli "
     "ölçüp getiriyor, takıyoruz.",
     "<p>Gölbaşı'nda jiletli tel satan yer olarak keşfe hızlı gelebiliyoruz; özellikle depo, şantiye ve tarım deposu sahipleri için bu "
     "önemli, çünkü güvenlik işi beklemeye gelmiyor.</p>",
     "<p>Gölbaşı'nda jiletli tele en çok şantiyelerde ve şehir dışındaki depo ve ahırlarda ihtiyaç duyuluyor. Yerleşim içindeki villalarda "
     "ise önce site yönetimi ve belediyeyle konuşmanızı öneriyoruz; çoğu zaman [[ankara-dikenli-tel|dikenli tel]] ya da düzlemsel jiletli "
     "tel komşuluk açısından daha uygun oluyor.</p>",
     "<p>Gölbaşı içinde nakliye payı olmadığı için fiyat doğrudan malzeme ve montajdan oluşuyor: galvaniz helezon jiletli tel Ekim 2026'da "
     "çapına göre 45–110 TL/metre. Y kollu direk ve gergi teli gerekiyorsa ayrıca hesaplanır.</p>"),
   P("Gölbaşı tel örgü işlerimizin merkezi :) Bahçe, arsa, tarla ya da site çevresi; Gölbaşı'nda tel örgüyü direğinden gergisine "
     "kadar biz kuruyoruz.",
     "<p>Gölbaşı'nda tel örgü satan yer arıyorsanız atölyemize uğrayabilir, telin kalınlığını ve gözünü elinizle görebilirsiniz. "
     "Adresimiz Gaziosmanpaşa, 377. Sokak.</p>",
     "<p>İncek ve Taşpınar gibi villa ve müstakil ev yoğun bölgelerde PVC kaplı yeşil ya da antrasit tel ve boru direk tercih ediliyor; "
     "Mogan'ın güneyindeki tarlalarda ise galvaniz tel ve beton direk. İlçe ÖÇK bölgesinde olduğu için kalıcı duvar yerine tel örgü "
     "çoğu zaman en pratik sınır.</p>",
     "<p>Ekim 2026'da Armut platformuna Gölbaşı'ndan gelen 100 metre, 180 cm tel örgü talebine 34.500–65.000 TL teklif verilmiş. "
     "Biz Gölbaşı'nda olduğumuz için nakliye payı yok; montajlı tel örgü piyasada 195–500 TL/metre.</p>"),
 ),
 V("Çankaya", "cankaya", "Çankaya'da", "19 km", ["golbasi", "mamak", "altindag", "yenimahalle", "etimesgut"],
   "952.198 (Ankara'nın en kalabalık ilçesi)", "483 km²", "124", "1.099 m", "OSB yok (OSBÜK)",
   [("Yerleşim", "Ümitköy ve Çayyolu gibi müstakil ve site yoğun mahalleler Çankaya'da.")],
   [("Çankaya (Vikipedi)", "https://tr.wikipedia.org/wiki/%C3%87ankaya")],
   P("Çankaya'da beton direk, çoğunlukla ilçenin batı ve güneyindeki arsalarda ve inşaat sahalarında lazım oluyor. Gölbaşı'ndan "
     "yaklaşık 19 km; direği getirip dikiyoruz.",
     "<p>Çankaya'da beton direk satan yer olarak sevkiyatı kendi aracımızla yapıyoruz. Şehir içi trafikte büyük kamyon zorlandığı için "
     "orta tonajlı araçla, gerekirse iki seferde getiriyoruz.</p>",
     "<p>Çankaya'nın yerleşik mahallelerinde beton direkten çok boru direk tercih ediliyor; görüntü önemli. Beton direk ise boş arsa, "
     "inşaat sahası ve ilçenin kırsal ucundaki parsellerde mantıklı. Şantiye çevirmede direği sökülüp tekrar kullanılabilecek şekilde dikiyoruz.</p>",
     "<p>Çankaya'ya sevkiyatta mesafe kısa ama şehir içi teslim zamanı uzun sürebiliyor. Direk fiyatı Ekim 2026'da 2 m düz için 132–265 TL; "
     "şantiye için 2,4 m eğik başlı direk 275–300 TL civarında.</p>"),
   P("Çankaya'da jiletli tel en çok inşaat sahalarında ve iş yerlerinin arka cephelerinde soruluyor. Gölbaşı'ndan 19 km; keşfe "
     "kısa sürede geliyoruz.",
     "<p>Çankaya'da jiletli tel satan yer olarak işi ölçerek veriyoruz: kaç metre, hangi çap, duvar mı panel mi. Yerleşim içinde "
     "olduğu için montajı yaya yoluna taşmayacak şekilde, içe yönlendirerek yapıyoruz.</p>",
     "<p>Çankaya, Ankara'nın en kalabalık ilçesi (952 bin); yani komşuluk ve görünüm her şeyden önemli. Konut ve sitelerde jiletli tel "
     "yerine düzlemsel tip ya da [[ankara-orgu-panel-cit|panel çit]] üstü tek sıra daha uygun. Kat malikleri kararı gereken ortak alanlarda "
     "önce yönetimle konuşun.</p>",
     "<p>Çankaya için jiletli tel fiyatı, şehir içi işçilik ve erişim zorluğu (iskele, sepetli araç) nedeniyle montajda değişiyor. Malzeme "
     "Ekim 2026'da 45–110 TL/metre; düzlemsel jiletli tel 45–65 TL/metre.</p>"),
   P("Çankaya'da tel örgü dendiğinde çoğu zaman bahçe, site ve okul çevresi akla geliyor. Gölbaşı'ndan Çankaya'ya 19 km; ölçüyü "
     "yerinde alıp kuruyoruz.",
     "<p>Çankaya'da tel örgü satan yer arayanlara malzemeyi kapıya getiriyor, montajı da yapıyoruz. Site ve apartman işlerinde yönetim "
     "kararı olduktan sonra gün planlıyoruz.</p>",
     "<p>Ümitköy ve Çayyolu gibi müstakil ve site yoğun mahallelerde PVC kaplı tel, boru direk ve istenirse [[ankara-cim-cit|çim çit]] "
     "en çok istenen kombinasyon. İlçenin kırsal parsellerinde ise galvaniz tel ve beton direk.</p>",
     "<p>Çankaya'da tel örgü fiyatını görünüm belirliyor: PVC kaplı tel ve boru direk, galvaniz ve beton direkten pahalı. Montajlı tel örgü "
     "Ekim 2026'da 195–500 TL/metre bandında; çim çit eklenecekse m² başına 270–550 TL daha.</p>"),
 ),
 V("Etimesgut", "etimesgut", "Etimesgut'ta", "31 km", ["yenimahalle", "sincan", "cankaya", "golbasi"],
   "632.458", "273 km²", "38", "853 m", "OSB yok (OSBÜK)",
   [("Zemin", "İlçede killi zemin üzerinde yağmur suyuyla beslenen Göksu Gölü var."),
    ("Yerleşim", "Bağlıca, Yapracık ve Eryaman Etimesgut'ta.")],
   [("Etimesgut (Vikipedi)", "https://tr.wikipedia.org/wiki/Etimesgut")],
   P("Etimesgut'ta beton direk en çok Bağlıca ve Yapracık tarafındaki müstakil ev ve arsa parsellerinde soruluyor. Gölbaşı'ndan "
     "yaklaşık 31 km; getirip dikiyoruz.",
     "<p>Etimesgut'ta beton direk satan yer olarak çevre yolu üzerinden kısa sürede ulaşıyoruz. Direkleri istif halinde değil, dikileceği "
     "hat boyunca bırakıyoruz; taşıma yükü size kalmıyor.</p>",
     "<p>Etimesgut'un bazı kesimleri killi zemin üzerinde. Killi toprak ıslanınca şişer, donunca kabarır; bu da direği zamanla oynatır. "
     "Bu tür zeminde direk çukurunu geniş açıp dibine mıcır seriyor, betonu buna göre döküyoruz.</p>",
     "<p>Etimesgut'ta zemin hazırlığı (mıcır, geniş temel) fiyatı biraz artırabiliyor. Direk malzemesi Ekim 2026'da 2,4 m düz için "
     "190–275 TL, payanda 217–270 TL bandında.</p>"),
   P("Etimesgut'ta jiletli tel en çok depolarda, şantiyelerde ve ilçenin dış kesimlerindeki işletmelerde isteniyor. Gölbaşı'ndan "
     "31 km; ölçüp takıyoruz.",
     "<p>Etimesgut'ta jiletli tel satan yer olarak malzemeyi metrajınıza göre getiriyor, artan rulo bırakmamaya çalışıyoruz. 10 metre "
     "için de 200 metre için de geliyoruz.</p>",
     "<p>Etimesgut hızla büyüyen bir konut ilçesi (632 bin nüfus). Yerleşim içinde jiletli tel yerine [[ankara-orgu-panel-cit|panel çit]] "
     "ve gerekirse düzlemsel jiletli tel öneriyoruz; inşaat sahalarında ise helezon jiletli tel hem hızlı hem caydırıcı.</p>",
     "<p>Etimesgut için jiletli tel fiyatı malzeme ve montajdan oluşuyor; Ekim 2026'da galvaniz helezon 45–110 TL/metre. Paslanmaz "
     "isteyen işletmeler için yaklaşık %30 fark var.</p>"),
   P("Etimesgut'ta tel örgü; bahçe, arsa ve şantiye çevresi için en çok istenen çit. Gölbaşı'ndan 31 km uzaktayız; tel örgüyü "
     "direğiyle birlikte kuruyoruz.",
     "<p>Etimesgut'ta tel örgü satan yer olarak malzemeyi getiriyor, montajı da yapıyoruz. Eryaman ve Bağlıca'daki siparişlerde "
     "teslimi genelde tek seferde tamamlıyoruz.</p>",
     "<p>Bağlıca ve Yapracık'taki müstakil evlerde PVC kaplı tel ve boru direk; boş arsalarda galvaniz tel ve beton direk. Killi zeminde "
     "direk temeline ayrıca özen gösteriyoruz, aksi halde birkaç kışta çit dalgalanıyor.</p>",
     "<p>Etimesgut için montajlı tel örgü Ekim 2026'da 195–500 TL/metre bandında; zemin hazırlığı gereken killi parsellerde biraz artabiliyor.</p>"),
 ),
 V("Yenimahalle", "yenimahalle", "Yenimahalle'de", "22 km", ["cankaya", "altindag", "kecioren", "etimesgut", "sincan", "kahramankazan"],
   "721.531", "219 km²", "57", "—", "OSTİM OSB ve İvedik OSB (ikisi de tam dolu); OSTİM Sanayi Sitesi'nde 3.000 işyeri",
   [],
   [],
   P("Yenimahalle'de beton direk en çok OSTİM ve İvedik çevresindeki işyeri arsalarında ve depolarda kullanılıyor. Gölbaşı'ndan "
     "yaklaşık 22 km; direği getirip dikiyoruz.",
     "<p>Yenimahalle'de beton direk satan yer olarak sanayi bölgesine hafta içi mesai saatlerinde teslim yapıyoruz; OSB içinde araç "
     "trafiği yoğun, teslim saatini önceden ayarlıyoruz.</p>",
     "<p>Yenimahalle, Ankara'nın iki büyük sanayi bölgesini barındırıyor: OSTİM OSB ve İvedik OSB, ikisi de tam dolu. Bu parsellerde "
     "beton direği genelde eğik başlı ya da Y kollu seçip üstüne [[ankara-jiletli-tel|jiletli tel]] ekliyoruz.</p>",
     "<p>Sanayi işlerinde Y kollu ve eğik başlı direk ağırlıkta olduğu için ortalama direk fiyatı yükseliyor. Ekim 2026'da eğik başlı "
     "2,4–3 m direk 275–350 TL; NATO tipi ağır direk 350–600 TL.</p>"),
   P("Yenimahalle jiletli tel denince ilk akla gelen ilçe; OSTİM ve İvedik'teki işletmelerin çoğu çitinin üstünde jiletli tel istiyor. "
     "Gölbaşı'ndan 22 km; ölçüp takıyoruz.",
     "<p>Yenimahalle'de jiletli tel satan yer olarak sanayi müşterilerine faturalı çalışıyor, işi hafta sonu ya da mesai dışına "
     "planlayabiliyoruz; üretim durmasın.</p>",
     "<p>OSTİM Sanayi Sitesi'nde 3.000 işyeri var; parseller birbirine yakın, duvarlar ortak. Bu yüzden jiletli teli içe dönük ve komşu "
     "parsele taşmayacak şekilde takıyoruz. Y kollu direk ortasında helezon tel en yaygın çözüm.</p>",
     "<p>Sanayi işlerinde metraj uzun olduğu için metre başına fiyat düşebiliyor. Ekim 2026'da galvaniz helezon 45–110 TL/metre; "
     "paslanmaz 304 kilosu 195 TL civarında.</p>"),
   P("Yenimahalle'de tel örgü; sanayi parselinden apartman bahçesine kadar geniş bir yelpazede isteniyor. Gölbaşı'ndan 22 km; tel örgüyü "
     "direğiyle kuruyoruz.",
     "<p>Yenimahalle'de tel örgü satan yer olarak hem sanayi hem konut müşterisine hizmet veriyoruz. Sanayi işlerinde faturalı, "
     "konut işlerinde malzemeli ya da yalnız işçilik çalışıyoruz.</p>",
     "<p>OSTİM ve İvedik'te kalın galvaniz tel (2,5–3 mm), 2 m ve üstü yükseklik ve üstte jiletli tel; konut tarafında ise PVC kaplı tel "
     "ve boru direk. Ortak duvarlı parsellerde tel örgüyü duvar üstüne de kurabiliyoruz.</p>",
     "<p>Yenimahalle için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; sanayi işlerinde kalın tel ve yükseklik nedeniyle aralığın "
     "üst yarısına çıkıyor.</p>"),
 ),
 V("Sincan", "sincan", "Sincan'da", "45 km", ["etimesgut", "yenimahalle", "kahramankazan", "ayas", "polatli"],
   "605.366 (2024'e göre +15.057; Ankara'nın en hızlı büyüyen ilçesi)", "880 km²", "57", "794 m",
   "5 OSB: ASO 1. OSB, ASO 2. ve 3. OSB, Başkent OSB, Anadolu OSB, Ankara Dökümcüler OSB",
   [("2025-26", "Saraycık'ta 20 bin konut planlanıyor; Saraycık 4. Bölge'de 817 konut 2025 yazında teslim edildi.")],
   [("Sincan TOKİ haberi (Yeni Ankara)", "https://www.yeniankara.com.tr/sincan/sincanda-toki-is-birligi-saraycik-mahallesindeki-calismalar-ne-durumda-167064")],
   P("Sincan'da beton direk ihtiyacı iki yerden geliyor: beş OSB'deki fabrika parselleri ve Saraycık gibi hızla büyüyen konut "
     "alanlarındaki şantiyeler. Gölbaşı'ndan 45 km; getirip dikiyoruz.",
     "<p>Sincan'da beton direk satan yer olarak büyük adetli siparişlerde kamyon bazlı sevkiyat yapıyoruz; OSB parsellerinde direkleri "
     "hat boyunca indiriyoruz.</p>",
     "<p>Sincan'da ASO 1. OSB'den Anadolu OSB'ye beş ayrı organize sanayi bölgesi var. Fabrika çevresinde 2,5–3 m eğik başlı ya da Y kollu "
     "direk, köşelerde çift payanda standart. Şantiye çevirmede ise 2,4 m düz direk yeterli.</p>",
     "<p>Sincan'a 45 km mesafe nedeniyle küçük siparişlerde nakliye payı oluşabiliyor; büyük adetlerde bu pay direk başına çok düşüyor. "
     "Ekim 2026'da 2,4 m düz direk 190–275 TL, eğik başlı 275–300 TL.</p>"),
   P("Sincan jiletli tel için Ankara'nın en yoğun ilçelerinden biri; beş OSB'deki fabrikalar çitlerinin üstüne jiletli tel istiyor. "
     "Gölbaşı'ndan 45 km; ölçüp takıyoruz.",
     "<p>Sincan'da jiletli tel satan yer olarak fabrika ve depo işlerinde faturalı çalışıyoruz. Yüksek duvar ve uzun hatlar için sepetli "
     "araç ya da iskele gerektiğinde bunu baştan konuşuyoruz.</p>",
     "<p>Sincan'daki OSB'lerde (ASO, Başkent, Anadolu, Dökümcüler) en çok Y kollu direk + ortada Ø60–90 cm helezon jiletli tel kullanılıyor. "
     "Ankara Dökümcüler OSB gibi ağır sanayi bölgelerinde paslanmaz jiletli tel uzun vadede daha mantıklı olabilir.</p>",
     "<p>Sincan'da fabrika işlerinin metrajı uzun; Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre. Kamu birim fiyatında temin + "
     "gerdirme 546 TL/metre; özel sektörde bunun altında kalıyor.</p>"),
   P("Sincan, 2025'te Ankara'nın en hızlı büyüyen ilçesi oldu; yeni konut alanları, şantiyeler ve OSB'ler tel örgü ihtiyacını sürekli "
     "artırıyor. Gölbaşı'ndan 45 km; tel örgüyü kuruyoruz.",
     "<p>Sincan'da tel örgü satan yer olarak malzemeyi metrajınıza göre top top getiriyor, montajı direkten başlıyoruz. OSB ve şantiye "
     "işlerinde hafta sonu çalışma da mümkün.</p>",
     "<p>Saraycık gibi yeni konut bölgelerinde şantiye çevirme için galvaniz tel ve beton direk; OSB parsellerinde kalın tel ve jiletli tel; "
     "ilçenin kırsal kesimindeki tarlalarda ise ekonomik galvaniz tel ve [[ankara-dikenli-tel|dikenli tel]].</p>",
     "<p>Sincan için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; uzun metrajlı OSB ve şantiye işlerinde metre başına maliyet düşüyor.</p>"),
 ),
 V("Mamak", "mamak", "Mamak'ta", "25 km", ["cankaya", "altindag", "golbasi", "kecioren"],
   "690.329", "321 km²", "64", "1.159 m", "OSB yok (OSBÜK)",
   [("2025", "Yeni Mamak kentsel dönüşümü (Araplar, Derbent, Dostlar, Köstence) sürüyor."),
    ("Tarih", "Mamak tarihte \"bölgenin meyve hanesi\" olarak anılmış; ilçe çevresinde bahçe ve bağ kültürü var.")],
   [("Mamak (Vikipedi)", "https://tr.wikipedia.org/wiki/Mamak"),
    ("Ankara 2025 projeleri (Yeni Ankara)", "https://www.yeniankara.com.tr/ankara/ankara-2025-yilinda-bu-projeleri-bekliyor-92539")],
   P("Mamak'ta beton direk; kentsel dönüşüm şantiyelerinde ve ilçenin doğusundaki bahçe ve arsalarda isteniyor. Gölbaşı'ndan yaklaşık "
     "25 km; direği getirip dikiyoruz.",
     "<p>Mamak'ta beton direk satan yer olarak dar sokaklı mahallelerde küçük araçla, şantiyelere ise kamyonla teslim yapıyoruz. "
     "Mamak'ın eğimli yollarında direği elle taşımanız gerekmesin diye indirme yerini önceden konuşuyoruz.</p>",
     "<p>Mamak 1.159 m rakımla Ankara'nın yüksek ilçelerinden; arazinin önemli kısmı eğimli. Eğimde direkleri kademeli dikiyor, alt "
     "taraftaki köşe direklerine payanda ekliyoruz. Yeni Mamak kentsel dönüşüm şantiyelerinde ise sökülüp taşınabilir düzen kuruyoruz.</p>",
     "<p>Mamak'ta eğimli arazide direk sayısı düz araziye göre artabiliyor. Ekim 2026'da 2 m düz direk 132–265 TL, payanda 217–270 TL bandında.</p>"),
   P("Mamak'ta jiletli tel en çok kentsel dönüşüm şantiyelerinde, depolarda ve ilçenin kenarındaki bahçelerde soruluyor. Gölbaşı'ndan "
     "25 km; ölçüp takıyoruz.",
     "<p>Mamak'ta jiletli tel satan yer olarak şantiye işlerinde hızlı çalışıyoruz; malzeme hırsızlığı riski olan sahada çit bir gün bile "
     "eksik kalmasın diye işi tek seferde bitiriyoruz.</p>",
     "<p>Araplar, Derbent, Dostlar ve Köstence'deki dönüşüm sahalarında şantiye çitinin üstüne helezon jiletli tel en hızlı güvenlik "
     "çözümü. Yerleşik mahallelerdeki bahçe duvarlarında ise düzlemsel jiletli tel ya da [[ankara-dikenli-tel|dikenli tel]] daha uygun.</p>",
     "<p>Mamak'taki şantiye işlerinde jiletli tel genelde kısa süreli kullanım için alınıyor; Ekim 2026'da galvaniz helezon 45–110 TL/metre. "
     "Sökülüp başka şantiyede kullanılacaksa montajı buna göre yapıyoruz.</p>"),
   P("Mamak'ta tel örgü; eski bağ ve bahçelerden yeni şantiyelere kadar her yerde ihtiyaç. Gölbaşı'ndan 25 km; tel örgüyü direğiyle kuruyoruz.",
     "<p>Mamak'ta tel örgü satan yer olarak malzemeyi kapıya getiriyoruz. Ekim 2026'da Armut'a Mamak'tan gelen 60 metre, 150 cm, beton "
     "direkli ve 4 m kapılı tel örgü talebine 30.000–43.265 TL teklif verilmiş; fiyatın neye göre değiştiğini aşağıda anlattık.</p>",
     "<p>Tarihte \"meyve hanesi\" diye anılan Mamak'ta hâlâ bahçe ve bağ parselleri var; buralarda galvaniz tel ve beton direk yeterli. Eğimli "
     "arazide teli kademelendiriyor, altta boşluk bırakmıyoruz.</p>",
     "<p>Mamak için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; eğim ve kapı sayısı fiyatı belirleyen başlıca etkenler.</p>"),
 ),
 V("Keçiören", "kecioren", "Keçiören'de", "26 km", ["altindag", "yenimahalle", "pursaklar", "kahramankazan"],
   "931.722", "159 km²", "51", "1.026 m", "OSB yok (OSBÜK)",
   [("Mahalleler", "Ovacık, Bağlum ve Kalaba Keçiören'de."),
    ("2025", "Belediyenin 2025 faaliyet raporunda kentsel dönüşümde kolaylığın süreceği belirtiliyor.")],
   [("Keçiören (Vikipedi)", "https://tr.wikipedia.org/wiki/Ke%C3%A7i%C3%B6ren"),
    ("Keçiören Bel. 2025 faaliyet raporu", "https://kecioren.bel.tr/faaliyet_raporlari_dosya_eki/2025_mali_yili_faaliyet_raporukecioren.bel.tr40.pdf")],
   P("Keçiören'de beton direk, çoğunlukla Bağlum ve Ovacık tarafındaki bahçe ve arsa parselleri için soruluyor. Gölbaşı'ndan 26 km; "
     "getirip dikiyoruz.",
     "<p>Keçiören'de beton direk satan yer olarak yoğun yerleşimli mahallelerde teslim saatini trafiğe göre ayarlıyoruz; direkleri sokakta "
     "bekletmeden dikim yerine bırakıyoruz.</p>",
     "<p>Keçiören 931 bin nüfusla Ankara'nın en kalabalık ikinci ilçesi, ama Bağlum ve Ovacık tarafında hâlâ bahçeli ve arsalı alanlar var. "
     "Buralarda 2–2,4 m düz direk; bahçe ön cephesinde görünüm isteniyorsa boru direk öneriyoruz.</p>",
     "<p>Keçiören işlerinde direk adedi genelde küçük (20–60 adet); Ekim 2026'da 2 m düz direk 132–265 TL. Az adette nakliyeyi tek seferde "
     "toplayıp maliyeti düşük tutuyoruz.</p>"),
   P("Keçiören'de jiletli tel; dönüşüm şantiyeleri, iş yerleri ve bahçe duvarları için isteniyor. Gölbaşı'ndan 26 km; ölçüp takıyoruz.",
     "<p>Keçiören'de jiletli tel satan yer olarak yerleşim içindeki işlerde komşu ve yaya güvenliğini önde tutuyoruz; teli içe dönük ve "
     "erişilemeyecek yükseklikte takıyoruz.</p>",
     "<p>Yoğun yerleşimli Keçiören'de helezon jiletli tel yerine çoğu zaman düzlemsel jiletli tel ya da düz hat tercih ediliyor; daha az yer "
     "kaplıyor, göze daha az batıyor. Kentsel dönüşüm şantiyelerinde ise helezon tel.</p>",
     "<p>Keçiören'de düzlemsel jiletli tel Ekim 2026'da 45–65 TL/metre, helezon 45–110 TL/metre. Duvar kolu ve gergi teli ayrı kalem.</p>"),
   P("Keçiören'de tel örgü; apartman bahçesinden Bağlum'daki hobi bahçesine kadar geniş bir ihtiyaç. Gölbaşı'ndan 26 km; tel örgüyü kuruyoruz.",
     "<p>Keçiören'de tel örgü satan yer olarak malzemeli ya da yalnız işçilik çalışıyoruz. Apartman ve site işlerinde önce yönetim kararını "
     "istiyoruz; sonra gün veriyoruz.</p>",
     "<p>Apartman bahçelerinde PVC kaplı tel ve boru direk, istenirse [[ankara-cim-cit|çim çit]]; Bağlum ve Ovacık'taki bahçelerde galvaniz tel "
     "ve beton direk. Bahçe duvarı üstüne kurulacak tel için duvarın sağlamlığına bakıyoruz.</p>",
     "<p>Keçiören için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; PVC kaplı tel ve boru direk aralığın üst kısmına çıkıyor.</p>"),
 ),
 V("Altındağ", "altindag", "Altındağ'da", "23 km", ["cankaya", "kecioren", "mamak", "pursaklar", "yenimahalle"],
   "418.072", "123 km²", "26", "1.196 m", "OSB yok (OSBÜK)",
   [("Coğrafya", "Çubuk Barajı ilçeyi kuzey ve güney olarak ikiye bölüyor.")],
   [("Altındağ (Vikipedi)", "https://tr.wikipedia.org/wiki/Alt%C4%B1nda%C4%9F")],
   P("Altındağ'da beton direk; ilçenin baraj çevresindeki boş arazilerinde ve dönüşüm şantiyelerinde lazım oluyor. Gölbaşı'ndan 23 km; "
     "getirip dikiyoruz.",
     "<p>Altındağ'da beton direk satan yer olarak dik yokuşlu mahallelerde direği araca yakın noktaya indirip kısa mesafede taşıyoruz. "
     "Altındağ'ın eski yerleşim dokusunda bu hesabı baştan yapıyoruz.</p>",
     "<p>Altındağ 1.196 m rakımla yüksek ve engebeli bir ilçe; Çubuk Barajı da ilçeyi ikiye bölüyor. Eğimli ve kayalık noktalarda direk çukurunu "
     "kırıcıyla açmak gerekebiliyor; bu durumda direk aralığını zemine göre ayarlıyoruz.</p>",
     "<p>Kayalık zeminde çukur açmak işçiliği artırıyor. Direk malzemesi Ekim 2026'da 2 m düz için 132–265 TL; payandalı köşe direği temin + "
     "montaj 450 TL'den başlıyor.</p>"),
   P("Altındağ'da jiletli tel; eski sanayi ve ticaret alanlarındaki iş yerleri ve dönüşüm şantiyeleri için isteniyor. Gölbaşı'ndan 23 km; "
     "ölçüp takıyoruz.",
     "<p>Altındağ'da jiletli tel satan yer olarak dar sokaklarda ve yüksek duvarlarda çalışmaya alışığız; gerekirse iskele kurup duvar üstü "
     "montajı güvenli yapıyoruz.</p>",
     "<p>Altındağ'ın ticaret ve depo alanlarında duvar üstü helezon jiletli tel yaygın. Yerleşim içinde düzlemsel jiletli tel öneriyoruz; "
     "yaya yoluna bakan cephelerde teli içe doğru yönlendiriyoruz.</p>",
     "<p>Altındağ'da duvar üstü işlerde demir kol ve gergi teli maliyete ekleniyor. Malzeme Ekim 2026'da 45–110 TL/metre.</p>"),
   P("Altındağ'da tel örgü; boş arsalar, baraj çevresi ve şantiyeler için isteniyor. Gölbaşı'ndan 23 km; tel örgüyü direğiyle kuruyoruz.",
     "<p>Altındağ'da tel örgü satan yer olarak malzemeyi getiriyor, eğimli parsellerde montajı kademeli yapıyoruz.</p>",
     "<p>Engebeli Altındağ arazisinde tel örgüyü düz hat yerine kademeli kuruyoruz; aksi halde çukur yerlerde altta boşluk kalıyor. Boş arsa "
     "işgalini önlemek için galvaniz tel ve beton direk, üstte 1–2 sıra dikenli tel yaygın tercih.</p>",
     "<p>Altındağ için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; kayalık ve eğimli zemin işçiliği artırabiliyor.</p>"),
 ),
 V("Pursaklar", "pursaklar", "Pursaklar'da", "38 km", ["kecioren", "altindag", "akyurt", "kahramankazan"],
   "172.810", "169 km²", "21", "1.058 m", "OSB yok (OSBÜK)",
   [("Mahalleler", "Saray Cumhuriyet, Saray Fatih, Saray Gümüşoluk ve Saray Osmangazi Pursaklar'da."),
    ("2026", "Gümüşoluk Göleti, belediye GES'i ve 126 bin m² Gümüşoluk Millet Bahçesi inşaatı sürüyor.")],
   [("Pursaklar (Vikipedi)", "https://tr.wikipedia.org/wiki/Pursaklar"),
    ("Gümüşoluk projeleri (Yeni Ankara)", "https://www.yeniankara.com.tr/pursaklar/pursaklarda-gumusoluk-goleti-ve-ges-yukseliyor-baskan-ertugrul-cetin-sahada-181444")],
   P("Pursaklar'da beton direk; Saray mahalleleri çevresindeki depolar, arsalar ve devam eden proje sahaları için isteniyor. Gölbaşı'ndan "
     "38 km; getirip dikiyoruz.",
     "<p>Pursaklar'da beton direk satan yer olarak Esenboğa yolu üzerinden ulaşıyoruz; Saray tarafındaki işlerde teslimi sabah erken saatte "
     "yapıp trafiğe takılmıyoruz.</p>",
     "<p>Pursaklar'da Gümüşoluk Göleti ve millet bahçesi gibi büyük projeler sürüyor; proje sahası ve depo çevirmede 2,4–2,5 m eğik başlı direk "
     "ve üstte dikenli tel en çok tercih edilen düzen. Konut parsellerinde 2 m düz direk yeterli.</p>",
     "<p>Pursaklar'a 38 km mesafe için orta adetli siparişlerde nakliyeyi direk fiyatına yayıyoruz. Ekim 2026'da eğik başlı direk 275–300 TL, "
     "düz direk 132–265 TL.</p>"),
   P("Pursaklar'da jiletli tel; Saray mahallelerindeki depolar, iş yerleri ve proje sahaları için soruluyor. Gölbaşı'ndan 38 km; ölçüp takıyoruz.",
     "<p>Pursaklar'da jiletli tel satan yer olarak depo ve iş yeri müşterilerimize faturalı çalışıyoruz; işi tek günde bitirecek şekilde "
     "planlıyoruz.</p>",
     "<p>Pursaklar'ın Saray tarafındaki depo ve ticari alanlarda panel ya da tel örgü üstü helezon jiletli tel yaygın. Konut mahallelerinde "
     "daha sade bir çözüm için [[ankara-dikenli-tel|dikenli tel]] öneriyoruz.</p>",
     "<p>Pursaklar için jiletli tel Ekim 2026'da 45–110 TL/metre (galvaniz helezon). 50 metrelik rulo 2.250–5.500 TL bandında.</p>"),
   P("Pursaklar'da tel örgü; konut bahçeleri, depo arsaları ve yeni proje alanları için isteniyor. Gölbaşı'ndan 38 km; tel örgüyü kuruyoruz.",
     "<p>Pursaklar'da tel örgü satan yer olarak sevkiyatı kendi aracımızla yapıyor, ölçüyü yerinde alıyoruz.</p>",
     "<p>Pursaklar 21 mahalleli kompakt bir ilçe; konut bahçelerinde PVC kaplı tel, Saray tarafındaki depo arsalarında galvaniz tel ve beton "
     "direk öne çıkıyor. Esenboğa yönündeki açık arazide rüzgâra karşı direk aralığını sık tutuyoruz.</p>",
     "<p>Pursaklar için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; açık ve rüzgârlı arazide sık direk maliyeti biraz artırabiliyor.</p>"),
 ),
 V("Akyurt", "akyurt", "Akyurt'ta", "55 km", ["pursaklar", "kalecik", "kahramankazan", "kecioren"],
   "45.644", "369 km²", "26", "1.035 m", "OSBÜK listesinde OSB yok",
   [("Konum", "Esenboğa Havalimanı'na yakın bir ilçe; tarım ve açık arazi geniş yer kaplıyor.")],
   [("Akyurt (Vikipedi)", "https://tr.wikipedia.org/wiki/Akyurt")],
   P("Akyurt'ta beton direk; açık tarım arazileri ve yeni yapılaşan parseller için isteniyor. Gölbaşı'ndan yaklaşık 55 km; direği getirip dikiyoruz.",
     "<p>Akyurt'ta beton direk satan yer olarak uzun hatlı tarla işlerinde kamyon bazlı sevkiyat yapıyoruz; direk başına nakliye payı böylece düşüyor.</p>",
     "<p>Akyurt 369 km²'lik alanının büyük kısmı açık arazi. Açık ve rüzgâr alan tarlalarda direk aralığını 2,5 metreye çekiyor, her köşeye ve "
     "uzun hatlarda belli aralıklarla payanda koyuyoruz. Tarla sınırında 2 m düz direk ve galvaniz tel ekonomik çözüm.</p>",
     "<p>Akyurt'a 55 km için az adetli siparişlerde nakliyeyi ayrıca konuşuyoruz. Ekim 2026'da 2 m düz direk 132–265 TL, payanda 217–270 TL.</p>"),
   P("Akyurt'ta jiletli tel; havalimanı çevresindeki lojistik ve depo alanları ile tarım depoları için soruluyor. Gölbaşı'ndan 55 km; ölçüp takıyoruz.",
     "<p>Akyurt'ta jiletli tel satan yer olarak uzak mesafe nedeniyle keşif ve montajı aynı gün planlamaya çalışıyoruz; fotoğrafla ön ölçü "
     "alırsak tek seferde bitiriyoruz.</p>",
     "<p>Akyurt'ta OSB bulunmuyor; jiletli tel ihtiyacı daha çok tek tek depo, ahır ve tarım deposundan geliyor. Bu tür yapılarda tel örgü üstüne "
     "Y kol ve ortada helezon jiletli tel yeterli güvenliği sağlıyor.</p>",
     "<p>Akyurt'ta işlerin metrajı genelde orta büyüklükte; Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre, düz hat jiletli tel daha ekonomik.</p>"),
   P("Akyurt'ta tel örgü; tarla, arsa ve hayvancılık alanları için isteniyor. Gölbaşı'ndan 55 km; tel örgüyü direğiyle kuruyoruz.",
     "<p>Akyurt'ta tel örgü satan yer olarak tarla işlerinde malzeme ve montajı birlikte veriyoruz; uzak parsellerde ulaşım yolunu önceden soruyoruz.</p>",
     "<p>Akyurt'un açık tarım arazilerinde galvaniz tel örgü ve beton direk; hayvan için tel örgünün altına ek bir sıra gergi teli ya da "
     "[[ankara-kafes-tel|kafes tel]] eklenebiliyor. Büyük tarlalarda yalnız [[ankara-dikenli-tel|dikenli tel]] de ekonomik bir seçenek.</p>",
     "<p>Akyurt için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; büyük metrajlı tarla işlerinde metre maliyeti aralığın alt yarısına iniyor.</p>"),
 ),
]

VERI += [
 V("Kahramankazan", "kahramankazan", "Kahramankazan'da", "76 km", ["sincan", "yenimahalle", "pursaklar", "ayas", "gudul"],
   "63.143", "547 km²", "48", "886 m", "Ankara Uzay ve Havacılık İhtisas OSB (tam dolu); TUSAŞ tesisleri; Saray ve Keresteciler'de depolama",
   [("Tarım", "Şeker pancarı, kuru fasulye, kavun, karpuz, buğday, arpa, nohut; seracılık gelişiyor.")],
   [("Kahramankazan (Vikipedi)", "https://tr.wikipedia.org/wiki/Kahramankazan")],
   P("Kahramankazan'da beton direk; hem sanayi ve depolama alanlarında hem de şeker pancarı ve sebze tarlalarında isteniyor. Gölbaşı'ndan "
     "yaklaşık 76 km; direği getirip dikiyoruz.",
     "<p>Kahramankazan'da beton direk satan yer olarak çevre yolu ve Kazan yolu üzerinden kamyonla sevkiyat yapıyoruz; uzun hatlı tarla ve "
     "depo işlerinde direkleri hat boyunca indiriyoruz.</p>",
     "<p>Kahramankazan'da Uzay ve Havacılık İhtisas OSB ile Saray ve Keresteciler'deki depolama alanları güçlü çit istiyor: eğik başlı ya da "
     "Y kollu direk. Tarlalarda ise 2 m düz direk; sulanan sebze tarlalarında direk dibini sulama suyuna karşı geniş betonluyoruz.</p>",
     "<p>76 km mesafe nedeniyle Kahramankazan'da büyük adetli siparişler daha ekonomik. Ekim 2026'da eğik başlı direk 275–350 TL, düz direk 132–265 TL.</p>"),
   P("Kahramankazan'da jiletli tel; depolama alanları, lojistik tesisleri ve sanayi parselleri için isteniyor. Gölbaşı'ndan 76 km; ölçüp takıyoruz.",
     "<p>Kahramankazan'da jiletli tel satan yer olarak uzun metrajlı depo işlerini planlı yapıyoruz; malzemeyi tek seferde getirip montajı "
     "ardışık günlere yayıyoruz.</p>",
     "<p>Saray ve Keresteciler'deki depolarda en yaygın düzen panel ya da tel örgü üstü Y kol + helezon jiletli tel. Tarım deposu ve seralarda "
     "ise maliyeti düşük tutmak için düz hat jiletli tel ya da [[ankara-dikenli-tel|dikenli tel]] yeterli olabiliyor.</p>",
     "<p>Kahramankazan'da Ekim 2026 itibarıyla galvaniz helezon jiletli tel 45–110 TL/metre; uzun hatta montaj maliyeti metre başına düşüyor.</p>"),
   P("Kahramankazan'da tel örgü; sera, tarla, depo ve lojistik alanlarının vazgeçilmezi. Gölbaşı'ndan 76 km; tel örgüyü kuruyoruz.",
     "<p>Kahramankazan'da tel örgü satan yer olarak tarla ve depo işlerine malzemeli montajla geliyoruz.</p>",
     "<p>Seracılığın geliştiği Kahramankazan'da sera ve sebze tarlası çevresinde galvaniz tel ve beton direk; kemirgen ve küçük hayvana karşı "
     "alt kısmı toprağa gömülü [[ankara-kafes-tel|kafes tel]] eklenebiliyor. Depolarda kalın tel ve üstte jiletli tel.</p>",
     "<p>Kahramankazan için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; büyük tarla metrajlarında aralığın alt yarısı.</p>"),
 ),
 V("Polatlı", "polatli", "Polatlı'da", "86 km", ["haymana", "sincan", "ayas", "nallihan"],
   "131.894", "3.618 km² (Ankara'nın en geniş ilçesi)", "95", "876 m",
   "Polatlı OSB (tam dolu), Polatlı Ticaret Odası OSB (%92,7), Bilgen SS (260 işyeri), Marangozlar SS",
   [("Tarım", "Buğday, arpa, şeker pancarı, kavun, soğan; büyükbaş, küçükbaş ve kümes hayvancılığı."),
    ("2026", "Mahkeme kararıyla Olukpınar, Kuşçu, Karapınar ve Kargalı'daki hobi bahçelerinde yıkım başladı (Temmuz 2026).")],
   [("Polatlı (Vikipedi)", "https://tr.wikipedia.org/wiki/Polatl%C4%B1"),
    ("Polatlı hobi bahçesi yıkımı (Yeni Ankara)", "https://www.yeniankara.com.tr/ankara/ankara-polatlida-hobi-bahcelerinin-yikimi-basladi-177307")],
   P("Polatlı, Ankara'nın en geniş ilçesi (3.618 km²); buğday tarlaları, hayvancılık ve iki OSB beton direği en çok tüketen yerler. "
     "Gölbaşı'ndan 86 km; getirip dikiyoruz.",
     "<p>Polatlı'da beton direk satan yer olarak tarla işlerinde kamyon bazlı sevkiyat yapıyoruz; 95 mahalleli geniş ilçede köy yollarına "
     "uygun araçla geliyoruz.</p>",
     "<p>Polatlı'nın düz ve geniş tarım arazilerinde uzun direk hatları kuruluyor; burada maliyeti belirleyen direk aralığı ve köşe sayısı. "
     "Büyükbaş ve küçükbaş işletmelerinde direk aralığını sıklaştırıp payandayı artırıyoruz. Polatlı OSB ve Ticaret Odası OSB parsellerinde ise "
     "eğik başlı direk standart.</p>"
     "<p>2026'da Polatlı'daki hobi bahçelerinde mahkeme kararıyla yıkımlar başladı; tarım arazisinde yapı yaptıracaksanız önce mevzuatı "
     "kontrol edin. Çit kurmadan önce parselinizin durumunu sormanızı öneririz.</p>",
     "<p>Polatlı'ya 86 km mesafe için küçük siparişlerde nakliye belirgin bir kalem; tarla işlerinde yüzlerce direk alındığında direk başına "
     "çok azalıyor. Ekim 2026'da 2 m düz direk 132–265 TL, payanda 217–270 TL.</p>"),
   P("Polatlı'da jiletli tel; OSB'lerdeki fabrikalar, hayvancılık işletmeleri ve tarım depoları için isteniyor. Gölbaşı'ndan 86 km; ölçüp takıyoruz.",
     "<p>Polatlı'da jiletli tel satan yer olarak fabrika ve çiftlik işlerini önceden planlıyor, malzeme ve ekibi tek seferde getiriyoruz.</p>",
     "<p>Polatlı OSB ve Ticaret Odası OSB'deki tesislerde panel çit üstü helezon jiletli tel; çiftlik ve ağıllarda ise hayvana zarar vermemesi "
     "için jiletli teli yalnız dış çevrede, hayvanın erişemeyeceği yükseklikte kullanıyoruz. İç bölmelerde [[ankara-tel-orgu|tel örgü]] yeterli.</p>",
     "<p>Polatlı'da uzun hatlı işlerde Ekim 2026 itibarıyla galvaniz helezon jiletli tel 45–110 TL/metre; düz hat jiletli tel daha ekonomik.</p>"),
   P("Polatlı'da tel örgü; buğday tarlası, ağıl, kümes ve sanayi parseli çevresinde en çok kullanılan çit. Gölbaşı'ndan 86 km; tel örgüyü kuruyoruz.",
     "<p>Polatlı'da tel örgü satan yer olarak tarla ve çiftlik işlerine malzemeli montajla geliyoruz. Ekim 2026'da Armut'a Polatlı'dan gelen "
     "150 metre, 150 cm, 1.000 m² ve kapılı tel örgü talebine 35.000–147.500 TL arası teklif verilmiş; aralığın neden bu kadar geniş olduğunu "
     "[[ankara-tel-orgu-fiyatlari|tel örgü fiyatları]] sayfasında anlattık.</p>",
     "<p>Kümes hayvancılığında küçük göz ve alt kısımda [[ankara-kafes-tel|kafes tel]]; büyükbaşta kalın tel ve sık direk; geniş buğday "
     "tarlalarında galvaniz tel ya da yalnız [[ankara-dikenli-tel|dikenli tel]].</p>",
     "<p>Polatlı için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; uzun tarla hatlarında aralığın alt kısmı.</p>"),
 ),
 V("Haymana", "haymana", "Haymana'da", "56 km", ["golbasi", "polatli", "bala"],
   "26.083", "2.164 km²", "78", "1.219 m", "OSB yok; Yeni Haymana Sanayi Sitesi (100 işyeri, %52 dolu)",
   [("2025", "Belediyenin 13.500 m² kaplıca tesisi Eylül 2025'te açıldı.")],
   [("Haymana (Vikipedi)", "https://tr.wikipedia.org/wiki/Haymana"),
    ("Haymana kaplıcası (Yeni Ankara)", "https://www.yeniankara.com.tr/haymana/haymana-tarihi-gune-taniklik-etti-turkiyenin-en-buyuk-kaplicasi-acildi-127346")],
   P("Haymana'da beton direk; geniş tarım ve mera arazilerinde ve hayvancılık işletmelerinde isteniyor. Gölbaşı'ndan yaklaşık 56 km; direği getirip dikiyoruz.",
     "<p>Haymana'da beton direk satan yer olarak Gölbaşı–Haymana yolu üzerinden doğrudan ulaşıyoruz; 78 mahalleli ilçede köy yollarına uygun "
     "araçla geliyoruz.</p>",
     "<p>Haymana 1.219 m rakımla Ankara'nın yüksek ve soğuk ilçelerinden. Don kabarması burada direğin en büyük düşmanı; direkleri derin "
     "gömüyor, köşelerde payandayı ihmal etmiyoruz. Mera ve tarlada 2 m düz direk ve galvaniz tel ya da [[ankara-dikenli-tel|dikenli tel]].</p>",
     "<p>Haymana'ya 56 km için orta ve büyük adetli siparişlerde nakliye direk fiyatına yayılıyor. Ekim 2026'da 2 m düz direk 132–265 TL.</p>"),
   P("Haymana'da jiletli tel; tarım depoları, çiftlikler ve sanayi sitesindeki iş yerleri için isteniyor. Gölbaşı'ndan 56 km; ölçüp takıyoruz.",
     "<p>Haymana'da jiletli tel satan yer olarak uzak köylerdeki işleri fotoğrafla ön ölçü alıp tek seferde bitirmeye çalışıyoruz.</p>",
     "<p>Yeni Haymana Sanayi Sitesi'ndeki iş yerlerinde duvar üstü jiletli tel; kırsaldaki depo ve çiftliklerde tel örgü üstü Y kol + helezon "
     "jiletli tel. Soğuk iklimde galvaniz kaplamanın kalitesi önemli; ucuz ve ince kaplamalı tel çabuk paslanıyor.</p>",
     "<p>Haymana için galvaniz helezon jiletli tel Ekim 2026'da 45–110 TL/metre; paslanmaz yaklaşık %30 daha pahalı.</p>"),
   P("Haymana'da tel örgü; mera, tarla, ağıl ve kaplıca bölgesindeki tesisler için isteniyor. Gölbaşı'ndan 56 km; tel örgüyü kuruyoruz.",
     "<p>Haymana'da tel örgü satan yer olarak Gölbaşı'na komşu olmanın avantajıyla keşfe hızlı geliyoruz.</p>",
     "<p>Haymana'nın 2.164 km²'lik geniş mera ve tarım arazilerinde hayvancılık için sık direkli galvaniz tel örgü; soğuk ve rüzgârlı "
     "yüksek alanlarda gergi tellerini daha sık çekiyoruz ki tel kış boyunca gevşemesin.</p>",
     "<p>Haymana için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; uzun mera hatlarında aralığın alt kısmı.</p>"),
 ),
 V("Bala", "bala", "Bala'da", "49 km", ["golbasi", "haymana", "serefliko", "evren"],
   "20.109", "1.851 km²", "56", "1.313 m", "OSB yok; ilçede güneş enerjisi santralleri (Astor Bala GES 13,95 MWe, 2024)",
   [("Tarım", "Buğday, arpa, ayçiçeği, mercimek, nohut, fasulye, şeker pancarı, kavun, karpuz."),
    ("2026", "Sırapınar ve Aşağıhacıbekir'de 30 MWe + 30 MWh depolamalı GES projesinin ÇED süreci sürüyor.")],
   [("Balâ (Vikipedi)", "https://tr.wikipedia.org/wiki/Bal%C3%A2"),
    ("Bala GES projesi (Evrensel, Ağu 2026)", "https://www.evrensel.net/haber/5996620/ankara-balada-396-milyon-liralik-ges-projesi-tarim-arazilerinin-yaninda-kurulacak")],
   P("Bala'da beton direk; geniş tarım arazilerinde ve son yıllarda artan güneş enerjisi santrali (GES) sahalarının çevresinde isteniyor. "
     "Gölbaşı'ndan 49 km; getirip dikiyoruz.",
     "<p>Bala'da beton direk satan yer olarak Gölbaşı'na komşu olduğumuz için sık sevkiyat yapıyoruz; büyük GES ve tarla işlerinde kamyon bazlı teslim.</p>",
     "<p>Bala'da bir GES 2024'te devreye girdi, 2026'da yeni bir GES projesinin ÇED süreci sürüyor. GES sahaları uzun ve düz çevre çiti ister: "
     "2,4–2,5 m eğik başlı direk, galvaniz tel ve üstte dikenli ya da jiletli tel. Tarlalarda 2 m düz direk yeterli.</p>",
     "<p>Bala'da GES ve tarla işlerinin direk adedi yüksek; adet arttıkça direk başına maliyet düşüyor. Ekim 2026'da eğik başlı direk 275–300 TL.</p>"),
   P("Bala'da jiletli tel; GES sahaları, tarım depoları ve çiftlikler için isteniyor. Gölbaşı'ndan 49 km; ölçüp takıyoruz.",
     "<p>Bala'da jiletli tel satan yer olarak uzun çevreli GES sahalarında çalışmaya uygun ekip ve malzemeyle geliyoruz.</p>",
     "<p>GES sahalarında panel hırsızlığına karşı çit üstüne helezon jiletli tel yaygın; Y kollu direk ortasında Ø60 cm iyi bir denge. "
     "Tarım depolarında daha sade bir çözüm için [[ankara-dikenli-tel|dikenli tel]] de iş görüyor.</p>",
     "<p>Bala'daki uzun hatlı işlerde Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre; kamu birim fiyatında temin + gerdirme 546 TL/metre.</p>"),
   P("Bala'da tel örgü; buğday ve ayçiçeği tarlaları, GES sahaları ve hayvancılık için isteniyor. Gölbaşı'ndan 49 km; tel örgüyü kuruyoruz.",
     "<p>Bala'da tel örgü satan yer olarak Gölbaşı–Bala yolu üzerinden düzenli geliyoruz; köy ve mahalle yollarını biliyoruz.</p>",
     "<p>Bala 1.313 m rakımla yüksek ve rüzgâra açık bir ilçe. Tarla ve GES çevresinde galvaniz tel örgüyü sık gergi teliyle kuruyoruz; rüzgâr "
     "alan uzun hatlarda belli aralıklarla ara gergi direği koyuyoruz.</p>",
     "<p>Bala için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; uzun tarla ve GES hatlarında aralığın alt kısmı.</p>"),
 ),
 V("Ayaş", "ayas", "Ayaş'ta", "80 km", ["gudul", "sincan", "polatli", "kahramankazan"],
   "13.136", "1.041 km²", "33", "954 m", "OSB yok (OSBÜK)",
   [("Tarım", "Ayaş domatesi menşe adı tescilli (2022) ve AB Korumalı Menşe Adı aldı (2023) — Ankara'nın ilk AB coğrafi işaretli ürünü.")],
   [("Ayaş (Vikipedi)", "https://tr.wikipedia.org/wiki/Aya%C5%9F"),
    ("AB Delegasyonu: Ayaş domatesi", "https://www.eeas.europa.eu/delegations/t%C3%BCrkiye/ab-ankara%E2%80%99n%C4%B1n-aya%C5%9F-domatesini-tan%C4%B1d%C4%B1_tr")],
   P("Ayaş'ta beton direk en çok domates ve sebze tarlalarının çevresinde isteniyor; Ayaş domatesi tarlası çitlenmeye değer :) "
     "Gölbaşı'ndan yaklaşık 80 km; direği getirip dikiyoruz.",
     "<p>Ayaş'ta beton direk satan yer olarak tarla işlerinde kamyonla sevkiyat yapıyor, direkleri tarla kenarına indiriyoruz.</p>",
     "<p>Ayaş'ın sulanan sebze tarlalarında direk dibi sürekli nem görüyor; burada direği daha geniş betonluyor, dibine mıcır seriyoruz. "
     "Hayvan ve izinsiz girişe karşı 2 m düz direk ve galvaniz tel yaygın düzen.</p>",
     "<p>Ayaş'a 80 km için küçük siparişlerde nakliyeyi önceden konuşuyoruz. Ekim 2026'da 2 m düz direk 132–265 TL, payanda 217–270 TL.</p>"),
   P("Ayaş'ta jiletli tel; tarım depoları, soğuk hava depoları ve çiftlikler için isteniyor. Gölbaşı'ndan 80 km; ölçüp takıyoruz.",
     "<p>Ayaş'ta jiletli tel satan yer olarak uzak işlerde ön ölçüyü fotoğrafla alıp malzemeyi eksiksiz getiriyoruz.</p>",
     "<p>Hasat döneminde ürün ve ekipman güvenliği önemli; tarım deposu ve ahır çevresinde tel örgü üstü Y kol + helezon jiletli tel. Tarla "
     "sınırında ise jiletli tel yerine [[ankara-dikenli-tel|dikenli tel]] çoğu zaman yeterli ve daha ekonomik.</p>",
     "<p>Ayaş için galvaniz helezon jiletli tel Ekim 2026'da 45–110 TL/metre; düz hat jiletli tel daha ekonomik.</p>"),
   P("Ayaş'ta tel örgü; domates ve sebze tarlaları, bağ ve bahçe çevresi için isteniyor. Gölbaşı'ndan 80 km; tel örgüyü kuruyoruz.",
     "<p>Ayaş'ta tel örgü satan yer olarak tarla işlerine malzemeli montajla geliyoruz; hasat dönemini bozmayacak şekilde gün planlıyoruz.</p>",
     "<p>AB tescilli Ayaş domatesinin yetiştiği tarlalarda galvaniz tel örgü ve beton direk; tavşan ve kemirgene karşı alt kısma "
     "[[ankara-kafes-tel|kafes tel]] eklemek işe yarıyor.</p>",
     "<p>Ayaş için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; tarla metrajı uzadıkça metre maliyeti düşüyor.</p>"),
 ),
 V("Güdül", "gudul", "Güdül'de", "125 km", ["ayas", "kahramankazan"],
   "8.028", "540 km²", "31", "737 m", "OSB yok",
   [("Tarım", "Ankara keçisinden tiftik üretimi ve bağcılık; Kirmir Çayı ve Sorgun Göleti ilçede.")],
   [("Güdül (Vikipedi)", "https://tr.wikipedia.org/wiki/G%C3%BCd%C3%BCl")],
   P("Güdül'de beton direk; bağlar, keçi ağılları ve dere kenarındaki bahçeler için isteniyor. Gölbaşı'ndan yaklaşık 125 km; direği getirip dikiyoruz.",
     "<p>Güdül'de beton direk satan yer olarak uzak mesafe nedeniyle siparişleri toplu planlıyor, malzemeyi tek seferde getiriyoruz.</p>",
     "<p>Güdül'de Ankara keçisi yetiştiriciliği ve bağcılık öne çıkıyor. Keçi ağılı çevresinde keçi tırmanmaya meyilli olduğu için direği sık "
     "ve teli gergin tutuyoruz; bağlarda 2 m düz direk yeterli. Kirmir Çayı kenarındaki nemli zeminde direk temelini geniş açıyoruz.</p>",
     "<p>Güdül'e 125 km için küçük adetli siparişlerde nakliye ayrı kalem; büyük siparişlerde direk başına payı düşük. Ekim 2026'da 2 m düz direk 132–265 TL.</p>"),
   P("Güdül'de jiletli tel daha çok depolar ve hayvancılık tesisleri için soruluyor. Gölbaşı'ndan 125 km; ölçüp takıyoruz.",
     "<p>Güdül'de jiletli tel satan yer olarak uzak işlerde keşfi fotoğraf ve videoyla yapıp montajı tek güne sığdırmaya çalışıyoruz.</p>",
     "<p>Hayvancılığın yoğun olduğu Güdül'de jiletli teli hayvanın erişemeyeceği yükseklikte ve yalnız dış çevrede kullanıyoruz; keçiler "
     "meraklıdır :) İç bölmelerde [[ankara-tel-orgu|tel örgü]] ya da [[ankara-dikenli-tel|dikenli tel]] daha güvenli.</p>",
     "<p>Güdül için Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre; uzak mesafede montajı tek seferde bitirmek maliyeti düşürüyor.</p>"),
   P("Güdül'de tel örgü; keçi ağılı, bağ ve bahçe çevresi için isteniyor. Gölbaşı'ndan 125 km; tel örgüyü kuruyoruz.",
     "<p>Güdül'de tel örgü satan yer olarak bağ ve ağıl işlerini önceden planlıyoruz; malzemeli montajla geliyoruz.</p>",
     "<p>Ankara keçisi ağıllarında küçük gözlü, kalın galvaniz tel ve sık direk; keçinin tırmanıp zorladığı yerlerde gergi tellerini artırıyoruz. "
     "Bağlarda ise ekonomik galvaniz tel yeterli.</p>",
     "<p>Güdül için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; ağıl işlerinde kalın tel ve sık direk nedeniyle aralığın orta-üst kısmı.</p>"),
 ),
 V("Nallıhan", "nallihan", "Nallıhan'da", "181 km", ["polatli", "ayas", "gudul"],
   "25.798", "2.079 km²", "84", "629 m", "OSB yok; Çayırhan Termik Santrali ve bor madeni ilçede",
   [("Doğa", "Sarıyar Barajı ve 2005'te Yaban Hayatı Geliştirme Sahası olarak tescil edilen Nallıhan Kuş Cenneti ilçede."),
    ("Tarım", "Fasulye ve domates yaygın.")],
   [("Nallıhan (Vikipedi)", "https://tr.wikipedia.org/wiki/Nall%C4%B1han"),
    ("Nallıhan Kuş Cenneti (Küre)", "https://kureansiklopedi.com/tr/detay/nallihan-kus-cenneti-ce202")],
   P("Nallıhan, hizmet verdiğimiz en uzak ilçe (Gölbaşı'ndan yaklaşık 181 km). Beton direği burada en çok tarla, bahçe ve enerji-maden "
     "tesislerinin çevresi için toplu siparişle getiriyoruz.",
     "<p>Nallıhan'da beton direk satan yer olarak uzak mesafe nedeniyle küçük siparişleri birleştirip tek sevkiyatla getiriyoruz. Direk adedi "
     "arttıkça nakliye payı direk başına çok düşüyor.</p>",
     "<p>Nallıhan 629 m rakımla hizmet bölgemizin en alçak ilçesi; kış Ankara merkezine göre daha ılıman. Sarıyar Barajı kıyısındaki nemli "
     "zeminlerde direk temelini geniş tutuyoruz. Kuş Cenneti gibi korunan alanların çevresinde çalışmadan önce izin durumunu sorun.</p>",
     "<p>Nallıhan için nakliye en belirgin kalem; bu yüzden direk siparişini tel örgü ve diğer malzemelerle birlikte vermek mantıklı. Ekim "
     "2026'da 2 m düz direk 132–265 TL.</p>"),
   P("Nallıhan'da jiletli tel; Çayırhan çevresindeki enerji ve maden tesisleri, depolar ve çiftlikler için isteniyor. Gölbaşı'ndan 181 km; "
     "toplu siparişle getirip takıyoruz.",
     "<p>Nallıhan'da jiletli tel satan yer olarak uzak işleri önceden planlıyoruz; malzeme listesini fotoğraf ve ölçüyle çıkarıp tek seferde geliyoruz.</p>",
     "<p>Çayırhan Termik Santrali ve maden sahaları gibi tesislerde şartnameye uygun güvenlik çiti ve Y kollu direk üstü helezon jiletli tel "
     "kullanılıyor. Çiftlik ve bahçelerde ise [[ankara-dikenli-tel|dikenli tel]] çoğu zaman yeterli.</p>",
     "<p>Nallıhan için Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre; uzak mesafede iş ne kadar büyükse metre başına nakliye o kadar düşük.</p>"),
   P("Nallıhan'da tel örgü; fasulye ve domates tarlaları, bahçeler ve tesis çevreleri için isteniyor. Gölbaşı'ndan 181 km; toplu işlerde "
     "tel örgüyü kuruyoruz.",
     "<p>Nallıhan'da tel örgü satan yer olarak uzak mesafeye rağmen geliyoruz; işi planlı ve toplu yapıyoruz.</p>",
     "<p>Nallıhan'ın görece ılıman ikliminde galvaniz tel uzun ömürlü; tarla ve bahçelerde galvaniz tel ve beton direk, yerleşim içinde PVC "
     "kaplı tel. Baraj kıyısındaki parsellerde zemine göre direk temelini ayarlıyoruz.</p>",
     "<p>Nallıhan için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; uzak mesafe nedeniyle küçük işlerde nakliye ayrıca konuşulur.</p>"),
 ),
 V("Kalecik", "kalecik", "Kalecik'te", "99 km", ["akyurt", "pursaklar"],
   "12.564", "1.110 km²", "57", "713 m", "OSB yok; bentonit, mermer ve krom yatakları",
   [("Tarım", "Kalecik karası üzüm bağları, şeker pancarı, buğday, elma, armut, kayısı, kiraz.")],
   [("Kalecik (Vikipedi)", "https://tr.wikipedia.org/wiki/Kalecik"),
    ("Kalecik Karası (Wines of Turkey)", "https://winesofturkey.org/kalecik-karasi/")],
   P("Kalecik'te beton direk denince akla bağlar geliyor; Kalecik karası bağlarının ve meyve bahçelerinin çevresi için direği getirip dikiyoruz. "
     "Gölbaşı'ndan yaklaşık 99 km.",
     "<p>Kalecik'te beton direk satan yer olarak bağ ve bahçe işlerinde toplu sevkiyat yapıyoruz; bağ yollarına uygun araçla geliyoruz.</p>",
     "<p>Kalecik karası Eylül'ün ikinci yarısında olgunlaşıyor; bağ çevresi çitlemesini hasattan önce bitirmek için yaz sonunu hedefliyoruz. "
     "Bağlarda 2 m düz direk ve galvaniz tel; meyve bahçelerinde de aynı düzen yeterli.</p>",
     "<p>Kalecik'e 99 km için nakliye belirgin bir kalem; direk siparişini tel örgüyle birlikte vermek maliyeti düşürüyor. Ekim 2026'da 2 m düz direk 132–265 TL.</p>"),
   P("Kalecik'te jiletli tel; maden ve taş ocağı sahaları, depolar ve tarım tesisleri için isteniyor. Gölbaşı'ndan 99 km; ölçüp takıyoruz.",
     "<p>Kalecik'te jiletli tel satan yer olarak uzak işlerde ön ölçüyü fotoğrafla alıp malzemeyi eksiksiz getiriyoruz.</p>",
     "<p>Kalecik'teki bentonit, mermer ve krom sahalarında güvenlik çiti üstüne helezon jiletli tel; bağ ve bahçelerde ise jiletli tel yerine "
     "[[ankara-dikenli-tel|dikenli tel]] çoğu zaman daha uygun.</p>",
     "<p>Kalecik için Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre; uzun maden sahası hatlarında metre maliyeti düşüyor.</p>"),
   P("Kalecik'te tel örgü; bağ, meyve bahçesi ve tarla çevresi için isteniyor. Gölbaşı'ndan 99 km; tel örgüyü kuruyoruz.",
     "<p>Kalecik'te tel örgü satan yer olarak bağ ve bahçe işlerini hasat takvimine göre planlıyoruz.</p>",
     "<p>Kalecik 713 m rakımla görece ılıman; bağlarda galvaniz tel ve beton direk, meyve bahçelerinde kuş ve yabani hayvana karşı daha sık "
     "gözlü tel. Eğimli bağlarda teli kademelendiriyoruz.</p>",
     "<p>Kalecik için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; bağ metrajları uzadıkça metre maliyeti düşüyor.</p>"),
 ),
 V("Evren", "evren", "Evren'de", "158 km", ["serefliko", "bala"],
   "2.927 (Ankara'nın en az nüfuslu ilçesi)", "222 km²", "13", "912 m", "OSB yok",
   [("Tarih", "Eski yerleşim Hirfanlı Baraj Gölü sularının altında kaldığı için 1957'de bugünkü yerine taşındı.")],
   [("Evren (Vikipedi)", "https://tr.wikipedia.org/wiki/Evren,_Ankara")],
   P("Evren, Ankara'nın en az nüfuslu ilçesi; beton direk ihtiyacı daha çok tarla, mera ve Hirfanlı kıyısındaki bahçelerden geliyor. "
     "Gölbaşı'ndan yaklaşık 158 km; toplu siparişle getiriyoruz.",
     "<p>Evren'de beton direk satan yer olarak uzak mesafe nedeniyle siparişleri toplu planlıyor, tek sevkiyatla getiriyoruz.</p>",
     "<p>Hirfanlı Baraj Gölü'nün su seviyesi yıllar içinde metrelerce değişiyor; kıyıya yakın parsellerde çiti su seviyesi değişimini hesaba "
     "katarak çekiyor, direkleri nemli zemine göre geniş temelle dikiyoruz.</p>",
     "<p>Evren'e 158 km için nakliye en büyük kalem; direk siparişini tel ve diğer malzemelerle birlikte vermenizi öneriyoruz. Ekim 2026'da 2 m düz direk 132–265 TL.</p>"),
   P("Evren'de jiletli tel daha çok tarım depoları ve çiftlikler için soruluyor. Gölbaşı'ndan 158 km; toplu işlerde takıyoruz.",
     "<p>Evren'de jiletli tel satan yer olarak uzak işleri fotoğraf ve ölçüyle önceden netleştirip tek seferde geliyoruz.</p>",
     "<p>Evren gibi küçük ve sakin ilçelerde jiletli tel çoğu zaman gereğinden ağır bir çözüm; depo ve ahırda tel örgü üstüne 2–3 sıra "
     "[[ankara-dikenli-tel|dikenli tel]] genelde yeterli. Yine de değerli ekipman varsa Y kol + helezon tel öneriyoruz.</p>",
     "<p>Evren için Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre; dikenli tel metresi 3–4 TL ile çok daha ekonomik.</p>"),
   P("Evren'de tel örgü; tarla, mera ve göl kıyısındaki bahçeler için isteniyor. Gölbaşı'ndan 158 km; toplu işlerde tel örgüyü kuruyoruz.",
     "<p>Evren'de tel örgü satan yer olarak uzak mesafeye rağmen geliyoruz; işi planlı yapıp tek seferde bitiriyoruz.</p>",
     "<p>Evren'in 13 mahallesinde tarla ve merada galvaniz tel ya da yalnız dikenli tel; Hirfanlı kıyısındaki bahçelerde nem ve su seviyesine "
     "göre direk temelini ayarlıyoruz.</p>",
     "<p>Evren için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; küçük işlerde nakliye ayrıca konuşulur.</p>"),
 ),
 V("Şereflikoçhisar", "serefliko", "Şereflikoçhisar'da", "132 km", ["evren", "bala", "haymana"],
   "32.831", "2.155 km²", "64", "947 m", "Şereflikoçhisar OSB (%58,7 dolu), Şereflikoçhisar Sanayi Sitesi (250 işyeri)",
   [("Coğrafya", "İlçe Tuz Gölü kıyısında; Tuz Gölü ile Hirfanlı Barajı arasında."),
    ("2026", "Mart 2026'da TBMM'de OSB'nin yeni yatırımlarla güçlendirilmesi istendi.")],
   [("Şereflikoçhisar (Vikipedi)", "https://tr.wikipedia.org/wiki/%C5%9Eerefliko%C3%A7hisar")],
   P("Şereflikoçhisar'da beton direk; OSB'deki tesisler, tuz ve tarım arazileri için isteniyor. Gölbaşı'ndan yaklaşık 132 km; toplu siparişle getirip dikiyoruz.",
     "<p>Şereflikoçhisar'da beton direk satan yer olarak OSB ve tarla işlerinde kamyon bazlı sevkiyat yapıyoruz.</p>",
     "<p>Şereflikoçhisar Tuz Gölü kıyısında; tuzlu toprak ve rüzgârla taşınan tuz metali hızla aşındırıyor. Burada demir boru direk yerine "
     "beton direk ciddi bir avantaj: beton direk paslanmıyor. Yine de direk içindeki demirin örtü betonu kalın, kaliteli direk seçmek önemli.</p>",
     "<p>Şereflikoçhisar'a 132 km için nakliye belirgin; OSB ve tarla işleri gibi büyük adetlerde direk başına payı düşük. Ekim 2026'da 2,4 m düz direk 190–275 TL.</p>"),
   P("Şereflikoçhisar'da jiletli tel; OSB'deki fabrikalar ve sanayi sitesindeki iş yerleri için isteniyor. Gölbaşı'ndan 132 km; ölçüp takıyoruz.",
     "<p>Şereflikoçhisar'da jiletli tel satan yer olarak OSB işlerinde faturalı çalışıyor, malzemeyi tek seferde getiriyoruz.</p>",
     "<p>Tuz Gölü kıyısındaki tuzlu hava galvaniz kaplamayı normalden hızlı yıpratıyor. Bu yüzden Şereflikoçhisar'da kalın galvaniz kaplamalı "
     "ya da paslanmaz (AISI 304) jiletli tel öneriyoruz; ilk maliyet yaklaşık %30 fazla ama uzun vadede kendini çıkarıyor.</p>",
     "<p>Şereflikoçhisar için Ekim 2026'da galvaniz helezon jiletli tel 45–110 TL/metre, paslanmaz 304 kilosu 195 TL civarında.</p>"),
   P("Şereflikoçhisar'da tel örgü; OSB parselleri, tarlalar ve tuz bölgesindeki tesisler için isteniyor. Gölbaşı'ndan 132 km; tel örgüyü kuruyoruz.",
     "<p>Şereflikoçhisar'da tel örgü satan yer olarak sanayi ve tarla işlerine malzemeli montajla geliyoruz.</p>",
     "<p>Tuzlu toprak ve hava nedeniyle Şereflikoçhisar'da çıplak galvaniz tel yerine PVC kaplı tel ve beton direk öneriyoruz; çift kat koruma "
     "tuzun teli yemesini geciktiriyor. Kesim ve bağlantı noktalarını da ayrıca koruyoruz.</p>",
     "<p>Şereflikoçhisar için montajlı tel örgü Ekim 2026'da 195–500 TL/metre; PVC kaplı tel tercihi aralığın üst kısmına çıkarıyor.</p>"),
 ),
]
