"""Ankara ilçe × ürün sayfaları verisi.

20 ilçe (Kızılcahamam, Çamlıdere, Elmadağ, Çubuk, Beypazarı HARİÇ) × 3 ürün = 60 sayfa, kullanıcı 2026-10-26 onayladı.
"Fiyatları" ve "Satan yerler" AYNI sayfada (aynı arama niyeti; ayrı sayfa = kopya riski).
Özgünlük: her ilçe × ürün için ayrı yazılmış giris/satan/uygulama/fiyat paragrafı + ilçenin kaynaklı verisi
(nüfus, OSB, arazi, iklim, mesafe) + ilçeden ilçeye değişen bölüm sırası ve başlık kalıbı.
⛔ İlçe verisini uydurma; kaynağı olmayan rakamı yazma. Fotoğraflar ilçeye ait DEĞİL — "X'te yaptığımız iş" deme.
"""
import json, os
from ilce_veri import VERI

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MAH = json.load(open(os.path.join(KOK, "_src/data/ankara_mahalleler.json"), encoding="utf-8"))

URUNLER = [
 {"k": "beton", "ek": "beton-direk", "ad": "Beton Direk", "kisa": "beton direk", "kat": "ankara-beton-direk", "ikon": "direk",
  "title": ["{ad} Beton Direk Fiyatları ve Satan Yerler (2026)", "Ankara {ad} Beton Direk Fiyatları ve Satan Yerler",
            "{ad} Beton Direk Satan Yerler ve Fiyatları 2026"],
  "desc": "{ad} beton direk fiyatları ve satan yer: düz, Y kollu ve köşe beton çit direği, Gölbaşı'ndan {km} sevkiyat ve montaj. "
          "Doğanay Tel Örgü sipariş hattı.",
  "gorsel": ["beton-direk-tel", "beton-direk", "beton-direk6", "tarlaya-tel", "dikenli-tel1", "tel-orgu3"],
  "bolum_sira": [["satan", "fiyat", "arazi"], ["arazi", "satan", "fiyat"], ["fiyat", "arazi", "satan"]],
  "sss": [
   ("{ad} beton direk nereden alınır?",
    "{ad} için beton direği Gölbaşı'ndaki Doğanay Tel Örgü'den alabilirsiniz; atölyemiz {ad} merkezine yaklaşık {km} mesafede. "
    "Adet ve boyu söyleyin, sevkiyat gününü telefonda verelim."),
   ("{ad} beton direk fiyatı ne kadar?",
    "Ekim 2026 piyasasında düz beton çit direği boyuna göre yaklaşık 140–500 TL/adet aralığında; Y kollu ve köşe direkleri daha "
    "pahalıdır. Net fiyat adet, boy ve teslim yerine göre verilir."),
   ("{de} beton direği siz mi dikiyorsunuz?",
    "Evet; istenirse yalnız direk satıyor, istenirse direği dikip tel örgüyü de çekiyoruz."),
  ]},
 {"k": "jilet", "ek": "jiletli-tel", "ad": "Jiletli Tel", "kisa": "jiletli tel", "kat": "ankara-jiletli-tel", "ikon": "jilet",
  "title": ["{ad} Jiletli Tel Fiyatları ve Satan Yerler (2026)", "Ankara {ad} Jiletli Tel Fiyatları ve Satan Yerler",
            "{ad} Jiletli Tel Satan Yerler ve Fiyatları 2026"],
  "desc": "{ad} jiletli tel fiyatları ve satan yer: helezon ve düzlemsel jiletli tel, duvar ve çit üstü montaj, Gölbaşı'ndan {km} "
          "sevkiyat. Sipariş hattı.",
  "gorsel": ["tel-cit", "dikenli-tel4", "jiletli-tel", "beton-direk-tel"],
  "bolum_sira": [["fiyat", "satan", "arazi"], ["satan", "arazi", "fiyat"], ["arazi", "fiyat", "satan"]],
  "sss": [
   ("{de} jiletli tel satan yer neresi?",
    "{ad} için jiletli teli Gölbaşı'ndaki Doğanay Tel Örgü getiriyor; atölyemiz {ad} merkezine yaklaşık {km} uzaklıkta. "
    "Metrajı ve takılacağı yeri (duvar, tel örgü, panel) söylemeniz yeterli."),
   ("{ad} jiletli tel fiyatı ne kadar?",
    "Ekim 2026 piyasasında galvaniz helezon jiletli tel çapına göre yaklaşık 45–110 TL/metre (montaj hariç); paslanmaz "
    "yaklaşık %30 daha pahalı."),
   ("{de} jiletli teli takıyor musunuz?",
    "Evet. Jiletli tel montajı eldiven, gözlük ve doğru ekipman ister; satın aldığınız teli de, bizden aldığınızı da takıyoruz."),
  ]},
 {"k": "orgu", "ek": "tel-orgu", "ad": "Tel Örgü", "kisa": "tel örgü", "kat": "ankara-tel-orgu", "ikon": "orgu",
  "title": ["{ad} Tel Örgü Fiyatları ve Satan Yerler (2026)", "Ankara {ad} Tel Örgü Fiyatları ve Satan Yerler",
            "{ad} Tel Örgü Satan Yerler ve Fiyatları 2026"],
  "desc": "{ad} tel örgü fiyatları ve satan yer: galvaniz ve PVC kaplı örgü tel, beton direkli montaj, Gölbaşı'ndan {km} "
          "sevkiyat. Doğanay Tel Örgü sipariş hattı.",
  "gorsel": ["tel-orgu3", "tel-orgu-resmi2", "tarlaya-tel2", "dikenli-tel2", "bahce-teli-kapi", "beton-direk-ve-tel-orgu"],
  "bolum_sira": [["arazi", "fiyat", "satan"], ["fiyat", "satan", "arazi"], ["satan", "arazi", "fiyat"]],
  "sss": [
   ("{de} tel örgü satan yer neresi?",
    "{ad} için tel örgüyü Gölbaşı'ndaki Doğanay Tel Örgü getiriyor ve kuruyor; atölyemiz {ad} merkezine yaklaşık {km} uzaklıkta."),
   ("{ad} tel örgü fiyatı ne kadar?",
    "Ekim 2026 piyasasında montajlı tel örgü çit yaklaşık 195–500 TL/metre; tel kalınlığı, yükseklik ve direk tipine göre değişir."),
   ("{de} tel örgü montajı kaç günde biter?",
    "Metraja, zemine ve direk tipine göre değişir; beton direklerde betonun oturması beklenir. Süreyi keşiften sonra net söylüyoruz."),
  ]},
]


def _ilce(v):
    v = dict(v)
    v["mahalleler"] = _MAH.get(v["ad"], [])
    return v


ILCE = [_ilce(v) for v in VERI]
