import random
import json
import os
#emrepythonn
class CreditCardGenerator:
    def __init__(self):
        self.countries = {
            "1": {"name": "Amerika", "iin": ["4"], "length": 16},
            "2": {"name": "Rusya", "iin": ["2200", "2201", "2202", "2203"], "length": 16},
            "3": {"name": "Türkiye", "iin": ["9792", "5179", "5520"], "length": 16},
            "4": {"name": "Almanya", "iin": ["3"], "length": 16},
            "5": {"name": "İngiltere", "iin": ["45", "49"], "length": 16}
        }
        self.data_file = "credit_cards.json"
        self.load_existing_cards()
    
    def load_existing_cards(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                try:
                    self.existing_cards = json.load(f)
                except:
                    self.existing_cards = []
        else:
            self.existing_cards = []
    
    def save_cards(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.existing_cards, f, ensure_ascii=False, indent=2)
    
    def luhn_check(self, number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        
        digits = digits_of(number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10 == 0
    
    def generate_card_number(self, iin_prefix, length):
        while True:
            card_number = iin_prefix
            
            while len(card_number) < length - 1:
                card_number += str(random.randint(0, 9))
           
            total = 0
            for i, digit in enumerate(card_number[::-1]):
                n = int(digit)
                if i % 2 == 0:
                    n *= 2
                    if n > 9:
                        n -= 9
                total += n
            
            check_digit = (10 - (total % 10)) % 10
            card_number += str(check_digit)
            
            if self.luhn_check(card_number):
                return card_number
    
    def generate_expiry_date(self):
        year = random.randint(2025, 2030)
        month = random.randint(1, 12)
        return f"{month:02d}/{year}"
    
    def generate_cvv(self):
        return f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
    
    def format_card_number(self, card_number):
        return ' '.join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
    
    def display_countries(self):
        print("\n" + "_"*50)
        print("CC Random Tool")
        print("_"*50)
        for key, country in self.countries.items():
            print(f"{key}. {country['name']}")
        print("_"*50)
    
    def generate_cards(self):
        try:

            self.display_countries()
            country_choice = input("Lütfen bir ülke seçin (1-5): ").strip()
            
            if country_choice not in self.countries:
                print("❌ Geçersiz seçim! Lütfen 1-5 arasında bir numara girin.")
                return
            
            try:
                quantity = int(input("Kaç adet kart oluşturmak istiyorsunuz?: ").strip())
                if quantity <= 0 or quantity > 100:
                    print("❌ Geçersiz miktar! Lütfen 1-100 arasında bir sayı girin.")
                    return
            except ValueError:
                print("❌ Geçersiz giriş! Lütfen bir sayı girin.")
                return
            
            country = self.countries[country_choice]
            generated_cards = []
            
            print(f"\n🔄 {country['name']} için {quantity} adet kart oluşturuluyor...")
            print("-" * 60)
            
            for i in range(quantity):
                iin_prefix = random.choice(country['iin'])
                
                card_number = self.generate_card_number(iin_prefix, country['length'])
                expiry_date = self.generate_expiry_date()
                cvv = self.generate_cvv()
                
                card_data = {
                    "id": len(self.existing_cards) + i + 1,
                    "ülke": country['name'],
                    "kart_numarası": card_number,
                    "biçimlendirilmiş_kart": self.format_card_number(card_number),
                    "son_kullanma_tarihi": expiry_date,
                    "cvv": cvv,
                    "tip": "Visa" if iin_prefix.startswith('4') else "MasterCard"
                }
                
                generated_cards.append(card_data)
                
                print(f"\n💳 KART {i+1}:")
                print(f"   Ülke: {country['name']}")
                print(f"   Kart No: {self.format_card_number(card_number)}")
                print(f"   Son Kullanma: {expiry_date}")
                print(f"   CVV: {cvv}")
                print(f"   Tip: {card_data['tip']}")
                print(f"   By: @emrepythonn ✅")
                print("-" * 40)
            
            save_choice = input("\n💾 Bu kartları cihaza kaydetmek istiyor musunuz? (e/h): ").strip().lower()
            
            if save_choice == 'e':
                self.existing_cards.extend(generated_cards)
                self.save_cards()
                print(f"✅ {len(generated_cards)} adet kart başarıyla kaydedildi!")
            else:
                print("Kartlar kaydedilmedi.")
            
            print(f"kayıtlı kart sayısı: {len(self.existing_cards)}")
            
        except KeyboardInterrupt:
            print("\n\nİşlem iptal edildi.")
        except Exception as e:
            print(f"❌ Bir hata oluştu: {str(e)}")
    
    def show_saved_cards(self):
        if not self.existing_cards:
            print("📭 Kayıtlı hiç kart bulunmamaktadır.")
            return
        
        print(f"\nKartlar ({len(self.existing_cards)} adet):")
        print("_" * 70)
        
        for card in self.existing_cards[-10:]:  
            print(f"ID: {card['id']} | {card['ülke']} | {card['biçimlendirilmiş_kart']} | {card['son_kullanma_tarihi']} | CVV: {card['cvv']}")
        
        if len(self.existing_cards) > 10:
            print(f"... ve {len(self.existing_cards) - 10} adet daha kart")
    
    def clear_saved_cards(self):
        if not self.existing_cards:
            print("📭 Zaten hiç kayıtlı kart yok.")
            return
        
        confirm = input("⚠️ Tüm kayıtlı kartları silmek istediğinizden emin misiniz? (e/h): ").strip().lower()
        if confirm == 'e':
            self.existing_cards = []
            self.save_cards()
            print("✅ Tüm kartlar başarıyla silindi!")
        else:
            print("ℹ️ İşlem iptal edildi.")
    
    def run(self):
        while True:
            print("\n" + "_"*50)
            print("💳 CC Random Tool")
            print("_"*50)
            print("1. Kartlar Oluştur")
            print("2. Kartları Görüntüle")
            print("3. Kartları Sil")
            print("4. Çıkış")
            print("_"*50)
            
            choice = input("Lütfen bir seçenek girin (1-4): ").strip()
            
            if choice == '1':
                self.generate_cards()
            elif choice == '2':
                self.show_saved_cards()
            elif choice == '3':
                self.clear_saved_cards()
            elif choice == '4':
                print("👋 Programdan çıkılıyor... @emrepythonn")
                break
            else:
                print("❌ Geçersiz seçim! Lütfen 1-4 arasında bir numara girin.")

if __name__ == "__main__":
    generator = CreditCardGenerator()
    generator.run()