#car0 = {
#        'model':'lacetti',
#        'rang':'oq',
#        'yil':2018,
#        'narh':13000,
#        'km':50000,
#        'korobka':'avtomat'
#        }
#
#car1 = {
#        'model':'nexia 3',
#        'rang':'qora',
#        'yil':2015,
#        'narh':9000,
#        'km':89000,
#        'korobka':'mexanika'
#        }
#
#car2 = {
#        'model':'gentra',
#        'rang':'qizil',
#        'yil':2019,
#        'narh':15000,
#        'km':20000,
#        'korobka':'mexanika'
#        }
#
#car = car0
#print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narh']}$")
#
#car = car1
#print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narh']}$")
#
#car = car2
#print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narh']}$")
#
#Keling, barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida birma-bir konsolga chiqaramiz:
#cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rang']} rang, "
#          f"{car['yil']}-yil, {car['narh']}$")
#
#Biror lug'atdagi elementga murojat qilish uchun esa quyidagi usuldan foydalanishimiz mumkin:
#print(cars[0])
#print(cars[0]['model'])
#
#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")
#
#for tsikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:
#malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
#for n in range(10):
#    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#        'model':'malibu',
#        'rang':None, # rangi noaniq
#        'yil':2020,
#        'narh':None, # narhi belgilanmagan
#        'km':0,
#        'korobka':'avto'
#        }
#    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
#
#Keyingi 3 tasiga esa qora:
#for malibu in malibus[:3]:
#        malibu['rang'] = 'qizil'
#
#Oxirgi 4 ta avtoni qora, lekin korobkasini mexanika qilamiz:
#for malibu in malibus[3:6]:
#        malibu['rang'] = 'qora'
#Keling endi, mashinalarning korobkasidan chiqqan holda narh belgilaymiz:
#for malibu in malibus:
#    if malibu['korobka']=='avto':
#        malibu['narh']=40000
#    else:
#        malibu['narh']=35000
#
#
#LUG'AT ICHIDA RO'YXAT
#dasturchilar = {
#    'ali':['python','c++'],
#    'vali':['html','css','js'],
#    'hasan':['php','sql'],
#    'husan':['python','php'],
#    'maryam':['c++','c#']
#    }
#
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#    for til in tillar:
#        print(til.upper())
#
#Pythondagi print() funktsiyasi har bir matndan so'ng yangi qator tashlaydi. Buning oldini olish uchun quyidagi usuldan foydalanish mumkin: print(string, end = '')
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
#    for til in tillar:
#       print(f'{til.upper()} ', end='')
#
#
#LUG'AT ICHIDA LUG'AT
#
#hamkasblar = {
#    'ali':{'familiya':'valiyev',
#           'tyil':1995,
#           'malumot':'oliy',
#           'tillar':['python','c++']
#           },
#    'vali':{'familiya':'aliyev',
#            'tyil':2001,
#            'malumot':"o'rta-maxsus",
#            'tillar':['html', 'css', 'js']},
#    'hasan':{'familiya':'husanov',
#             'tyil':1999,
#             'malumot':'maxsus',
#             'tillar':['python','php']}
#    }
#
#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()}, "
#          f"{info['tyil']}-yilda tug'ilgan. "
#          f"Ma'lumoti: {info['malumot']}. \n"
#          "Quyidagi dasturlash tillarini biladi:")
#    for til in info['tillar']:
#        print(til.upper())



