#!/usr/bin/env python3
"""Logodan şeffaf amblem + favicon seti üretir.

Kaynak images/doganal-tel-orgu-logo.png lacivert degrade zeminli (saydamlık yok).
Zemin koyu ve doygun lacivert; amblem beyaz/gri zincir + turuncu. Alfa = parlaklık ya da turuncu oranı.
Çıktı: images/logo-amblem.png (şeffaf, amblem), images/logo-tam.png (şeffaf, yazılı), favicon seti.
"""
import os
from PIL import Image, ImageFilter

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(KOK, "images/doganal-tel-orgu-logo.png")


def seffaf(im):
    im = im.convert("RGB")
    px = im.load(); w, h = im.size
    out = Image.new("RGBA", im.size); po = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            parlak = (r + g + b) / 3
            turuncu = max(0, r - b)                      # turuncu: r yüksek, b düşük; zemin: b > r
            a = max(min(255, (parlak - 55) * 2.2), min(255, (turuncu - 40) * 2.5))
            a = int(max(0, a))
            po[x, y] = (r, g, b, a)
    return out


def main():
    src = Image.open(KAYNAK)
    tam = seffaf(src)
    bb = tam.split()[-1].point(lambda v: 255 if v > 40 else 0).getbbox()
    tam = tam.crop(bb)
    tam.thumbnail((640, 640), Image.LANCZOS)
    tam.save(os.path.join(KOK, "images/logo-tam.png"), optimize=True)
    # amblem: yazı bandının üstü (kaynakta ~y<0.63)
    W, H = src.size
    amb = seffaf(src.crop((0, 0, W, int(H * 0.625))))
    amb = amb.crop(amb.split()[-1].point(lambda v: 255 if v > 40 else 0).getbbox())
    amb.thumbnail((240, 240), Image.LANCZOS)
    amb.save(os.path.join(KOK, "images/logo-amblem.png"), optimize=True)
    # favicon: amblem lacivert kare üzerinde
    for s, ad in ((48, "favicon-48.png"), (192, "favicon-192.png"), (180, "../apple-touch-icon.png"), (512, "logo-512.png")):
        zemin = Image.new("RGBA", (s, s), (6, 29, 61, 255))
        a = amb.copy(); a.thumbnail((int(s * .86), int(s * .86)), Image.LANCZOS)
        zemin.alpha_composite(a, ((s - a.width) // 2, (s - a.height) // 2))
        zemin.convert("RGB").save(os.path.join(KOK, "images", ad))
    ico = Image.new("RGBA", (64, 64), (6, 29, 61, 255)); a = amb.copy(); a.thumbnail((58, 58), Image.LANCZOS)
    ico.alpha_composite(a, ((64 - a.width) // 2, (64 - a.height) // 2))
    ico.convert("RGB").save(os.path.join(KOK, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    # og için kare logo jpg (zeminli, olduğu gibi)
    src.convert("RGB").resize((630, 630), Image.LANCZOS).save(os.path.join(KOK, "images/logo-kare.jpg"), quality=85)
    print("logo tamam", tam.size, amb.size)


if __name__ == "__main__":
    main()
