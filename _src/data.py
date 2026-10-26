"""Doğanay Tel Örgü — içerik verisi. Görünür metnin tek kaynağı.

⛔ Teyitsiz iddia yazma: üretim, garanti, yıl/deneyim, 7/24, fiyat, "en ucuz/en iyi" — denetim.py listesinde.
Görseller Unsplash stok (temsili): "bizim işimiz" diye sunma.
"""

# (dosya adı, alt metin) — kaynak img/stok/<ad>.jpg
# Kullanıcının gerçek iş fotoğrafları (images/*.webp) — "Uygulamamızdan" etiketiyle gösterilir
GERCEK = ["beton-direk-ve-tel-orgu", "tel-cit", "tel-orgu-cesidi", "tel-orgu-resmi", "tel-orgu-resmi2"]
AFIS = "ankara-doganay-tel-orgu"   # metinli marka afişi: ⛔ kırpma, üstüne bindirme yok

GORSEL = {
 "beton-direk-ve-tel-orgu": "Yol kenarı boyunca beton direkli galvaniz tel örgü, direk başlarında dikenli tel kolları",
 "tel-cit": "Fabrika önünde beton duvar üstüne yeşil panel çit ve spiral jiletli tel",
 "tel-orgu-cesidi": "Sanayi parseli sınırında beton direkli galvaniz tel örgü, üstte dikenli tel",
 "tel-orgu-resmi": "Boş arazi kenarında beton direkler arasında gerdirilmiş tel örgü ve dikenli tel",
 "tel-orgu-resmi2": "Sürülmüş tarla kenarında beton direkli tel örgü çit hattı",
 "ankara-doganay-tel-orgu": "Doğanay Tel Örgü tanıtım afişi: Dayanıklı Tel Örgü Sistemleri, telefon 0530 155 29 27",
 "panel-cit-jiletli-tel": "Uzun hat boyunca yeşil panel çit, üstünde spiral jiletli tel",
 "bahce-teli": "Çim alan önünde koyu renk örgü bahçe teli",
 "tel-orgu-yakin": "Yakından baklava gözlü tel örgü, arkada yeşillik",
 "panel-cit": "Gökyüzü önünde direklere bağlanmış tel çit",
 "jiletli-tel": "Tel örgü köşe direğinin üstünde spiral jiletli tel",
 "dikenli-tel": "Tel örgü çitin üstünde üç sıra dikenli tel ve eğimli kol",
 "dikenli-tel-tarla": "Tarla kenarında gergin tek sıra dikenli tel",
 "tel-orgu-kapi": "Çim sahaya açılan çift kanatlı tel örgü kapı",
 "arsa-cevirme": "Arazi kenarında üstü dikenli tel örgü çit",
 "spor-sahasi-teli": "Gökyüzüne doğru yükselen yüksek saha teli",
 "tel-orgu-doku": "Galvaniz tel örgünün baklava gözleri, yakın çekim",
}

