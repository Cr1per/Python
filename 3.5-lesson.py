###############Classwork!#################

## Botta man harflarni sort orqali tartiblab oldim va reverse orqali teskari qildim
#harflar = ['p', 'z', 'm', 'e', 'k', "g'", 'd', 's', 'r', 'n']
#print(sorted(harflar, reverse=True))

## Bu yerda ham sonlarni tartiblab oldim va reverse orqali teskarisiga o'girdim
#sonlar = [4, 8, 562, 721, 5656, 47, -87, -999, 5464.14]
#print(sorted(sonlar, reverse=True))

## Bu yerda len orqali harf yoki sonlarni nechtaligini bilib oldim
#print(len(harflar))
#print(len(sonlar))

## Men bu yerda range orqali sonlar ro'yxatidan 0 dan 10 gacha sonlarni tartibladim
#sonlar = list(range(0,11))
#print(sonlar)

## Bu yerda 0 dan 100 gacha 10 tadan son tartibladim
#sonlar = list(range(0,101,10))
#print(sonlar)

## Bu yerda o'zim uchun bir misol qilib kordim
#sonlar = [10, 20, 50, 100, 200, 400, 600, 800, 1000]
#print(
# "Minimum songa, Maksimum sonlarni qo'shamiz\n va chiqgan songa yig'indini qo'shamiz ",
# min(sonlar) + max(sonlar) + sum(sonlar)
#)
## bu orqali ro'yxatdan kerakli joyini kesib oldim
#print(sonlar[1:5])

#men ro'yxatdan nusxa olmoqchi bolsam : bundan foydalanaman
#son1 = sonlar[:]
#print(son1)
#son1.remove(200)
#son1.append(6000)
#son1.insert(1, 879)
#print(son1)
#print(sonlar)

## Bu yerda men ro'yxatni o'zgarmas qilmoqchi bolsam tuple yordamida qilishim mumkin ekan
#sonlar = [10, 20, 50, 100, 200, 400, 600, 800, 1000]
#sonlar = tuple(sonlar)
#print(type(sonlar))
##xatolik berdi chunki endi buni o'zgartirib bolmaydi
#sonlar.append(555)
#print(sonlar)
## agarda kerak bo'lib qolsa list yordamida ro'yxatni asliga qaytarib keyin o'zgartirsa boladi
#sonlar = list(sonlar)
#sonlar.append(555)
#print(sonlar)

##############################  H O M E W O R K  ############################
#1.
#davlat = ['Russia', "O'zbekiston", 'Turkmaniston', 'Xitoy', 'Amerika', 'Germaniya']
#print(sorted(davlat, reverse=True))
#davlat = list(davlat)
#print(type(davlat))
#print(davlat)
#print(list(reversed(davlat)))
#davlat.sort(reverse=True)
#print(davlat)

#2.
#print(list(range(120,1201,2)))
#sonlar = [125, 1634, 1234, 168, 478, 1349, 1200, 123000,]
#print(sum(sonlar))
#a = max(sonlar)
#b = min(sonlar)
#print(a - b)
#print(len(sonlar))
#
#print(list(range(0, 21)))
#print(list(range(50, 71)))
#print(list(range(100, 121)))

#3.
#taomlar = ['Osh', "Sho'rva", 'Mastava', "Moshho'rda", 'Halim']
#nonushta = taomlar[:]
#del nonushta[0]
#del nonushta[1]
#nonushta.append('Makaron')
#nonushta.append('Sirguruch')
#print(taomlar)
#print(nonushta)
#nonushta = tuple(nonushta)
#nonushta[0] = 'qaymoq va non'













