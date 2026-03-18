import asyncio
import time
import os
import requests
import yt_dlp
from pyrogram import Client, filters, idle
from pyrogram.enums import ChatAction, ChatMemberStatus
from pyrogram.errors import FloodWait, RPCError

# --- YAPILANDIRMA ---
# Geliştirici: ZEUS
API_ID = 3699825
API_HASH = "14c4ebe1f0aab2b766455d2620z"
SESSION_NAME = "zeus_userbot_session" 

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# Bellek Yönetimi
MUTED_USERS = set()
IS_AFK = False
AFK_REASON = "Şu an meşgulüm, en kısa sürede bakacağım."
GHOST_MODE = False
ANTISPM_MODE = False 
DM_SPAM_CHECK = {} # DM spam takibi için

# --- ULTRA HIZLI SHIELD ---
async def shield(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except FloodWait as e:
        print(f"⚠️ Limit: {e.value} sn bekleniyor...")
        await asyncio.sleep(e.value)
        return await func(*args, **kwargs)
    except Exception as e:
        print(f"❌ Sistem Hatası: {e}")
        return None

# --- [YENİ] OSINT (YANIT VEREREK ÇALIŞIR) ---
@app.on_message(filters.me & filters.command("osint", "."))
async def osint_handler(client, message):
    if not message.reply_to_message:
        return await shield(message.edit, "❌ **Hata:** Bilgi toplamak için bir kullanıcıya yanıt verin!")
    
    await shield(message.edit, "🔍 **Veriler Sorgulanıyor...**")
    target = message.reply_to_message.from_user
    
    try:
        # Daha detaylı bilgi için full user çekiyoruz
        user_info = await client.get_users(target.id)
        common = await client.get_common_chats(target.id)
        
        res = (
            f"🕵️ **OSINT ANALİZİ**\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **Ad:** `{user_info.first_name}`\n"
            f"🆔 **ID:** `{user_info.id}`\n"
            f"📧 **User:** @{user_info.username if user_info.username else 'Yok'}\n"
            f"🌍 **DC:** `{user_info.dc_id if user_info.dc_id else 'Bilinmiyor'}`\n"
            f"👥 **Ortak Grup:** `{len(common)}` adet\n"
            f"🤖 **Bot:** `{'Evet' if user_info.is_bot else 'Hayır'}`\n"
            f"🚫 **Kısıtlı:** `{'Evet' if user_info.is_restricted else 'Hayır'}`\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **Analist:** `ZEUS`"
        )
        await shield(message.edit, res)
    except Exception as e:
        await shield(message.edit, f"❌ Veri çekilemedi: {e}")

# --- [KORUNAN ÖZELLİKLER] DM ANTI-SPAM ---
@app.on_message(filters.private & ~filters.me & filters.incoming, group=2)
async def dm_antispm_engine(client, message):
    global ANTISPM_MODE
    if not ANTISPM_MODE: return
    uid = message.from_user.id
    if uid in MUTED_USERS:
        await message.delete()
        return
    now = time.time()
    user_msgs = DM_SPAM_CHECK.get(uid, [])
    user_msgs = [t for t in user_msgs if now - t < 5]
    user_msgs.append(now)
    DM_SPAM_CHECK[uid] = user_msgs
    if len(user_msgs) > 3:
        MUTED_USERS.add(uid)
        await client.send_message(uid, "⚠️ **SPAM ALGILANDI!**\nSusturuldunuz.")

# --- [KORUNAN ÖZELLİKLER] MEDYA İNDİRİCİ ---
@app.on_message(filters.me & filters.command("indir", "."))
async def download_handler(client, message):
    if not message.reply_to_message:
        return await shield(message.edit, "❌ Bir dosyaya yanıt verin!")
    await shield(message.edit, "📥 **İndiriliyor...**")
    try:
        path = await message.reply_to_message.download()
        await shield(message.edit, f"✅ **İndirildi:**\n`{path}`")
    except Exception as e:
        await shield(message.edit, f"❌ Hata: {e}")

# --- [KORUNAN ÖZELLİKLER] IP LOOKUP ---
@app.on_message(filters.me & filters.command("iplookup", "."))
async def iplookup_handler(client, message):
    if len(message.command) < 2:
        return await shield(message.edit, "❌ IP adresi yazın!")
    ip = message.command[1]
    await shield(message.edit, f"🔍 `{ip}` sorgulanıyor...")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
        res = (
            f"🌐 **IP BİLGİSİ**\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"📍 **Ülke:** `{data.get('country')}`\n"
            f"🏙️ **Şehir:** `{data.get('city')}`\n"
            f"📡 **ISP:** `{data.get('isp')}`\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **Geliştirici:** `ZEUS`"
        )
        await shield(message.edit, res)
    except:
        await shield(message.edit, "❌ IP hatası.")

# --- [DİĞER TÜM KOMUTLAR - DEĞİŞTİRİLMEDİ] ---

@app.on_message(filters.me & filters.command("antispm", "."))
async def antispm_toggle(client, message):
    global ANTISPM_MODE
    ANTISPM_MODE = not ANTISPM_MODE
    await shield(message.edit, f"🛡️ **Anti-Spam:** `{'AÇIK' if ANTISPM_MODE else 'KAPALI'}`")

@app.on_message(filters.me & filters.command("spam", "."))
async def spam_handler(client, message):
    args = message.text.split(None, 2)
    if len(args) < 3: return
    count, text = int(args[1]), args[2]
    await message.delete()
    for _ in range(count):
        await client.send_message(message.chat.id, text)
        await asyncio.sleep(0.08)

@app.on_message(filters.me & filters.command("guvenlik", "."))
async def security_check(client, message):
    target = message.reply_to_message.text if message.reply_to_message else (message.command[1] if len(message.command) > 1 else None)
    if not target or "http" not in target: return await shield(message.edit, "❌ Link yok!")
    is_danger = any(w in target.lower() for w in ["free", "bedava", "gift", "login", "bit.ly"])
    status = "🚩 **TEHLİKELİ!**" if is_danger else "✅ **GÜVENLİ**"
    await shield(message.edit, f"🛡️ **GÜVENLİK RAPORU**\n━━━━━━━━━━━━━━━━━━━━\n📊 **Durum:** {status}\n👤 **Geliştirici:** `ZEUS`\n━━━━━━━━━━━━━━━━━━━━")

@app.on_message(filters.me & filters.command("tagall", "."))
async def tag_all_handler(client, message):
    await message.delete()
    mentions = ""
    count = 0
    async for member in client.get_chat_members(message.chat.id):
        if member.user.is_bot: continue
        mentions += f"@{member.user.username} " if member.user.username else f"[{member.user.first_name}](tg://user?id={member.user.id}) "
        count += 1
        if count % 5 == 0:
            await client.send_message(message.chat.id, mentions)
            mentions = ""; await asyncio.sleep(0.3)
    if mentions: await client.send_message(message.chat.id, mentions)

@app.on_message(filters.me & filters.command(["mute", "unmute", "ban", "unban"], "."))
async def admin_actions(client, message):
    if not message.reply_to_message: return await shield(message.edit, "❌ Yanıt ver!")
    uid = message.reply_to_message.from_user.id
    cmd = message.command[0]
    if cmd == "mute": MUTED_USERS.add(uid); res = "🔇 Susturuldu."
    elif cmd == "unmute": MUTED_USERS.discard(uid); res = "🔊 Engel kaldırıldı."
    elif cmd == "ban": await client.ban_chat_member(message.chat.id, uid); res = "🚫 Yasaklandı."
    elif cmd == "unban": await client.unban_chat_member(message.chat.id, uid); res = "🔓 Yasak kaldırıldı."
    await shield(message.edit, res)

@app.on_message(filters.incoming, group=1)
async def mute_engine(client, message):
    if message.from_user and message.from_user.id in MUTED_USERS:
        await message.delete()

@app.on_message(filters.me & filters.command("song", "."))
async def song_handler(client, message):
    if len(message.command) < 2: return
    query = " ".join(message.command[1:])
    await shield(message.edit, f"🎵 **'{query}'** aranıyor...")
    fname = f"zeus_{int(time.time())}.mp3"
    try:
        with yt_dlp.YoutubeDL({'format': 'bestaudio/best', 'outtmpl': fname, 'quiet': True}) as ydl:
            ydl.download([f"ytsearch:{query}"])
        await client.send_audio(message.chat.id, audio=fname, caption="👤 **ZEUS USERBOT**")
        await message.delete()
    finally:
        if os.path.exists(fname): os.remove(fname)

@app.on_message(filters.me & filters.command("menu", "."))
async def menu_handler(client, message):
    await shield(message.edit, (
        "**ZEUS USERBOT**\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "🛡️ `.guvenlik` | 📢 `.tagall` | 🎵 `.song`\n"
        "🔇 `.mute` | 🔊 `.unmute` | 🚫 `.ban` | 🔓 `.unban`\n"
        "🚀 `.spam` | 👻 `.ghost` | 🌙 `.afk` | 🏓 `.ping`\n"
        "📂 `.indir` | 🔍 `.iplookup` | 🛡️ `.antispm`\n"
        "🕵️ `.osint` \n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "👤 **Geliştirici:** `ZEUS`"
    ))

@app.on_message(filters.me & filters.command("ping", "."))
async def ping_handler(client, message):
    start = time.time()
    ms = round((time.time() - start) * 1000)
    await shield(message.edit, f"🚀 **ZEUS HIZI:** `{ms}ms`")

# --- BAŞLATICI ---
async def start_bot():
    try:
        await app.start()
        print("✅ ZEUS USERBOT AKTİF.")
        await idle()
    except Exception as e: print(f"❌ Hata: {e}")
    finally:
        if app.is_connected: await app.stop()

if __name__ == "__main__":
    app.run(start_bot())
