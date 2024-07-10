# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def set_bosqich(self, bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
#
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
#
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil
#
# class Fan:
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
#
#     def add_student(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#
#     def get_name(self):
#         return self.nomi
#
#     def get_student(self):
#         return [talaba.get_fullname() for talaba in self.talabalar]
#
#     def get_student_num(self):
#         return self.talabalar_soni
#
#
# matematika = Fan("Olim Matematika")
# talaba1 = Talaba("Alijon", "Ganiyev", 2000)
# talaba2 = Talaba("Islomjon", "Ganiyev", 2004)
# talaba3 = Talaba("G'anijon", "Ganiyev", 2003)
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

class Avto:
    def __init__(self,model,rang,korobka,narh,yil):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yil = yil
        self.kilometr = 0

    def get_info(self):
        return f"Modeli {self.model}, Rangi {self.rang}, Korobka {self.korobka}, Narhi {self.narh}, Ishlab chiqarilgan yili {self.yil}"

    def set_kilometr(self,kilometr):
        self.kilometr = kilometr

    def update_kilometr(self):
        self.kilometr += 2

    class Avtosalon:
        def __init__(self,nomi,manzili,sotuv_avto):
            self.nomi = nomi
            self.manzili = manzili
            self.sotuv_avto = sotuv_avto
            self.avtolar_soni = 0
            self.avtolar = []

        def set_avto(self,avto):
            self.avtolar_soni += 1
            self.avtolar = avto

        def get_info(self):
            return f"Avtomobillar soni {self.avtolar_soni}, Avtomobillar {self.avtolar}"





