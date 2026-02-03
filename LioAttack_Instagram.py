from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, ElementNotInteractableException
import time
import random

# ==========================================
# ⚙️ AYARLAR - BURADAN DEĞİŞTİREBİLİRSİNİZ
# ==========================================

BEKLEME = 10
HIZLI_MOD = True  # True = Hızlı (resimler kapalı), False = Normal
GORUNMEZ_MOD = True  # True = Tarayıcı görünmez (arka plan), False = Tarayıcı görünür

# ⏱️ KONTROL BEKLEMESİ (Dakika cinsinden)
KONTROL_BEKLEME_DAKIKA = 4  # 4 dakika sonra kontrol et

# 👤 VARSAYILAN KULLANICI ADI (Manuel değiştirmek için)
VARSAYILAN_KULLANICI = "LionBulls"

# ==========================================
# 📋 SİTE LİSTESİ 1 - TAKİPÇİ HİLESİ
# ==========================================
# Format: {"url": "site adresi", "kullanici": "kullanıcı_adı", "adet": "miktar", "ozel": True/False}
# "ozel": True -> Zor sitelerde kullanın (daha fazla deneme yapar)
# "ozel": False veya yazmayın -> Normal siteler için
# "sadece_kullanici": True -> Adet alanı olmayan siteler için
# "enter": True            -> Adet yok VE button yok, sadece kullanıcı adı gir + Enter bas

SITELER_GRUP_1 = [
    {
        "url": "https://sosyalify.com/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "30",
        "ozel": True  # Yavaş yüklenen site
    },
    {
        "url": "https://sosyora.com.tr/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "20"
    },
    {
        "url": "https://takipcievin.com/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "50"
    },
    {
        "url": "https://takipcisatinal.com.tr/instagram-takipci-hilesi/",
        "kullanici": VARSAYILAN_KULLANICI,
        "sadece_kullanici": True,  # Bu sitede adet alanı yok, sadece kullanıcı adı + onay
        "ozel": True
    },
    {
        "url": "https://takipci.al/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "50"
    },
    {
        "url": "https://popigram.com/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "10"
    },
    {
        "url": "https://roxmedya.com.tr/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "5"
    },
    {
        "url": "https://sosyalton.com.tr/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "10"
    },
    {
        "url": "https://sosyalzone.com/instagram-ucretsiz-takipci/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "75"
    },
    {
        "url": "https://instantusername.com/",
        "kullanici": VARSAYILAN_KULLANICI,
        "sadece_kullanici": True,  # Adet alanı yok
        "enter": True             # Button yok -> kullanıcı adı gir + Enter bas
    }
]

# ==========================================
# 📋 SİTE LİSTESİ 2 - BEĞENİ HİLESİ
# ==========================================

SITELER_GRUP_2 = [
    {
        "url": "https://sosyalify.com/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "30",
        "ozel": True  # Yavaş yüklenen site
    },
    {
        "url": "https://sosyora.com.tr/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "20"
    },
    {
        "url": "https://takipcievin.com/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "50"
    },
    {
        "url": "https://takipcisatinal.com.tr/instagram-begeni-hilesi/",
        "kullanici": VARSAYILAN_KULLANICI,
        "sadece_kullanici": True,  # Adet yok, sadece link + onay
        "ozel": True
    },
    {
        "url": "https://takipci.al/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "50"
    },
    {
        "url": "https://popigram.com/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "10"
    },
    {
        "url": "https://roxmedya.com.tr/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "5"
    },
    {
        "url": "https://sosyalton.com.tr/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "10"
    },
    {
        "url": "https://sosyalzone.com/instagram-ucretsiz-begeni/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "75"
    }
]

# ==========================================
# 📋 SİTE LİSTESİ 3 - İZLENME HİLESİ
# ==========================================

