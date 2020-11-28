# Örnek 10: Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli) hesaplayınız.
print("Vücut kitle endeksi hesaplama programına hoşgeldiniz..")
boy = float(input("boyunuzu giriniz (metre): "))
ağırlık = int(input("ağırlığınızı giriniz: "))
vki = ağırlık / (boy * boy)
if vki>=18 and vki<=25:
    print(" zayıf vki= ",vki)
elif vki>25 and vki<=30:
    print(" kilolu vki= ",vki)
elif vki>30 and vki<=35:
    print(" obez = ",vki)
elif vki>35:
    print(" ciddi obez = ",vki)