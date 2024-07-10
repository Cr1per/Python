# def toliq_ism(ism, familiya):
#     """Toliq ism qaytarib chiqaruvchi funk"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
#
# talaba = toliq_ism('Mohir', 'Mohirov')
# print(f"Darsga bugun {talaba} kelmadi")
#
# def toliq_ism(ism, familiya, otasining_ismi=''):
#     """Toliq ism qaytarib chiqaruvchi funk """
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
#
# talaba1 = toliq_ism('olim', 'hakimov')
# talaba2 = toliq_ism('olim', 'hakimov', 'abrorivich')
# print(talaba2)
#
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya, 'model':model, 'rangi':rangi, 'korobka':korobka, 'yili':yili, 'narhi':narhi}
#     return avto
#
# avto1 = avto_info('GM', 'Malibu', 'Oq', 'Texanika', 2002)
# avto2 = avto_info('GM', 'Jentra', 'Qora', 'Texanika', 2009, 19200 )
# avtolar = [avto1, avto2]
#
# print('Onlayn bozorda bor mashinalar: ')
#
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rangi']} {avto['model']}. Narhi: {narh}")

# def oraliq(min,max, qadam= 1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return  sonlar
#     if qadam:
#         oraliq = f"{max} {min} {qadam}"
#
# print(oraliq(0,10))
# print(oraliq(10,21))
# print(oraliq(10, 51, 3))
#
#
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ", end='')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#
#     # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
#
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rangi'].title()} {avto['model']}. Narhi: {narh}")
#
#
################### H O M E W O R K #########################
# 1.
# def foydalanuvchi(ism, familiya, t_yil, t_joy, email_manzili= None, telefon_raqami= None):
#     """Bu Funksiyada foydalanuvchi o'zi haqida ma'lumot kiritadi"""
#     foy_malumot = {'ism': ism,
#             'familiya': familiya,
#             't_yil': t_yil,
#             't_joy': t_joy,
#             'email_manzili': email_manzili,
#             'telefon_raqami': telefon_raqami}
#     return foy_malumot
#
# print("O'zingiz haqingizdagi bir nechta ma'lumotlarni kiritishingiz kerak boladi.")
# foyda_malumot = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting\n", end='')
#     ism = input("Ismingiz: ")
#     familiya = input("Familiyangiz: ")
#     t_yil = input("Tug'ilgan yilingiz: ")
#     t_joy = input("Qayerda tug'ilgansiz: ")
#     email_manzili = input("Emailingiz: ")
#     telefon_raqami = input("telefon raqamingiz: ")
#
#     foyda_malumot.append(foydalanuvchi(ism, familiya, t_yil, t_joy, email_manzili, telefon_raqami))
#
#     javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
#
# print("\nRo'yxatimizdagi ma'lumotlar:")
# for malumot in foyda_malumot:
#     if malumot['email_manzili']:
#         email_manzili = malumot['email_manzili']
#     elif malumot['telefon_raqami']:
#         telefon_raqami = malumot['telefon_raqami']
#     else:
#         email_manzili = "Noma'lum"
#         telefon_raqami = "Noma'lum"
#     print(f"{malumot['ism'].title()} \n{malumot['familiya']} \n{malumot['t_yil']} \n{malumot['t_joy']} \n{malumot['email_manzili']} \n{malumot['telefon_raqami']}")

# 2.
# def sonlar(son1, son2, son3):
#     """Bu funksiyada uchta son olib ularni ichida kattasini chiqaradi"""
#     son1 = input("Birinchi sonni kiriting:\n>>>")
#     son2 = input("Ikkinchi sonni kiriting:\n>>>")
#     son3 = input("Uchinchi sonni kiriting:\n>>>")
#
#     if son1 > son2 and son1 > son3:
#         print(f"{son2} < {son1}: {son1} katta"
#               f"\n{son3} < {son1}: {son1} katta")
#     elif son2 > son1 and son2 > son3:
#         print(f"{son1} < {son2}: {son2} katta"
#               f"\n{son3} < {son2}: {son2} katta")
#     elif son3 > son1 and son3 > son2:
#         print(f"{son1} < {son3}: {son3} katta"
#               f"\n{son2} < {son3}: {son3} katta")
#     elif son1 == son2 and son1 == son3:
#         print(f"{son1} = {son3}: teng")
#     return sonlar
#
# son = sonlar(0, 0, 0)

# 3.
# def aylana_r(radius, pi=3.14159):
#     aylana = {"radiusi":radius, "diametri":2*radius, "perimetri":2*radius*pi, "yuzi":pi*radius**2}
#
#     return aylana
#
# print(aylana_r(123))

# 5.
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
#
# print(fibonacci(123))