SITELER_GRUP_3 = [
    {
        "url": "https://sosyalify.com/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "30",
        "ozel": True  # Yavaş yüklenen site
    },
    {
        "url": "https://sosyora.com.tr/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "20"
    },
    {
        "url": "https://takipcievin.com/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "50"
    },
    {
        "url": "https://takipcisatinal.com.tr/instagram-izlenme-hilesi/",
        "kullanici": VARSAYILAN_KULLANICI,
        "sadece_kullanici": True,  # Adet yok, sadece link + onay
        "ozel": True
    },
    {
        "url": "https://takipci.al/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "50"
    },
    {
        "url": "https://popigram.com/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "10"
    },
    {
        "url": "https://roxmedya.com.tr/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "5"
    },
    {
        "url": "https://sosyalton.com.tr/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "10"
    },
    {
        "url": "https://sosyalzone.com/instagram-ucretsiz-izlenme/",
        "kullanici": VARSAYILAN_KULLANICI,
        "adet": "75"
    }
]

# ==========================================
# 🔧 FONKSİYONLAR - DOKUNMAYIN
# ==========================================

def log(msg):
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] {msg}")

def log_baslik(baslik):
    print("\n" + "="*60)
    print(f"  {baslik}")
    print("="*60)

# Global değişkenler (main'de başlatılacak)
driver = None
wait = None

def chrome_baslat():
    """Chrome tarayıcısını başlat"""
    global driver, wait
    
    if GORUNMEZ_MOD:
        log("👻 GÖRÜNMEZ MOD - Tarayıcı arka planda çalışacak")
    else:
        log("🌐 Tarayıcı başlatılıyor...")
    
    # Chrome ayarları
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Görünmez mod ayarları
    if GORUNMEZ_MOD:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        log("   ✓ Headless mod aktif")
    else:
        options.add_argument("--start-maximized")
    
    if HIZLI_MOD:
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.notifications": 2
        }
        options.add_experimental_option("prefs", prefs)
        log("   ✓ Hızlı mod aktif (resimler kapalı)")
    
    driver = webdriver.Chrome(options=options)
    
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """
    })
    
    wait = WebDriverWait(driver, BEKLEME)
    log("✅ Tarayıcı hazır!")

def close_popups_fast():
    """Popup'ları hızlıca kapat"""
    try:
        driver.execute_script("""
            document.querySelectorAll('.modal, .popup, [class*="cookie"], .modal-dialog, .modal-backdrop, [class*="overlay"]').forEach(el => {
                el.style.display = 'none';
                el.style.visibility = 'hidden';
                el.style.opacity = '0';
            });
        """)
    except:
        pass

def find_visible_element(selectors, timeout=10):
    """Birden fazla selector ile görünür element bul"""
    for by, value in selectors:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except:
            continue
    raise Exception("Element bulunamadı!")

def find_element_flexible(selectors, timeout=10):
    """Görünür olmasa bile element bul (JS ile scroll + click için)"""
    for by, value in selectors:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except:
            continue
    raise Exception("Element bulunamadı!")

def smart_input(element, text):
    """Akıllı input - Farklı yöntemler dene + event tetikle"""
    try:
        # Önce JS ile value set et
        driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element, text)
        return
    except:
        pass
    
    try:
        element.clear()
        element.send_keys(text)
        return
    except:
        pass
    
    try:
        element.send_keys(text)
    except:
        pass

def quick_click(element):
    """Hızlı tıklama"""
    try:
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        time.sleep(0.3)
        driver.execute_script("arguments[0].click();", element)
    except:
        element.click()

def kontrol_ve_onayla():
    """Kullanıcıdan onay al"""
    log_baslik("⏸️  KONTROL NOKTASI")
    log("🔍 Lütfen açık sekmeleri kontrol edin")
    log("✅ Her şey yolunda mı?")
    input("\n➡️  Devam etmek için ENTER'a basın...")
    log("▶️  Devam ediliyor...")

