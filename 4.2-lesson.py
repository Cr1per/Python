###############  Classwork  ############################
#yosh = int(input("Yoshingiz nehchchida:"))
#if yosh <= 7:
#    narh = 0
#elif yosh <= 16:
#    narh = 10000
#else:
#    narh = 15000
#print(f"Kirish {narh} So'm")

#kun = input("Bugun nima kun:")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni")

#kun = input("Bugun nima kun:")
#harorat = float(input("Havo harorati qanday:"))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print("Dachaga ketdik!")
#elif kun.lower()=='yakshanba' and harorat<=30:
#    print("Dam olamiz!")
#else:
#    print("Bugun ishlaymiz")

#kun = input("Bugun nima kun:")
#harorat = float(input("Havo harorati qanday:"))
#
#if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat>=30:
#    print("Dachaga ketdik!")
#elif kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat<=30:
#    print("Uyda Dam olamiz!")
#else:
#    print("Bugun ishlaymiz")

#narh = 15000
#osh = True
#salat = False
#
#if osh and salat:
#    narh = narh + 10000
#elif osh or salat:
#    narh = narh + 5000
#
#print(f"Jami {narh} so'm")

#narh = 15000
#choy = 0
#osh = 1
#salat = 0
#suv = 1
#if choy:
#    print("choy oldi")
#    narh = narh + 5000
#if osh:
#    print("osh oldi")
#    narh = narh + 5000
#if salat:
#    print("salat oldi")
#   narh = narh + 5000
#if suv:
#    print("suv oldi")
#    narh = narh + 5000
#
#print(f"Jami {narh} Boldi")

#menu = ['Osh', 'Qozon kabob', 'somsa', 'manti', 'pitsa', 'sho\'rva']
#ovqat = input("nima yeysiz? :")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi!")
#else:
#    print("Afsuski bizda bunday ovqat yo'q")

#menu = ['Osh', 'Qozon kabob', 'somsa', 'manti', 'pitsa', 'sho\'rva']
#buyurtma = ['Osh', 'shashlik', 'manti', 'pitsa', 'sirguruch']
#
#for taom in buyurtma:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q")


#########################  $H $O $M $E $W $O $R $K  $######################
#1.
#son = list(range(0,10000000,2))
#k_son = int(input("Juft son kiriting: "))
#
#if k_son in son:
#    print("Raxmat")
#else:
#    print("Juft son kiriting!")

#2.
#yosh = int(input("Yoshingizni kiriting: "))
#if yosh <=4 or yosh >= 60:
#    print("Kirish bepul")
#elif yosh < 18:
#    print("Kirish 10000 so'm")
#else:
#    print("Kirish 20000 so'm")

#3.
#b_son = input("birinchi sonni kiriting: ")
#i_son = input("ikkinchi sonni kiriting: ")
#
#if b_son == i_son:
#    print("Sonlar teng")
#elif b_son > i_son:
#    print("birinchi son katta")
#else:
#    print("Ikkinchi son katta")

#4.
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#
#
#print("5 ta mahsulot kiriting: ")
#
#for n in range(5):
#    mahsulot = input(f"{n+1}-mahsulotni qo'shing:\n>>> ")
#
#    if mahsulot in mahsulotlar:
#        print("Do'konda mahsulot bor")
#        savat.append(mahsulot)
#        print(mahsulot)
#    else:
#        print("Do'konda mahsulot yo'q")

#5.
#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#
#bor_mahsulot = []
#yoq_mahsulot = []
#
#print("5 ta mahsulot kiriting: ")
#
#for n in range(5):
#    mahsulot = input(f"{n+1}-mahsulotni qo'shing:\n>>> ")
#
#    if mahsulot in mahsulotlar:
#        bor_mahsulot.append(mahsulot)
#
#    elif mahsulot not in mahsulotlar:
#        yoq_mahsulot.append(mahsulot)
#
#if mahsulot in mahsulotlar:
#    print("Do'konda hamma mahsulotlar bor")
#else:
#    print(f"Quyidagi mahsulotlar do'konda yo'q {yoq_mahsulot}")

#6.
#foydalanuvchilar = ['Asilbek', 'Hojiakbar', 'Umar', 'Suxrob', 'Ali']
#
#login = input("Yangi login kiriting:\n>>>")
#
#if login in foydalanuvchilar:
#    print("Login band, yangi login tanlang!")
#else:
#    print("Xush kelibsiz!")

#7.

son = int(input("Butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")



















