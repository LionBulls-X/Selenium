#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instagram Takip Kontrol Aracı - Termux Edition
API tabanlı, tarayıcı gerektirmez
"""

from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ChallengeRequired, PleaseWaitFewMinutes
import time
import json
import os

def banner():
    print("""
    ╔═══════════════════════════════════════╗
    ║     Instagram Takipçi Kontrolü       ║
    ║          Termux Edition              ║
    ║        LionBulls-X / 2025            ║
    ╚═══════════════════════════════════════╝
    """)

def save_session(cl, username):
    """Oturum bilgilerini kaydet"""
    session_file = f"{username}_session.json"
    try:
        cl.dump_settings(session_file)
        print(f"[✓] Oturum kaydedildi: {session_file}")
    except Exception as e:
        print(f"[!] Oturum kaydedilemedi: {e}")

def load_session(cl, username):
    """Kaydedilmiş oturumu yükle"""
    session_file = f"{username}_session.json"
    if os.path.exists(session_file):
        try:
            cl.load_settings(session_file)
            cl.login(username, "")  # Boş şifre ile oturum kontrolü
            print(f"[✓] Kaydedilmiş oturum yüklendi")
            return True
        except:
            print(f"[!] Oturum yüklenemedi, yeniden giriş gerekiyor")
            return False
    return False

def login_instagram(username, password):
    """Instagram'a giriş yap"""
    cl = Client()
    
    # Önce kaydedilmiş oturumu dene
    if load_session(cl, username):
        return cl
    
    try:
        print(f"\n[*] {username} ile giriş yapılıyor...")
        
        # Delay ekle (spam koruması)
        cl.delay_range = [1, 3]
        
        cl.login(username, password)
        print("[✓] Giriş başarılı!")
        
        # Oturumu kaydet
        save_session(cl, username)
        
        return cl
        
    except ChallengeRequired:
        print("\n[!] Instagram güvenlik kontrolü gerektiriyor!")
        print("[!] Lütfen şu adımları takip edin:")
        print("    1. Normal tarayıcıdan Instagram'a giriş yapın")
        print("    2. Güvenlik kontrolünü tamamlayın")
        print("    3. Birkaç dakika bekleyip tekrar deneyin")
        return None
        
    except PleaseWaitFewMinutes:
        print("[!] Çok fazla istek! Lütfen 5-10 dakika bekleyin.")
        return None
        
    except LoginRequired:
        print("[✗] Hatalı kullanıcı adı veya şifre!")
        return None
        
    except Exception as e:
        print(f"[✗] Giriş hatası: {e}")
        return None

def get_user_info(cl, username):
    """Kullanıcı bilgilerini al"""
    try:
        print(f"\n[*] @{username} profil bilgileri alınıyor...")
        user_info = cl.user_info_by_username(username)
        print(f"[✓] Profil bulundu: {user_info.full_name}")
        return user_info
    except Exception as e:
        print(f"[✗] Profil bulunamadı: {e}")
        return None

def get_followers(cl, user_id, username):
    """Kullanıcının takipçilerini al"""
    try:
        print(f"\n[*] @{username} takipçileri alınıyor...")
        print("[!] Bu işlem birkaç dakika sürebilir...")
        
        followers = cl.user_followers(user_id)
        follower_usernames = set(followers.keys())
        
        print(f"[✓] {len(follower_usernames)} takipçi bulundu")
        return follower_usernames
        
    except Exception as e:
        print(f"[✗] Takipçiler alınamadı: {e}")
        return None

def get_following(cl, user_id, username):
    """Kullanıcının takip ettiklerini al"""
    try:
        print(f"\n[*] @{username} takip ettikleri alınıyor...")
        print("[!] Bu işlem birkaç dakika sürebilir...")
        
        following = cl.user_following(user_id)
        following_usernames = set(following.keys())
        
        print(f"[✓] {len(following_usernames)} takip edilen bulundu")
        return following_usernames
        
    except Exception as e:
        print(f"[✗] Takip edilenler alınamadı: {e}")
        return None

def find_non_followers(followers, following):
    """Takip etmeyenleri bul"""
    non_followers = following - followers
    return non_followers

def save_to_file(username, non_followers):
    """Sonuçları dosyaya kaydet"""
    filename = f"{username}_takip_etmeyenler.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"=== @{username} Takip Etmeyenler ===\n")
            f.write(f"Toplam: {len(non_followers)} kişi\n\n")
            for user in sorted(non_followers):
                f.write(f"@{user}\n")
        print(f"\n[✓] Sonuçlar '{filename}' dosyasına kaydedildi")
        return filename
    except Exception as e:
        print(f"[✗] Dosya kaydedilemedi: {e}")
        return None

def main():
    banner()
    
    # Kullanıcı bilgileri
    print("\n[!] Kendi Instagram hesabınızla giriş yapın:")
    print("[!] (Sadece takipçi kontrolü için kullanılacak)")
    my_username = input("\n[?] Kullanıcı adınız: ").strip()
    my_password = input("[?] Şifreniz: ").strip()
    
    # Giriş yap
    cl = login_instagram(my_username, my_password)
    if not cl:
        print("\n[✗] Program sonlandırılıyor...")
        return
    
    # Rate limiting için bekle
    time.sleep(2)
    
    # Kontrol edilecek kullanıcı
    print("\n" + "="*50)
    target_username = input("[?] Kontrol edilecek kullanıcı adı: ").strip()
    
    # Kullanıcı bilgilerini al
    user_info = get_user_info(cl, target_username)
    if not user_info:
        return
    
    user_id = user_info.pk
    
    # Rate limiting
    time.sleep(2)
    
    # Takipçileri al
    followers = get_followers(cl, user_id, target_username)
    if followers is None:
        return
    
    # Rate limiting
    time.sleep(2)
    
    # Takip ettiklerini al
    following = get_following(cl, user_id, target_username)
    if following is None:
        return
    
    # Takip etmeyenleri bul
    print("\n[*] Takip etmeyenler hesaplanıyor...")
    non_followers = find_non_followers(followers, following)
    
    # Sonuçları göster
    print("\n" + "="*50)
    print(f"[✓] SONUÇLAR:")
    print(f"    Takipçi sayısı: {len(followers)}")
    print(f"    Takip edilen: {len(following)}")
    print(f"    Takip etmeyen: {len(non_followers)}")
    print("="*50)
    
    if len(non_followers) > 0:
        print(f"\n[!] @{target_username} hesabını takip etmeyenler:\n")
        for i, user in enumerate(sorted(non_followers), 1):
            print(f"    {i}. @{user}")
        
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
