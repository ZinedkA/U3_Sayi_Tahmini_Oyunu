import time
import os
from random import randint
rand = randint(1, 99)
sayac = 0

def ekran_temizleme():
    os.system('cls')

def oyunu_resetle():
    global rand, sayac
    rand = randint(1, 99)
    sayac = 0

while True:
    sayac += 1
    sayi = int(input("1-99 arasında bir sayı (0 çıkış, 100 reset):"))
    if(sayi == 0):
        print("Oyun Kapatılıyor")
        print("Rastele seçilen sayı {0}!".format(rand))
        time.sleep(3)
        break

    elif sayi == 100:
        oyunu_resetle()
        ekran_temizleme()
        print("Yeni sayı seçildi. Oyun Restlendi.")
        continue    

    elif sayi < rand // 4:
        ekran_temizleme()
        print(format(sayi))
        print("Sayısından Çok Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi < rand // 2:
        ekran_temizleme()
        print(format(sayi))
        print("Sayısından Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi < rand:
        ekran_temizleme()
        print(format(sayi))
        print("Sayısından Yüksek Bir Sayı Girin.")
        continue
#---------------------------------------------------------------------------------    
    elif sayi // 4 > rand:
        ekran_temizleme()
        print(format(sayi))
        print("Sayısından Çok Daha Düşük Bir Sayı Girin.")
        continue
    elif sayi // 2 > rand:
        ekran_temizleme()
        print(format(sayi))
        print("Sayısından Daha Düşük Bir Sayı Girin.")
        continue
    elif sayi > rand:
        ekran_temizleme()
        print(format(sayi))
        print("Sayısından Düşük Bir Sayı Girin.")
        continue
#---------------------------------------------------------------------------------    
    else:
        print("  ")
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
        time.sleep(5)
        oyunu_resetle()
        ekran_temizleme()

    