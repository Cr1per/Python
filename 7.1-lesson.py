# While toki ubu narsa tugamagunicha ishlidi
#1.
#son = 1
#while son<=5:
#    print(son, end=' ')
#    son = son + 1
#print('Dastur tugadi')
#2.
#print("Kiritilgan sonning kvadratini chiqaradi")
#savol = "Istalgan sonni kiriting "
#savol += "(dasturni toxtatish uchun 'exit' deb yozing)"
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#       print(float(qiymat)**2)
#print("Dastur tugadi")
#
#3.
#savol = "Istalgan sonni kiriting "
#savol += "(dasturni toxtatish uchun 'exit' deb yozing)"
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat) ** 2)
#print("Dastur tugadi")
#
#4.
#savol = "Istalgan sonni kiriting "
#savol += "(dasturni toxtatish uchun 'exit' deb yozing)"
#
#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat) ** 2)
#print("Dastur tugadi")
#
#5.
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        break # to'xtatish ## continue ortga qaytarib yuboradi.
#    print(f"{son} ning kvadrati {son**2} ga teng")

#6.
#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)

#########################$#$#$#$ H O M E W O R K $#$#$#$##########################
#1.
#savol = "Yaxshi ko'rgan kitobingizni nomini kiriting!\n "
#savol += "(dasturni toxtatish uchun 'stop' deb yozing):\n>>>"
#
#while True:
#    qiymat = input(savol)
#    if qiymat == 'stop':
#        break
#    else:
#        print(qiymat)
#print("Dastur tugadi")

#2.
#savol = "Yoshingizni kiriting!\n "
#savol += "(dasturni toxtatish uchun 'exit' yoki 'quit' deb yozing):\n>>>"
#
#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit' or qiymat == 'quit':
#        break
#    yosh = int(qiymat)
#
#    if yosh < 7:
#        narh = 2000
#    elif 7 <= yosh < 18:
#        narh = 3000
#    elif 18 <= yosh < 65:
#        narh = 10000
#    else:
#        narh = 0
#
#    if narh == 0:
#        print("Sizga chipta bepul")
#    else:
#        print(f"Chipta {narh} so'm")
#print("Dastur tugadi!")

#3.
#savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
#savol += "Musbat son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
#while True:
#    qiymat = int(input(savol))
#    son = int(qiymat)
#    son += 1
#    if qiymat<0:
#        continue
#    elif qiymat=='Exit':
#        break
#    else:
#        ildiz = float(qiymat**0.5)
#        print(f"{qiymat} ning ildizi {ildiz} ga teng")














