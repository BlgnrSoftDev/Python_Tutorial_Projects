'''Aşağıda verilen sayılar listesi için,
 1-) listedeki tüm elemanların toplamını bulunuz
 2-) listedeki üçün katı olan sayıları yazdırınız
 3-) listedeki 2 nin katı olanların karesini alınız
 Sehirler listesi için,
 1-) listedeki maksimum 5 karakterli sehirleri yazdırınız
 urunler listesi için,
 1-) ürünlerin tamamının fiyatının toplamını bulunuz
 2-) Maksimum ücreti 5000 olan ürünleri yazdırınız '''

def toplam(array):
    sum = 0
    for el in array:
        sum += el
    return sum
def ucunkati(array):
    total = []  #call by reference kuralı olduğu için orjinal dizinin bozulmaması için fonksiyonlardayapılan işlemler için ek dizi tanımladım
    for el in array:
        if el % 3 == 0:
            total.append(el)
    return total

def tekartop(array):
    total = []
    for el in array:
        if el % 2 != 0:
            total.append(el**2)
    return total
def maxfive(array):
    total = []
    for el in array:
        if len(el) <= 5:
            total.append(el)
    return total
def totalprice(array):
    total = 0
    for el in array:
        total += int(el['price'])
    return total
def maxfivehundred(array):
    total = []
    for el in array:
        if int(el['price']) <= 5000:
            total.append(el)
    return total

liste = [1, 3, 5, 7, 9, 12, 19, 21]

urunler = [ { 'name': 'samsung s6', 'price': '3000'},
            { 'name': 'samsung s7', 'price': '4000'},
            { 'name': 'samsung s8', 'price': '5000'},
            { 'name': 'samsung s9', 'price': '6000'},
            { 'name': 'samsung s10', 'price': '7000'} ]

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']



print(f'\nOrjinal Sayılar Listesi : {liste}')
print(1000*'*')
print("Listedeki elemanlarin Toplami : ", toplam(liste))
print(1000*'*')
print(f'Listedeki 3 ün kati olan elemanlar : {ucunkati(liste)}')
print(1000*'*')
print("Listedeki Tek sayıların karesinin alımı sonucu : {}".format(tekartop(liste)))
print(1000*'*')
print(f'Orjinal Sehirler Listesi {sehirler}')
print(1000*'*')
print("Sehirler Arasında max 5 karakterli sehirler : {}".format(maxfive(sehirler)))
print(1000*'*')
print(f'Orjinal Ürünlerin Fiyat Listesi : {urunler}')
print(1000*'*')
print("Toplam urunlerin Fiyatı : {}".format(totalprice(urunler)))
print(1000*'*')
print("Maksimum 5000 tl lik ürünler : {} ".format(maxfivehundred(urunler)))