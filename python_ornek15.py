import random
randomnum = random.randint(1,30)
trial = 0
while (1):
    num = int(input("1 ile 100 arası sayı griniz: "))
    trial += 1
    if num == randomnum :
        print("tebrikler doğru bildiniz !! {}. denemede buldunuz..".format(trial))
        break
    else:
        print("Bulamadınız HAHAHAHAH tekrar deneyin HAHAHAH")