HIZMETLER = [
 {
  "slug": "ankara-tel-orgu", "ad": "Tel Örgü", "baslik": "Ankara Tel Örgü Çit Montajı",
  "kisa": "Bahçe, arsa ve site çevresi için galvaniz ya da PVC kaplı örgü tel; direği dikilmiş, gerdirilmiş halde.",
  "gorsel": "beton-direk-ve-tel-orgu", "gorsel2": "tel-orgu-cesidi", "ikon": "orgu",
  "title": "Ankara Tel Örgü Çit Montajı | Doğanay Tel Örgü",
  "desc": "Ankara'da tel örgü çit: galvaniz veya PVC kaplı örgü tel, beton ya da demir direk, gergi teli ve montaj. Gölbaşı'ndan keşif için arayın.",
  "giris": [
   "Tel örgü, bir alanı çevirmenin en yaygın ve en ekonomik yolu. Bahçenizi, arsanızı, deponuzu ya da sitenizin "
   "çevresini çevirmek istiyorsanız çoğu zaman ilk konuşacağımız şey budur.",
   "Bir tel örgü çitin ömrünü telden çok direk, gergi ve montaj belirler. Direk sağlam oturmazsa ya da tel gerilmeden "
   "bağlanırsa çit birkaç kışta sarkar. Biz işe direkten başlıyoruz."],
  "secenek": [
   ("Galvaniz tel", "Çinko kaplı, gri renkli tel. Arsa, tarla ve depo çevresinde sık kullanılır."),
   ("PVC (plastik) kaplı tel", "Galvaniz telin üstü yeşil ya da antrasit kaplanır; bahçe ve konutta daha temiz görünür."),
   ("Göz aralığı ve tel kalınlığı", "Küçük hayvan, top ya da sadece sınır belirleme; ihtiyaca göre seçilir."),
   ("Direk", "Beton direk ya da boyalı/galvaniz demir boru; zemin ve yüksekliğe göre karar verilir."),
  ],
  "dikkat": [
   "Köşe ve uç direkleri payandayla desteklenmeli; gerilimi en çok onlar taşır.",
   "Tel, alt-orta-üst gergi telleriyle gerdirilerek bağlanmalı; yoksa ortası göbek yapar.",
   "Eğimli arazide tel, zemine göre kademelendirilmeli; altta boşluk kalmamalı.",
   "Komşu sınırında çalışmadan önce sınırın net olması gerekir.",
  ],
  "sss": [
   ("Tel örgü çitin metresi ne kadar?",
    "Fiyat; telin cinsine (galvaniz ya da PVC kaplı), yüksekliğe, direk tipine ve metraja göre değişir. Metrajı ve "
    "yüksekliği söylediğinizde size net fiyat veriyoruz."),
   ("Tel örgü kaç metre yükseklikte yapılır?",
    "Bahçe ve arsada genellikle 1,5–2 metre arası tercih edilir. Saha ve güvenlik çevresinde daha yüksek yapılabilir."),
   ("Beton direk mi demir direk mi?",
    "İkisi de kullanılır. Zemin, yükseklik ve görüntü beklentisine göre keşifte birlikte karar veriyoruz."),
  ],
 },
 {
  "slug": "panel-cit", "ad": "Panel Çit", "baslik": "Ankara Panel Çit",
  "kisa": "Kaynaklı, boyalı hazır panellerle düzgün ve sağlam çit; site, fabrika, okul ve müstakil ev çevresi için.",
  "gorsel": "tel-cit", "gorsel2": "panel-cit", "ikon": "panel",
  "title": "Ankara Panel Çit Montajı | Doğanay Tel Örgü",
  "desc": "Ankara'da panel çit montajı: boyalı kaynaklı panel, direk ve kelepçe ile düzgün hat. Site, fabrika ve müstakil ev çevresi için keşif.",
  "giris": [
   "Panel çit, kaynaklı telden hazırlanmış ve boyanmış panellerin direklere kelepçeyle bağlanmasıyla kurulur. Örgü tele "
   "göre daha rijittir; uzun hatlarda bile düz ve derli toplu durur.",
   "Site, fabrika, okul, otopark ve müstakil ev çevresinde sık tercih ediliyor. Üstüne jiletli tel eklenerek güvenliği "
   "artırılabilir."],
  "secenek": [
   ("Panel yüksekliği", "Bahçe sınırından fabrika çevresine kadar farklı yükseklikte panel kullanılabilir."),
   ("Renk", "Yeşil ve antrasit en yaygın renkler; binanın ve bahçenin görüntüsüne göre seçilir."),
   ("Direk ve bağlantı", "Panel, direğe kelepçeyle sabitlenir; direk betonla zemine oturtulur."),
   ("Ek güvenlik", "Panel üstüne jiletli ya da dikenli tel eklenebilir."),
  ],
  "dikkat": [
   "Panel hattı ip çekilerek kurulmalı; bir direğin kaçması tüm hattı bozar.",
   "Eğimli zeminde paneller basamaklı yerleştirilir, alt boşluklar kapatılır.",
   "Kesilen panel uçlarında boya kalkar; uygun boya ile kapatılmalıdır.",
   "Kapı yeri ve genişliği panel hesabından önce belirlenmelidir.",
  ],
  "sss": [
   ("Panel çit mi tel örgü mü?",
    "Panel çit daha düzgün ve rijit görünür; tel örgü ise daha ekonomiktir ve engebeli arazide kolay uyum sağlar. "
    "Alanınızı görünce hangisinin uygun olduğunu söyleriz."),
   ("Panel çit fiyatı neye göre değişir?",
    "Panel yüksekliği, tel kalınlığı, direk tipi, metraj ve kapı olup olmamasına göre değişir. Metrajı söyleyin, net fiyat verelim."),
   ("Panel çitin üstüne jiletli tel takılır mı?",
    "Evet. Direğe takılan kollarla ya da doğrudan panel üstüne jiletli tel eklenebilir."),
  ],
 },
 {
  "slug": "jiletli-tel", "ad": "Jiletli Tel", "baslik": "Ankara Jiletli Tel",
  "kisa": "Duvar, çit ve panel üstüne spiral jiletli tel; depo, şantiye ve fabrika çevresinde caydırıcı güvenlik.",
  "gorsel": "jiletli-tel", "gorsel2": "tel-cit", "ikon": "jilet",
  "title": "Ankara Jiletli Tel Montajı | Doğanay Tel Örgü",
  "desc": "Ankara'da jiletli tel montajı: duvar, tel örgü ve panel çit üstüne spiral jiletli tel. Depo, şantiye ve fabrika için keşfe gelelim.",
  "giris": [
   "Jiletli tel, keskin bıçaklı şeritlerin spiral halde açılmasıyla kurulan bir güvenlik telidir. Tek başına bir çit "
   "değildir; genellikle mevcut duvarın, tel örgünün ya da panel çitin üstüne eklenir.",
   "Depo, şantiye, fabrika, trafo ve tarım alanı gibi yerlerde içeri girişi zorlaştırmak için kullanılır."],
  "secenek": [
   ("Spiral çapı", "Duvar ve çit yüksekliğine göre farklı çapta spiral seçilir."),
   ("Duvar üstü", "Duvara sabitlenen demir kollar ya da Y/L şeklinde destekler üzerine kurulur."),
   ("Çit üstü", "Tel örgü ya da panel çit direklerine takılan kollar üzerinde taşınır."),
   ("Zemin tipi", "Gerektiğinde zemine yatay serilerek ikinci bir engel hattı oluşturulabilir."),
  ],
  "dikkat": [
   "Montaj kalın eldiven ve uygun ekipmanla yapılmalı; jiletli tel elle tutulmaz.",
   "Yaya yollarına ve komşu tarafına taşmayacak şekilde yönlendirilmelidir.",
   "Spiral, belli aralıklarla gergi teline bağlanmalı; yoksa zamanla sarkar.",
   "Yerleşim alanlarında kullanmadan önce belediye ve site kurallarına bakılmalıdır.",
  ],
  "sss": [
   ("Jiletli tel duvara nasıl takılır?",
    "Duvar üstüne demir kollar ya da destekler sabitlenir, üzerlerine gergi teli çekilir ve spiral jiletli tel bu tellere bağlanır."),
   ("Jiletli tel ile dikenli tel arasındaki fark ne?",
    "Dikenli tel, aralıklı dikenleri olan düz teldir. Jiletli tel ise keskin bıçaklı ve spiral yapıdadır; daha caydırıcıdır."),
   ("Mevcut tel örgümün üstüne jiletli tel eklenir mi?",
    "Direkler sağlamsa evet. Keşifte direklerin durumuna bakıyoruz."),
  ],
 },
 {
  "slug": "dikenli-tel", "ad": "Dikenli Tel", "baslik": "Ankara Dikenli Tel",
  "kisa": "Tarla, mera ve arsa sınırı için gergin dikenli tel; tel örgü üstüne ek sıra olarak da çekilir.",
  "gorsel": "tel-orgu-resmi", "gorsel2": "dikenli-tel-tarla", "ikon": "diken",
  "title": "Ankara Dikenli Tel Çekimi | Doğanay Tel Örgü",
  "desc": "Ankara'da dikenli tel çekimi: tarla, mera ve arsa sınırı, tel örgü ve duvar üstüne dikenli tel. Gölbaşı ve çevresi için arayın.",
  "giris": [
   "Dikenli tel, geniş alanları düşük maliyetle çevirmenin bilinen yoludur. Tarla, mera, bağ-bahçe ve arsa sınırında "
   "birkaç sıra halinde direkler arasında gerdirilerek çekilir.",
   "Tel örgü ya da duvarın üstüne bir iki sıra eklendiğinde de üstten geçişi zorlaştırır."],
  "secenek": [
   ("Sıra sayısı", "Sadece sınır belirlemek için az, hayvan için daha sık sıra çekilir."),
   ("Direk", "Ahşap, beton ya da demir direk; arazi ve bütçeye göre seçilir."),
   ("Tel örgü üstü", "Eğimli kollarla çitin üstüne bir ya da birkaç sıra eklenir."),
   ("Galvaniz tel", "Paslanmaya karşı galvaniz kaplı dikenli tel tercih edilir."),
  ],
  "dikkat": [
   "Dikenli tel gergin çekilmezse kısa sürede sarkar ve işlevini kaybeder.",
   "Uzun hatlarda belli aralıklarla ara gergi direği konmalıdır.",
   "Yol ve yaya tarafına yakın hatlarda dikkatli konumlandırılmalıdır.",
  ],
  "sss": [
   ("Tarlaya dikenli tel kaç sıra çekilir?",
    "Amaca göre değişir. Sınır belirlemek için az, hayvanı içeride ya da dışarıda tutmak için daha sık sıra gerekir."),
   ("Dikenli tel mi tel örgü mü?",
    "Geniş tarla ve merada dikenli tel daha ekonomiktir. Küçük hayvanların geçmemesi gereken yerde tel örgü daha uygundur."),
   ("Dikenli teli siz mi getiriyorsunuz?",
    "Malzemeli ya da yalnız işçilik çalışabiliriz; arayıp ihtiyacınızı söyleyin, birlikte netleştirelim."),
  ],
 },
 {
  "slug": "tel-orgu-kapi", "ad": "Çit Kapısı", "baslik": "Ankara Tel Örgü ve Panel Çit Kapısı",
  "kisa": "Çitinize uygun yaya ve araç kapısı; tek ya da çift kanatlı, kilit yerli.",
  "gorsel": "tel-orgu-kapi", "gorsel2": "bahce-teli", "ikon": "kapi",
  "title": "Ankara Çit Kapısı ve Bahçe Kapısı | Doğanay Tel Örgü",
  "desc": "Ankara'da tel örgü ve panel çit kapısı: tek veya çift kanatlı yaya ve araç kapısı, kilit yeri ile. Çitle birlikte ya da ayrıca yapılır.",
  "giris": [
   "Bir çitin en çok kullanılan ve en çok zorlanan yeri kapısıdır. Kapı direği sağlam oturmazsa kanat zamanla düşer, "
   "kilit tutmaz hale gelir.",
   "Tel örgü ya da panel çitinize uygun yaya ve araç kapısını çitle birlikte ya da sonradan ekliyoruz."],
  "secenek": [
   ("Yaya kapısı", "Tek kanatlı, bahçe ve arsa girişleri için."),
   ("Araç kapısı", "Çift kanatlı, araç geçişine göre genişlikte."),
   ("Dolgu", "Çitle aynı görünüm için tel örgü ya da panel dolgulu."),
   ("Kilit", "Asma kilit yeri ya da kilit karşılığı ile."),
  ],
  "dikkat": [
   "Kapı direkleri çit direklerinden daha güçlü seçilmeli ve iyi betonlanmalıdır.",
   "Kanadın açılacağı yönde zemin eğimi kontrol edilmeli; kapı yere sürtmemelidir.",
   "Araç kapısının genişliği, girecek en büyük araca göre belirlenmelidir.",
  ],
  "sss": [
   ("Mevcut çitime sonradan kapı eklenir mi?",
    "Evet. Kapı yerindeki tel ya da panel açılır, güçlü kapı direkleri dikilir ve kapı takılır."),
   ("Araç kapısı kaç metre olmalı?",
    "Girecek araca ve manevra alanına göre değişir; keşifte birlikte ölçüyoruz."),
   ("Kapı kilitli mi oluyor?",
    "Asma kilit yeri ya da kilit karşılığı bırakıyoruz; ihtiyacınızı söylemeniz yeterli."),
  ],
 },
 {
  "slug": "arsa-tarla-cevirme", "ad": "Arsa ve Tarla Çevirme", "baslik": "Ankara Arsa, Tarla ve Bahçe Çevirme",
  "kisa": "Arsa, tarla, bağ-bahçe ve şantiye çevresini tel örgü, dikenli tel ya da panelle çeviriyoruz.",
  "gorsel": "tel-orgu-resmi2", "gorsel2": "arsa-cevirme", "ikon": "arsa",
  "title": "Ankara Arsa ve Tarla Çevirme | Doğanay Tel Örgü",
  "desc": "Ankara'da arsa, tarla, bağ-bahçe ve şantiye çevirme: tel örgü, dikenli tel veya panel çit. Metrajı söyleyin, keşfe gelelim.",
  "giris": [
   "Arsanızı, tarlanızı ya da bağ evinizin bahçesini çevirmek istiyorsunuz ama hangi çitin uygun olduğundan emin "
   "değilseniz, işin bu kısmını birlikte düşünelim.",
   "Uzun ve engebeli hatlarda tel örgü ya da dikenli tel, düz ve görünür sınırlarda panel çit öne çıkar. Çoğu zaman "
   "ikisini birlikte kullanıyoruz: yol tarafı panel, arka taraf tel örgü gibi."],
  "secenek": [
   ("Arsa", "Sınırı belirlemek ve izinsiz kullanımı önlemek için tel örgü ya da panel."),
   ("Tarla ve mera", "Geniş alan için dikenli tel ya da tel örgü."),
   ("Bağ-bahçe", "Görüntüsü de önemli olduğu için PVC kaplı tel örgü ya da panel."),
   ("Şantiye", "Hızlı kurulan, gerektiğinde jiletli tel eklenen çevirme."),
  ],
  "dikkat": [
   "Sınır noktaları tapu ve kadastro bilgisine göre belli olmalı; çit sınırdan kaymamalıdır.",
   "Eğimli arazide tel, zemine göre kademelendirilmelidir.",
   "Kapı yeri ve sayısı baştan planlanmalıdır.",
   "Ulaşımı zor arazilerde malzeme indirme yeri önceden konuşulmalıdır.",
  ],
  "sss": [
   ("Arsa çevirmek için hangi tel uygun?",
    "Bütçe, görünüm ve güvenlik ihtiyacına göre tel örgü, panel çit ya da dikenli tel kullanılabilir. Metrajı ve arsanın "
    "konumunu söyleyin, önerimizi yapalım."),
   ("Sınırı nasıl belirliyorsunuz?",
    "Çit, sizin gösterdiğiniz ve tapu/kadastroya göre belli olan sınır noktalarına göre çekilir."),
   ("Ankara dışındaki arsaya geliyor musunuz?",
    "Gölbaşı'ndayız ve Ankara'da çalışıyoruz. Uzak bir yer için arayıp sorun, durumu konuşalım."),
  ],
 },
 {
  "slug": "spor-sahasi-teli", "ad": "Saha Teli", "baslik": "Ankara Spor Sahası ve Halı Saha Teli",
  "kisa": "Halı saha, okul bahçesi ve spor alanı çevresine yüksek tel örgü; top dışarı çıkmasın.",
  "gorsel": "spor-sahasi-teli", "gorsel2": "tel-orgu-doku", "ikon": "saha",
  "title": "Ankara Halı Saha ve Spor Sahası Teli | Doğanay Tel Örgü",
  "desc": "Ankara'da halı saha, okul bahçesi ve spor sahası teli: yüksek tel örgü ve direk sistemi. Saha ölçüsünü söyleyin, keşfe gelelim.",
  "giris": [
   "Spor sahası teli, normal bir bahçe çitinden farklıdır: daha yüksektir, topun çarpmasına dayanmalı ve uzun süre "
   "gergin kalmalıdır.",
   "Halı saha, okul bahçesi, basketbol ve tenis alanı gibi yerlerin çevresine yüksek tel örgü yapıyoruz."],
  "secenek": [
   ("Yükseklik", "Sahanın türüne ve çevresine göre belirlenir; kale arkaları genellikle daha yüksek tutulur."),
   ("Direk", "Yüksek tel için daha kalın ve derine betonlanan demir direk."),
   ("Tel", "Top darbesine dayanacak kalınlıkta galvaniz ya da PVC kaplı örgü tel."),
   ("Kapı", "Bakım ve giriş için yaya kapısı."),
  ],
  "dikkat": [
   "Yüksek direkler rüzgâr yükü taşır; temel derinliği buna göre olmalıdır.",
   "Tel, ara gergi telleriyle birkaç sıra halinde gerdirilmelidir.",
   "Saha zemini yapılmadan önce direk yerleri planlanmalıdır.",
  ],
  "sss": [
   ("Halı saha teli kaç metre olmalı?",
    "Sahanın türü ve çevresine göre değişir. Ölçüyü ve sahanın yerini söylerseniz önerimizi yapalım."),
   ("Eski saha telini yeniliyor musunuz?",
    "Direkler sağlamsa yalnız tel yenilenebilir; değilse direklerle birlikte yeniliyoruz."),
   ("Okul ve kurumlara çalışıyor musunuz?",
    "Evet, kurum ve site yönetimleriyle de çalışıyoruz. Arayıp ihtiyacınızı anlatın."),
  ],
 },
]

