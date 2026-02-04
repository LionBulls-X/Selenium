from playwright.sync_api import sync_playwright
import time

USERNAME = "ravisseurs"
EMAIL = "ars.arslanboga@gmail.com"
URL = "https://countik.com/tiktok-likes-generator"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # True yaparsan arka planda çalışır
    page = browser.new_page()

    # 1️⃣ Siteyi aç
    page.goto(URL, timeout=60000)
    page.wait_for_load_state("networkidle")

    # 2️⃣ Username alanını doldur
    page.wait_for_selector("input", timeout=10000)
    page.fill("input", USERNAME)

    # 3️⃣ Search / Submit butonuna bas
    # (Buton selector'u siteye göre değişebilir)
    page.click("button")

    # 4️⃣ Sonuçların gelmesini bekle
    # Bu kısım dinamik → selector değişebilir
    page.wait_for_timeout(5000)

    # 5️⃣ En son paylaşıma tıkla
    posts = page.query_selector_all("a")
    if posts:
        posts[-1].click()
    else:
        print("Post bulunamadı")

    # 6️⃣ Email alanını doldur
    page.wait_for_selector("input[type='email']", timeout=10000)
    page.fill("input[type='email']", EMAIL)

    # 7️⃣ Enter
    page.keyboard.press("Enter")

    time.sleep(10)
    browser.close()
