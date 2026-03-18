# fake_gps.py
# Author: Eragon
import os, time
try:
    from colorama import init, Fore, Style
    init()
except: pass

def spoof(lat, lon):
    os.system(f"adb shell am start-foreground-service -n com.lexa.fakegps/.FakeGPSService --ef lat {lat} --ef lon {lon}")

while True:
    os.system('clear')
    print(Fore.CYAN + "🌍 FAKE GPS - BY ERAGON" + Style.RESET_ALL)
    lat = input(Fore.YELLOW + "Latitude (e.g. 41.0082): " + Style.RESET_ALL)
    lon = input(Fore.GREEN + "Longitude (e.g. 28.9784): " + Style.RESET_ALL)
    print(Fore.RED + "Spoofing location..." + Style.RESET_ALL)
    spoof(lat, lon)
    input("Stop → Enter: ")
    os.system("adb shell am force-stop com.lexa.fakegps")