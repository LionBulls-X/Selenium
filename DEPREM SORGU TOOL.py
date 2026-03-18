import requests, os
from bs4 import BeautifulSoup

class BatuTools:
    def __init__(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("""⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡠⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⢉⡗⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠈⡱⠖⠀⠀⠀⠀⠀⠀⠀⠀⣄⣠⠆⠀
⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠰⠓⠒⢴⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢨⠀⣰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⢹⡀⠀⠀⠀⠈⠀
⠀⠀⠀⠀⢠⣀⣶⠀⠀⠀⠀⠀⠀⠀⠀⢤⢀⣀⣀⣀⡠⠋⠀⠀⢇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⣄⠊⠁⠀⠀⠀⠀⠀⢀⡨⢦⠀⠀⠀⠀⠀⠀⠀⠘⠒⠤⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡀⠔⠊⠁⢀⡀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠼⠋
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠈⡀⠄⠂⠉⢀⡀⢰⠁⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀
⠀⠀⠀⠀⠀⠀⡠⢊⠠⠒⣁⠤⠐⣀⡁⠤⢤⠃⢀⣀⡠⢄⡀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⡠⡪⢐⡡⢐⠩⠐⠊⠁⠀⠀⠀⠚⠉⠉⠀⠀⠀⠙⠢⣀⡇⠀⠀⠀⠀
⠀⠀⢠⡪⡪⡲⠕⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⠃⠀⠀⠀⠀
⠀⣰⣿⠞⠉⠀⠀⠀⠀⠀⡄⡰⡆⠀⠀⠀⠀⠀⠀⢐⣌⡶⠀⠀⠀⠀⠀⠀⠀⠀
⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⣸⠤⡐⠁⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀""")
            print("\033[92m=\033[0m" * 60)
            print("\033[91m-By: \033[0m@BatuPy")
            print("\033[92m=\033[0m" * 60)
            print("\033[93m1️⃣ Son depremi göster \033[0m")
            print("\033[94m2️⃣ Son 100 depremi listele \033[0m")
            print("\033[95m0️⃣ Çıkış\n\033[0m")
            secim = input("\033[96mSeçimini yap (1/2/0): \033[0m").strip()
            if secim == "0":
                print("\033[91m👋 Görüşürüz knk!\033[0m")
                break
            html = requests.get("https://deprem.afad.gov.tr/last-earthquakes.html")
            html.encoding = "utf-8-sig"
            soup = BeautifulSoup(html.text, "html.parser")
            tablo = soup.find("table", {"class": "content-table"})
            if not tablo:
                print("\033[91m❌ Deprem verisi alınamadı! \033[0m")
                input("\nDevam etmek için Enter’a bas 🔁  ")
                continue
            satirlar = tablo.find_all("tr")[1:]
            for i, row in enumerate(satirlar, 1):
                BatuPy = [c.get_text(strip=True) for c in row.find_all("td")]
                if len(BatuPy) >= 7:
                    BatuC5 = float(BatuPy[5].replace(",", "."))
                    uyarı = "\033[91m🚨 DİKKAT! ŞİDDETLİ DEPREM! \033[0m" if BatuC5 >= 4.0 else "\033[92m✅ Hafif deprem.\033[0m"
                    if secim == "1" and i == 1:
                        print("\033[93m🆕 SON DEPREM BİLGİLERİ\033[0m")
                        print("\033[94m==================================================\033[0m")
                        print("\033[95m📅 Tarih:\033[0m " + BatuPy[0])
                        print("\033[96m📍 Yer:\033[0m " + BatuPy[6])
                        print("\033[91m💥 Büyüklük:\033[0m " + BatuPy[5] + " (" + BatuPy[4] + ")")
                        print("\033[92m📏 Derinlik:\033[0m " + BatuPy[3] + " km")
                        print("\033[93m🧭 Koordinatlar:\033[0m Enlem " + BatuPy[1] + ", Boylam " + BatuPy[2])
                        print(uyarı)
                        break
                    elif secim == "2":
                        renkler = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]
                        print(renkler[0] + "🔹 #" + str(i) + " \033[0m")
                        print(renkler[1] + "📅 Tarih:\033[0m " + BatuPy[0])
                        print(renkler[2] + "📍 Yer:\033[0m " + BatuPy[6])
                        print(renkler[3] + "💥 Büyüklük:\033[0m " + BatuPy[5] + " (" + BatuPy[4] + ")")
                        print(renkler[4] + "📏 Derinlik:\033[0m " + BatuPy[3] + " km")
                        print(renkler[5] + "🧭 Koordinatlar:\033[0m Enlem " + BatuPy[1] + ", Boylam " + BatuPy[2])
                        print(uyarı)
                        print(renkler[6] + "-" * 55 + "\033[0m")
            if secim not in ["1", "2", "0"]:
                print("\033[91m❌ Geçersiz seçim yaptın \033[0m")
            input("\033[96m\nDevam etmek için Enter’a bas 🔁  \033[0m")

BatuTools()