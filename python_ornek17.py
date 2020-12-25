import random
randomnum = random.randint(1,100)
guess = int(input("Lutfen 1-100 arası bir tahmin giriniz : "))
deneme = 1
while (guess != randomnum):
    if guess > randomnum:
        print("Lutfen daha kücük bir deger giriniz.")
    else:
        print("lütfen daha büyük bir sayi giriniz.")
    deneme+=1
    guess = int(input("Lutfen bir tahmin daha giriniz : "))
if randomnum == guess:
    print(f'tebrikler doğru sayiyi {randomnum}, {deneme} deneme ile buldunuz ')