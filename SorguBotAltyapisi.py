import requests
import telebot
import time

BOT_TOKEN = "Token Gir Kkm"
bot = telebot.TeleBot(BOT_TOKEN)

KANAL_USERNAME = "@hanesizler"
KANAL_USERNAME2 = "@deltasorgupanel"

API_BASE = "http://deltavip.online"

def kullanici_kanalda_uye(user_id):
    try:
        durum = bot.get_chat_member(KANAL_USERNAME, user_id)
        durum2 = bot.get_chat_member(KANAL_USERNAME2, user_id)
        return durum.status in ['member', 'administrator', 'creator'] and durum2.status in ['member', 'administrator', 'creator']
    except:
        return False

def get_tc(tc):
    try:
        response = requests.get(f"{API_BASE}/tc.php?tc={tc}", timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def get_aile(tc):
    try:
        response = requests.get(f"{API_BASE}/aile.php?tc={tc}", timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def get_sulale(tc):
    try:
        response = requests.get(f"{API_BASE}/sulale.php?tc={tc}", timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def get_gsm_tc(gsm):
    try:
        response = requests.get(f"{API_BASE}/gsm.php?gsm={gsm}", timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def get_tc_gsm(tc):
    try:
        response = requests.get(f"{API_BASE}/gsm.php?tc={tc}", timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def get_isyeri(tc):
    try:
        response = requests.get(f"{API_BASE}/isyeri.php?tc={tc}", timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

def get_ad_soyad(ad, soyad, il="", ilce=""):
    try:
        url = f"{API_BASE}/adsoyad.php?ad={ad}&soyad={soyad}"
        if il: url += f"&il={il}"
        if ilce: url += f"&ilce={ilce}"
        response = requests.get(url, timeout=10)
        return response.json() if response.status_code == 200 else None
    except:
        return None

@bot.message_handler(commands=['start'])
def start(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        bot.send_message(message.chat.id, f"❌ KANAL KONTROLÜ ❌\n\nBotu kullanmak için kanallara katılın:\n\n{KANAL_USERNAME}\n{KANAL_USERNAME2}\n\nKatıldıktan sonra /start yazın.")
        return
        
    bot.send_message(message.chat.id, "Sorgu komutları:\n\n/tc [TC]\n/aile [TC]\n/sulale [TC]\n/gsmtc [GSM]\n/tcgsm [TC]\n/isyeri [TC]\n/adsoyadpro -ad [AD] -soyad [SOYAD] -il [İL] -ilce [İLÇE]")

def txt_gonder(chat_id, icerik, dosya_adi="sonuc.txt"):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(icerik)
    with open(dosya_adi, "rb") as f:
        bot.send_document(chat_id, f)

@bot.message_handler(commands=['tc'])
def tc_sorgu(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        return
    try:
        tc = message.text.split()[1]
        data = get_tc(tc)
        if data:
            result = f"""TC: {data.get('TC', '')}
Ad: {data.get('ADI', '')}
Soyad: {data.get('SOYADI', '')}
Doğum: {data.get('DOGUMTARIHI', '')}
Yaş: {data.get('YAS', '')}
Nüfus İl: {data.get('NUFUSIL', '')}
Nüfus İlçe: {data.get('NUFUSILCE', '')}
Anne: {data.get('ANNEADI', '')} ({data.get('ANNETC', '')})
Baba: {data.get('BABAADI', '')} ({data.get('BABATC', '')})"""
            txt_gonder(message.chat.id, result, "tc_sorgu.txt")
        else:
            bot.send_message(message.chat.id, "TC bilgisi bulunamadı")
    except:
        bot.send_message(message.chat.id, "Kullanım: /tc [TC]")

@bot.message_handler(commands=['aile'])
def aile_sorgu(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        return
    try:
        tc = message.text.split()[1]
        data = get_aile(tc)
        if data and data.get('success') == 'true' and data.get('data'):
            result = ""
            for kisi in data['data']:
                result += f"""TC: {kisi.get('TC', '')}
Ad: {kisi.get('ADI', '')}
Soyad: {kisi.get('SOYADI', '')}
Doğum: {kisi.get('DOGUMTARIHI', '')}
Anne: {kisi.get('ANNEADI', '')}
Baba: {kisi.get('BABAADI', '')}

"""
            txt_gonder(message.chat.id, result, "aile.txt")
        else:
            bot.send_message(message.chat.id, "Aile bilgisi bulunamadı")
    except:
        bot.send_message(message.chat.id, "Kullanım: /aile [TC]")

@bot.message_handler(commands=['sulale'])
def sulale_sorgu(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        return
    try:
        tc = message.text.split()[1]
        data = get_sulale(tc)
        if data and data.get('success') == 'true' and data.get('sülale'):
            result = ""
            for kisi in data['sülale']:
                result += f"""TC: {kisi.get('TC', '')}
Ad: {kisi.get('ADI', '')}
Soyad: {kisi.get('SOYADI', '')}
Doğum: {kisi.get('DOGUMTARIHI', '')}
Anne: {kisi.get('ANNEADI', '')}
Baba: {kisi.get('BABAADI', '')}

"""
            txt_gonder(message.chat.id, result, "sulale.txt")
        else:
            bot.send_message(message.chat.id, "Sülale bilgisi bulunamadı")
    except:
        bot.send_message(message.chat.id, "Kullanım: /sulale [TC]")

@bot.message_handler(commands=['gsmtc'])
def gsmtc_sorgu(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        return
    try:
        gsm = message.text.split()[1]
        data = get_gsm_tc(gsm)
        if data and data.get('success') == 'true' and data.get('data'):
            result = ""
            for kayit in data['data']:
                result += f"TC: {kayit.get('TC', '')}\nGSM: {kayit.get('GSM', '')}\n\n"
            txt_gonder(message.chat.id, result, "gsmtc.txt")
        else:
            bot.send_message(message.chat.id, "GSM’ye kayıtlı TC bulunamadı")
    except:
        bot.send_message(message.chat.id, "Kullanım: /gsmtc [GSM]")

@bot.message_handler(commands=['tcgsm'])
def tcgsm_sorgu(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        return
    try:
        tc = message.text.split()[1]
        data = get_tc_gsm(tc)
        if data and data.get('success') == 'true' and data.get('data'):
            result = ""
            for kayit in data['data']:
                result += f"TC: {kayit.get('TC', '')}\nGSM: {kayit.get('GSM', '')}\n\n"
            txt_gonder(message.chat.id, result, "tcgsm.txt")
        else:
            bot.send_message(message.chat.id, "TC’ye kayıtlı GSM bulunamadı")
    except:
        bot.send_message(message.chat.id, "Kullanım: /tcgsm [TC]")

@bot.message_handler(commands=['isyeri'])
def isyeri_sorgu(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        return
    try:
        tc = message.text.split()[1]
        data = get_isyeri(tc)
        if data and data.get('success') == 'true' and data.get('data'):
            isyeri = data['data']
            result = f"""Çalışan: {isyeri.get('calisanAdSoyad', '')}
TC: {isyeri.get('calisanKimlikNo', '')}
İşyeri: {isyeri.get('isyeriUnvani', '')}
Sektör: {isyeri.get('isyeriSektoru', '')}
Durum: {isyeri.get('calismaDurumu', '')}"""
            txt_gonder(message.chat.id, result, "isyeri.txt")
        else:
            bot.send_message(message.chat.id, "İşyeri bilgisi bulunamadı")
    except:
        bot.send_message(message.chat.id, "Kullanım: /isyeri [TC]")

@bot.message_handler(commands=['adsoyadpro'])
def adsoyadpro_sorgu(message):
    if not kullanici_kanalda_uye(message.from_user.id):
        return
    try:
        text = message.text
        ad = soyad = il = ilce = ""
        parts = text.split()
        if "-ad" in parts:
            ad = parts[parts.index("-ad")+1]
        if "-soyad" in parts:
            soyad = parts[parts.index("-soyad")+1]
        if "-il" in parts:
            il = parts[parts.index("-il")+1]
        if "-ilce" in parts:
            ilce = parts[parts.index("-ilce")+1]

        if not ad or not soyad:
            bot.send_message(message.chat.id, "Kullanım: /adsoyadpro -ad [AD] -soyad [SOYAD] -il [İL] -ilce [İLÇE]")
            return

        data = get_ad_soyad(ad, soyad, il, ilce)
        if data and data.get('success') == 'true' and data.get('data'):
            result = ""
            for kisi in data['data']:
                result += f"""TC: {kisi.get('TC', '')}
Ad: {kisi.get('ADI', '')}
Soyad: {kisi.get('SOYADI', '')}
Doğum: {kisi.get('DOGUMTARIHI', '')}
İl: {kisi.get('NUFUSIL', '')}
İlçe: {kisi.get('NUFUSILCE', '')}

"""
            txt_gonder(message.chat.id, result, "adsoyad.txt")
        else:
            bot.send_message(message.chat.id, "Arama sonucu bulunamadı")
    except:
        bot.send_message(message.chat.id, "Hata")

print("Bot başlatıldı...")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Hata: {e}")
        time.sleep(15)
        #İyi Kullanimlar Dileri ~ DRANSİT TOOL SUNAR