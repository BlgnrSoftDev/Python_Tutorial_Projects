fruits = {"banana","apple","watermelon"} #sets ler de liste gibibir. tuple da olduğu gibi küçük farklılıklar vardır.

#print(fruits[0]) indekslenemez !!....
# sıralayamayız......

fruits.add('cherry') # böyle ekleyebiliriz...
print(fruits)

fruits.update(['salatalık','zeytin']) # update metodu ile yeni bir listeyi ekleyebiliriz...
print(fruits)

fruits.update(['salatalık','zeytin','apple']) # eğer önceden var olan elemanı tekrar eklersek, iki tane yazmaz sadece tek bir tanesini yazar...
print(fruits)

mylist = [1,2,3,4]
print(mylist)
print(set(mylist)) # bu şekilde artık set formatında yazdırırız..

fruits.remove("cherry") #içinden eleman kaldırmak için kullanırız..
fruits.discard("apple") # ikisi de kullanılabilir ...
print(fruits)

fruits.clear() # tüm elemanlar silinir...
print(fruits)

