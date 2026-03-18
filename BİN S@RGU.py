import re, requests, json, urllib.parse
from urllib.parse import urlparse, parse_qs
from requests.utils import dict_from_cookiejar
from cfonts import render
class BatuKurucu:
    def __init__(self):
        print("\033[95m" + "=" * 60 )
        print(render('BIN', colors=['red', 'cyan', 'yellow'], align='center'))
        print("\033[95m" + "=" * 60 )
        print("\033[94mBy: @Batupy")
        print("\033[95m" + "=" * 60  )
        batupy = input("\033[92m• BİN NUMARASI GİR: \033[0m").strip()
        print("\033[95m" + "=" * 60)
        response = requests.get("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LenoYUfAAAAABiVts42vmUI7eDm87pFCctEiWPc&co=aHR0cHM6Ly9iaW5jaGVja2VyLnBybzo0NDM.&hl=tr&v=07cvpCr3Xe3g2ttJNUkC6W0J&size=invisible&anchor-ms=20000&execute-ms=15000&cb=fkijllt5pjny", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"})
        heykir = re.search(r'value="([^"]+)"', response.text).group(1)
        response = requests.post("https://www.google.com/recaptcha/api2/reload", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","Referer": response.url,"Content-Type": "application/x-www-form-urlencoded"}, data={'v': '07cvpCr3Xe3g2ttJNUkC6W0J','reason': 'q','c': heykir,'k': '6LenoYUfAAAAABiVts42vmUI7eDm87pFCctEiWPc','co': 'aHR0cHM6Ly9iaW5jaGVja2VyLnBybzo0NDM.','hl': 'tr','size': 'invisible'})
        amk = re.search(r'\["rresp","([^"]+)"', response.text).group(1)
        s = requests.Session()
        s.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.9','Referer': "https://binchecker.pro/"})
        response = s.get("https://binchecker.pro/", timeout=10)
        xsrf_cookie = dict_from_cookiejar(s.cookies).get('XSRF-TOKEN') or dict_from_cookiejar(s.cookies).get('XSRF_TOKEN')
        if xsrf_cookie:
            xsrf_cookie = urllib.parse.unquote(xsrf_cookie)
        x_csrf_token = None
        m = re.search(r'<meta[^>]+name=["\']csrf-token["\'][^>]+content=["\']([^"\']+)["\']', response.text, flags=re.I)
        if m: x_csrf_token = m.group(1)
        if not x_csrf_token:
            m = re.search(r'["\']csrfToken["\']\s*[:=]\s*["\']([^"\']+)["\']', response.text)
            if m: x_csrf_token = m.group(1)
        if not x_csrf_token:
            m = re.search(r'x-csrf-token["\']?\s*[:=]\s*["\']([^"\']+)["\']', response.text)
            if m: x_csrf_token = m.group(1)
        s.headers.update({'Accept': 'application/json','Content-Type': 'application/json','Origin': "https://binchecker.pro",'Referer': "https://binchecker.pro/",'x-csrf-token': x_csrf_token if x_csrf_token else "",'X-XSRF-TOKEN': xsrf_cookie if xsrf_cookie else ""})
        response = s.post("https://binchecker.pro/bincheck", json={'bin': int(batupy),'g-recaptcha-response': amk}, timeout=15)
        try:
            batu = response.json()
        except ValueError:
            batu = {}
        if not batu:
            print("\033[91m❌ HATA ÇIKTI\033[0m")
        else:
            print(f"""\033[91m🪪 BIN:\033[0m {batu.get('bin', '')}
\033[92m🗽 Banka:\033[0m {batu.get('bank', '')}
\033[93m💼 Kart Türü:\033[0m {batu.get('card', '')}
\033[94m🫗 Kart Tipi:\033[0m {batu.get('type', '')}
\033[95m🪫 Seviye:\033[0m {batu.get('level', '')}
\033[96m👑 Ülke:\033[0m {batu.get('country', '')}
\033[91m🎓 Ülke Kodu:\033[0m {batu.get('countrycode', '')}
\033[92m📺 Website:\033[0m {batu.get('website', '')}
\033[93m📱 Telefon:\033[0m {batu.get('phone', '')}
\033[94m✅ Geçerli:\033[0m {batu.get('valid', '')}
""")
        print("\033[95m" + "=" * 60 + "\033[92m")
BatuKurucu()