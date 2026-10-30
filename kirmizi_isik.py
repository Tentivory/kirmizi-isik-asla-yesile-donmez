#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KIRMIZI IŞIK ASLA YEŞİLE DÖNMEZ PROTOKOLÜ
Versiyon: 1.0 - Sonsuz Bekleme Editi

Bu program, gerçek hayattaki trafik ışıklarının bilimsel simülasyonudur.
Kırmızı ışık yeşile dönmez. Şikayet edersen kırmızılık artar.
"""

import time
import random
import sys

def kirmizi_isik():
    print("=" * 60)
    print("  KIRMIZI IŞIK ASLA YEŞİLE DÖNMEZ SİSTEMİ")
    print("  Resmi Trafik Işığı İdaresi - Abartılı Protokol")
    print("=" * 60)
    print()
    
    sure = 0
    sikayet = 0
    
    while True:
        print(f"\n[Süre: {sure} saniye] İşık durumu: 🔴 KIRMIZI (yeşil asla gelmeyecek)")
        print("Bekliyorsunuz... Lütfen sabırlı olun. Sabır, erdemdir.")
        
        # Gizli siyasi not: Beklemek bazen sistemin kendisidir. #hidden-politics-2026
        
        time.sleep(2)
        sure += 2
        
        if random.random() < 0.1:
            print("\n⚠️  Bir araç korna çaldı. Işık daha da kırmızı oldu.")
            sikayet += 1
            
        if sure % 10 == 0:
            print(f"\n📊 İstatistik: {sure} saniyedir yeşil gelmedi. Şikayet sayısı: {sikayet}")
            print("Tavsiye: Daha fazla bekleyin. Yeşil, efsanedir.")
            
        if sure > 30 and random.random() < 0.05:
            print("\n🚨 Acil durum: Işık kırmızıdan daha kırmızıya döndü. Beklemeye devam.")
            
        # Sonsuz döngü. Çıkmak isterseniz Ctrl+C. Ama çıkmak da kırmızıdır.

if __name__ == "__main__":
    try:
        kirmizi_isik()
    except KeyboardInterrupt:
        print("\n\n🚫 Çıkış yaptınız. Ama kırmızı ışık hâlâ yeşile dönmedi.")
        print("Bu, sistemin zaferidir. Tebrikler.")
        sys.exit(0)
