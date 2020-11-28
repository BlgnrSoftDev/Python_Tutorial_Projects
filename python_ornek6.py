# Örnek 12: 1-100 Arası Sayıları Ekranda Listeleyen Python Örneği.
kontrol = 0
for x in range (1,1000,1):
    for y in range (2,x+1,1):
        if x % y == 0:
            kontrol = 1
            break
    if kontrol == 1 and x == y:
        print("{},".format(x))
        