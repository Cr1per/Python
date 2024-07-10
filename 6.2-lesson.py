#talaba_0 = {
#    'ism':'alijon',
#    'familiya':'shamshiyev',
#    'yosh':22,
#    'fakultet':'matematika',
#    'kurs':4
#    }
#
#print(talaba_0.items())
#
#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#   }
#items kalit va qiymatni korsatib beradi
#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}")
#
#
#mahsulotlar = {  'Do\'kondagi mahsulotlar'
#    'olma':10000,
#    'anor':20000,
#    'uzum':40000,
#    'anjir':25000,
#    'shaftoli':30000
#    }
# keys royxatning kalitini chiqarib beradi
#print(mahsulotlar.keys())
#
#
#bozorlik = ['anor','uzum','non','baliq']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
#
#
#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310',
#    'hamida':'galaxy s9',
#    'maryam':'huawei p30',
#    'tohir':'iphone x',
#    'umar':'iphone x'
#    }
# values foydalanuvchi nima ishlatishini chiqarib beradi
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in telefonlar.values():
#    print(tel)
#
# set ro'yxatda bor narsani ikki marta takrorlamaydi
#print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
#for tel in set(telefonlar.values()):
#    print(tel)


###########################HOMEWORK#####################
#1.
#lugat = {
#    'apple':'olma', 'apricot':'o\'rik',
#    'melon':'qovun', 'watermelon':'tarvuz',
#    'tomatoes':'pamidor', 'carrot':'sabzi'
#}
#for k, q in sorted(lugat.items()):
#    print(f"{k.title()} ning tarjimasi {q}")

#2.
#davlat = {
#    "O'zbekiston":"Toshkent", 'Rossiya':'Moskva', 'Amerika':'Vashington',
#    'Germaniya': 'berlin', 'Turkiya':'Anqada', 'Xitoy':'Beijing',
#}
#for k in sorted(davlat.keys()):
#    print(f"davlatlar: {k.title()} ")
#for q in sorted(davlat.values()):
#    print(f"Poytaxtlar: {q.title()} ")

#3.
#davlat = {
#    "O'zbekiston":"Toshkent", 'Rossiya':'Moskva', 'Amerika':'Vashington',
#    'Germaniya': 'berlin', 'Turkiya':'Anqada', 'Xitoy':'Beijing',
#}
#foy_davlat = input("Davlatning nomini kiriting:\n>>>")
#foy_davlat = davlat.get(f"{foy_davlat.title()}", "Bizda bunday ma'lumot mavjud emas")
#print(foy_davlat.title())

#4.
menu = {
    'osh':'15000', 'shashlik':'25000', 'xalim':'20000', 'baliq':'35000',
    'pitsa':'26000', 'gamburger':'30000', 'kampot':'10000', 'choy':'5000'
}
print("3 ta taom tanlang!")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom.title()} {menu[taom]} so'm")
    else:
        print(f"Kechirasiz, bizda {taom} yo'q.")










