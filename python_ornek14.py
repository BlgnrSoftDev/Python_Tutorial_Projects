# maraton idman yardımcısı........
def saniyeleştir(a,b,c):
    b += a * 60
    c += b * 60
    return hız(c)
def hız(d):
    sürat = float(1000 / d)
    return sürat    
def düzenlisüre(m):
    sec = m % 60
    minu = m // 60
    hour = minu // 60
    minu = minu % 60
    print(" {} saat, {} dakika, {} saniye".format(hour,minu,sec))
    
print("öncelikle 1 km'yi kaç saat,dakika,saniye ' de aldığınızı yazınız...")
saat = int(input("saat: "))
dakika = int(input("dakika: "))
saniye = int(input("saniye: "))

mesafe = int(input("kaç km koşmak istiyorsunuz ? : "))
print("----------------Sonuçlar-----------------------")
print("Ortalama hızınız :",saniyeleştir(saat,dakika,saniye)," m/s 'dir.")
print("Ayırmanız gereken süre : ")
düzenlisüre(mesafe*1000/saniyeleştir(saat,dakika,saniye))