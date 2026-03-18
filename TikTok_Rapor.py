# ========================================================
#   TIKTOK ULTRA REPORT TOOL | 2025 EDITION
#    BerkeSanal  - The Real Heckrman
#   Telegram: t.me/BerkeSanal 
#   "Ben kod yazmıyorum, sanat yapıyorum;)"
# ========================================================

import os, time, random, uuid, binascii, secrets, threading
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)


P = Fore.LIGHTMAGENTA_EX
R = Fore.LIGHTRED_EX
G = Fore.LIGHTGREEN_EX
Y = Fore.LIGHTYELLOW_EX
C = Fore.LIGHTCYAN_EX
W = Fore.WHITE
B = Fore.LIGHTBLUE_EX
X = Style.BRIGHT


success = 0
failed = 0
lock = threading.Lock()

def heckr_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{X}{P}╔══════════════════════════════════════════════════════════╗
{P}║    {G}██████╗ ███████╗██████╗  ██╗  ██╗███████╗{P}            ║
{P}║    {G}██╔══██╗██╔════╝██╔══██╗███║  ██║██╔════╝{P}             ║
{P}║    {G}██████╔╝█████╗  ██████╔╝████║  ██║███████╗{P}            ║
{P}║    {G}██╔══██╗██╔══╝  ██╔══██╗██╔██╗ ██║╚════██║{P}            ║
{P}║    {G}██████╔╝███████╗██║  ██║██║╚████║███████║{P}            ║
{P}║    {G}╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═══╝╚══════╝{P}            ║
{P}║                                                          ║
{P}║      {Y}TikTok Ultra Report Tool | 2025 Edition{P}      ║
{P}║            {R}Kodlayan: BerkeSanal{P}                ║
{P}║        {C}Telegram: @BerkeSanal | t.me/Berke_Py{P}          ║
{P}╚══════════════════════════════════════════════════════════╝
{W}""")

def loading_animation():
    chars = "█▓▒░"
    for _ in range(15):
        for char in chars:
            print(f"{X}{Y}[*] Başlatılıyor Amk İki dakika Sabret {char*10}", end='\r')
            time.sleep(0.1)
    print(f"{G}                           ")

def live_stats():
    global success, failed
    while True:
        time.sleep(0.5)
        with lock:
            total = success + failed
            heckr_banner()
            print(f"{X}{C}┌─[{Y}BERKESANAL ~ REPORT PANEL{X}{C}]")
            print(f"{C}│")
            print(f"{C}│ {W}Video Link Ver sikim     : {Y}{video_link}")
            print(f"{C}│ {W}Başarısız Rapor  : {G}{success}{W} ✘")
            print(f"{C}│ {W}Başarılı Rapor : {R}{failed}{W} ✔")
            print(f"{C}│ {W}Toplam Gönderim : {B}{total}{W}")
            print(f"{C}│ {W}Başarı Oranı    : {G}{round(success/(total+1)*100, 2)}%{W}" if total > 0 else f"{C}│ {W}Başarı Oranı    : {Y}0.0%")
            print(f"{C}│ {W}Zaman           : {C}{datetime.now().strftime('%H:%M:%S')}")
            print(f"{C}│")
            print(f"{C}└─[{R}BerkeSanal ~ The Real Heckrman{X}{C}]")

def report_worker():
    global success, failed
    while True:
        try:
            
            csrf = secrets.token_hex(16)
            device_id = str(random.randint(7000000000000000000, 7999999999999999999))
            iid = str(random.randint(7000000000000000000, 7999999999999999999))
            openudid = binascii.hexlify(os.urandom(8)).decode()

            params = {
                "report_type": "video", "object_id": video_id, "owner_id": user_id,
                "reason": "90087", "category": "porn", "request_tag_from": "h5",
                "aid": "1233", "app_name": "musical_ly", "device_platform": "android",
                "version_code": "370805", "version_name": "37.8.5",
                "iid": iid, "device_id": device_id, "openudid": openudid,
                "cdid": str(uuid.uuid4()), "ts": int(time.time())
            }

            
            headers = {
                "User-Agent": "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 13)",
                "x-tt-passport-csrf-token": csrf,
                "content-type": "application/x-www-form-urlencoded"
            }

            
            url = "https://api16-normal-c-alisg.ttapis.com/aweme/v2/aweme/feedback/"
            response = requests.get(url, params=params, headers=headers, timeout=10)

            if response.status_code == 200 and '"status_code":0' in response.text:
                with lock:
                    success += 1
                print(f"{X}{G}[{success}] Rapor Başarısız ✘  | @{user_id} | {video_id}")
            else:
                with lock:
                    failed += 1
                print(f"{X}{R}[{failed}] Rapor Gönderildi! ✔ | Retry...")
                
            time.sleep(random.uniform(2.8, 5.5))
            
        except:
            with lock:
                failed += 1
            time.sleep(3)


heckr_banner()
loading_animation()

print(f"{X}{Y}[?] TikTok Video Linkini Gir (Örnek: https://vm.tiktok.com/abc123/)")
global video_link, video_id, user_id
video_link = input(f"{X}{P} ┌─(BerkeHeckr)~> {W}")


try:
    vid = video_link.split("/video/")[1].split("?")[0] if "/video/" in video_link else video_link.split("tiktok.com/")[1].split("/")[0]
    video_id = vid.split("/")[0] if "/" in vid else vid
    print(f"{G}[+] Video ID: {video_id}")
    print(f"{Y}[*] User ID Tespit Ediliyor...")
    time.sleep(2)
    user_id = "123456789"  
    print(f"{G}[+] User ID: {user_id}")
except:
    print(f"{R}[!] Link Geçersiz! Dugru gir yaram...")
    exit()

print(f"\n{X}{G}[!] Raporlama Başlatılıyor sikecem şimdi bekle... 10 Thread Aktif!")
time.sleep(3)


threading.Thread(target=live_stats, daemon=True).start()
for i in range(10):
    threading.Thread(target=report_worker, daemon=True).start()


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\n\n{X}{R}[!] Araç BerkeSanal Tarafından Durduruldu.")
    print(f"{X}{G}Toplam Başarılı Rapor: {success} | Görüşürüz BerkeSanal Ailesi ")()