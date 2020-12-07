# kullanıcıdan alınan bilgilerle dictionary oluşturma örneğidir......


'''ogrenciler = {

    101 : {
        "ad" : "huseyin",
        "soyadı" : "bilginer",
        "bölüm" : "bilgisayar müh.",
        "yas" : "19"
    },
    102 : {
        "ad" : "hakkı",
        "soyadı" : "dağdeviren",
        "yas" : 20,
        "bölüm" : "mekatronik müh."

    }
}'''

for x in range(0,1):
    num =input("öğrenci numaranızı giriniz: ")
    ad = input("Adınızı giriniz: ")
    soyad = input("soyadınızı giriniz: ")
    bölüm = input("bölümünüzü giriniz: ")
    yas = input("yasınızı giriniz: ")

    ogrenciler = {}
    ogrenciler[num] = {"ad" : ad ,"soyad" : soyad,"yas" : yas,"bölüm" :bölüm}

print(ogrenciler)


# bu yukaridaki işlemleri daha kolay olarak yapabilririz;
ogrenciler.update({
    "ekleme" :{
        "ad" : "huseyin",
        "soyad" : "bilginer",
        "bölüm" : "mekatronik"
    }
})
print("*"*50)
ara = input("hangi öğrenci bilgilerini istiyorsunuz: ")
ogrenci = ogrenciler[ara]

print(f'ogrencinin numarası : {ara}, ogrencinizin adı : {ogrenci["ad"]}, ogrencinin soyadı : {ogrenci["soyad"]} ,ogrencinin bölümü {ogrenci["bölüm"]} dir')

