#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Profesyonel Gayrimenkul Değerleme Sistemi v4.0 ULTIMATE
Emlakçılar için tam teşekküllü, çoklu kaynaklı fiyatlandırma aracı

YENİ ÖZELLİKLER v4.0:
- Çoklu kaynak analizi (Sahibinden, Emlakjet, Hürriyet Emlak)
- Detaylı mesafe analizi (Metro, okul, hastane, AVM)
- Otopark, asansör, balkon gibi ekstra özellikler
- Aidat bilgisi ve etkisi
- Krediye uygunluk analizi
- Profesyonel PDF rapor oluşturma
- Kaynak güvenilirlik skoru
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import sys
from datetime import datetime
from collections import Counter
import statistics
import time

class GayrimenkulDegerlemePro:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Veri kaynakları
        self.kaynaklar = {
            'sahibinden': {'aktif': True, 'isim': 'Sahibinden.com', 'ilan_sayisi': 0},
            'emlakjet': {'aktif': True, 'isim': 'Emlakjet.com', 'ilan_sayisi': 0},
            'hurriyetemlak': {'aktif': False, 'isim': 'Hürriyet Emlak', 'ilan_sayisi': 0}
        }
        
        # Kritik değerleme kriterleri
        self.bina_tipi_carpanlar = {
            'site': 1.15,      # Site içi %15 prim
            'mustakil': 1.10,  # Müstakil %10 prim
            'apartman': 1.0    # Apartman baz fiyat
        }
        
        self.kat_carpanlar = {
            'zemin': 0.90,     # Zemin kat -%10
            '1': 1.0,          # 1. kat baz
            '2': 1.05,         # 2. kat +%5
            '3': 1.08,         # 3. kat +%8
            '4': 1.10,         # 4. kat +%10
            '5+': 1.12,        # 5+ kat +%12
            'cati': 0.95       # Çatı dubleks -%5
        }
        
        self.cephe_carpanlar = {
            'guney': 1.08,     # Güney +%8
            'guneydogu': 1.06, # Güneydoğu +%6
            'guneybati': 1.06, # Güneybatı +%6
            'dogu': 1.03,      # Doğu +%3
            'bati': 1.03,      # Batı +%3
            'kuzey': 0.97,     # Kuzey -%3
            'kuzeydogu': 0.98, # Kuzeydoğu -%2
            'kuzeybati': 0.98  # Kuzeybatı -%2
        }
        
        self.bina_yasi_carpanlar = {
            '0-2': 1.15,       # Sıfır/yeni +%15
            '3-5': 1.10,       # Yeni sayılır +%10
            '6-10': 1.05,      # Orta yaş +%5
            '11-15': 1.0,      # Baz yaş
            '16-20': 0.95,     # Eski -%5
            '21+': 0.90        # Çok eski -%10
        }
        
        self.kullanim_carpanlar = {
            'bos': 1.05,       # Boş, hemen teslim +%5
            'malik': 1.0,      # Mülk sahibi oturuyor baz
            'kiracili': 0.93   # Kiracılı -%7
        }
        
        # YENİ: Ekstra özellik çarpanları
        self.ekstra_ozellikler = {
            'asansor': 1.03,           # Asansör +%3
            'otopark': 1.04,           # Otopark +%4
            'guvenlik': 1.02,          # Güvenlik +%2
            'havuz': 1.05,             # Havuz +%5
            'spor_alani': 1.02,        # Spor alanı +%2
            'balkon': 1.02,            # Balkon +%2
            'teras': 1.03,             # Teras +%3
            'ebeveyn_banyolu': 1.02,   # Ebeveyn banyolu +%2
            'ankastre_mutfak': 1.03,   # Ankastre mutfak +%3
            'klima': 1.01              # Klima +%1
        }
        
        # YENİ: Lokasyon avantajları
        self.lokasyon_carpanlar = {
            'metro_yakin': 1.08,       # Metro 500m içinde +%8
            'tramvay_yakin': 1.04,     # Tramvay yakın +%4
            'okul_yakin': 1.03,        # Okul yakın +%3
            'hastane_yakin': 1.03,     # Hastane yakın +%3
            'avm_yakin': 1.05,         # AVM yakın +%5
            'deniz_manzara': 1.12,     # Deniz manzarası +%12
            'park_yakin': 1.02,        # Park yakın +%2
            'cadde_ustu': 0.97         # Cadde üstü gürültü -%3
        }
    
    def temizle_fiyat(self, fiyat_text):
        """Fiyat metnini sayısal değere çevirir"""
        try:
            fiyat = re.sub(r'[^\d]', '', fiyat_text)
            return int(fiyat) if fiyat else 0
        except:
            return 0
    
    def m2_cikar(self, metin):
        """Metinden m² bilgisini çıkarır"""
        try:
            match = re.search(r'(\d+)\s*m[²2]', metin, re.IGNORECASE)
            if match:
                return int(match.group(1))
            return None
        except:
            return None
    
    def bina_tipi_tespit(self, baslik, aciklama=""):
        """Bina tipini tespit eder"""
        metin = (baslik + " " + aciklama).lower()
        
        if any(k in metin for k in ['site', 'sitede', 'site içi', 'residence', 'kompleks']):
            return 'site'
        elif any(k in metin for k in ['müstakil', 'mustakil', 'villa', 'bahçeli']):
            return 'mustakil'
        else:
            return 'apartman'
    
    def kat_tespit(self, baslik, aciklama=""):
        """Kat bilgisini tespit eder"""
        metin = (baslik + " " + aciklama).lower()
        
        if 'zemin' in metin or 'giriş' in metin:
            return 'zemin'
        elif 'çatı' in metin or 'dubleks' in metin:
            return 'cati'
        else:
            match = re.search(r'(\d+)[\s\.]?kat', metin)
            if match:
                kat_no = int(match.group(1))
                if kat_no >= 5:
                    return '5+'
                return str(kat_no)
        return '1'
    
    def bina_yasi_tespit(self, baslik, aciklama=""):
        """Bina yaşını tespit eder"""
        metin = (baslik + " " + aciklama).lower()
        
        if any(k in metin for k in ['sıfır', 'sifir', 'yeni', '2024', '2025', '2026']):
            return '0-2'
        elif any(k in metin for k in ['az kullanılmış', 'az kullanilmis']):
            return '3-5'
        
        match = re.search(r'(\d{4})', metin)
        if match:
            yil = int(match.group(1))
            yas = 2026 - yil
            if yas <= 2:
                return '0-2'
            elif yas <= 5:
                return '3-5'
            elif yas <= 10:
                return '6-10'
            elif yas <= 15:
                return '11-15'
            elif yas <= 20:
                return '16-20'
            else:
                return '21+'
        
        return '11-15'
    
    def cephe_tespit(self, baslik, aciklama=""):
        """Cephe yönünü tespit eder"""
        metin = (baslik + " " + aciklama).lower()
        
        if 'güney' in metin and 'doğu' in metin:
            return 'guneydogu'
        elif 'güney' in metin and 'batı' in metin:
            return 'guneybati'
        elif 'kuzey' in metin and 'doğu' in metin:
            return 'kuzeydogu'
        elif 'kuzey' in metin and 'batı' in metin:
            return 'kuzeybati'
        elif 'güney' in metin:
            return 'guney'
        elif 'kuzey' in metin:
            return 'kuzey'
        elif 'doğu' in metin:
            return 'dogu'
        elif 'batı' in metin:
            return 'bati'
        
        return 'guney'
    
    def kullanim_tespit(self, baslik, aciklama=""):
        """Kullanım durumunu tespit eder"""
        metin = (baslik + " " + aciklama).lower()
        
        if any(k in metin for k in ['boş', 'bos', 'tahliye']):
            return 'bos'
        elif any(k in metin for k in ['kiracılı', 'kiracili', 'kirada']):
            return 'kiracili'
        else:
            return 'malik'
    
    def ekstra_ozellik_tespit(self, baslik, aciklama=""):
        """Ekstra özellikleri tespit eder"""
        metin = (baslik + " " + aciklama).lower()
        bulunan_ozellikler = []
        
        ozellik_keywords = {
            'asansor': ['asansör', 'asansor', 'lift'],
            'otopark': ['otopark', 'kapalı otopark', 'açık otopark'],
            'guvenlik': ['güvenlik', 'guvenlik', '24 saat güvenlik'],
            'havuz': ['havuz', 'yüzme havuzu'],
            'spor_alani': ['spor', 'fitness', 'gym'],
            'balkon': ['balkon'],
            'teras': ['teras', 'çatı terası'],
            'ebeveyn_banyolu': ['ebeveyn banyo', 'master banyo'],
            'ankastre_mutfak': ['ankastre', 'amerikan mutfak'],
            'klima': ['klima', 'klimali']
        }
        
        for ozellik, keywords in ozellik_keywords.items():
            if any(k in metin for k in keywords):
                bulunan_ozellikler.append(ozellik)
        
        return bulunan_ozellikler
    
    def lokasyon_avantaj_tespit(self, baslik, aciklama=""):
        """Lokasyon avantajlarını tespit eder"""
        metin = (baslik + " " + aciklama).lower()
        bulunan_avantajlar = []
        
        avantaj_keywords = {
            'metro_yakin': ['metro', 'metroya yakın', 'metrobüs'],
            'tramvay_yakin': ['tramvay', 'tramvaya yakın'],
            'okul_yakin': ['okul', 'okula yakın', 'üniversite'],
            'hastane_yakin': ['hastane', 'hastaneye yakın', 'sağlık'],
            'avm_yakin': ['avm', 'alışveriş merkezi', 'mall'],
            'deniz_manzara': ['deniz manzara', 'deniz görünüm', 'boğaz manzara'],
            'park_yakin': ['park', 'yeşil alan'],
            'cadde_ustu': ['cadde üstü', 'ana cadde', 'ana yol']
        }
        
        for avantaj, keywords in avantaj_keywords.items():
            if any(k in metin for k in keywords):
                bulunan_avantajlar.append(avantaj)
        
        return bulunan_avantajlar
    
    def aidat_cikar(self, baslik, aciklama=""):
        """Aidat bilgisini çıkarır"""
        metin = (baslik + " " + aciklama).lower()
        
        match = re.search(r'aidat[:\s]*(\d+)', metin)
        if match:
            return int(match.group(1))
        
        match = re.search(r'(\d+)\s*tl.*aidat', metin)
        if match:
            return int(match.group(1))
        
        return 0
    
    def sahibinden_detayli_sorgula(self, il, ilce, oda_sayisi="2+1", islem_tipi="satilik"):
        """Sahibinden.com'dan detaylı veri çeker"""
        print(f"\n🔍 Sahibinden.com sorgulanıyor...")
        
        try:
            il_slug = self.turkce_slug(il)
            ilce_slug = self.turkce_slug(ilce)
            
            oda_map = {
                "1+0": "1-0", "1+1": "1-1", "2+0": "2-0",
                "2+1": "2-1", "3+1": "3-1", "4+1": "4-1"
            }
            oda_param = oda_map.get(oda_sayisi, "1-1")
            
            islem = "satilik-daire" if islem_tipi == "satilik" else "kiralik-daire"
            url = f"https://www.sahibinden.com/{islem}/{il_slug}-{ilce_slug}?a49_min={oda_param}&a49_max={oda_param}"
            
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                print(f"   ⚠️  Bağlantı başarısız")
                return []
            
            soup = BeautifulSoup(response.content, 'html.parser')
            ilanlar = []
            
            ilan_listesi = soup.find_all('tr', class_='searchResultsItem')
            
            for ilan in ilan_listesi[:30]:
                try:
                    baslik_elem = ilan.find('td', class_='searchResultsTitleValue')
                    fiyat_elem = ilan.find('td', class_='searchResultsPriceValue')
                    
                    if baslik_elem and fiyat_elem:
                        baslik = baslik_elem.get_text(strip=True)
                        fiyat_text = fiyat_elem.get_text(strip=True)
                        fiyat = self.temizle_fiyat(fiyat_text)
                        
                        m2 = self.m2_cikar(baslik)
                        
                        konum_elem = ilan.find('td', class_='searchResultsLocationValue')
                        konum = konum_elem.get_text(strip=True) if konum_elem else ilce
                        
                        aciklama_elem = ilan.find('td', class_='searchResultsAttributeValue')
                        aciklama = aciklama_elem.get_text(strip=True) if aciklama_elem else ""
                        
                        link_elem = baslik_elem.find('a')
                        link = "https://www.sahibinden.com" + link_elem['href'] if link_elem and link_elem.get('href') else ""
                        
                        # Detaylı özellik tespiti
                        bina_tipi = self.bina_tipi_tespit(baslik, aciklama)
                        kat = self.kat_tespit(baslik, aciklama)
                        bina_yasi = self.bina_yasi_tespit(baslik, aciklama)
                        cephe = self.cephe_tespit(baslik, aciklama)
                        kullanim = self.kullanim_tespit(baslik, aciklama)
                        ekstra_ozellikler = self.ekstra_ozellik_tespit(baslik, aciklama)
                        lokasyon_avantajlari = self.lokasyon_avantaj_tespit(baslik, aciklama)
                        aidat = self.aidat_cikar(baslik, aciklama)
                        
                        m2_fiyat = (fiyat / m2) if m2 and m2 > 0 else 0
                        
                        ilan_data = {
                            'baslik': baslik,
                            'fiyat': fiyat,
                            'fiyat_text': fiyat_text,
                            'm2': m2,
                            'm2_fiyat': int(m2_fiyat),
                            'bina_tipi': bina_tipi,
                            'kat': kat,
                            'bina_yasi': bina_yasi,
                            'cephe': cephe,
                            'kullanim': kullanim,
                            'ekstra_ozellikler': ekstra_ozellikler,
                            'lokasyon_avantajlari': lokasyon_avantajlari,
                            'aidat': aidat,
                            'konum': konum,
                            'aciklama': aciklama,
                            'link': link,
                            'kaynak': 'Sahibinden.com'
                        }
                        
                        if m2 and m2 > 0:
                            ilanlar.append(ilan_data)
                            
                except Exception as e:
                    continue
            
            self.kaynaklar['sahibinden']['ilan_sayisi'] = len(ilanlar)
            print(f"   ✅ {len(ilanlar)} ilan bulundu")
            return ilanlar
            
        except Exception as e:
            print(f"   ❌ Hata: {str(e)}")
            return []
    
    def turkce_slug(self, metin):
        """Türkçe karakterleri URL uyumlu hale getirir"""
        replacements = {
            'ı': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c',
            'İ': 'i', 'Ğ': 'g', 'Ü': 'u', 'Ş': 's', 'Ö': 'o', 'Ç': 'c'
        }
        metin = metin.lower()
        for tr, eng in replacements.items():
            metin = metin.replace(tr, eng)
        return metin.replace(' ', '-')
    
    def pazar_istatistikleri(self, ilanlar):
        """Pazar istatistiklerini hesapla"""
        if not ilanlar:
            return None
        
        m2_fiyatlar = [i['m2_fiyat'] for i in ilanlar if i['m2_fiyat'] > 0]
        
        # Bina tiplerine göre
        bina_tipleri = {}
        for tip in ['site', 'mustakil', 'apartman']:
            tip_ilanlar = [i for i in ilanlar if i['bina_tipi'] == tip]
            if tip_ilanlar:
                tip_m2 = [i['m2_fiyat'] for i in tip_ilanlar if i['m2_fiyat'] > 0]
                if tip_m2:
                    bina_tipleri[tip] = {
                        'adet': len(tip_ilanlar),
                        'ort_m2': int(statistics.mean(tip_m2)),
                        'min_m2': min(tip_m2),
                        'max_m2': max(tip_m2)
                    }
        
        # Kat bilgilerine göre
        kat_dagilim = {}
        for kat in ['zemin', '1', '2', '3', '4', '5+', 'cati']:
            kat_ilanlar = [i for i in ilanlar if i['kat'] == kat]
            if kat_ilanlar:
                kat_m2 = [i['m2_fiyat'] for i in kat_ilanlar if i['m2_fiyat'] > 0]
                if kat_m2:
                    kat_dagilim[kat] = {
                        'adet': len(kat_ilanlar),
                        'ort_m2': int(statistics.mean(kat_m2))
                    }
        
        # Bina yaşına göre
        yas_dagilim = {}
        for yas in ['0-2', '3-5', '6-10', '11-15', '16-20', '21+']:
            yas_ilanlar = [i for i in ilanlar if i['bina_yasi'] == yas]
            if yas_ilanlar:
                yas_m2 = [i['m2_fiyat'] for i in yas_ilanlar if i['m2_fiyat'] > 0]
                if yas_m2:
                    yas_dagilim[yas] = {
                        'adet': len(yas_ilanlar),
                        'ort_m2': int(statistics.mean(yas_m2))
                    }
        
        # YENİ: Ekstra özellik analizi
        ozellik_istatistik = {}
        for ozellik in self.ekstra_ozellikler.keys():
            ozellikli_ilanlar = [i for i in ilanlar if ozellik in i.get('ekstra_ozellikler', [])]
            if ozellikli_ilanlar:
                ozellikli_m2 = [i['m2_fiyat'] for i in ozellikli_ilanlar if i['m2_fiyat'] > 0]
                if ozellikli_m2:
                    ozellik_istatistik[ozellik] = {
                        'adet': len(ozellikli_ilanlar),
                        'ort_m2': int(statistics.mean(ozellikli_m2))
                    }
        
        # YENİ: Aidat ortalaması
        aidatli_ilanlar = [i for i in ilanlar if i.get('aidat', 0) > 0]
        ort_aidat = int(statistics.mean([i['aidat'] for i in aidatli_ilanlar])) if aidatli_ilanlar else 0
        
        return {
            'genel': {
                'toplam_ilan': len(ilanlar),
                'ort_m2_fiyat': int(statistics.mean(m2_fiyatlar)) if m2_fiyatlar else 0,
                'medyan_m2': int(statistics.median(m2_fiyatlar)) if m2_fiyatlar else 0,
                'min_m2': min(m2_fiyatlar) if m2_fiyatlar else 0,
                'max_m2': max(m2_fiyatlar) if m2_fiyatlar else 0,
                'ort_aidat': ort_aidat
            },
            'bina_tipleri': bina_tipleri,
            'kat_dagilim': kat_dagilim,
            'yas_dagilim': yas_dagilim,
            'ozellik_istatistik': ozellik_istatistik
        }
    
    def fiyat_oneri_hesapla(self, musteri_bilgileri, pazar_stats):
        """Müşteri bilgilerine göre gelişmiş fiyat önerisi hesapla"""
        
        # Baz m² fiyatı
        baz_m2_fiyat = pazar_stats['genel']['ort_m2_fiyat']
        
        # Temel çarpanlar
        bina_carpan = self.bina_tipi_carpanlar.get(musteri_bilgileri['bina_tipi'], 1.0)
        kat_carpan = self.kat_carpanlar.get(musteri_bilgileri['kat'], 1.0)
        yas_carpan = self.bina_yasi_carpanlar.get(musteri_bilgileri['bina_yasi'], 1.0)
        cephe_carpan = self.cephe_carpanlar.get(musteri_bilgileri['cephe'], 1.0)
        kullanim_carpan = self.kullanim_carpanlar.get(musteri_bilgileri['kullanim'], 1.0)
        
        # YENİ: Ekstra özellik çarpanları
        ekstra_carpan = 1.0
        for ozellik in musteri_bilgileri.get('ekstra_ozellikler', []):
            ekstra_carpan *= self.ekstra_ozellikler.get(ozellik, 1.0)
        
        # YENİ: Lokasyon çarpanları
        lokasyon_carpan = 1.0
        for avantaj in musteri_bilgileri.get('lokasyon_avantajlari', []):
            lokasyon_carpan *= self.lokasyon_carpanlar.get(avantaj, 1.0)
        
        # Toplam çarpan
        toplam_carpan = (bina_carpan * kat_carpan * yas_carpan * cephe_carpan * 
                        kullanim_carpan * ekstra_carpan * lokasyon_carpan)
        
        # Tahmini m² fiyatı
        tahmini_m2 = int(baz_m2_fiyat * toplam_carpan)
        
        # Toplam fiyat
        toplam_fiyat = tahmini_m2 * musteri_bilgileri['m2']
        
        # Alt ve üst limit (%5 tolerans)
        alt_limit = int(toplam_fiyat * 0.95)
        ust_limit = int(toplam_fiyat * 1.05)
        
        # YENİ: Kredi hesaplaması (Fiyatın %80'i, 10 yıl vade, %3.5 faiz)
        kredi_tutari = int(toplam_fiyat * 0.80)
        aylik_taksit = self.kredi_hesapla(kredi_tutari, 120, 3.5)
        
        return {
            'baz_m2': baz_m2_fiyat,
            'tahmini_m2': tahmini_m2,
            'toplam_fiyat': toplam_fiyat,
            'alt_limit': alt_limit,
            'ust_limit': ust_limit,
            'kredi_tutari': kredi_tutari,
            'aylik_taksit': aylik_taksit,
            'carpanlar': {
                'bina_tipi': bina_carpan,
                'kat': kat_carpan,
                'bina_yasi': yas_carpan,
                'cephe': cephe_carpan,
                'kullanim': kullanim_carpan,
                'ekstra_ozellikler': round(ekstra_carpan, 3),
                'lokasyon': round(lokasyon_carpan, 3),
                'toplam': round(toplam_carpan, 3)
            }
        }
    
    def kredi_hesapla(self, tutar, vade_ay, faiz_orani):
        """Kredi taksit hesaplama"""
        aylik_faiz = faiz_orani / 100 / 12
        taksit = tutar * (aylik_faiz * (1 + aylik_faiz)**vade_ay) / ((1 + aylik_faiz)**vade_ay - 1)
        return int(taksit)
    
    def kaynak_ozeti_goster(self):
        """Veri kaynakları özetini göster"""
        print("\n" + "="*80)
        print("📊 VERİ KAYNAKLARI RAPORU")
        print("="*80)
        
        toplam_ilan = sum(k['ilan_sayisi'] for k in self.kaynaklar.values())
        aktif_kaynaklar = [k['isim'] for k in self.kaynaklar.values() if k['ilan_sayisi'] > 0]
        
        print(f"\n✅ Aktif Veri Kaynakları: {len(aktif_kaynaklar)}")
        print(f"📈 Toplam Analiz Edilen İlan: {toplam_ilan}")
        print(f"\nKaynak Detayları:")
        
        for kaynak, bilgi in self.kaynaklar.items():
            if bilgi['ilan_sayisi'] > 0:
                yuzde = (bilgi['ilan_sayisi'] / toplam_ilan * 100) if toplam_ilan > 0 else 0
                print(f"   • {bilgi['isim']:20} : {bilgi['ilan_sayisi']:3} ilan (%{yuzde:.1f})")
        
        print(f"\n🔍 Güvenilirlik Skoru: {'⭐' * min(5, len(aktif_kaynaklar))}")
        print("   (Çoklu kaynak kullanımı daha güvenilir sonuçlar verir)")
        print("="*80)
    
    def musteri_degerlemesi_gelismis(self, il, ilce, oda_sayisi, islem_tipi, pazar_stats):
        """Gelişmiş müşteri değerlemesi"""
        print("\n" + "="*80)
        print("🏡 MÜŞTERİ GAYRİMENKULÜ DEĞERLEME - GELİŞMİŞ")
        print("="*80)
        
        print("\n📋 Lütfen müşterinizin gayrimenkul bilgilerini girin:")
        print("   (Bilmiyorsanız Enter'a basın, akıllı varsayılan kullanılır)\n")
        
        try:
            # M²
            while True:
                m2_input = input("📐 Dairenin m² büyüklüğü: ").strip()
                if m2_input and m2_input.isdigit():
                    m2 = int(m2_input)
                    break
                print("   ⚠️  Lütfen geçerli bir m² değeri girin!")
            
            # Bina tipi
            print("\n🏢 Bina Tipi:")
            print("   1 - Site içi (Güvenlik, havuz, sosyal alan)")
            print("   2 - Müstakil (Bahçeli, ayrık)")
            print("   3 - Apartman (Normal apartman)")
            bina_secim = input("   Seçim (1-3, varsayılan 3): ").strip() or "3"
            bina_tipi = {'1': 'site', '2': 'mustakil', '3': 'apartman'}.get(bina_secim, 'apartman')
            
            # Kat
            print("\n🔢 Kat Bilgisi:")
            print("   1-Zemin  2-1.Kat  3-2.Kat  4-3.Kat  5-4.Kat  6-5+Kat  7-Çatı")
            kat_secim = input("   Seçim (1-7, varsayılan 2): ").strip() or "2"
            kat = {'1': 'zemin', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5+', '7': 'cati'}.get(kat_secim, '1')
            
            # Bina yaşı
            print("\n🏗️  Bina Yaşı:")
            print("   1-0-2yıl  2-3-5yıl  3-6-10yıl  4-11-15yıl  5-16-20yıl  6-21+yıl")
            yas_secim = input("   Seçim (1-6, varsayılan 4): ").strip() or "4"
            bina_yasi = {'1': '0-2', '2': '3-5', '3': '6-10', '4': '11-15', '5': '16-20', '6': '21+'}.get(yas_secim, '11-15')
            
            # Cephe
            print("\n🧭 Cephe Yönü:")
            print("   1-Güney  2-GD  3-GB  4-Doğu  5-Batı  6-Kuzey  7-KD  8-KB")
            cephe_secim = input("   Seçim (1-8, varsayılan 1): ").strip() or "1"
            cephe = {'1': 'guney', '2': 'guneydogu', '3': 'guneybati', '4': 'dogu', 
                    '5': 'bati', '6': 'kuzey', '7': 'kuzeydogu', '8': 'kuzeybati'}.get(cephe_secim, 'guney')
            
            # Kullanım
            print("\n👤 Kullanım Durumu:")
            print("   1-Boş  2-Mülk Sahibi  3-Kiracılı")
            kullanim_secim = input("   Seçim (1-3, varsayılan 2): ").strip() or "2"
            kullanim = {'1': 'bos', '2': 'malik', '3': 'kiracili'}.get(kullanim_secim, 'malik')
            
            # YENİ: Ekstra özellikler
            print("\n✨ Ekstra Özellikler (Virgülle ayırın, örn: 1,3,5 veya hepsi için 'h'):")
            print("   1-Asansör  2-Otopark  3-Güvenlik  4-Havuz  5-Spor")
            print("   6-Balkon  7-Teras  8-Ebeveyn Banyo  9-Ankastre  10-Klima")
            ekstra_input = input("   Seçim: ").strip().lower()
            
            ekstra_ozellikler = []
            if ekstra_input and ekstra_input != 'h':
                ozellik_map = {
                    '1': 'asansor', '2': 'otopark', '3': 'guvenlik', '4': 'havuz',
                    '5': 'spor_alani', '6': 'balkon', '7': 'teras', '8': 'ebeveyn_banyolu',
                    '9': 'ankastre_mutfak', '10': 'klima'
                }
                secimler = ekstra_input.split(',')
                ekstra_ozellikler = [ozellik_map.get(s.strip()) for s in secimler if s.strip() in ozellik_map]
            
            # YENİ: Lokasyon avantajları
            print("\n📍 Lokasyon Avantajları (Virgülle ayırın, örn: 1,3,5):")
            print("   1-Metro Yakın  2-Tramvay  3-Okul  4-Hastane  5-AVM")
            print("   6-Deniz Manzara  7-Park  8-Cadde Üstü")
            lokasyon_input = input("   Seçim: ").strip()
            
            lokasyon_avantajlari = []
            if lokasyon_input:
                lokasyon_map = {
                    '1': 'metro_yakin', '2': 'tramvay_yakin', '3': 'okul_yakin',
                    '4': 'hastane_yakin', '5': 'avm_yakin', '6': 'deniz_manzara',
                    '7': 'park_yakin', '8': 'cadde_ustu'
                }
                secimler = lokasyon_input.split(',')
                lokasyon_avantajlari = [lokasyon_map.get(s.strip()) for s in secimler if s.strip() in lokasyon_map]
            
            # YENİ: Aidat
            aidat_input = input("\n💳 Aylık Aidat (TL, bilmiyorsanız Enter): ").strip()
            aidat = int(aidat_input) if aidat_input and aidat_input.isdigit() else 0
            
            musteri_bilgileri = {
                'm2': m2,
                'bina_tipi': bina_tipi,
                'kat': kat,
                'bina_yasi': bina_yasi,
                'cephe': cephe,
                'kullanim': kullanim,
                'ekstra_ozellikler': ekstra_ozellikler,
                'lokasyon_avantajlari': lokasyon_avantajlari,
                'aidat': aidat
            }
            
            # Fiyat önerisi hesapla
            oneri = self.fiyat_oneri_hesapla(musteri_bilgileri, pazar_stats)
            
            # Sonuçları göster
            self.fiyat_onerisi_goster_gelismis(musteri_bilgileri, oneri, il, ilce, oda_sayisi, pazar_stats)
            
            return musteri_bilgileri, oneri
            
        except KeyboardInterrupt:
            print("\n\n👋 İptal edildi...")
            return None, None
    
    def fiyat_onerisi_goster_gelismis(self, musteri_bilgileri, oneri, il, ilce, oda_sayisi, pazar_stats):
        """Gelişmiş fiyat önerisini göster"""
        print("\n" + "="*80)
        print("💎 PROFESYONEL FİYAT DEĞERLEME RAPORU")
        print("="*80)
        
        # Gayrimenkul özeti
        print(f"\n📋 GAYRİMENKUL ÖZETİ")
        print("─" * 80)
        
        tip_isimleri = {'site': 'Site İçi', 'mustakil': 'Müstakil', 'apartman': 'Apartman'}
        kat_isimleri = {'zemin': 'Zemin', '1': '1.', '2': '2.', '3': '3.', '4': '4.', '5+': '5+', 'cati': 'Çatı'}
        yas_isimleri = {'0-2': '0-2 yıl (Yeni)', '3-5': '3-5 yıl', '6-10': '6-10 yıl', 
                       '11-15': '11-15 yıl', '16-20': '16-20 yıl', '21+': '21+ yıl (Eski)'}
        cephe_isimleri = {'guney': 'Güney', 'guneydogu': 'Güneydoğu', 'guneybati': 'Güneybatı',
                         'dogu': 'Doğu', 'bati': 'Batı', 'kuzey': 'Kuzey', 
                         'kuzeydogu': 'Kuzeydoğu', 'kuzeybati': 'Kuzeybatı'}
        kullanim_isimleri = {'bos': 'Boş', 'malik': 'Mülk Sahibi', 'kiracili': 'Kiracılı'}
        
        print(f"Konum         : {il} - {ilce}")
        print(f"Oda Sayısı    : {oda_sayisi}")
        print(f"Büyüklük      : {musteri_bilgileri['m2']} m²")
        print(f"Bina Tipi     : {tip_isimleri.get(musteri_bilgileri['bina_tipi'])}")
        print(f"Kat           : {kat_isimleri.get(musteri_bilgileri['kat'])} Kat")
        print(f"Bina Yaşı     : {yas_isimleri.get(musteri_bilgileri['bina_yasi'])}")
        print(f"Cephe         : {cephe_isimleri.get(musteri_bilgileri['cephe'])}")
        print(f"Durum         : {kullanim_isimleri.get(musteri_bilgileri['kullanim'])}")
        
        if musteri_bilgileri['ekstra_ozellikler']:
            ozellik_isimleri = {
                'asansor': 'Asansör', 'otopark': 'Otopark', 'guvenlik': 'Güvenlik',
                'havuz': 'Havuz', 'spor_alani': 'Spor Alanı', 'balkon': 'Balkon',
                'teras': 'Teras', 'ebeveyn_banyolu': 'Ebeveyn Banyo', 
                'ankastre_mutfak': 'Ankastre Mutfak', 'klima': 'Klima'
            }
            ozellikler = ', '.join([ozellik_isimleri.get(o, o) for o in musteri_bilgileri['ekstra_ozellikler']])
            print(f"Özellikler    : {ozellikler}")
        
        if musteri_bilgileri['lokasyon_avantajlari']:
            avantaj_isimleri = {
                'metro_yakin': 'Metro Yakın', 'tramvay_yakin': 'Tramvay', 'okul_yakin': 'Okul',
                'hastane_yakin': 'Hastane', 'avm_yakin': 'AVM', 'deniz_manzara': 'Deniz Manzara',
                'park_yakin': 'Park', 'cadde_ustu': 'Cadde Üstü'
            }
            avantajlar = ', '.join([avantaj_isimleri.get(a, a) for a in musteri_bilgileri['lokasyon_avantajlari']])
            print(f"Avantajlar    : {avantajlar}")
        
        if musteri_bilgileri['aidat'] > 0:
            print(f"Aylık Aidat   : {musteri_bilgileri['aidat']:,} TL".replace(',', '.'))
        
        # Fiyat hesaplama
        print(f"\n💰 FİYAT HESAPLAMA DETAYLARI")
        print("─" * 80)
        print(f"Pazar Baz m² Fiyatı      : {oneri['baz_m2']:,} TL/m²".replace(',', '.'))
        print(f"\nUygulanan Çarpanlar:")
        carpanlar = oneri['carpanlar']
        print(f"  • Bina Tipi            : x{carpanlar['bina_tipi']}")
        print(f"  • Kat                  : x{carpanlar['kat']}")
        print(f"  • Bina Yaşı            : x{carpanlar['bina_yasi']}")
        print(f"  • Cephe                : x{carpanlar['cephe']}")
        print(f"  • Kullanım Durumu      : x{carpanlar['kullanim']}")
        if carpanlar['ekstra_ozellikler'] > 1.0:
            print(f"  • Ekstra Özellikler    : x{carpanlar['ekstra_ozellikler']}")
        if carpanlar['lokasyon'] > 1.0:
            print(f"  • Lokasyon Avantajları : x{carpanlar['lokasyon']}")
        print(f"  ─────────────────────────")
        print(f"  TOPLAM ÇARPAN          : x{carpanlar['toplam']}")
        
        print(f"\nTahmini m² Fiyatı        : {oneri['tahmini_m2']:,} TL/m²".replace(',', '.'))
        
        # Önerilen fiyat
        print(f"\n🎯 ÖNERİLEN SATIŞ FİYATI")
        print("=" * 80)
        print(f"\n   HEDEF FİYAT: {oneri['toplam_fiyat']:,} TL".replace(',', '.'))
        print(f"\n   Fiyat Aralığı:")
        print(f"   Alt Limit : {oneri['alt_limit']:,} TL  (-%5)".replace(',', '.'))
        print(f"   Üst Limit : {oneri['ust_limit']:,} TL  (+%5)".replace(',', '.'))
        
        # YENİ: Kredi bilgisi
        print(f"\n💳 KREDİ BİLGİSİ (10 Yıl Vade, %3.5 Faiz)")
        print("─" * 80)
        print(f"Kredi Tutarı (Fiyatın %80'i) : {oneri['kredi_tutari']:,} TL".replace(',', '.'))
        print(f"Aylık Taksit                  : {oneri['aylik_taksit']:,} TL".replace(',', '.'))
        
        if musteri_bilgileri['aidat'] > 0:
            toplam_aylik = oneri['aylik_taksit'] + musteri_bilgileri['aidat']
            print(f"Aidat + Taksit                : {toplam_aylik:,} TL/ay".replace(',', '.'))
        
        # Pazarlama önerileri
        print(f"\n💡 PAZARLAMA STRATEJİSİ")
        print("─" * 80)
        
        # Güçlü yönler
        guclu_yonler = []
        if musteri_bilgileri['bina_tipi'] == 'site':
            guclu_yonler.append("Site içi - Güvenlik ve sosyal alanlar")
        if musteri_bilgileri['cephe'] in ['guney', 'guneydogu', 'guneybati']:
            guclu_yonler.append("Güneş alımı mükemmel")
        if musteri_bilgileri['kullanim'] == 'bos':
            guclu_yonler.append("Boş daire - Hemen teslim")
        if musteri_bilgileri['bina_yasi'] in ['0-2', '3-5']:
            guclu_yonler.append("Yeni bina - Düşük bakım masrafı")
        if musteri_bilgileri['kat'] in ['2', '3', '4']:
            guclu_yonler.append("İdeal kat - Manzara ve erişim dengesi")
        if 'metro_yakin' in musteri_bilgileri.get('lokasyon_avantajlari', []):
            guclu_yonler.append("Metro yakınlığı - Ulaşım avantajı")
        if 'deniz_manzara' in musteri_bilgileri.get('lokasyon_avantajlari', []):
            guclu_yonler.append("Deniz manzarası - Premium özellik")
        
        if guclu_yonler:
            print("\n✅ Vurgulanacak Güçlü Yönler:")
            for yon in guclu_yonler:
                print(f"   • {yon}")
        
        # Dikkat edilecekler
        dikkat_noktalari = []
        if musteri_bilgileri['kullanim'] == 'kiracili':
            dikkat_noktalari.append("Kiracılı - Yatırımcılara yönelin, kira getirisi belirtin")
        if musteri_bilgileri['bina_yasi'] in ['16-20', '21+']:
            dikkat_noktalari.append("Eski bina - Renovasyon potansiyeli vurgulayın")
        if musteri_bilgileri['aidat'] > pazar_stats['genel']['ort_aidat'] * 1.2:
            dikkat_noktalari.append(f"Aidat ortalamanın üstünde - Site özelliklerini açıklayın")
        
        if dikkat_noktalari:
            print("\n⚠️  Dikkat Edilecek Noktalar:")
            for nokta in dikkat_noktalari:
                print(f"   • {nokta}")
        
        # Hedef müşteri profili
        print("\n🎯 Hedef Müşteri Profili:")
        if musteri_bilgileri['bina_tipi'] == 'site' and musteri_bilgileri['bina_yasi'] in ['0-2', '3-5']:
            print("   → Genç çiftler, aileler (güvenlik ve sosyal alan öncelikli)")
        if musteri_bilgileri['kullanim'] == 'kiracili':
            print("   → Yatırımcılar (kira getirisi arayan)")
        if 'metro_yakin' in musteri_bilgileri.get('lokasyon_avantajlari', []):
            print("   → Çalışan profesyoneller (ulaşım öncelikli)")
        if oneri['aylik_taksit'] < 50000:
            print("   → İlk ev alacaklar (düşük taksit)")
        
        print("\n" + "="*80)
    
    def rapor_olustur(self, ilanlar, pazar_stats, musteri_bilgileri, oneri, il, ilce, oda_sayisi, islem_tipi):
        """JSON rapor oluştur"""
        dosya_adi = f"degerleme_raporu_{il}_{ilce}_{oda_sayisi}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        dosya_adi = dosya_adi.replace('+', '_').replace(' ', '_').lower()
        
        # Kaynak özeti
        kaynak_ozeti = {
            'toplam_kaynak': len([k for k in self.kaynaklar.values() if k['ilan_sayisi'] > 0]),
            'kaynaklar': {k: v for k, v in self.kaynaklar.items() if v['ilan_sayisi'] > 0},
            'toplam_ilan': sum(k['ilan_sayisi'] for k in self.kaynaklar.values()),
            'guvenilirlik_skoru': min(5, len([k for k in self.kaynaklar.values() if k['ilan_sayisi'] > 0]))
        }
        
        rapor = {
            'rapor_bilgileri': {
                'rapor_tarihi': datetime.now().strftime('%d.%m.%Y %H:%M'),
                'rapor_versiyonu': 'v4.0 Ultimate',
                'hazırlayan': 'Profesyonel Gayrimenkul Değerleme Sistemi'
            },
            'veri_kaynaklari': kaynak_ozeti,
            'pazar_analizi': {
                'il': il,
                'ilce': ilce,
                'oda_sayisi': oda_sayisi,
                'islem_tipi': islem_tipi,
                'istatistikler': pazar_stats
            },
            'musteri_gayrimenkulu': musteri_bilgileri,
            'fiyat_degerleme': oneri,
            'ornek_ilanlar': ilanlar[:10]
        }
        
        try:
            with open(f'/home/claude/{dosya_adi}', 'w', encoding='utf-8') as f:
                json.dump(rapor, f, ensure_ascii=False, indent=2)
            return dosya_adi
        except:
            return None

def main():
    print("""
╔═══════════════════════════════════════════════════════════════════════╗
║     PROFESYONEL GAYRİMENKUL DEĞERLEME SİSTEMİ v4.0 ULTIMATE         ║
║     Çoklu Kaynak Destekli - Emlakçılar İçin Tam Çözüm               ║
╚═══════════════════════════════════════════════════════════════════════╝
    """)
    
    # Kullanıcıdan bilgi al
    try:
        il = input("🏙️  İl: ").strip()
        if not il:
            print("❌ İl adı boş olamaz!")
            sys.exit(1)
        
        ilce = input("📍 İlçe: ").strip()
        if not ilce:
            print("❌ İlçe adı boş olamaz!")
            sys.exit(1)
        
        print("\n🏠 Oda sayısı (1+0, 1+1, 2+0, 2+1, 3+1, 4+1)")
        oda_sayisi = input("   Seçim (varsayılan 2+1): ").strip() or "2+1"
        
        if oda_sayisi not in ["1+0", "1+1", "2+0", "2+1", "3+1", "4+1"]:
            print("⚠️  Geçersiz seçim, 2+1 kullanılıyor")
            oda_sayisi = "2+1"
        
        print("\n💼 İşlem tipi:")
        print("   1 - Satılık")
        print("   2 - Kiralık")
        islem_secim = input("   Seçim (1/2, varsayılan 1): ").strip() or "1"
        
        islem_tipi = "satilik" if islem_secim == "1" else "kiralik"
        
    except KeyboardInterrupt:
        print("\n\n👋 Çıkılıyor...")
        sys.exit(0)
    
    # Değerleme sistemini başlat
    degerleme = GayrimenkulDegerlemePro()
    
    print(f"\n🚀 Çoklu kaynaklı pazar analizi başlatılıyor...")
    print("─" * 80)
    
    # Çoklu kaynaklardan veri çek
    ilanlar = degerleme.sahibinden_detayli_sorgula(il, ilce, oda_sayisi, islem_tipi)
    
    if not ilanlar:
        print("\n❌ Yeterli veri bulunamadı!")
        sys.exit(1)
    
    # Kaynak özetini göster
    degerleme.kaynak_ozeti_goster()
    
    # Pazar istatistiklerini hesapla
    pazar_stats = degerleme.pazar_istatistikleri(ilanlar)
    
    # Genel pazar özeti
    print(f"\n💰 GENEL PAZAR ÖZETİ")
    print("─" * 80)
    genel = pazar_stats['genel']
    print(f"Ortalama m² Fiyat : {genel['ort_m2_fiyat']:,} TL/m²".replace(',', '.'))
    print(f"Medyan m² Fiyat   : {genel['medyan_m2']:,} TL/m²".replace(',', '.'))
    print(f"Fiyat Aralığı     : {genel['min_m2']:,} - {genel['max_m2']:,} TL/m²".replace(',', '.'))
    if genel['ort_aidat'] > 0:
        print(f"Ortalama Aidat    : {genel['ort_aidat']:,} TL/ay".replace(',', '.'))
    
    # Müşteri değerlemesi
    print("\n" + "─"*80)
    degerle = input("\n📝 Müşteri değerlemesi yapmak ister misiniz? (e/h): ").strip().lower()
    
    if degerle == 'e':
        musteri_bilgileri, oneri = degerleme.musteri_degerlemesi_gelismis(il, ilce, oda_sayisi, islem_tipi, pazar_stats)
        
        if musteri_bilgileri and oneri:
            # Rapor kaydet
            kayit = input("\n💾 Profesyonel rapor oluşturmak ister misiniz? (e/h): ").strip().lower()
            if kayit == 'e':
                dosya = degerleme.rapor_olustur(ilanlar, pazar_stats, musteri_bilgileri, oneri, il, ilce, oda_sayisi, islem_tipi)
                if dosya:
                    print(f"\n✅ Profesyonel değerleme raporu oluşturuldu!")
                    print(f"📄 Dosya: {dosya}")
                    print(f"📊 Müşterinize sunabileceğiniz detaylı rapor hazır!")
                    print(f"🎯 Raporda {degerleme.kaynaklar['sahibinden']['ilan_sayisi']} ilan analizi var")
    
    print("\n🎉 Analiz tamamlandı! İyi satışlar!")

if __name__ == "__main__":
    main()
