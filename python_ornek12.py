#armstrong sayısı mı değil mi hesaplama...
bilesenler = []
bilesensayisi = 0
sonuc = 0
orjinalsayi = int(input("Lütfen sayiyi giriniz: "))
sayi = orjinalsayi
while(sayi != 0):
    bilesenler.append(sayi % 10)
    sayi = sayi // 10
    bilesensayisi += 1
for x in range(0,bilesensayisi):
    sonuc = sonuc + bilesenler[x]**3
if sonuc == orjinalsayi:
    print(orjinalsayi," ---> girilen sayi armstrong sayidir..")
else:
    print(orjinalsayi," ---> girilen sayi armstrong sayi değildir..")
    
print(bilesenler)