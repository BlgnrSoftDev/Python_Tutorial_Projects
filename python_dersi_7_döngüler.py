# 1 ile 100 arası asal sayıları yazdırma
kontrol = 0
for x in range (1,100):
    for y in range(2,x+1): # ilk değere 2 atar ve x+1'e kadar döngü devam eder..
        if x % y == 0:
            kontrol = 1
            break
    if kontrol == 1 and x == y:
        print("{},".format(x))
        
isim = "Hüseyin"
for harf in isim:
    print(harf)
    
names = ["ali", "ayşe", "aslı"]
for nam in names:
    print(nam, end=" ")

for ch in names[0]:
    print(ch, end="-")

print()

list = [(1, 2), (3, 4), (6, 7), (8, 9)]

for x, y in list:
    print(x, y)


dic = {"key1": 1, "key2": 2, "key3": 3}

for ke,va in dic.items():
    print(ke, va)