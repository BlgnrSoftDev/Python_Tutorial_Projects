print("Verilen bilgilere göre dairenin alanını ve çevresini hesaplayalım")
yarıcap = int(input("yarıcapı giriniz:"))
print("Dairenizin alanı : {} , Çevresi : {} ' dir..".format(3.14 * pow(yarıcap,2), 2 * 3.14 * yarıcap ))

''' pow() a alternatif olarak ** kullanabiliriz yani ,
pow(yarıcap,2) == yarıcap ** 2 '''