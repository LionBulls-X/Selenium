#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instagram Takip Kontrol Aracı (Termux Uyumlu)
Selenium yerine Instaloader kullanır
"""

import instaloader
from getpass import getpass
import time

def banner():
    print("""
    ╔═══════════════════════════════════════╗
    ║   Instagram Takip Kontrol Aracı      ║
    ║          Termux Edition              ║
    ║        LionBulls-X / 2025            ║
    ╚═══════════════════════════════════════╝
    """)

def login_instagram(username, password):
    """Instagram'a giriş yap"""
    L = instaloader.Instaloader()
    
    try:
        print(f"\n[*] {username} ile giriş yapılıyor...")
        L.login(username, password)
        print("[✓] Giriş başarılı!")
        return L
    except instaloader.exceptions.BadCredentialsException:
        print("[✗] Hatalı kullanıcı adı veya şifre!")
        return None
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("[!] İki faktörlü kimlik doğrulama gerekli!")
        code = input("[?] Doğrulama kodunu girin: ")
        try:
            L.two_factor_login(code)
            print("[✓] Giriş başarılı!")
            return L
        except:
            print("[✗] Doğrulama başarısız!")
            return None
    except Exception as e:
        print(f"[✗] Giriş hatası: {e}")
        return None

def get_followers(L, username):
    """Kullanıcının takipçilerini al"""
    try:
        print(f"\n[*] @{username} kullanıcısının takipçileri alınıyor...")
        profile = instaloader.Profile.from_username(L.context, username)
        followers = set(profile.get_followers())
        print(f"[✓] {len(followers)} takipçi bulundu")
        return followers
    except Exception as e:
        print(f"[✗] Takipçiler alınamadı: {e}")
        return None

def get_followees(L, username):
    """Kullanıcının takip ettiklerini al"""
    try:
        print(f"\n[*] @{username} kullanıcısının takip ettikleri alınıyor...")
        profile = instaloader.Profile.from_username(L.context, username)
        followees = set(profile.get_followees())
        print(f"[✓] {len(followees)} takip edilen hesap bulundu")
        return followees
    except Exception as e:
        print(f"[✗] Takip edilenler alınamadı: {e}")
        return None

def find_non_followers(followers, followees):
    """Takip etmeyenleri bul"""
    non_followers = followees - followers
    return non_followers

def save_to_file(username, non_followers):
    """Sonuçları dosyaya kaydet"""
    filename = f"{username}_takip_etmeyenler.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=== @{username} Takip Etmeyenler ===\n")
            f.write(f"Toplam: {len(non_followers)} kişi\n\n")
            for user in sorted(non_followers, key=lambda x: x.username):
                f.write(f"@{user.username}\n")
        print(f"\n[✓] Sonuçlar '{filename}' dosyasına kaydedildi")
        return filename
    except Exception as e:
        print(f"[✗] Dosya kaydedilemedi: {e}")
        return None

def main():
    banner()
    
    # Kullanıcı bilgileri
    print("\n[!] Instagram giriş bilgilerinizi girin:")
    my_username = input("[?] Kullanıcı adınız: ").strip()
    my_password = getpass("[?] Şifreniz (görünmez): ")
    
    # Giriş yap
    L = login_instagram(my_username, my_password)
    if not L:
        print("\n[✗] Program sonlandırılıyor...")
        return
    
    # Kontrol edilecek kullanıcı
    print("\n" + "="*50)
    target_username = input("[?] Kontrol edilecek kullanıcı adı: ").strip()
    
    # Takipçileri al
    followers = get_followers(L, target_username)
    if followers is None:
        return
    
    # Takip ettiklerini al
    followees = get_followees(L, target_username)
    if followees is None:
        return
    
    # Takip etmeyenleri bul
    print("\n[*] Takip etmeyenler hesaplanıyor...")
    non_followers = find_non_followers(followers, followees)
    
    # Sonuçları göster
    print("\n" + "="*50)
    print(f"[✓] SONUÇLAR:")
    print(f"    Takipçi sayısı: {len(followers)}")
    print(f"    Takip edilen: {len(followees)}")
    print(f"    Takip etmeyen: {len(non_followers)}")
    print("="*50)
    
    if len(non_followers) > 0:
        print(f"\n[!] @{target_username} hesabını takip etmeyenler:\n")
        for i, user in enumerate(sorted(non_followers, key=lambda x: x.username), 1):
            print(f"    {i}. @{user.username}")
            if i % 20 == 0:  # Her 20 kişide bir ara ver
                time.sleep(2)
        
        # Dosyaya kaydet
        save_choice = input("\n[?] Sonuçları dosyaya kaydetmek ister misiniz? (e/h): ")
        if save_choice.lower() == 'e':
            save_to_file(target_username, non_followers)
    else:
        print(f"\n[✓] Tebrikler! Takip ettiğin herkes seni de takip ediyor.")
    
    print("\n[✓] İşlem tamamlandı!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Program kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\n[✗] Beklenmeyen hata: {e}")
