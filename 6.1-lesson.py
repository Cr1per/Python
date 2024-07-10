##1.
#car_0 = {'model':"ferrari", 'rang': 'qizil'}
#print(car_0['model'])
#print(car_0['rang'])
#
##2.
#en_uz = {'apple': 'olma', 'apricot': 'O\'rik', 'banana': 'banan'}
#print(en_uz['apple'])
#
##3.
#mevalar = {'olma': 1000, 'tarvuz': 2000, 'qovun': 3000}
#print(f"Olma narhi {mevalar['olma']} so'm")
#
##4.
#talaba_0 = ['ism': 'Asilbek', 'yoshi':16, 't_yil':2008]
#print(f"{talaba_0['ism'].title()}, {talaba_0['yoshi']}-yoshda {talaba_0['t_yil']}-yilda tug'ilgan")
#
##qo'shish
#talaba_0['ism'] = 'qobil rasulov'
#talaba_0['kurs'] = 3
#talaba_0['yosh'] = 20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

##6
#talaba_1['ism'] = 'qobil rasulov'
#talaba_1['kurs'] = 3
#talaba_1['yosh'] = 20
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#7
#meva = en.uz.get('apple', 'Bunday meva mavjud emas')
#print(meva)



#############################HOMEWORK######################
#1.
#oilam = {'onam':'Samikjanova Shoxista', 't_yil_O': 1982, 'manzil_O':'S_Darvoza T_58',
#         'Otam': 'Samikjanov Rustam', 't_yil_A': 1973, 'manzil_A': 'S_Darvoza T_58',
#         'Ukam': 'Samikjanov Muhammad', 't_yil_U': 2022, 'manzil_U':'S_Darvoza T_58',
#          'Opam': 'Samikjanova Xonzoda', 't_yil_Op': 2007, 'manzil_Op':'S_Darvoza T_58'
#}
#print(f"{oilam['onam'].title()}, {oilam['t_yil_O']}-yil, {oilam['manzil_O']} yashash joyi")

#2.
#taom = {
#    'Onam':'Oyim', 's_taom_O': 'osh',
#    'Otam':'Adam', 's_taom_A': "Moshxo'rda",
#    'Opam':'Xonzoda', 's_taom_Op': 'osh'
#}
#print(f"{taom['Onam'].title()}ning sevimli taomlari {taom['s_taom_O']}")
#print(f"{taom['Otam'].title()}ning sevimli taomlari {taom['s_taom_A']}")
#(f"{taom['Opam'].title()}ning sevimli taomi {taom['s_taom_Op']}")

#3.
#lugat = {
#    'if':'agar', 'else': 'aks holda', 'upper': 'kattalashtirish',
#    'integer': 'son', 'float': 'o\'nlik', 'string': 'matn'
#}
#print(f"{lugat['if'].title()}, {lugat['integer'].title()}, {lugat['string'].title()}")

#4.
#lugat = {
#    'if':'agar', 'else': 'aks holda', 'upper': 'kattalashtirish',
#    'integer': 'son', 'float': 'o\'nlik', 'string': 'matn'
#}
#foy_lug = input("Biron bir so'z kiriting:\n>>>")
#foy_lug = lugat.get(f'{foy_lug}', 'Bu so\'z mavjud emas!')
#
#print(foy_lug)

#5.
lugat = {
    'if':'agar', 'else': 'aks holda', 'upper': 'kattalashtirish',
    'integer': 'son', 'float': 'o\'nlik', 'string': 'matn'
}
foy_lug = input("Biron bir so'z kiriting:\n>>>")
if foy_lug == 'if':
    print('Agar')
elif foy_lug == 'else':
    print("Ask holda")
elif foy_lug == 'upper':
    print("Kattalashtirish")
elif foy_lug == 'integer':
    print("son")
elif foy_lug == 'float':
    print("o'nlik")
elif foy_lug == 'string':
    print("Matn")
else:
    print("Bu so'z mavjud emas")
















