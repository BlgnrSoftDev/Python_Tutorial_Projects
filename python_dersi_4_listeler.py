liste = [1,2.5,"ali",8]
print(liste)

print(liste[0]) #listelerde içindeki istediğimiz elemana ulaşmak için stringlerde ki gibi indis kullanırız..
print(liste[2])

liste[3] = "Cebrail" #listelerdeki değerleri değiştirmek için indisi yazıp atamak istedğimiz değeri yazarız.
print(liste)

liste.append("Fenerbahçe") #listeye yeni eleman eklmek için bu fonksiyonu kullanırız..
print(liste)

liste2 = [9.99,8,"Execute",]
liste = liste + liste2 # iki listeyi bu şekilde birleştirebiliriz..
print(liste)

print(liste[:3]) #sınırladığımız indisler arası bastırmak için bu şekilde yaparız.
# ---> unutmayalım ki yukarıdaki yazdığımız indis değeri 3'e kadar yazar 3'ü yazmaz..

liste[:3] = [] #bu şekilde 3. indise boşaltmış oluruz.
print(liste )


      


