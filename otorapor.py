import subprocess
import sys
import os
import time

try:
    import requests
    import random
    import string
except ImportError:
    print("Gerekli modüller kuruluyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests
    import random
    import string

KIRMIZI = '\033[91m'
SIFIRLA = '\033[0m'

def proxy_listesi_al():
    try:
       
        yanit = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", timeout=10)
        if yanit.status_code == 200:
            return yanit.text.splitlines()
    except:
        return []
    return []

def telefon_olustur():
    rakamlar = ''.join(random.choice('0123456789') for _ in range(10))
    on_ek = random.choice(["+1", "+7", "+44", "+49", "+33", "+39", "+34", "+61", "+81", "+90", "+380"])
    return on_ek + rakamlar

def email_olustur():
    kullanici_adi = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(7, 12)))
    alan_adi = random.choice(["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "protonmail.com", "live.com", "yandex.com"])
    return f"{kullanici_adi}@{alan_adi}"

def isim_olustur():
    isimler = ["Ahmet", "Mehmet", "Mustafa", "Ali", "Ayşe", "Fatma", "Zeynep", "Elif", "Can", "Cem", "Deniz", "Emre", "Hakan", "Kemal", "Ömer", "Serkan"]
    soyisimler = ["Yılmaz", "Kaya", "Demir", "Şahin", "Çelik", "Yıldız", "Yıldırım", "Öztürk", "Aydın", "Özdemir", "Arslan", "Doğan", "Kılıç", "Aslan", "Çetin", "Koç"]
    return f"{random.choice(isimler)} {random.choice(soyisimler)}"

def kullanici_adi_ayikla(hesap_linki):
    if "https://t.me/" in hesap_linki:
        return hesap_linki.split("https://t.me/")[1].split("/")[0].strip()
    elif "t.me/" in hesap_linki:
        return hesap_linki.split("t.me/")[1].split("/")[0].strip()
    elif hesap_linki.startswith("@"):
        return hesap_linki[1:].strip()
    return hesap_linki.strip()

def rapor_mesaji_olustur(tam_hesap_linki, hesap_kullanici_adi):
    sablonlar = [
        f"Merhaba Telegram Destek Ekibi. Bu hesabı şüpheli aktiviteler nedeniyle bildiriyorum. Hesap, spam, oltalama ve taciz faaliyetlerinde bulunuyor ve Telegram Hizmet Şartlarını ihlal ediyor. Hesap Linki: {tam_hesap_linki} | Kullanıcı Adı: @{hesap_kullanici_adi}. Lütfen inceleyin ve uygun önlemleri alın. Platform güvenliğini koruduğunuz için teşekkür ederim.",
        f"Sayın Telegram Güvenlik Ekibi, Bu hesap spam içerik yayma, oltalama saldırıları ve topluluk kurallarını ihlal etme gibi kötü amaçlı davranışlarda bulunuyor. Hedef Hesap: {tam_hesap_linki} (@{hesap_kullanici_adi}). Acil inceleme ve politikalarınızın uygulanmasını talep ediyorum. Bu konuya göstereceğiniz hızlı ilgi için minnettarım.",
        f"Telegram Destek, Hizmet şartlarınızı açıkça ihlal eden ve şüpheli ve zararlı faaliyetlerde bulunan bir hesabı bildirmek istiyorum. Söz konusu hesap: {tam_hesap_linki} (Kullanıcı Adı: @{hesap_kullanici_adi}) spam dağıtımı ve potansiyel dolandırıcılık içeriği ile ilgileniyor. Lütfen topluluğu korumak için gerekli önlemleri alın.",
        f"Merhaba, Aşağıdaki Telegram hesabı hakkında resmi bir şikayette bulunuyorum: {tam_hesap_linki} (@{hesap_kullanici_adi}). Bu hesabın spam dağıtımı ve olası dolandırıcılık operasyonları dahil olmak üzere Telegram topluluk standartlarını ihlal eden faaliyetler yürüttüğü gözlemlendi. Bu konuyu kapsamlı bir şekilde araştırmanızı ve uygun yaptırım önlemlerini almanızı rica ediyorum."
    ]
    return random.choice(sablonlar)

# b / h --
def rapor_gonder(tam_hesap_linki, hesap_kullanici_adi, rapor_sayisi, proxy_ip=None):
    url = "https://telegram.org/support"
    veri = {
        "full_name": isim_olustur(),
        "email": email_olustur(),
        "phone": telefon_olustur(),
        "message": rapor_mesaji_olustur(tam_hesap_linki, hesap_kullanici_adi),
        "setln": random.choice(["tr", "en", "es", "fr", "de", "it", "ru"])
    }
    basliklar = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]),
        "Referer": "https://telegram.org/"
    }
    
    proxies = None
    if proxy_ip:
        proxies = {"http": f"http://{proxy_ip}", "https": f"http://{proxy_ip}"}
    
    try:
        yanit = requests.post(url, data=veri, headers=basliklar, proxies=proxies, timeout=10)
        if yanit.status_code == 200:
            ip_bilgi = proxy_ip if proxy_ip else "Yerel IP"
            print(f"{KIRMIZI}Rapor #{rapor_sayisi} başarıyla gönderildi | IP: {ip_bilgi} | Hedef: @{hesap_kullanici_adi}{SIFIRLA}")
            return True
        else:
            return False
    except:
        return False

def ana():
    print(f"{KIRMIZI}╔════════════════════════════════════════════════════{SIFIRLA}")
    print("""
███████╗ █████╗ ███████╗████████╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝
█████╗  ███████║███████╗   ██║
██╔══╝  ██╔══██║╚════██║   ██║
██║     ██║  ██║███████║   ██║
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝
         @tgfastlifee | @fastsystemm_bot""")
    print(f"{KIRMIZI}{'═' * 60}{SIFIRLA}")
    
    hedef_link = input(f"{KIRMIZI} Sikilecek Hesabın Kulanıcı Adini Girin: {SIFIRLA}").strip()
    
    if not hedef_link:
        return
    
    kullanici_adi = kullanici_adi_ayikla(hedef_link)
    tam_link = f"https://t.me/{kullanici_adi}" if not hedef_link.startswith("http") else hedef_link
    
    print(f"{KIRMIZI}Proxy listesi alınıyor...{SIFIRLA}")
    proxyler = proxy_listesi_al()
    print(f"{KIRMIZI}{len(proxyler)} adet aktif IP/Proxy bulundu.{SIFIRLA}")
    
    rapor_sayaci = 1
    basarili_raporlar = 0
    
    try:
        while True:
            
            secilen_proxy = random.choice(proxyler) if proxyler else None
            
            basari = rapor_gonder(tam_link, kullanici_adi, rapor_sayaci, proxy_ip=secilen_proxy)
            
            if basari:
                basarili_raporlar += 1
            
            if rapor_sayaci % 5 == 0:
                print(f"{KIRMIZI}--- Durum: {basarili_raporlar} Başarılı Rapor ---{SIFIRLA}")
            
            rapor_sayaci += 1
            time.sleep(random.uniform(1, 3))            
    except KeyboardInterrupt:
        print(f"\n{KIRMIZI}İşlem durduruldu.{SIFIRLA}")

if __name__ == "__main__":
    ana()
