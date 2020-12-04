import sys

hak = 3

print("Hosgeldiniz......")
for x in range (1,100):
    user = input("Kullanıcı adını giriniz: ")
    password = input("parolayı giriniz: ")

    if user == "admin" and password == '12345' :
        print("Hosgeldiniz " + user)
        answer = input("eğer güncel borcunuzu öğrenmek istiyorsanız '1' yazınız: ")
        if answer == '1':
            print("Toplam borcunuz : ",1000," tl dir....")
            sys.exit()
    else :
        hak-=1
        if hak == 0:
            print("Hesabın bloklandı...")
            sys.exit()
        
        print("kullanıcı adı veya parola hatalı!!! , kalan deneme = ",hak)
    
       