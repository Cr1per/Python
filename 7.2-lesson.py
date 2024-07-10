#1.
#print("Yaqin do'stlaringiz ro'yxatini tuzamiz!")
#ismlar = []
#n=1
#while True:
#    savol = f"{n}-do'stingizni ismini kiriting: "
#    ism = input(savol)
#    ismlar.append(ism)
#    takrorlash = input("Yana ism qo'shasizmi?  (ha/yo'q)")
#    n+=1
#    if takrorlash != 'ha':
#        break
#print("Do'stlaringiz ro'yxati:")
#for ism in ismlar:
#    print(ism.title())
#2.
#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingiz ismini kiriting: ")
#    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#    dostlar[ism] = int(yosh)  # ism kalit, yosh qiymat
#
#    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#    if javob == "yo'q":
#       ishora = False
#
#for ism, yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")

#3.
#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#    cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
#print(cars)

#4.
#talabalar = ['hasan', 'husan', 'olim', 'botir']
#baholangan_talabalar = {}
#while talabalar:
#   talaba = talabalar.pop()
#    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#    print(f"{talaba.title()} baholandi")
#    baholangan_talabalar[talaba] = baho


#################### HOMEWORK ######################
#1.
#print("Buyurtmalar qabul qilamiz")
#buyurtmalar = []
#n=1
#while True:
#    savol = f"{n}-buyurtmani nomini kiriting: "
#    buyurtma = input(savol)
#    buyurtmalar.append(buyurtma)
#    takrorlash = input("Yana buyurtma qo'shasizmi?  (ha/yo'q)")
#    n+=1
#    if takrorlash != 'ha':
#        break
#print("buyurtmalar ro'yxati:")
#for buyurtma in buyurtmalar:
#    print(buyurtma.title())

#2.
#print("e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur ")
#mah = {}
#ishora = True
#while ishora:
#    ism = input("Mahsulotni nomini kiriting: ")
#    narh = input(f"{ism.title()}ning narhini kiriting: ")
#    mah[ism] = int(narh)  # ism kalit, yosh qiymat
#
#    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#    if javob == "yo'q":
#       ishora = False
#
#for ism, narh in mah.items():
#    print(f"{ism.title()} {narh} so'm")

#3.
buyurtmalar = ['olma','olcha','uzum','tarvuz']
mahsulotlar = {'olma':10000, 'shaftoli':24000, 'tarvuz':16000, 'uzum':20000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")