####################$#$# H O M E W O R K #$#$###################
#1.
#buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil', 'tyil':810,
#           'vyil':870, 'tjoy':'Buxoro'}
#qodiriy = {'ism':'Abdulla Qodiriy', 'tyil':1894,
#           'vyil':1938, 'tjoy':'Toshkent'}
#vohidov = {'ism':'Erkin Vohidov', 'tyil':1936,
#           'vyil':2016, 'tjoy':"Farg'ona"}
#navoiy = {'ism':'Alisher Navoiy', 'tyil':1441,
#           'vyil':1501, 'tjoy':"Xirot"}
#karobka = [buxoriy, qodiriy, vohidov, navoiy]
#for shaxs in karobka:
#    ism = shaxs['ism']
#    tyil = shaxs['tyil']
#    vyil = shaxs['vyil']
#    tjoy = shaxs['tjoy']
#    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#          f"{vyil-tyil} yil umr ko'rgan.")
#
#2.
#buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil', 'tyil':810,
#           'vyil':870, 'tjoy':'Buxoro', 'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]}
#qodiriy = {'ism':'Abdulla Qodiriy', 'tyil':1894,
#           'vyil':1938, 'tjoy':'Toshkent', 'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']}
#vohidov = {'ism':'Erkin Vohidov', 'tyil':1936,
#           'vyil':2016, 'tjoy':"Farg'ona", 'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]}
#navoiy = {'ism':'Alisher Navoiy', 'tyil':1441,
#           'vyil':1501, 'tjoy':"Xirot", 'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']}
#karobka = [buxoriy, qodiriy, vohidov, navoiy]
#for shaxs in karobka[0:]:
#    ism = shaxs['ism']
#    asarlar = shaxs['asarlar']
#    print(f"\n{ism} ning mashxur asarlari: ")
#    for asar in asarlar:
#        print(asar)

#3.

#film = {
#    'ali':['terminator', 'Rambo', 'Titanic'],
#    'vali':['Tenet','Inception','Interstellar'],
#    'husan':['Abdullajon','Bomba','Shaytanat'],
#    'hasan':['Mahallada duv-duv gap','John Wick']
#}
#for ism, film in film.items():
#    print(f"\n{ism.title()}ning yoqtirgan kinolari: ")
#    for kino in film:
#        print(kino)

#4.
#davlatlar = {
#    "o'zbekiston":{'poytaxt':"toshkent", 'maydon':448978,
#                   'aholi':33_000_000, 'pul birligi':"so'm"},
#    "rossiya":{'poytaxt':"moskva", 'maydon':17_098_246,
#               'aholi':144_000_000, 'pul birligi':"rubl"},
#    "aqsh":{'poytaxt':"vashington", 'maydon':9_631_418,
#            'aholi':327_000_000, 'pul birligi':"dollar"},
#    "malayziya":{'poytaxt':"kuala-lumpur", 'maydon':329750,
#                   'aholi':25_000_000, 'pul birligi':"rinngit"}}
#for davlat, i in davlatlar.items():
#    if davlat.lower()=='aqsh':
#        davlat = davlat.upper()
#    else:
#        davlat = davlat.capitalize()
#    print(f"\n{davlat}ning poytaxti {i['poytaxt'].title()}"
#          f"\nHududi: {i['maydon']} kv.km"
#          f"\nAholisi: {i['aholi']}"
#          f"\nPul birligi: {i['pul birligi']}")

#5.
#davlatlar = {
#    "o'zbekiston":{'poytaxt':"toshkent", 'maydon':448978,
#                   'aholi':33_000_000, 'pul birligi':"so'm"},
#    "rossiya":{'poytaxt':"moskva", 'maydon':17_098_246,
#               'aholi':144_000_000, 'pul birligi':"rubl"},
#    "aqsh":{'poytaxt':"vashington", 'maydon':9_631_418,
#            'aholi':327_000_000, 'pul birligi':"dollar"},
#    "malayziya":{'poytaxt':"kuala-lumpur", 'maydon':329750,
#                   'aholi':25_000_000, 'pul birligi':"rinngit"}}
#
#davlat = input('Davlat nomini kiriting: ').lower()
#if davlat in davlatlar:
#    info = davlatlar[davlat]
#    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#          f"\nHududi: {info['maydon']} kv.km"
#          f"\nAholisi: {info['aholi']}"
#          f"\nPul birligi: {info['pul birligi']}")
#else:
#    print("Bizda bu davlat haqida ma'lumot mavjud emas")