# ==========================================
# 🎯 SADECE KULLANİCI ADI SİTELERİ (adet yok)
# "enter": True  -> kullanıcı adı gir + Enter bas   (button yok)
# "enter": False/yok -> kullanıcı adı gir + onay butonu tıkla
# ==========================================
def site_islem_sadece_kullanici(site, index, total):
    """Adet alanı olmayan siteler için.
       enter: True  -> input'a yaz + Enter bas
       enter: False -> input'a yaz + onay butonu tıkla
    """
    max_deneme = 3
    kullan_enter = site.get("enter", False)  # default: button tıkla

    for deneme in range(max_deneme):
        try:
            if deneme > 0:
                log(f"🔄 {deneme+1}. deneme...")

            log(f"\n{'='*50}")
            log(f"🔄 {index+1}/{total} - {site['url']}")
            log(f"{'='*50}")

            driver.get(site["url"])
            time.sleep(3)

            WebDriverWait(driver, 25).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            time.sleep(2)

            close_popups_fast()

            # ── KULLANICI ADI / POST LİNKİ ──
            log("📝 Kullanıcı adı / Link giriliyor...")
            user_selectors = [
                (By.NAME, "freetool[process_item]"),
                (By.ID, "freeUsername"),
                (By.XPATH, "//input[contains(@placeholder,'Kullanıcı')]"),
                (By.XPATH, "//input[contains(@placeholder,'kullanıcı')]"),
                (By.XPATH, "//input[contains(@placeholder,'Username')]"),
                (By.XPATH, "//input[contains(@placeholder,'username')]"),
                (By.XPATH, "//input[contains(@placeholder,'instagram')]"),
                (By.XPATH, "//input[contains(@placeholder,'Instagram')]"),
                (By.XPATH, "//input[contains(@placeholder,'link')]"),
                (By.XPATH, "//input[contains(@placeholder,'Link')]"),
                (By.CSS_SELECTOR, "input.ord-control"),
                (By.CSS_SELECTOR, "input[type='text']"),
                (By.XPATH, "//input[@type='text']"),
                (By.XPATH, "//input[not(@type='hidden') and not(@type='submit')]"),
            ]

            user_input = find_element_flexible(user_selectors, timeout=20)

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", user_input)
            time.sleep(0.5)

            # Click + focus
            try:
                user_input.click()
                time.sleep(0.3)
            except:
                driver.execute_script("arguments[0].focus();", user_input)
                time.sleep(0.3)

            # send_keys ile yaz (JS value set değil — Enter sonrası tetikleme lazım)
            user_input.clear()
            user_input.send_keys(site["kullanici"])
            time.sleep(1)

            close_popups_fast()

            # ── KARAR: Enter mi yoksa Button mi? ──
            if kullan_enter:
                # ── ENTER YOLU ──
                log("⌨️  Enter basılıyor...")
                user_input.send_keys(Keys.ENTER)
                time.sleep(3)
                log(f"✅ {index+1}. site TAMAMLANDI (Enter)")
                return  # başarılı

            else:
                # ── BUTTON YOLU ──
                log("🔘 Onay butonu aranıyor...")
                btn_selectors = [
                    (By.CSS_SELECTOR, "button.free-start-btn"),
                    (By.XPATH, "//button[contains(text(),'Başlat')]"),
                    (By.XPATH, "//button[contains(text(),'BAŞLAT')]"),
                    (By.XPATH, "//button[contains(text(),'Gönder')]"),
                    (By.XPATH, "//button[contains(text(),'GÖNDER')]"),
                    (By.XPATH, "//button[contains(text(),'Onay')]"),
                    (By.XPATH, "//button[contains(text(),'ONAY')]"),
                    (By.XPATH, "//button[contains(text(),'Submit')]"),
                    (By.XPATH, "//button[contains(text(),'Tamamla')]"),
                    (By.XPATH, "//button[@type='submit']"),
                    (By.CSS_SELECTOR, "button[type='submit']"),
                    (By.XPATH, "//input[@type='submit']"),
                    (By.CSS_SELECTOR, "input[type='submit']"),
                    (By.XPATH, "//button[contains(@class,'btn')]"),
                    (By.XPATH, "//button[1]"),
                ]

                btn = find_element_flexible(btn_selectors, timeout=20)
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                time.sleep(1)

                clicked = False
                click_methods = [
                    ("JS Click",     lambda: driver.execute_script("arguments[0].click();", btn)),
                    ("Normal Click", lambda: btn.click()),
                    ("Form Submit",  lambda: driver.execute_script("arguments[0].closest('form').submit();", btn)),
                    ("ActionChain",  lambda: ActionChains(driver).move_to_element(btn).click(btn).perform()),
                ]

                for method_name, method_func in click_methods:
                    try:
                        method_func()
                        log(f"✓ Tıklama yöntemi: {method_name}")
                        clicked = True
                        break
                    except Exception as ex:
                        log(f"  ✗ {method_name}: {str(ex)[:40]}")
                        continue

                if not clicked:
                    raise Exception("Hiçbir tıklama yöntemi çalışmadı!")

                time.sleep(3)
                log(f"✅ {index+1}. site TAMAMLANDI (Button)")
                return  # başarılı

        except Exception as e:
            if deneme < max_deneme - 1:
                log(f"⚠️ {index+1}. site HATA: {str(e)[:60]} - Tekrar denenecek...")
                time.sleep(2)
            else:
                log(f"❌ {index+1}. site BAŞARISIZ ({max_deneme} deneme): {str(e)}")
                try:
                    driver.save_screenshot(f"hata_sadece_kullanici_{index+1}.png")
                except:
                    pass

