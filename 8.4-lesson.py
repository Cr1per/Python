###    *args   hohlagan qiymat oladi
# def summa(*son):
#     return sum(son)
#
# print(summa(55,66,44,88,98))
# print(summa(55,66,88,98))
# print(summa(55,66))
#
# def summa(x,y, *son):
#     return x+y+sum(son)
#
# print(summa(55,66,44,88,98))
# print(summa(55,66,88,98))
# print(summa(55,66))
### **kwargs Hohlagan qiymat oladi faqat lugat korinishida
# def avto_info(kompaniya,model,**malumot):
#     malumot['kompaniya']=kompaniya
#     malumot['model']=model
#     return malumot
#
# avto1 = avto_info("GM", "Malibu", rang='qora', yil=2008)
# avto2 = avto_info("Kia", "K5", rang='oq', yil=2009, narh=3000)
#
# print(avto1)
##############HOMEWORK####################
#1.
# def kopaytma(*son):
#     kopayt = 1
#     for s in son:
#         kopayt *= s
#     return kopayt
#
# print(kopaytma(10,20,30,40,50,60,70,80,90,100))

#2.
def malumot_f(ism,familiya,**malumot):
    """Funk bu ..."""
    malumot['ism']=ism
    malumot['familiya']=familiya
    return malumot
print(malumot_f('Gani','Ganiyev',yosh='14',yil=2010))











