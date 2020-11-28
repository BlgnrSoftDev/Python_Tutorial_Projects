# Örnek 5: Girilen Vize ve Final Notu Ortalaması Hesaplayan Python Örneği
vize = input("Vize notunu giriniz :")
final = input("Final notunu giriniz : ")
ortalama = int(vize) * 0.3 + int(final) * 0.7
if ortalama >= 50:
    print("Tebrikler dersten geçtiniz notunuz:",ortalama)
else:
    print("Maalesef, dersten kaldınız notunuz:",ortalama)