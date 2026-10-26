"""Doğanay Tel Örgü — ortak veri (görseller, ilçeler, süreç, genel SSS). Kategori içerikleri: _src/icerik/.

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
 "kafes-teli-altigen": "Ahşap çerçeveye gerilmiş altıgen gözlü kümes teli",
 "puntali-kafes-teli": "Kare gözlü puntalı kafes teli ve altıgen kümes teli, paslı demir kapı önünde",
 "kumes-teli": "Tel örgünün arkasında bekleyen tavuk",
 "cim-cit-duvar": "Mavi gökyüzü önünde sık yeşil çit duvarı",
 "cim-cit-yol": "Yürüyüş yolu boyunca uzanan sık yeşil çit",
}

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
