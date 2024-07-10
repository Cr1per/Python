# def bahola(ismlar):
#     """Bu Funksiya odamni uyqisi keganda ishlidigan funkdir!"""
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar
#
# talabalar = ['Ali', 'Hali', 'Mayli', 'bopti']
# baholar = bahola(talabalar[:])
# print(baholar)

#1.
# def matnla(matn):
#     matn = matn[:]
#     for i in range(len(matn)):
#         matn[i]=matn[i].title()
#     return matn
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = matnla(ismlar)
# print(ismlar)
# print(yangi_ismlar)

#2.
talabalar = ['Ali', 'Hali', 'Mayli', 'bopti']
def bahola(ismlar):
    """Bu Funksiya odamni uyqisi keganda ishlidigan funkdir!"""
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar

baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)







