from tkinter import *
import datetime
def kontrol_et():
    dosya = open("usom.txt", "r") # zaralı ip leri çektiğimiz dosyayı okuma modunda açtık
    icerik = dosya.read() # dosyanın içeriğini 'icerik' degiskenine atadık
    dosya.close() #dosyayı kapattık
    ip = entry1.get() # entry1 bölümünden aldığımız veriyi ip ye atadık
    bugun = datetime.datetime.now() # log seklinde kayıt tutabilmek icin datetime modulunun anlık zamanı döndüren methodunu kullandık
    if str(ip) in icerik: # kullanıcıdan aldığımız ip'yi zaralı ip ler arasında arıyoruz ve var ise;
        dosya = open("log.txt", "a") # logları kaydeteceğimiz dosyayı yazma açtık
        yazi = str(ip) + " : zararli\n" + "Tarih:" + str(bugun) + "\n" # logların yazım şeklini ayarlıyoruz
        dosya.write(yazi) # logları dosyaya yazıyoruz
        dosya.close() #dosyayı kapattık
        v.set("IP IS DANGEROUS!!") #ikinci entry'mizdeki v textvariable'a sorgulamamızın sonucu atıyoruz.
    else:
        dosya = open("log.txt", "a")  # logları kaydeteceğimiz dosyayı yazma modunda açtık
        yazi = str(ip) + " : zarali degil\n" + "Tarih: " + str(bugun) + "\n" # logların yazım şeklini ayarlıyoruz
        dosya.write(yazi)  # logları dosyaya yazıyoruz
        dosya.close() #dosyayı kapattık
        v.set("IP is Reliable") #ikinci entry'mizdeki v textvariable'a sorgulamamızın sonucu atıyoruz.


top = Tk() # top adlı nesnemizi olusturduk
top.title("Usom IP konrol") # nesnemizin üstteki baslıgını atadık
B = Button(top,text="Check",command=kontrol_et) # buton ekledik, üstüne 'check' yazdık ve komut belirttik
B.place(x = 50, y = 50) # butonun konumunu ayarladık.
B.pack() # butonu kullanılabilir hale getirdik
label1 = Label(top,text="Enter IP here :") # etiket ekledik ve üstüne "Enter IP here :" yazdık.
label1.place(x = 50, y = 80) # etiketinin konumunu ayarladık.
label1.pack() # etiketi kullanılabilir hale getirdik
entry1 = Entry(top) # giriş için nesne ekledik
entry1.place(x = 50, y = 90) # ip girilecek nesnenin konumunu ayarladık
entry1.pack() # nesneyi kullanılabilir hale getirdik
v = StringVar() # ilgili ifadenin içeriğinin değiştirilmesini sağlar
entry2 = Entry(top,textvariable = v)  # ıp sorgulamasının sonucunu göreceğimiz nesneyi olusturduk
entry2.place(x = 50, y = 100) # nesnenin konumunu ayarladık.
entry2.pack() # nesneyi kullanılabilir hale getirdik
top.mainloop()