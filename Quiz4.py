from math import *
x  = int(input("x koordinatını giriniz : "))
y  = int(input("y koordinatını giriniz : "))

if sqrt(pow(x,2) + pow(y,2)) > 5:
    print("çemberin dışındadır...")
elif sqrt(pow(x,2) + pow(y,2)) == 5:
    print("çemberin üstündedir....")
else:
    print("çemberin içindedir...")