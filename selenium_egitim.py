"""
SELENIUM EĞİTİM PROJESİ
========================
Bu proje Selenium ile web otomasyonu öğrenmek için hazırlanmıştır.
Gerçek siteler yerine test siteleri kullanılarak pratik yapılabilir.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, 
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
from typing import List, Tuple, Optional

# Logging yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


class SeleniumEgitim:
    """
    Selenium web otomasyon eğitim sınıfı
    """
    
    def __init__(self, headless: bool = False, wait_time: int = 10):
        """
        Args:
            headless: Tarayıcı görünür olmasın mı?
            wait_time: Maximum bekleme süresi (saniye)
        """
        self.headless = headless
        self.wait_time = wait_time
        self.driver = None
        self.wait = None
        
    def setup_driver(self):
        """Tarayıcıyı yapılandır"""
        logger.info("Tarayıcı başlatılıyor...")
        
        options = webdriver.ChromeOptions()
        
        # Headless mod (tarayıcı görünmeden çalışır)
        if self.headless:
            options.add_argument('--headless')
            
        # Bot algılamayı zorlaştır
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # Performans optimizasyonları
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Tarayıcı kapatma davranışı
        options.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, self.wait_time)
        
        # Pencere boyutunu ayarla
        self.driver.maximize_window()
        
        logger.info("Tarayıcı hazır ✓")
        
    # ========================================
    # DERS 1: Element Bulma Yöntemleri
    # ========================================
    
    def ders1_element_bulma(self):
        """Element bulma stratejileri"""
        logger.info("\n" + "="*50)
        logger.info("DERS 1: Element Bulma Yöntemleri")
        logger.info("="*50)
        
        # Test sitesi aç
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        # 1. ID ile bulma (en hızlı ve güvenilir)
        username_field = self.driver.find_element(By.ID, "username")
        logger.info("✓ ID ile element bulundu")
        
        # 2. NAME ile bulma
        password_field = self.driver.find_element(By.NAME, "password")
        logger.info("✓ NAME ile element bulundu")
        
        # 3. CLASS_NAME ile bulma
        try:
            element = self.driver.find_element(By.CLASS_NAME, "radius")
            logger.info("✓ CLASS_NAME ile element bulundu")
        except NoSuchElementException:
            logger.warning("✗ CLASS_NAME ile element bulunamadı")
        
        # 4. CSS_SELECTOR ile bulma (çok güçlü)
        button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
        logger.info("✓ CSS_SELECTOR ile element bulundu")
        
        # 5. XPATH ile bulma (en esnek ama yavaş)
        button_xpath = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        logger.info("✓ XPATH ile element bulundu")
        
        # 6. LINK_TEXT ile bulma
        self.driver.get("https://the-internet.herokuapp.com/")
        link = self.driver.find_element(By.LINK_TEXT, "Form Authentication")
        logger.info("✓ LINK_TEXT ile element bulundu")
        
        # 7. PARTIAL_LINK_TEXT ile bulma
        link_partial = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Form Auth")
        logger.info("✓ PARTIAL_LINK_TEXT ile element bulundu")
        
        time.sleep(2)
    
    # ========================================
    # DERS 2: Gelişmiş Element Bulma
    # ========================================
    
    def find_element_safe(
        self, 
        selectors: List[Tuple[str, str]], 
        clickable: bool = False,
        visible: bool = False
    ) -> Optional[object]:
        """
        Birden fazla selector ile güvenli element bulma
        
        Args:
            selectors: [(By.ID, "value"), (By.CSS_SELECTOR, "value"), ...]
            clickable: Element tıklanabilir olmalı mı?
            visible: Element görünür olmalı mı?
        
        Returns:
            Element veya None
        """
        for by, value in selectors:
            try:
                if clickable:
                    element = self.wait.until(
                        EC.element_to_be_clickable((by, value))
                    )
                elif visible:
                    element = self.wait.until(
                        EC.visibility_of_element_located((by, value))
                    )
                else:
                    element = self.wait.until(
                        EC.presence_of_element_located((by, value))
                    )
                
                logger.info(f"✓ Element bulundu: {by} = '{value}'")
                return element
                
            except TimeoutException:
                logger.debug(f"✗ Element bulunamadı: {by} = '{value}'")
                continue
        
        logger.error("✗ Hiçbir selector ile element bulunamadı!")
        return None
    
    def ders2_gelismis_element_bulma(self):
        """Gelişmiş element bulma stratejileri"""
        logger.info("\n" + "="*50)
        logger.info("DERS 2: Gelişmiş Element Bulma")
        logger.info("="*50)
        
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        
        # Start butonuna tıkla
        start_btn = self.driver.find_element(By.CSS_SELECTOR, "#start button")
        start_btn.click()
        
        # Dinamik olarak yüklenen elementi bekle
        logger.info("Dinamik element bekleniyor...")
        finish_text = self.wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        logger.info(f"✓ Dinamik element yüklendi: {finish_text.text}")
        
        # Birden fazla selector ile deneme
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username_selectors = [
            (By.ID, "username"),
            (By.NAME, "username"),
            (By.CSS_SELECTOR, "input#username"),
            (By.XPATH, "//input[@id='username']")
        ]
        
        username = self.find_element_safe(username_selectors)
        if username:
            username.send_keys("test")
        
        time.sleep(2)
    
    # ========================================
    # DERS 3: Form İşlemleri
    # ========================================
    
    def ders3_form_islemleri(self):
        """Form doldurma ve gönderme"""
        logger.info("\n" + "="*50)
        logger.info("DERS 3: Form İşlemleri")
        logger.info("="*50)
        
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        # Input'a yazma
        username = self.driver.find_element(By.ID, "username")
        username.clear()  # Önce temizle
        username.send_keys("tomsmith")
        logger.info("✓ Kullanıcı adı girildi")
        
        password = self.driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("SuperSecretPassword!")
        logger.info("✓ Şifre girildi")
        
        # Enter tuşu ile gönderme
        # password.send_keys(Keys.RETURN)
        
        # Veya buton ile gönderme
        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()
        logger.info("✓ Form gönderildi")
        
        # Sonucu kontrol et
        time.sleep(1)
        success_msg = self.driver.find_element(By.CSS_SELECTOR, ".flash.success")
        logger.info(f"✓ Başarı mesajı: {success_msg.text.strip()}")
        
        time.sleep(2)
    
    # ========================================
    # DERS 4: JavaScript ile Etkileşim
    # ========================================
    
    def ders4_javascript_kullanimi(self):
        """JavaScript executor kullanımı"""
        logger.info("\n" + "="*50)
        logger.info("DERS 4: JavaScript Kullanımı")
        logger.info("="*50)
        
        self.driver.get("https://the-internet.herokuapp.com/")
        
        # 1. Scroll işlemleri
        # En alta scroll
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logger.info("✓ Sayfanın en altına scroll yapıldı")
        time.sleep(1)
        
        # En üste scroll
        self.driver.execute_script("window.scrollTo(0, 0);")
        logger.info("✓ Sayfanın en üstüne scroll yapıldı")
        time.sleep(1)
        
        # 2. Elemente scroll
        link = self.driver.find_element(By.LINK_TEXT, "Dropdown")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
        logger.info("✓ Elemente scroll yapıldı")
        time.sleep(1)
        
        # 3. JavaScript ile tıklama (bazı durumlarda normal tıklama çalışmaz)
        self.driver.execute_script("arguments[0].click();", link)
        logger.info("✓ JavaScript ile tıklama yapıldı")
        time.sleep(1)
        
        # 4. Element stilini değiştirme (debugging için kullanışlı)
        dropdown = self.driver.find_element(By.ID, "dropdown")
        self.driver.execute_script(
            "arguments[0].style.border='5px solid red'; arguments[0].style.backgroundColor='yellow';",
            dropdown
        )
        logger.info("✓ Element stili değiştirildi")
        time.sleep(2)
        
        # 5. Sayfa bilgisi alma
        title = self.driver.execute_script("return document.title;")
        logger.info(f"✓ Sayfa başlığı: {title}")
        
        url = self.driver.execute_script("return window.location.href;")
        logger.info(f"✓ Sayfa URL: {url}")
    
    # ========================================
    # DERS 5: Bekleme Stratejileri
    # ========================================
    
    def ders5_bekleme_stratejileri(self):
        """Implicit, Explicit ve Fluent Wait"""
        logger.info("\n" + "="*50)
        logger.info("DERS 5: Bekleme Stratejileri")
        logger.info("="*50)
        
        # 1. Implicit Wait (tüm elementler için geçerli)
        self.driver.implicitly_wait(5)  # 5 saniye bekle
        logger.info("✓ Implicit wait ayarlandı (5 saniye)")
        
        # 2. Explicit Wait (belirli koşul için)
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        
        start_btn = self.driver.find_element(By.CSS_SELECTOR, "#start button")
        start_btn.click()
        
        # Element görünür olana kadar bekle
        wait = WebDriverWait(self.driver, 10)
        hello_text = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        logger.info(f"✓ Explicit wait ile element bulundu: {hello_text.text}")
        
        # 3. Custom bekleme koşulları
        self.driver.get("https://the-internet.herokuapp.com/")
        
        # Başlık belirli bir metin içerene kadar bekle
        wait.until(EC.title_contains("Internet"))
        logger.info("✓ Sayfa başlığı koşulu sağlandı")
        
        # Element tıklanabilir olana kadar bekle
        link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Checkboxes"))
        )
        logger.info("✓ Element tıklanabilir hale geldi")
        
        # 4. Thread.sleep (son çare olarak kullanılmalı)
        time.sleep(1)
        logger.info("✓ Hard wait (1 saniye)")
    
    # ========================================
    # DERS 6: Çoklu Tab/Window Yönetimi
    # ========================================
    
    def ders6_tab_yonetimi(self):
        """Çoklu tab ve window işlemleri"""
        logger.info("\n" + "="*50)
        logger.info("DERS 6: Tab/Window Yönetimi")
        logger.info("="*50)
        
        self.driver.get("https://the-internet.herokuapp.com/windows")
        
        # Mevcut window handle'ını sakla
        main_window = self.driver.current_window_handle
        logger.info(f"✓ Ana pencere handle: {main_window}")
        
        # Yeni pencere açan linke tıkla
        self.driver.find_element(By.LINK_TEXT, "Click Here").click()
        time.sleep(1)
        
        # Tüm pencere handle'larını al
        all_windows = self.driver.window_handles
        logger.info(f"✓ Toplam açık pencere sayısı: {len(all_windows)}")
        
        # Yeni pencereye geç
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                logger.info(f"✓ Yeni pencereye geçildi")
                logger.info(f"  Yeni pencere başlığı: {self.driver.title}")
                time.sleep(2)
                
                # Yeni pencereyi kapat
                self.driver.close()
                logger.info("✓ Yeni pencere kapatıldı")
        
        # Ana pencereye geri dön
        self.driver.switch_to.window(main_window)
        logger.info("✓ Ana pencereye geri dönüldü")
        
        # JavaScript ile yeni tab aç
        self.driver.execute_script("window.open('https://www.google.com', '_blank');")
        time.sleep(1)
        
        # Yeni tab'a geç
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logger.info(f"✓ Yeni tab açıldı: {self.driver.title}")
        time.sleep(2)
        
        # Tab'ı kapat ve ana pencereye dön
        self.driver.close()
        self.driver.switch_to.window(main_window)
        logger.info("✓ Ana pencereye dönüldü")
    
    # ========================================
    # DERS 7: İstisna Yönetimi (Exception Handling)
    # ========================================
    
    def ders7_exception_handling(self):
        """Hata yakalama ve yönetme"""
        logger.info("\n" + "="*50)
        logger.info("DERS 7: Exception Handling")
        logger.info("="*50)
        
        self.driver.get("https://the-internet.herokuapp.com/")
        
        # 1. NoSuchElementException
        try:
            element = self.driver.find_element(By.ID, "olmayan-element")
        except NoSuchElementException:
            logger.warning("✓ NoSuchElementException yakalandı")
        
        # 2. TimeoutException
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.presence_of_element_located((By.ID, "olmayan-element")))
        except TimeoutException:
            logger.warning("✓ TimeoutException yakalandı")
        
        # 3. ElementClickInterceptedException
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        start_btn = self.driver.find_element(By.CSS_SELECTOR, "#start button")
        start_btn.click()
        
        try:
            # Element üstü kapalıyken tıklamaya çalış
            time.sleep(0.1)
            hidden_element = self.driver.find_element(By.ID, "finish")
            hidden_element.click()
        except ElementClickInterceptedException:
            logger.warning("✓ ElementClickInterceptedException yakalandı")
        
        # Doğru yaklaşım - elementi bekle
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        logger.info("✓ Element görünür hale geldi")
        
        # 4. StaleElementReferenceException
        self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")
        remove_btn = self.driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")
        remove_btn.click()
        
        time.sleep(2)
        
        try:
            # Eski element referansını kullanmaya çalış (DOM değişti)
            remove_btn.click()
        except StaleElementReferenceException:
            logger.warning("✓ StaleElementReferenceException yakalandı")
            # Elementi yeniden bul
            add_btn = self.driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")
            logger.info(f"✓ Element yeniden bulundu: {add_btn.text}")
    
    # ========================================
    # DERS 8: ActionChains (İleri Seviye Etkileşimler)
    # ========================================
    
    def ders8_action_chains(self):
        """Mouse ve klavye ileri seviye etkileşimleri"""
        logger.info("\n" + "="*50)
        logger.info("DERS 8: ActionChains")
        logger.info("="*50)
        
        # 1. Hover (mouse üzerine getirme)
        self.driver.get("https://the-internet.herokuapp.com/hovers")
        
        action = ActionChains(self.driver)
        avatar = self.driver.find_element(By.CSS_SELECTOR, ".figure:nth-child(3)")
        
        action.move_to_element(avatar).perform()
        logger.info("✓ Mouse hover yapıldı")
        time.sleep(2)
        
        # 2. Drag and Drop
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        
        source = self.driver.find_element(By.ID, "column-a")
        target = self.driver.find_element(By.ID, "column-b")
        
        action.drag_and_drop(source, target).perform()
        logger.info("✓ Drag and drop yapıldı")
        time.sleep(2)
        
        # 3. Sağ tık (context menu)
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        
        box = self.driver.find_element(By.ID, "hot-spot")
        action.context_click(box).perform()
        logger.info("✓ Sağ tık yapıldı")
        
        # Alert'i kapat
        time.sleep(1)
        alert = self.driver.switch_to.alert
        logger.info(f"  Alert mesajı: {alert.text}")
        alert.accept()
        logger.info("✓ Alert kapatıldı")
        
        # 4. Çift tık
        action.double_click(box).perform()
        logger.info("✓ Çift tık yapıldı")
        time.sleep(1)
    
    # ========================================
    # DERS 9: Screenshot Alma
    # ========================================
    
    def ders9_screenshot(self):
        """Ekran görüntüsü alma"""
        logger.info("\n" + "="*50)
        logger.info("DERS 9: Screenshot")
        logger.info("="*50)
        
        self.driver.get("https://the-internet.herokuapp.com/")
        
        # Tam sayfa screenshot
        screenshot_path = "/home/claude/full_page_screenshot.png"
        self.driver.save_screenshot(screenshot_path)
        logger.info(f"✓ Tam sayfa screenshot alındı: {screenshot_path}")
        
        # Belirli elementin screenshot'ı
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        element_screenshot_path = "/home/claude/element_screenshot.png"
        heading.screenshot(element_screenshot_path)
        logger.info(f"✓ Element screenshot alındı: {element_screenshot_path}")
        
        # Base64 olarak alma (veritabanında saklamak için)
        base64_screenshot = self.driver.get_screenshot_as_base64()
        logger.info(f"✓ Base64 screenshot alındı (uzunluk: {len(base64_screenshot)})")
    
    # ========================================
    # DERS 10: Kapsamlı Örnek
    # ========================================
    
    def ders10_kapsamli_ornek(self):
        """Tüm teknikleri birleştiren kapsamlı örnek"""
        logger.info("\n" + "="*50)
        logger.info("DERS 10: Kapsamlı Örnek - Form Doldurma Botu")
        logger.info("="*50)
        
        try:
            # Test formu sayfasına git
            self.driver.get("https://the-internet.herokuapp.com/login")
            logger.info("✓ Sayfa yüklendi")
            
            # Kullanıcı adı girişi - birden fazla selector dene
            username_selectors = [
                (By.ID, "username"),
                (By.NAME, "username"),
                (By.CSS_SELECTOR, "input[type='text']")
            ]
            
            username_field = self.find_element_safe(username_selectors, visible=True)
            if not username_field:
                raise Exception("Kullanıcı adı alanı bulunamadı!")
            
            # Scroll ve highlight
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'}); "
                "arguments[0].style.border='3px solid red';",
                username_field
            )
            time.sleep(0.5)
            
            # Yazma animasyonu
            username = "tomsmith"
            for char in username:
                username_field.send_keys(char)
                time.sleep(0.1)
            logger.info("✓ Kullanıcı adı girildi")
            
            # Şifre girişi
            password_selectors = [
                (By.ID, "password"),
                (By.NAME, "password"),
                (By.CSS_SELECTOR, "input[type='password']")
            ]
            
            password_field = self.find_element_safe(password_selectors, visible=True)
            if password_field:
                self.driver.execute_script(
                    "arguments[0].style.border='3px solid red';",
                    password_field
                )
                password_field.send_keys("SuperSecretPassword!")
                logger.info("✓ Şifre girildi")
            
            # Butonu bul ve tıkla
            button_selectors = [
                (By.CSS_SELECTOR, "button[type='submit']"),
                (By.XPATH, "//button[contains(@class, 'radius')]"),
                (By.CSS_SELECTOR, ".radius")
            ]
            
            submit_btn = self.find_element_safe(button_selectors, clickable=True)
            if submit_btn:
                # JavaScript ile tıklama (daha güvenilir)
                self.driver.execute_script("arguments[0].click();", submit_btn)
                logger.info("✓ Form gönderildi")
            
            # Sonucu bekle ve kontrol et
            wait = WebDriverWait(self.driver, 10)
            success_message = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success"))
            )
            
            logger.info(f"✓ Başarılı giriş: {success_message.text.strip()}")
            
            # Screenshot al
            self.driver.save_screenshot("/home/claude/login_success.png")
            logger.info("✓ Başarı screenshot'ı alındı")
            
            time.sleep(2)
            
        except Exception as e:
            logger.error(f"✗ Hata oluştu: {str(e)}")
            # Hata durumunda screenshot al
            self.driver.save_screenshot("/home/claude/error_screenshot.png")
            raise
    
    # ========================================
    # ANA ÇALIŞTIRMA FONKSİYONU
    # ========================================
    
    def tum_dersleri_calistir(self):
        """Tüm dersleri sırayla çalıştır"""
        try:
            self.setup_driver()
            
            logger.info("\n" + "🎓 " + "="*48)
            logger.info("🎓  SELENIUM EĞİTİM PROJESİ BAŞLIYOR")
            logger.info("🎓 " + "="*48 + "\n")
            
            # Her dersi çalıştır
            dersler = [
                ("Element Bulma", self.ders1_element_bulma),
                ("Gelişmiş Element Bulma", self.ders2_gelismis_element_bulma),
                ("Form İşlemleri", self.ders3_form_islemleri),
                ("JavaScript Kullanımı", self.ders4_javascript_kullanimi),
                ("Bekleme Stratejileri", self.ders5_bekleme_stratejileri),
                ("Tab Yönetimi", self.ders6_tab_yonetimi),
                ("Exception Handling", self.ders7_exception_handling),
                ("ActionChains", self.ders8_action_chains),
                ("Screenshot", self.ders9_screenshot),
                ("Kapsamlı Örnek", self.ders10_kapsamli_ornek)
            ]
            
            for i, (ders_adi, ders_fonk) in enumerate(dersler, 1):
                try:
                    ders_fonk()
                    logger.info(f"✅ Ders {i} tamamlandı: {ders_adi}\n")
                    time.sleep(1)
                except Exception as e:
                    logger.error(f"❌ Ders {i} hatası ({ders_adi}): {str(e)}\n")
                    continue
            
            logger.info("\n" + "🎉 " + "="*48)
            logger.info("🎉  TÜM DERSLER TAMAMLANDI!")
            logger.info("🎉 " + "="*48 + "\n")
            
            input("Tarayıcıyı kapatmak için ENTER'a basın...")
            
        except KeyboardInterrupt:
            logger.info("\n⚠️  Kullanıcı tarafından durduruldu")
        except Exception as e:
            logger.error(f"\n❌ Kritik hata: {str(e)}")
        finally:
            if self.driver:
                self.driver.quit()
                logger.info("✓ Tarayıcı kapatıldı")


# ========================================
# PROGRAM BAŞLANGICI
# ========================================

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║        SELENIUM WEB OTOMASYON EĞİTİMİ             ║
    ║                                                    ║
    ║  Bu program Selenium kütüphanesini öğrenmek       ║
    ║  için hazırlanmış interaktif bir eğitim projesi   ║
    ║                                                    ║
    ║  Kapsanan Konular:                                ║
    ║  • Element Bulma Stratejileri                     ║
    ║  • Form İşlemleri                                 ║
    ║  • JavaScript Executor                            ║
    ║  • Bekleme Teknikleri                             ║
    ║  • Tab/Window Yönetimi                            ║
    ║  • Exception Handling                             ║
    ║  • ActionChains (Hover, Drag-Drop)                ║
    ║  • Screenshot Alma                                ║
    ║  • Kapsamlı Uygulamalar                           ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """)
    
    # Kullanıcı seçimi
    print("\nNasıl çalıştırmak istersiniz?")
    print("1. Tüm dersleri otomatik çalıştır")
    print("2. Sadece belirli bir ders")
    print("3. Headless modda çalıştır (tarayıcı görünmez)")
    
    secim = input("\nSeçiminiz (1-3): ").strip()
    
    egitim = SeleniumEgitim(headless=(secim == "3"))
    
    if secim == "1" or secim == "3":
        egitim.tum_dersleri_calistir()
    elif secim == "2":
        print("\nHangi dersi çalıştırmak istersiniz?")
        print("1. Element Bulma")
        print("2. Gelişmiş Element Bulma")
        print("3. Form İşlemleri")
        print("4. JavaScript Kullanımı")
        print("5. Bekleme Stratejileri")
        print("6. Tab Yönetimi")
        print("7. Exception Handling")
        print("8. ActionChains")
        print("9. Screenshot")
        print("10. Kapsamlı Örnek")
        
        ders = input("\nDers numarası (1-10): ").strip()
        
        try:
            egitim.setup_driver()
            
            ders_map = {
                "1": egitim.ders1_element_bulma,
                "2": egitim.ders2_gelismis_element_bulma,
                "3": egitim.ders3_form_islemleri,
                "4": egitim.ders4_javascript_kullanimi,
                "5": egitim.ders5_bekleme_stratejileri,
                "6": egitim.ders6_tab_yonetimi,
                "7": egitim.ders7_exception_handling,
                "8": egitim.ders8_action_chains,
                "9": egitim.ders9_screenshot,
                "10": egitim.ders10_kapsamli_ornek
            }
            
            if ders in ders_map:
                ders_map[ders]()
                input("\nDers tamamlandı. ENTER'a basın...")
            else:
                print("Geçersiz ders numarası!")
                
        finally:
            if egitim.driver:
                egitim.driver.quit()
    else:
        print("Geçersiz seçim!")
