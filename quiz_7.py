dosya = open("once.txt",mode = "r" ,encoding="utf-8")
icerik = dosya.read()
dosya.close()
uz = len(icerik)
for harf in icerik:
    icerik = icerik + ' ' + harf

uz2 = len(icerik)
print(icerik[uz:uz2])
dosya2 = open("sonra.txt", mode="w",encoding="utf-8")
dosya2.write(icerik[uz:uz2])
dosya2.close()