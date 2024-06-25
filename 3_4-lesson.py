#1.
#mevalar = ['Uzum', 'Olcha', 'Olma', 'Gilos']
#narhlar = [2000, 3000, 55000, 70000, 100000, 25.2, -54]
#sonlar = ['bir', 'ikki', 3, 4, 5]
#ism = []
#mevalar.append('Tarvuz')
#mevalar.insert(5, 'banan')
#print(mevalar)
#2.
#cars = []
#cars.append("Lacetti")
#cars.append("Malibu")
#cars.append("My car")
#cars.append("My new car")
#del cars[-1]
#cars.remove('My car')
#print(cars)
#3.
#hayvonlar = ['Ot', 'Sigir', 'Mushuk', 'Quyon', 'Mol', 'Sher', 'Zebra', "Yo'lbars", 'Quyon']
#hayvonlar.remove('Quyon')
#print(hayvonlar)
#4
#bozorlik = ["Yog'", 'Un', 'Shakar', 'Tuz', 'Banan', 'Olcha']
#mahsulot = bozorlik.pop(5)
#print("Men " + mahsulot + " sotib oldim")
#print("Yana olishim kerak bo'lgan narsalar:", bozorlik)






#################  H O M E W O R K  #################
#1.
#ism = ["Hojiakbar", "Suxrob", "Asilbek", "Umar"]
#ism2 = ism.pop(2)
#print("Salom " + ism[0] + ", bugun choyxona bormi?")
#print(ism2 + ", choyxonaga boramizmi.")

#2.
#sonlar = [7, 96, 487, 14.5, -78, 3000]
#A_amal = sonlar[0] + sonlar[5]
#A_amal2 = sonlar[1] - sonlar[0]
#A_amal3 = sonlar[2] / sonlar[0]
#A_amal4 = sonlar[0] * sonlar[1]
#print(sonlar)
#print(A_amal)
#print(A_amal2)
#print(A_amal3)
#print(A_amal4)

#sonlar.append(789)
#son2 = sonlar[0] + sonlar[3]
#print(son2)

#sonlar.remove(3000)
#del sonlar[1]
#son1 = sonlar.pop(2)
#print("Men ",  son1,  " ni ",  sonlar[0], " ga Qo'shsam nechchi chiqadi?")

#3.
#t_shaxs = ['Imom Buxoriy', 'Alisher Navoiy', 'Zaxiriddin Muhammad Bobur']
#z_shaxs = ['Bill Gates']
#tarixiy = t_shaxs.pop(0)
#zamonaviy = z_shaxs.pop(0)
#print('Men tarixiy shaxslardan ',  tarixiy, ' bilan,\n Zamonaviy shaxslardan'
# ' esa ', zamonaviy, 'bilan\n suhbat qilishni istardim')

#4.
friend = [
    'Suxrob', 'Hojiakbar', 'Asilbek', 'Umar',
    'Abdulloh', 'Bobur', 'Abubakir', 'Abdurashid'
]
#mehmonga kela olmaydigan do'stlarim
friend.remove('Abdurashid')
friend.remove('Abubakir')
friend.remove('Umar')

# yangi do'stlarimni qo'shdim
friend.append('Jalol')
friend.insert(0, 'Jamol')
#mehmon degan yangi bo'sh ro'yxat ochdim
mehmonlar = []
#mehmonga keladigan do'stlarimni mehmon ro'yxatiga qo'shaman
ism1 = friend.pop(0)
ism2 = friend.pop(2)
ism3 = friend.pop(1)
#endi append yordamida chaqirib chiqaman
mehmonlar.append(ism1)
mehmonlar.append(ism2)
mehmonlar.append(ism3)
print(mehmonlar)


























