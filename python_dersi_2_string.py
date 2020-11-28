x="Hüseyin" #çift tırnak içinde de kullanabiliriz..
y="Bilginer"
print('Ben ' + x + y) #tek tırnak kullanabiliriz.. slash işareti ile yorum yapabiliriz.
print("benim adım " + x + " " + y + " dir.")# değişkene atadığımız stringleri print içinde birleştirebliriz..

#print("numaram : " + 99) --> kod hata verir çünkü printf içinde string ile sayıları + ile yazamayız..
print("numaram : " + str(99)) #--> bu şekilde tür dönüşümü yaparsak sorun kalkar..

#print("18" + 66)  str türünden bir ifade ile int türünden ifadeyi toplamaya çalıştığımız için hata alırız...
print(int("18")+66) #Böylelikle str türü int'e dönüştürerek sorun kalakar
#print("18.5"+66) kesirli sayılar için int yerine başka tür kullanmalıyız..
print(float("18.5")+ 66 ) #float dönüşümü yaparsak sorun kalkar...      

print(x*3) #çarptığımız sayı kadar kendini tekrarlar...
print("Yazılım","Bilimi") # aralarında tek boşluk bırakır ve ilk değerden hemen sonra yazar..
print("Yazılım",3,3.45,"bilimi")


print(x) #string ifadeler tanımlanırken her bir karaktere indis verilir,eğer herhangi bir karaktere ulaşmak istersek indisini bastırmamız yeterlidir..
print(x[1]) # 1. indisi yani ü harfini basar..
print(x[6]) # 6. indisi yani n yi basar..
print(x[-1]) # tersten başlar ve ilk indisi basar yani n yi basar
print(x[3:5]) # 3. indisten 5. indise kadar basar..

print(len(x)) # x değişkenine atanmış olan stringin uzunluğunu basar..
print(len("ali")) # sonuç olarak 3 ü basar a,l,i

print(x[::-1]) # x karakter dizisinin tersten yazılımı..
print(x[3:5])


