import requests, time, hashlib, json
from cfonts import say
from colorama import Fore, Style
import pyfiglet

RENK_YESIL = Fore.GREEN
RENK_KIRMIZI = Fore.RED
RENK_SARI = Fore.YELLOW
RENK_MAVI = Fore.BLUE
RENK_LOGO = Fore.MAGENTA
RENK_GRI = Fore.LIGHTBLACK_EX

def yıkım():
        text = " YIKIM-TOOL"
        try:
            	logo = pyfiglet.figlet_format(text, font="slant")
            	print(RENK_LOGO + logo.center(80))
        except Exception:
            print(RENK_LOGO + text.center(80))
        print(RENK_LOGO + "@YIKIM44".center(40))
yıkım()
        
G = '\033[1;30;40m'
rito = f'{G}\t1 GB APP 45-50 FREEBYTE TOOL\n'
print(rito)

Y = '\033[92m'
S = '\033[93m'
K = '\033[31m'
B = '\033[37m'

def hashuret(tid):
    secret="6a5de8a0a5f0ec70ee254b2046"
    return hashlib.md5((tid+secret).encode()).hexdigest()

def odul(token):
    url="https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/user/check-in"
    headers={
        'Authorization': f"Bearer {token}",
        'Content-Type': 'application/json',
        'authority': '3uptzlakwi.execute-api.eu-west-1.amazonaws.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://1gbapp.com',
        'referer': 'https://1gbapp.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    r=requests.post(url,json={"etkAccepted":False},headers=headers)
    print(Y+"Giris odulu alindi" if r.status_code==200 else f"{K}Odul alinmadi")

def reklam(token):
    s="https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/admob/start"
    f="https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/admob/finish"
    h={
        'Authorization': f"Bearer {token}",
        'Content-Type': 'application/json',
        'authority': '3uptzlakwi.execute-api.eu-west-1.amazonaws.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://1gbapp.com',
        'referer': 'https://1gbapp.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    rs=requests.post(s,json={},headers=h)
    if rs.status_code==200 and "transactionId" in rs.json():
        tid=rs.json()["transactionId"]
        print(S+"Reklam baslatildi",tid)
        hsh=hashuret(tid)
        time.sleep(1)
        rf=requests.post(f,json={"transactionId":tid,"hash":hsh},headers=h)
        print(Y+"Reklam tamamlandi" if rf.status_code==200 else f"{K}Hata")
    else:
        print(f"{K}Gunluk reklam limiti doldu" if rs.status_code==400 and "daily_limit_reached" in rs.text else f"{K}Limit dolmus veya hata")

def first_login_event(msisdn, token):
    url_event = "https://6mpp1sq7k1.execute-api.eu-west-1.amazonaws.com/prod/event"
    headers_event = {
        'authority': '6mpp1sq7k1.execute-api.eu-west-1.amazonaws.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://1gbapp.com',
        'referer': 'https://1gbapp.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }
    json_event = {
        'msisdn': msisdn,
        'product': 'kgbappweb',
        'userId': '',
        'event': 'user_first_login_success',
    }
    payload_event = json.dumps(json_event, separators=(',', ':'))
    r_event = requests.post(url_event, headers=headers_event, data=payload_event)
    print(Y + "First login event logged" if r_event.status_code == 200 else f"{K}Event log failed: {r_event.status_code}")

def giris(msisdn):
    url_verify = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/auth/pin/verify"
    pin = input(S + "PIN: " + B)
    
    json_verify = {'msisdn': msisdn, 'osType': 'UNKNOWN', 'pin': pin}
    payload_verify = json.dumps(json_verify, separators=(',', ':'))
    
    headers_verify = {
        'authority': '3uptzlakwi.execute-api.eu-west-1.amazonaws.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://1gbapp.com',
        'referer': 'https://1gbapp.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'x-client-device-id': 'c2453b31-562b-4d62-98d0-b1205f7bf060',
    }

    r_verify = requests.post(url_verify, headers=headers_verify, data=payload_verify)
    
    try:
        j = r_verify.json()
    except:
        print(K + "Verify response error: " + r_verify.text[:200])
        j = {}
        
    if "token" in j:
        print(Y + "PIN dogrulamasi basarili")
        t = j["token"]
        first_login_event(msisdn, t)
        odul(t)
        for i in range(4):
            print(i+1, ".reklam")
            reklam(t)
            time.sleep(2)
    else:
        error_msg = j.get("message", j.get("code", "Bilinmeyen hata"))
        print(K + "PIN hatali", error_msg)

if __name__=="__main__":
    m = input(S + "Telefon (905xxxxxxxxx): " + B)
    if m.startswith("905") and len(m)==12:
        giris(m)
    else:
        print(K + "Numara hatali" + B)