def site_islem_ozel(site, index, total):
    """Özel/zor siteler için gelişmiş işlem (2 deneme)"""
    max_deneme = 2
    
    for deneme in range(max_deneme):
        try:
            if deneme > 0:
                log(f"🔄 {deneme+1}. deneme...")
            
            log(f"\n{'='*50}")
            log(f"🔄 {index+1}/{total} - {site['url']}")
            log(f"{'='*50}")
            
            driver.get(site["url"])
            time.sleep(2)
            
            WebDriverWait(driver, 20).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            time.sleep(1.5)
            
            close_popups_fast()
            
            # KULLANICI ADI
            log("📝 Kullanıcı adı...")
            user_selectors = [
                (By.NAME, "freetool[process_item]"),
                (By.ID, "freeUsername"),
                (By.XPATH, "//input[contains(@placeholder,'Kullanıcı')]"),
                (By.XPATH, "//input[contains(@placeholder,'kullanıcı')]"),
                (By.XPATH, "//input[contains(@placeholder,'Username')]"),
                (By.XPATH, "//input[contains(@placeholder,'username')]"),
                (By.CSS_SELECTOR, "input.ord-control"),
                (By.XPATH, "//input[@type='text' and not(@type='number')]"),
                (By.XPATH, "//input[@type='text']")
            ]
            
            user_input = find_visible_element(user_selectors, timeout=20)
            
            time.sleep(0.5)
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", user_input)
            time.sleep(0.5)
            
            smart_input(user_input, site["kullanici"])
            time.sleep(1)
            
            close_popups_fast()
            
            # ADET
            log("🔢 Adet...")
            qty_selectors = [
                (By.NAME, "freetool[quantity]"),
                (By.XPATH, "//input[@type='number']"),
                (By.XPATH, "//input[contains(@placeholder,'Miktar')]"),
                (By.XPATH, "//input[contains(@placeholder,'Adet')]")
            ]
            
            qty_input = find_visible_element(qty_selectors, timeout=20)
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", qty_input)
            time.sleep(0.5)
            
            smart_input(qty_input, site["adet"])
            time.sleep(1)
            
            close_popups_fast()
            
            # BAŞLAT
            log("🔘 Başlatılıyor...")
            btn_selectors = [
                (By.CSS_SELECTOR, "button.free-start-btn"),
                (By.XPATH, "//button[contains(text(),'Başlat')]"),
                (By.XPATH, "//button[contains(text(),'BAŞLAT')]"),
                (By.XPATH, "//button[contains(text(),'Gönder')]"),
                (By.XPATH, "//button[@type='submit']"),
                (By.CSS_SELECTOR, "button[type='submit']"),
            ]
            
            btn = find_visible_element(btn_selectors, timeout=20)
            
            attempts = [
                ("JavaScript", lambda: driver.execute_script("arguments[0].click();", btn)),
                ("Normal", lambda: btn.click()),
                ("Form submit", lambda: driver.execute_script("arguments[0].closest('form').submit();", btn)),
            ]
            
            for method_name, method_func in attempts:
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                    time.sleep(1)
                    method_func()
                    log(f"✓ {method_name} BAŞARILI!")
                    break
                except:
                    continue
            
            time.sleep(3)
            log(f"✅ {index+1}. site TAMAMLANDI")
            return  # Başarılı olduysa çık
            
        except Exception as e:
            if deneme < max_deneme - 1:
                log(f"⚠️ {index+1}. site HATA: {str(e)[:50]} - Tekrar denenecek...")
            else:
                log(f"❌ {index+1}. site BAŞARISIZ (2 deneme): {str(e)}")
                try:
                    driver.save_screenshot(f"hata_{index+1}.png")
                except:
                    pass

