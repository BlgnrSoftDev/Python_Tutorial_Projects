def ucgenmi(a,b,c):
    if(abs(a - b)< c <abs(a + b)):
        if(abs(a - c)< b < abs(a + c)):
            if(abs(b - c)< a <abs(b + c)):
                return 1
    else:
        return 0


a = int(input("a değeri : "))
b = int(input("b değeri : "))
c = int(input("c değeri : "))

if(ucgenmi(a,b,c) == 1):
    print("Üçgen oluşturur")
else:
    print("Üçgen oluşturmaz")