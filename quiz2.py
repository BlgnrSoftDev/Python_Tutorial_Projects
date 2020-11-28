#Python'da liste yapılarını kullanarak 5 adet il adı içeren b#ir liste oluşturunuz.

#Sonra bu illerin ilk 2 ve son 2 karakterini ekrana basacak bir döngü yazınız. Örneğin il adı "İstanbul" ise ekrana "İsul" yazacak. 5 ilin her biri için bunu yapacaktır.

#Not: Liste oluştururken il adlarını sabit girin, kullanıcıdan giriş almaya gerek yok. Cevabınızı Thonny veya herhangi bir editörde yazıp aşağıya yapıştırınız. Süreniz 15 dakikadır.

il_liste = ["Aydın","Ankara","bursa","burdur","istanbul"]
for x in range (5):
    print("{}{}".format(il_liste[x][0:2],il_liste[x][len(il_liste[x])-2:len(il_liste[x])]))
    
          