# Hizmet bölgesi — kullanıcı teyit etmedi; "Ankara geneli" varsayıldı, sayfa AÇILMADI (yalnız liste)
ILCELER = ["Gölbaşı", "Çankaya", "Etimesgut", "Yenimahalle", "Sincan", "Mamak", "Keçiören", "Altındağ",
           "Pursaklar", "Elmadağ", "Bala", "Haymana", "Polatlı", "Kahramankazan"]

SUREC = [
 ("Arayın, anlatın", "Alanın yerini, yaklaşık metrajını ve ne için çevirmek istediğinizi söyleyin. Fotoğraf atarsanız daha da iyi."),
 ("Keşif ve ölçü", "Yerinde metrajı, eğimi, zemini ve kapı yerlerini ölçüyoruz; tel ve direk tipine birlikte karar veriyoruz."),
 ("Net fiyat", "Malzeme ve işçiliği ayrı ayrı konuşuyoruz; sürpriz kalem çıkmasın."),
 ("Direk ve montaj", "Direkleri ip hattında dikip betonluyoruz, beton oturunca teli ya da panelleri gerdirip bağlıyoruz."),
 ("Teslim", "Kapıları ayarlıyor, hattı birlikte geziyor ve alanı temiz teslim ediyoruz."),
]

GENEL_SSS = [
 ("Tel örgü fiyatları neye göre belirleniyor?",
  "Telin cinsi, yükseklik, direk tipi, toplam metraj, zemin durumu ve kapı sayısı fiyatı belirler. Metrajı ve yaklaşık "
  "yüksekliği söylediğinizde net fiyat veriyoruz."),
 ("Keşfe geliyor musunuz?",
  "Evet. Gölbaşı'ndayız; Ankara'daki işler için yerinde ölçü almaya geliyoruz. Gün ve saati telefonda birlikte ayarlıyoruz."),
 ("Malzemeyi ben alsam olur mu?",
  "Olur; malzemeli ya da yalnız işçilik çalışabiliriz. Hangi malzemenin ne kadar gerektiğini biz söylüyoruz."),
 ("Montaj kaç günde biter?",
  "Metraja, zemine ve direk tipine göre değişir. Beton direkler için betonun oturması beklenir. Süreyi keşiften sonra net söylüyoruz."),
]
