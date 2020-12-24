def not_hesapla(vize1,proje1,proje2,final):
    sonuc = vize1 * 0.30 + proje1 * 0.05 + proje2 * 0.05 + final * 0.60
    return sonuc



a =int(input("vize notunu giriniz : "))
b =int(input("1. proje notunu giriniz : "))
c =int(input("2. proje notunu giriniz : "))
d =int(input("final notunu giriniz : "))

print("Ağırlıklı ortalamanız =  "not_hesapla(a,b,c,d))