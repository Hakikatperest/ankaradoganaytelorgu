"""Doğanay Tel Örgü — ortak veri (görseller, ilçeler, süreç, genel SSS). Kategori içerikleri: _src/icerik/.

⛔ Teyitsiz iddia yazma: üretim, garanti, yıl/deneyim, fiyat, "en ucuz/en iyi" — denetim.py listesinde. (7/24: kullanıcı 2026-10-30 hero için onayladı)
Görseller Unsplash stok (temsili): "bizim işimiz" diye sunma.
"""

# (dosya adı, alt metin) — kaynak img/stok/<ad>.jpg
# Kullanıcının gerçek iş fotoğrafları (images/*.webp) — "Uygulamamızdan" etiketiyle gösterilir
GERCEK = ["beton-direk-ve-tel-orgu", "tel-cit", "tel-orgu-cesidi", "tel-orgu-resmi", "tel-orgu-resmi2",
          # 2026-10-26 kullanıcının yüklediği 22 iş fotoğrafı
          "beton-direk6", "beton-direk-tel", "tel-orgu-sistemi", "kapi", "tel-orgu-kapi-panel", "bahce-kapisi", "koruma-kapisi",
          "bahce-teli5", "dikenli-tel4", "okul-teli", "tel-orgu3", "beton-direk", "tarlaya-tel2", "bahce-teli-kapi",
          "panel-tel3", "tarlaya-tel", "yesil-panel-tel", "dikenli-tel2", "dikenli-tel1", "tel-cim-1", "panel-tel-1", "panelcit"]
# anasayfa / hakkımızda galerisi (hepsi değil, seçki)
GALERI = ["beton-direk-ve-tel-orgu", "tel-orgu3", "beton-direk-tel", "tel-orgu-sistemi", "bahce-teli5", "beton-direk",
          "koruma-kapisi", "dikenli-tel4", "yesil-panel-tel", "tel-cit", "tarlaya-tel2", "tel-cim-1"]
AFIS = "ankara-doganay-tel-orgu"   # metinli marka afişi: ⛔ kırpma, üstüne bindirme yok

GORSEL = {
 "beton-direk-ve-tel-orgu": "Yol kenarı boyunca beton direkli galvaniz tel örgü, direk başlarında dikenli tel kolları",
 "tel-cit": "Fabrika önünde beton duvar üstüne yeşil panel çit ve spiral jiletli tel",
 "tel-orgu-cesidi": "Sanayi parseli sınırında beton direkli galvaniz tel örgü, üstte dikenli tel",
 "tel-orgu-resmi": "Boş arazi kenarında beton direkler arasında gerdirilmiş tel örgü ve dikenli tel",
 "tel-orgu-resmi2": "Sürülmüş tarla kenarında beton direkli tel örgü çit hattı",
 "beton-direk6": "Sürülmüş tarlada yeni dikilmiş beton çit direkleri, tel örgü öncesi direk hattı",
 "beton-direk-tel": "Y kollu beton direkler ve payandalı köşe direğiyle kurulmuş galvaniz tel örgü çit",
 "tel-orgu-sistemi": "Fabrika önünde beton duvar üstüne kurulmuş antrasit 3D panel çit hattı",
 "kapi": "Çam ağaçları arasındaki arazide yeşil panel çit hattı",
 "tel-orgu-kapi-panel": "Yeşil panel çit kapısı ve arkasında çim çit kaplı panel hattı",
 "bahce-kapisi": "Çakıllı bahçe girişinde çift kanatlı yeşil panel bahçe kapısı",
 "koruma-kapisi": "Ağaçlık arazi girişinde çift kanatlı yeşil panel araç kapısı",
 "bahce-teli5": "Villa bahçesinde tel çit üzerine kaplanmış yeşil çim çit",
 "dikenli-tel4": "Hobi bahçeleri arasında çim çit kaplı tel örgü ve üstünde spiral jiletli tel",
 "okul-teli": "Okul bahçesi sınırında çim çit kaplı tel çit",
 "tel-orgu3": "Doğanay ustası beton direkli galvaniz tel örgüyü gergi teline bağlıyor",
 "beton-direk": "Traktörle getirilen beton çit direklerinin sürülmüş tarlaya dikilmesi",
 "tarlaya-tel2": "Köy yolu kenarında payandalı beton direklerle çekilmiş tel örgü",
 "bahce-teli-kapi": "Arazi girişinde beton direkli tel örgü ve yeşil tel bahçe kapısı",
 "panel-tel3": "Apartman bahçe duvarı üstüne monte edilmiş yeşil panel çit",
 "tarlaya-tel": "Tarla kenarında payandalı beton köşe direği ve gerdirilmiş tel örgü",
 "yesil-panel-tel": "Site yürüyüş yolu boyunca çim çit kaplı yeşil panel çit",
 "dikenli-tel2": "Kuru otlu arsada beton direkli tel örgü çit hattı",
 "dikenli-tel1": "Ağaçlık arazide payandalı beton direklerle kurulan tel örgü çit",
 "tel-cim-1": "Okul binası önünde panel çite kaplanmış yeşil çim çit",
 "panel-tel-1": "Yol kenarındaki parselde yeşil panel çit hattı",
 "panelcit": "Köy yolu boyunca uzanan yeşil panel çit",
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
 "kafes-teli-altigen": "Ahşap çerçeveye gerilmiş altıgen gözlü kümes teli",
 "puntali-kafes-teli": "Kare gözlü puntalı kafes teli ve altıgen kümes teli, paslı demir kapı önünde",
 "kumes-teli": "Tel örgünün arkasında bekleyen tavuk",
 "cim-cit-duvar": "Mavi gökyüzü önünde sık yeşil çit duvarı",
 "cim-cit-yol": "Yürüyüş yolu boyunca uzanan sık yeşil çit",
}

# Hizmet bölgesi — kullanıcı teyit etmedi; "Ankara geneli" varsayıldı, sayfa AÇILMADI (yalnız liste)
# Hizmet verilen 20 ilçe (Kızılcahamam, Çamlıdere, Elmadağ, Çubuk, Beypazarı HARİÇ — kullanıcı 2026-10-26)
ILCELER = ["Gölbaşı", "Çankaya", "Etimesgut", "Yenimahalle", "Sincan", "Mamak", "Keçiören", "Altındağ", "Pursaklar",
           "Akyurt", "Kahramankazan", "Polatlı", "Haymana", "Bala", "Ayaş", "Güdül", "Nallıhan", "Kalecik", "Evren",
           "Şereflikoçhisar"]

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
