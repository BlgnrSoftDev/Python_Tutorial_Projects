a = int(input("Lutfen bir sayi girin :"))
b = int(input("Lutfen ikinci değeri giriniz :"))
print("Sayilarin toplamı:",a+b)


print("Oyuncu kaydetme programına hoşgeldiniz")
adı = input("Oyuncu adını giriniz:")
soyadı = input("Oyuncunun soyadını giriniz:")
yaş = input("Oyuncunun yaşını giriniz:")
takım = input("Oyuncun takımını giriniz:")

bilgiler = [adı,soyadı,yaş,takım]
print("Oyuncun adı:",adı,"Oyuncunun soyadı:",soyadı,"Oyuncunun yaşı:",yaş,"Oyuncunun takımı:",takım)
print("Oyuncun Adı:{} \n Oyuncunun Soyadı:{} \n Oyuncunun Yaşı:{} \n Oyuncunun Takımı:{} \n".format(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler[3]))
print("kaydedildi ...")