def site_islem_normal(site, index, total):
    """Normal siteler için işlem"""
    try:
        log(f"\n{'='*50}")
        log(f"🔄 {index+1}/{total} - {site['url']}")
        log(f"{'='*50}")
        
        driver.get(site["url"])
        time.sleep(1.5)
        
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        close_popups_fast()
        
        # KULLANICI ADI
        log("📝 Kullanıcı adı...")
        user_input = find_visible_element([
            (By.NAME, "freetool[process_item]"),
            (By.ID, "freeUsername"),
            (By.XPATH, "//input[contains(@placeholder,'Kullanıcı')]"),
            (By.CSS_SELECTOR, "input.ord-control"),
            (By.XPATH, "//input[@type='text']")
        ])
        smart_input(user_input, site["kullanici"])
        time.sleep(0.5)
        
        # ADET
        log("🔢 Adet...")
        qty_input = find_visible_element([
            (By.NAME, "freetool[quantity]"),
            (By.XPATH, "//input[@type='number']")
        ])
        smart_input(qty_input, site["adet"])
        time.sleep(0.5)
        
        close_popups_fast()
        
        # BAŞLAT
        log("🔘 Başlatılıyor...")
        btn = find_visible_element([
            (By.CSS_SELECTOR, "button.free-start-btn"),
            (By.XPATH, "//button[contains(text(),'Başlat')]"),
            (By.XPATH, "//button[@type='submit']")
        ])
        quick_click(btn)
        log(f"✅ {index+1}. site BAŞARILI")
        time.sleep(2)
        
    except Exception as e:
        log(f"❌ {index+1}. site HATA: {str(e)[:100]}")

def grup_isle(siteler, grup_adi):
    """Bir site grubunu işle"""
    log_baslik(f"📋 {grup_adi} BAŞLIYOR")
    log(f"Toplam {len(siteler)} site işlenecek")
    
    for i, site in enumerate(siteler):
        if i > 0:
            driver.execute_script("window.open('about:blank', '_blank');")
            time.sleep(0.5)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(0.5)
        
        # İşlem türünü belirle
        if site.get("sadece_kullanici", False):
            # Adet alanı olmayan siteler (takipcisatinal vb)
            site_islem_sadece_kullanici(site, i, len(siteler))
        elif site.get("ozel", False):
            site_islem_ozel(site, i, len(siteler))
        else:
            site_islem_normal(site, i, len(siteler))
        
        if i < len(siteler) - 1:
            time.sleep(1)
    
    log_baslik(f"✅ {grup_adi} TAMAMLANDI!")

def menu_goster():
    """Ana menüyü göster ve seçim al"""
    log_baslik("🎯 INSTAGRAM HİLESİ MENÜSÜ")
    print("\n" + "="*60)
    print("  🎭 LÜTFEN BİR SEÇENEK SEÇİN:")
    print("="*60)
    print("\n  1️⃣  - Takipçi Hilesi")
    print("  2️⃣  - Beğeni Hilesi")
    print("  3️⃣  - İzlenme Hilesi")
    print("  4️⃣  - Tüm Hileler (Takipçi + Beğeni + İzlenme)")
    print("\n" + "="*60)
    
    while True:
        secim = input("\n➡️  Seçiminiz (1/2/3/4): ").strip()
        if secim in ['1', '2', '3', '4']:
            return secim
        else:
            print("❌ Geçersiz seçim! Lütfen 1, 2, 3 veya 4 girin.")

