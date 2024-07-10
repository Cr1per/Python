import math

uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,15))

kvadrat = lambda x, y : x ** y
print(kvadrat(10,10))
###
def daraja(n):
    return lambda x : x**n
# lambda funksiyasi hda qiulay funkni ichida foydalanishga
kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga "
      f"kubi {kub(3)} ga teng")
###

from math import sqrt
# map funksiyasi bitta funk va royxat qabul qilib royxatni ichidagi narsalarni funk orqali bajarib chiqarib keradi
sonlar = list(range(11))
ildizlar = list(map(sqrt, sonlar))
print(ildizlar)
###
def daraja2(x):
    return x*x
print(list(map(daraja2, sonlar)))
# lambda nomsiz funksiya bu funksiya juda qulay va qisqa kod yozish uchun zor
kvadrat = list(map(lambda x: x*x, sonlar))
print(kvadrat)

###bunda ani b ga qoshvotti
a = [1,15,19]
b = [2,16,20]
a_plus_b = list(map(lambda x,y:x+y, a,b))
print(a_plus_b)

###
import random as r
# sample orqali tasodifiy sonlani nechtaligini yozsa boladi
sonlar = r.sample(range(100),10)
print(sonlar)
def juftmi(x):
    return x%2==0
# filter filterdan otqizib eradi yani saralab oladi
juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)
# osonroq yoli juftligini chiqaradi
juft_son = list(filter(lambda son: son%2==0,sonlar))
print(juft_son)


#####
mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
#bu b harf bilan boshlanadigan sozlarni chiqaradi
mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)
#statswith bu bilan boshlanadimi yoqmi tek qiladi
#bu 5 ta harfli sozlarni chiqaridi
mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)








