import instaloader
import os
from colorama import Fore, Style

def instagram_sorgulama(username):
    L = instaloader.Instaloader()

    try:
        profil = instaloader.Profile.from_username(L.context, username)

        result = f"""
        {Fore.CYAN}╔══════════════════════════════════════════════════╗
        ┃                                                      ┃
        ┃  {Fore.YELLOW}Kullanıcı Adı: {Fore.WHITE}{username: <30} {Fore.CYAN}┃
        ┃                                                      ┃
        ╠══════════════════════════════════════════════════╣
        ┃  {Fore.YELLOW}İSİM: {Fore.WHITE}{profil.full_name: <38} {Fore.CYAN}┃
        ┃  {Fore.YELLOW}Takipçi: {Fore.WHITE}{profil.followers: <35} {Fore.CYAN}┃
        ┃  {Fore.YELLOW}Takip: {Fore.WHITE}{profil.followees: <37} {Fore.CYAN}┃
        ┃  {Fore.YELLOW}Paylaşım: {Fore.WHITE}{profil.mediacount: <34} {Fore.CYAN}┃
        ┃  {Fore.YELLOW}Biyografi: {Fore.WHITE}{profil.biography[:40]: <30} {Fore.CYAN}┃
        ┃                                                      ┃
        ┃  {Fore.YELLOW}Telegram: {Fore.WHITE}@HEXADİCİAL | @HEXADİCİALVipTools  {Fore.CYAN}┃
        ╚══════════════════════════════════════════════════╝
        {Style.RESET_ALL}
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(result)
    except Exception as e:
        print(Fore.RED + f'\nHatalı Kullanıcı Adı ❌' + Style.RESET_ALL)

banner = f"""
{Fore.MAGENTA}
  _   _ _____ __  __ _____  _____ _____ _      _____ 
 | | | | ____|  \/  | ____|/ ____|_   _| |    | ____|
 | |_| |  _| | |\/| |  _| | |      | | | |    |  _|  
 |  _  | |___| |  | | |___| |____ _| |_| |____| |___ 
 |_| |_|_____|_|  |_|_____|\_____|_____|______|_____|
 
 {Fore.CYAN}——————————————————————————————————————————————————
 {Fore.YELLOW}Noctis Hack Team
 {Fore.CYAN}——————————————————————————————————————————————————
{Style.RESET_ALL}
"""
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
username = input(Fore.GREEN + f'Instagram Kullanıcı Adı Gir : ' + Style.RESET_ALL)
instagram_sorgulama(username)