# ==========================================
# 🚀 ANA PROGRAM - BURASI ÇALIŞIR
# ==========================================

def main():
    log_baslik("🎯 INSTAGRAM HİLESİ BOTU")
    log(f"⚙️  Ayarlar:")
    log(f"   - Hızlı Mod: {HIZLI_MOD}")
    log(f"   - Görünmez Mod: {GORUNMEZ_MOD}")
    log(f"   - Kontrol Bekleme: {KONTROL_BEKLEME_DAKIKA} dakika")
    
    # ==========================================
    # 1️⃣ MENÜ SEÇİMİ
    # ==========================================
    secim = menu_goster()
    
    # ==========================================
    # 2️⃣ INPUT ALMA (Seçime göre farklı)
    # ==========================================
    
    if secim == '1':
        # --- TAKİPÇİ: Sadece kullanıcı adı ---
        log(f"\n✅ Seçildi: TAKİPÇİ HİLESİ")
        log_baslik("📝 KULLANICI ADI")
        print(f"\n📝 Varsayılan: {VARSAYILAN_KULLANICI}")
        print(f"💡 Instagram kullanıcı adını girin\n")
        
        kullanici_input = input(f"➡️  Kullanıcı adı: ").strip()
        
        if kullanici_input:
            for site in SITELER_GRUP_1:
                site["kullanici"] = kullanici_input
            log(f"✅ Kullanıcı adı ayarlandı: {kullanici_input}")
        else:
            log(f"⚠️  Giriş yapılmadı! Varsayılan kullanılacak: {VARSAYILAN_KULLANICI}")
        
        input("\n⏸  Devam etmek için ENTER'a basın...")
        chrome_baslat()
        grup_isle(SITELER_GRUP_1, "TAKİPÇİ HİLESİ")
        
    elif secim == '2':
        # --- BEĞENİ: Sadece post linki ---
        log(f"\n✅ Seçildi: BEĞENİ HİLESİ")
        log_baslik("📝 POST LİNKİ")
        print(f"\n💡 Instagram post linkini girin\n")
        
        post_link = input(f"➡️  Post linki: ").strip()
        
        if post_link:
            for site in SITELER_GRUP_2:
                site["kullanici"] = post_link
            log(f"✅ Post linki ayarlandı: {post_link}")
        else:
            log(f"⚠️  Link girmediniz! Varsayılan kullanılacak: {VARSAYILAN_KULLANICI}")
        
        input("\n⏸  Devam etmek için ENTER'a basın...")
        chrome_baslat()
        grup_isle(SITELER_GRUP_2, "BEĞENİ HİLESİ")
        
    elif secim == '3':
        # --- İZLENME: Sadece post linki ---
        log(f"\n✅ Seçildi: İZLENME HİLESİ")
        log_baslik("📝 POST LİNKİ")
        print(f"\n💡 Instagram post linkini girin\n")
        
        post_link = input(f"➡️  Post linki: ").strip()
        
        if post_link:
            for site in SITELER_GRUP_3:
                site["kullanici"] = post_link
            log(f"✅ Post linki ayarlandı: {post_link}")
        else:
            log(f"⚠️  Link girmediniz! Varsayılan kullanılacak: {VARSAYILAN_KULLANICI}")
        
        input("\n⏸  Devam etmek için ENTER'a basın...")
        chrome_baslat()
        grup_isle(SITELER_GRUP_3, "İZLENME HİLESİ")
        
    elif secim == '4':
        # =====================================================
        # 4️⃣ HEPSİ: Kullanıcı adı VE post linki ayrı ayrı al
        # =====================================================
        log(f"\n✅ Seçildi: TÜM HİLELER (Takipçi + Beğeni + İzlenme)")
        
        # --- Kullanıcı adı al (Grup 1 için) ---
        log_baslik("📝 KULLANICI ADI (Takipçi Hilesi için)")
        print(f"\n📝 Varsayılan: {VARSAYILAN_KULLANICI}")
        print(f"💡 Instagram kullanıcı adını girin\n")
        
        kullanici_input = input(f"➡️  Kullanıcı adı: ").strip()
        
        if kullanici_input:
            for site in SITELER_GRUP_1:
                site["kullanici"] = kullanici_input
            log(f"✅ Kullanıcı adı ayarlandı: {kullanici_input}")
        else:
            log(f"⚠️  Giriş yapılmadı! Varsayılan kullanılacak: {VARSAYILAN_KULLANICI}")
        
        # --- Post linki al (Grup 2 ve 3 için) ---
        log_baslik("📝 POST LİNKİ (Beğeni + İzlenme Hilesi için)")
        print(f"\n💡 Instagram post linkini girin\n")
        
        post_link = input(f"➡️  Post linki: ").strip()
        
        if post_link:
            for site in SITELER_GRUP_2:
                site["kullanici"] = post_link
            for site in SITELER_GRUP_3:
                site["kullanici"] = post_link
            log(f"✅ Post linki ayarlandı: {post_link}")
        else:
            log(f"⚠️  Link girmediniz! Grup 2 ve 3 için varsayılan kullanılacak: {VARSAYILAN_KULLANICI}")
        
        # Özet göster
        log_baslik("📊 ÖZET")
        log(f"   Takipçi hilesi kullanıcı adı : {kullanici_input if kullanici_input else VARSAYILAN_KULLANICI}")
        log(f"   Beğeni + İzlenme post linki  : {post_link if post_link else VARSAYILAN_KULLANICI}")
        log(f"   Grup 1 site sayısı           : {len(SITELER_GRUP_1)}")
        log(f"   Grup 2 site sayısı           : {len(SITELER_GRUP_2)}")
        log(f"   Grup 3 site sayısı           : {len(SITELER_GRUP_3)}")
        
        input("\n⏸  Devam etmek için ENTER'a basın...")
        chrome_baslat()
        
        # --- GRUP 1: TAKİPÇİ ---
        grup_isle(SITELER_GRUP_1, "TAKİPÇİ HİLESİ")
        
        # Grup arası kısa bekleme
        log("\n⏳ Grup arası bekleme (3 sn)...")
        time.sleep(3)
        
        # --- GRUP 2: BEĞENİ ---
        grup_isle(SITELER_GRUP_2, "BEĞENİ HİLESİ")
        
        # Grup arası kısa bekleme
        log("\n⏳ Grup arası bekleme (3 sn)...")
        time.sleep(3)
        
        # --- GRUP 3: İZLENME ---
        grup_isle(SITELER_GRUP_3, "İZLENME HİLESİ")
    
    # ==========================================
    # ⏳ BEKLEME VE KONTROL
    # ==========================================
    log_baslik(f"⏳ {KONTROL_BEKLEME_DAKIKA} DAKİKA BEKLEME BAŞLADI")
    
    bekleme_saniye = KONTROL_BEKLEME_DAKIKA * 60
    bitis_zamani = time.time() + bekleme_saniye
    
    while time.time() < bitis_zamani:
        kalan = int(bitis_zamani - time.time())
        dakika = kalan // 60
        saniye = kalan % 60
        print(f"\r⏱️  Kalan süre: {dakika:02d}:{saniye:02d}", end="", flush=True)
        time.sleep(1)
    
    print("\n")
    log("✅ Bekleme tamamlandı!")
    
    # Kontrol ve onaylama
    kontrol_ve_onayla()
    
    # ==========================================
    # 🎉 BİTİŞ
    # ==========================================
    log_baslik("🎉 TÜM İŞLEMLER TAMAMLANDI!")
    log(f"🔖 Açık sekme sayısı: {len(driver.window_handles)}")
    
    input("\n⏸  Tarayıcıyı kapatmak için ENTER'a basın...")
    driver.quit()
    log("👋 Bot sonlandırıldı.")

# Program başlat
if __name__ == "__main__":
    main()
