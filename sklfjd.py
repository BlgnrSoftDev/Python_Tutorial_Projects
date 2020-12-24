def ucgenmi(a,b,c):
    kontrol = 0
    if (abs(a - b) < c < abs(a + b)):
        kontrol = 1
    if (abs(a - c) < b < abs(a + c)):
        kontrol += 1
    if (abs(b - c) < a < abs(b + c)):
        kontrol += 1
    return kontrol

a = int(input("a değeri : "))
b = int(input("b değeri : "))
c = int(input("c değeri : "))

if(kontrol == 3):
    print("ücgen olusturur")
else:
    print("olusturmaz")