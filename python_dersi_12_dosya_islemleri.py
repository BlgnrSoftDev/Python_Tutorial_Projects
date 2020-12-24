dosya = open("dosyaoku.txt",mode = "a" ,encoding="utf-8")
# print(dosya.read()) --> dosya içindeki tüm yazıları okur
# print(dosya.readline()) --> dosya içinde tek bir satırı okur
dosya.write("\ngüzel bir eğitimdi.") # --> dosya içine bir şey yazmak için kullanılır.
dosya.close() # ---> dosya ile işimiz bitince kapatıyoruz.

dosya2 = open("dosyaoku.txt",encoding="utf-8")
print(dosya2.read())
dosya2.close()