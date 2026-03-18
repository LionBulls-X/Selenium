import requests
from user_agent import *
import telebot
import webbrowser
webbrowser.open('https://t.me/+XvswG1lbHFE4OTZl')

token = ''

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def r(message):
	bot.send_message(message.chat.id,text='''
	
مرحباً بك في بوت أخبار كرة القدم ⚽

هنا تجد آخر الأخبار والنتائج من جميع الدوريات العالمية والعربية  
مع تحديثات فورية لأحداث المباريات.

لمعرفه اخر الاخبار ارسل :
sport/	
	
	
	
	''',parse_mode='HTML')
	
@bot.message_handler(commands=['sport'])

def s(message):
	
	headers = {
	    'authority': 'mobilews.365scores.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'origin': 'https://www.365scores.com',
	    'referer': 'https://www.365scores.com/',
	    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': str(generate_user_agent()),
	}
	
	response = requests.get(
	    'https://mobilews.365scores.com/Data/News/?apptype=1&competitions=7170&filtersourcesout=true&lang=27&limitnews=true&maxcategoriestofill=30&maxnewsitems=30&minnewsitems=0&minnewsitemspercategory=0&newstype=9&onlyinlang=false&startdate=23/02/2020&storeversion=5.2.7&theme=dark&tz=15&uc=122',
	    headers=headers,
	).json()
	
	
	
	for item in response['Items']:
		
		itle = item["Title"]
	
		id = item['ID']
		
		SourceID = item["SourceID"]
		
		Type = item['Type']
		
		Description = item['Description']
		
		Images = item['Images']
		
		
		
		sport = f'''
		name : {itle}
		
		
		بطاقة تعريف : {id}
		
		
		معرف المصدر : {SourceID}
		
		
		الكاتب : {Type}
		
		
		وصف : {Description}
		
		
		الصور : {Images}
		
		
		
		'''
	
		bot.send_message(message.chat.id,sport)
		
bot.polling()