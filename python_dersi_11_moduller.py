from time import *  # bununla zaman kütüphanesinden * yani tüm elemanları ekler...
from math import *
'''
zaman1 = perf_counter() # sayacı baslatır
sleep(3)  # 3 saniye bekler....
print("adınız nedir ? ")
isim = input()
zaman2 = perf_counter() # islem bittikten sonra sayacı baslatır..
print(zaman2 - zaman1) # sayaclar arası farkı bulur yani bizim islemin gerceklesme suresini bulur.
'''

a = int(input("A kenaırnı giriniz : "))
b = int(input("B kenarını giriniz : "))
hipotenus = sqrt(pow(a,2) + pow(b,2))
print("sonuc : ",hipotenus)