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
    
    