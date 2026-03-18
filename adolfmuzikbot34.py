import telebot
from telebot import types
import yt_dlp
import os
import json
import threading
import time
import uuid
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# ========= AYARLAR =========
BOT_TOKEN = "BOTFATHER_TOKEN"
SPOTIFY_CLIENT_ID = "SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "SPOTIFY_CLIENT_SECRET"

bot = telebot.TeleBot(BOT_TOKEN, threaded=True)

spotify = Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    )
)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

stats_file = "stats.json"
DEFAULT_FORMAT = "mp3"
DEFAULT_QUALITY = "192"

waiting_for_song = {}

# ========= STATS =========
def load_stats():
    if os.path.exists(stats_file):
        with open(stats_file) as f:
            return json.load(f)
    return {"users": [], "songs": 0}

stats = load_stats()

def save_stats():
    with open(stats_file, "w") as f:
        json.dump(stats, f)

# ========= İLERLEME =========
def progress(chat, song):
    msg = bot.send_message(chat, f"⏳ İndiriliyor: *{song}*", parse_mode="Markdown")
    for i in range(3):
        time.sleep(4)
        try:
            bot.edit_message_text(
                f"⏳ İndiriliyor: *{song}*" + "." * (i + 1),
                chat,
                msg.message_id,
                parse_mode="Markdown"
            )
        except:
            break

# ========= İNDİR =========
def download_song(query, uid):
    filename = f"{uid}_{uuid.uuid4()}"
    out = os.path.join(DOWNLOAD_DIR, filename)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": out + ".%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": DEFAULT_QUALITY
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{query}", download=True)
        return ydl.prepare_filename(info["entries"][0])

# ========= START =========
@bot.message_handler(commands=["start"])
def start(m):
    chat = m.chat.id

    if chat not in stats["users"]:
        stats["users"].append(chat)
        save_stats()

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🎵 Şarkı indir")

    bot.send_message(
        chat,
        "🎧 *Müzik İndirme Botu*\n\n"
        "Bir şarkı adı veya Spotify linki gönder.",
        reply_markup=kb,
        parse_mode="Markdown"
    )

# ========= MESAJ =========
@bot.message_handler(func=lambda m: True)
def messages(m):
    chat = m.chat.id
    text = m.text.strip()

    if text.startswith("🎵"):
        bot.send_message(chat, "🎶 Şarkı adını veya Spotify linkini yaz:")
        waiting_for_song[chat] = True
        return

    if waiting_for_song.get(chat):
        waiting_for_song.pop(chat, None)
        song = text

        # Spotify link ise
        if "spotify.com" in song:
            try:
                track = spotify.track(song)
                title = track["name"]
                artist = track["artists"][0]["name"]
                search = f"{title} {artist}"
            except:
                bot.send_message(chat, "❌ Spotify linki okunamadı.")
                return
        else:
            search = song

        threading.Thread(target=progress, args=(chat, search), daemon=True).start()

        try:
            file_path = download_song(search, chat)

            with open(file_path, "rb") as audio:
                bot.send_audio(
                    chat,
                    audio,
                    caption="✅ İndirme tamamlandı 🎶"
                )

            os.remove(file_path)
            stats["songs"] += 1
            save_stats()

        except Exception as e:
            bot.send_message(chat, "❌ Bir hata oluştu. Tekrar dene.")

    else:
        bot.send_message(chat, "ℹ️ Şarkı indirmek için *Şarkı indir* butonuna bas.",
                         parse_mode="Markdown")

# ========= ÇALIŞ =========
bot.infinity_polling()