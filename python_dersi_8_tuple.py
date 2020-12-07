
liste = [1,2,3]

tuple = (1,2,3) # ikisi birbirine benziyor ama küçük farklılıklar var...

print(type(liste))
print(type(tuple))

print(len(tuple))
print(len(liste))

tuple = ("ali","ayşe","hakan","ayşe")
liste = ["ali","ayşe"] # aynı şekilde böyle atamalar yapabiliyoruz..

print(liste)
print(tuple)

liste[0] = "ahmet"
#tuple[0] = "mehmet"   tuple ile liste neredeyse tamamen  aynı amaçlar için kullanılıyor ama bu şekilde indexe atama yapılamıyor..


print(tuple.count("ayşe"))  # bu şekilde ayşe nin kaç defa geçtiğini bulabiliyoruz...
print(tuple.index("ayşe"))  # bununla index numarasını bulabiliriz ....... ama sadece ilk geçtiği yeri döndürür..

tuple2 = (1,2,3) + tuple # bu şekilde iki tuple nesnesini birleştirebiliyoruz...
print(tuple2)



