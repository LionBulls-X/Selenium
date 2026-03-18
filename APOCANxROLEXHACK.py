
import os
import random

#KODLAYAN --> @amcasxd @C4kOzi

def banner():
    print("""   _   _  _____        _______ ____  
       APOxROLEX
                                   cahilsinix   """)
    print("----------------------------------------------------")
    print("[1] Şifre Kırıcı")
    print("[2] Ağ Tarama")
    print("[3] Exploit Kullanma")
    print("[4] Sosyal Mühendislik Aracı")
    print("[5] Veritabanı Sızma")
    print("[6] Geri Bildirim")
    print("[7] Çıkış")
    print("----------------------------------------------------")

def password_cracker():
    print("Şifre kırıcı başlatılıyor...")

def network_scanner():
    print("Ağ taraması başlatılıyor...")

def exploit():
    print("Exploit kullanma işlemi başlatılıyor...")

def social_engineering():
    print("Sosyal mühendislik aracı çalıştırılıyor...")

def database_hacking():
    print("Veritabanı sızma işlemi başlatılıyor...")

def feedback():
    print("Geri bildirim bölümüne hoş geldiniz. Lütfen yorumlarınızı ve önerilerinizi yazın:")
    feedback = input()
    print("Teşekkürler! Geri bildiriminiz alınmıştır.")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

banner()

while True:
    choice = input("Seçiminiz (1-7): ")

    if choice == "1":
        password_cracker()
    elif choice == "2":
        network_scanner()
    elif choice == "3":
        exploit()
    elif choice == "4":
        social_engineering()
    elif choice == "5":
        database_hacking()
    elif choice == "6":
        feedback()
    elif choice == "7":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen 1 ile 7 arasında bir sayı girin.")