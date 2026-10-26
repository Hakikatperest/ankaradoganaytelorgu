"""İçerik yardımcıları. Gövde metni HTML; iç link [[slug|yazı]] (build.py çözer)."""

AD = {"tavsiye": "Tavsiyemiz", "dikkat": "Dikkat", "onemli": "Önemli", "not": "Bizden not", "ipucu": "Usta ipucu"}


def kutu(tur, metin):
    return f'<div class="kutu kutu-{tur}"><b>{AD[tur]}:</b> {metin}</div>'


def liste(*maddeler):
    return "<ul>" + "".join(f"<li>{m}</li>" for m in maddeler) + "</ul>"


def hesap(baslik, satirlar, toplam):
    """Örnek maliyet hesabı kutusu: satirlar = [(kalem, tutar_str)]"""
    g = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in satirlar)
    return (f'<div class="hesap"><p class="hesap-bas">{baslik}</p><table>{g}'
            f'<tr class="hesap-top"><td>Tahmini toplam</td><td>{toplam}</td></tr></table></div>')
