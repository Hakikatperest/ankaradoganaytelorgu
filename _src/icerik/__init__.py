"""9 kategori içeriği. Sıra = menü/kart sırası.

Fiyatlar Ekim 2026 piyasa araştırması (2026-10-26). ⛔ Rakip Ankara imalatçı sitelerine (panelcitankara/citbu) LİNK VERME;
rakamları "Ankara imalatçı listesi" olarak kaynaksız an. Doğanay'ın kendi fiyatı YOK (kullanıcı: piyasa aralığı yaz).
"""
from .tel_orgu import K as TEL_ORGU
from .dikenli_tel import K as DIKENLI
from .kafes_tel import K as KAFES
from .panel_cit import K as PANEL
from .jiletli_tel import K as JILETLI
from .cim_cit import K as CIM
from .cit_kapisi import K as KAPI
from .arsa_cevirme import K as ARSA
from .saha_teli import K as SAHA

KATEGORILER = [TEL_ORGU, DIKENLI, KAFES, PANEL, JILETLI, CIM, KAPI, ARSA, SAHA]
FIYAT_TARIH = "Ekim 2026"
# TCMB döviz satış kuru, 23.10.2026 bülteni (2026/201)
KUR = {"USD": (49.6540, "TCMB, 23 Ekim 2026"), "EUR": (55.5997, "TCMB, 23 Ekim 2026"), "GBP": (66.5325, "TCMB, 23 Ekim 2026")}
