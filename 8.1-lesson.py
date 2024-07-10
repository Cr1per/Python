#def toliq_ism(ism, familiya):
#    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}\n"
#          f"Foydalanuvchi familiyasi: {familiya.title()}")
#toliq_ism('olim', 'hakimov')
#
#def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#yosh_hisobla(1993)

######################### HOMEWORK ####################
#1.
#def tugilgan_yil(ism, yosh):
#    """Foydalanuvchidan ismini va yoshini so'rab tug'ilgan yilini chiqaradigan funksiya"""
#    print(f"{ism.title()} {2024-yosh} yilsiz")
#
#tugilgan_yil('Mohir', 16)

#2.
#def kvadrat_kub(son):
#    """Foydalanuvchidan son olib kvadrati va kubini chiqaruvchi funksiya"""
#    print(f"{son}ning kvadrati {son**2}\n"
#          f"{son}ning kubi {son**3}")
#kvadrat_kub(100)

#3.
#def kvadrat_kub(son):
#    """Foydalanuvchidan son olib toq yoki juftligini chiqaruvchi funksiya"""
#    if son % 2:
#        print(f"{son} toq")
#    else:
#        print(f"{son} juft")
#
#kvadrat_kub(123456789)

#4.
#def son_teng_katta(son1, son2):
#    """Foydalanuvchidan ikkita son olib kattasini yoki tengini chiqaruvchi funksiya"""
#    if son1 > son2:
#        print(f"{son1} katta")
#    elif son1 < son2:
#        print(f"{son2} katta")
#    else:
#        print("teng")
#
#son_teng_katta(1230, 123)

#5.
#def sonlar(x, y):
#    """Foydalanuvchidan son olib uni x y chiqaruvchi funksiya"""
#    print(f"{x} {y}")
#sonlar(12469, 1569)

#6.
def qoldiqsiz_son(son):
    """Foydalanuvchidan son olib uni 2 dan 10 gacha qoldiqsiz bolinadigan sonlarni chiqaruvchi funksiya"""
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bolinadi")

qoldiqsiz_son(1234567890000000000000000000)









