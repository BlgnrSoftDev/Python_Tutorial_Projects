print("Hoşgeldiniz..")
print("Öncelikle bilgilerinizi giriniz..")
ad = input("Adınız:")
soyad = input("soyadınız:")
yaş = int(input("yaşınız:"))
bilgiler = [ad,soyad,yaş]

if yaş >= 18:
    print("Hosgeldiniz {} {} Bey, Yaşınız ({}) uygundur mekana girebilirsiniz".format(ad,soyad,yaş))
elif yaş < 18:
    print("Malesef {} {} Bey,  Yaşınız ({}) tutmamaktadır mekana giremezsiniz".format(ad,soyad,yaş))