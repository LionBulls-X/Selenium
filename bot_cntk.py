from playwright.sync_api import sync_playwright
import time

USERNAME = "ravisseurs"
EMAIL = "ars.arslanboga@gmail.com"
URL = "https://countik.com/tiktok-likes-generator"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            print("1. Siteye gidiliyor...")
            page.goto(URL, timeout=60000)
            page.wait_for_load_state("networkidle")
            
            print("2. Username giriliyor...")
            # Daha spesifik selector kullan
            page.wait_for_selector("input[placeholder*='username'], input[name='username'], input#username", timeout=10000)
            page.fill("input[placeholder*='username'], input[name='username'], input#username", USERNAME)
            
            print("3. Search butonuna tıklanıyor...")
            # Buton metnine veya class'ına göre bul
            page.click("button:has-text('Search'), button[type='submit'], button.search-btn")
            
            print("4. Sonuçlar bekleniyor...")
            page.wait_for_timeout(5000)
            
            print("5. Post listesi kontrol ediliyor...")
            # Daha spesifik post selector'u
            posts = page.query_selector_all("a[href*='tiktok.com'], .post-item a, .video-item a")
            
            if posts:
                print(f"{len(posts)} post bulundu, son posta tıklanıyor...")
                posts[-1].click()
                page.wait_for_load_state("networkidle")
            else:
                print("❌ Post bulunamadı!")
                # Sayfadaki tüm linkleri göster
                all_links = page.query_selector_all("a")
                print(f"Sayfada toplam {len(all_links)} link var")
                return
            
            print("6. Email alanı dolduruluyor...")
            page.wait_for_selector("input[type='email']", timeout=10000)
            page.fill("input[type='email']", EMAIL)
            
            print("7. Enter tuşuna basılıyor...")
            page.keyboard.press("Enter")
            
            print("✅ İşlem tamamlandı!")
            time.sleep(10)
            
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")
            # Hata anında screenshot al
            page.screenshot(path="hata_screenshot.png")
            print("Screenshot kaydedildi: hata_screenshot.png")
            
        finally:
            browser.close()

if __name__ == "__main__":
    main()