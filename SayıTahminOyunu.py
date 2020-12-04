#Sayı tahmin oyunu....
import random

randlist = []
guestnum = []
tutmayansayılar = []
fail =1
print("------| Sayı Tahmin Oyununa Hoşgeldiniz  |------")
dongu = int(input(" Kaç sayı tahmin etmek istersiniz ? : "))

for i in range(0,dongu,1):
    randlist.append(random.randint(1,20))
    guestnum.append(int(input(" sayıyı giriniz: ")))
for j in range(0,dongu,1):
    if (randlist[j] != guestnum[j]):
        fail = 1
        tutmayansayılar.append(j+1)

if (fail == 1):
    print("Maaleseef ki sayılarınız tutmaıştır...")
    print("Sizin sayılarınız : ",guestnum," Random sayılar : ",randlist)
    print(tutmayansayılar," bu sıradaki sayılarınız tutmamıştır.")
    
else:
    print("Tebrikler !! Tüm Sayılar Tutmuştur...")
    print("Sizin sayılarınız : ",guestnum," Random sayılar : ",randlist)

        
        
        