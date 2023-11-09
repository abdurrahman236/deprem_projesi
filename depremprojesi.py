import requests

# PROJE HAKKKINDA : 
# SON ZAMANLARDA OLAN DEPREMLER İLE İLGİLİ BAZI BİLGİLERİ VEREN BİR PROJE

class Deprem:
    def __init__(self) -> None:
        self.api_url = "http://hasanadiguzel.com.tr/api/sondepremler"
        self.index = int(input("sondan kaçıncı deprem bilgisini ogrenmek istiyorsunuz(son bilgi icin 0 a basınız): "))
        
        
    def deprem_tarihi(self):
        response = requests.get(self.api_url)
        tarihler = response.json()['data']
        tarihler_ = []
        for tarih in tarihler:
            tarihler_.append(tarih['tarih'])
        print(tarihler_[self.index])
    
    def deprem_saati(self):
        response = requests.get(self.api_url)
        saatler =  response.json()['data']
        saatler_ = []
        for saat in saatler:
            saatler_.append(saat['saat'])
        print(saatler_[self.index])
    
    def deprem_derinligi(self):
        response = requests.get(self.api_url)
        derinlikler = response.json()['data']
        derinlikler_ = []
        for derinlik in derinlikler:
            derinlikler_.append(derinlik['derinlik_km'])
        print(derinlikler_[self.index])
    
    def deprem_yeri(self):
        response = requests.get(self.api_url)
        yerler = response.json()['data']
        yerler_ = []
        for yer in yerler:
            yerler_.append(yer['yer'])
        print(yerler_[self.index])
    
    def tarihteki_deprem_sayisi(self,tarih):
        response = requests.get(self.api_url)
        depremler = response.json()['data']
        depremler_ = []
        for deprem in depremler:
            depremler_.append(deprem['tarih'])
        print(depremler_.count(tarih))
    
    def deprem_buyuklugu(self):
        response = requests.get(self.api_url)
        buyuklukler = response.json()['data']
        buyuklukler_ = []
        for buyukluk in buyuklukler:
            buyuklukler_.append(buyukluk['ml'])
        print(buyuklukler_[self.index])
            
deprem = Deprem()

while True:
    secim = input("1-son deprem tarihi\n2-son deprem saati\n3-son depremin derinliği\n4-son depremin oldugu yer\n5-hangi tarihteki toplam deprem sayısını ogrenmek istiyorsunuz\n6-depremin büyüklüğü\n7-exit\nSeciminiz: ")
    
    if secim == '7':
        break
    elif secim == '1':
        deprem.deprem_tarihi()
    elif secim == '2':
        deprem.deprem_saati()
    elif secim == '3':
        deprem.deprem_derinligi()
    elif secim == '4':
        deprem.deprem_yeri()
    elif secim == '5':
        tarih = input("Hangi tarihteki deprem sayısını öğrenmek istiyorsunuz:(yıl/ay/gün şeklinde yazınız.) ")
        deprem.tarihteki_deprem_sayisi(tarih=tarih)
    elif secim == '6':
        deprem.deprem_buyuklugu()
    else:
        print("Yanlış seçim lütfen 1 ile 7 arasında bir sayı seçiniz.")
        
