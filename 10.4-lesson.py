# from uuid import uuid4
#
#
# class Avto:
#     """Avtomobil klassi"""
#
#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id
#
#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")
#
# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# avto1.add_km(1500)
# print(avto1.get_km())
#
#
# class Avto:
#     """Avtomobil klassi"""
#     __num_avto = 0
#
#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto
#
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(Avto.get_num_avto())


from uuid import uuid4
class Shaxs:
    """Shaxs klassi"""
    shaxslar_soni = 0
    def __init__(self, ism, familiya, passport, tyil,pul=0):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__pul = pul
        self.__id_raqam = uuid4()
        Shaxs.shaxslar_soni += 1

    @classmethod
    def get_shaxslar_soni(cls):
        return cls.shaxslar_soni

    def get_id_raqam(self):
        return self.__id_raqam

    def get_pul(self):
        return self.__pul

    def add_pul(self, pul):
        if pul>=0:
            self.__pul += pul
        else:
            print("Shaxsning pulini kamaytirib bo'lmaydi")

class Talaba(Shaxs):
    """Talaba klassi"""
    talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam, pul=0):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
        self.__pul = pul
        Talaba.talabalar_soni += 1

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_pul(self):
        return self.__pul

    def add_pul(self, pul):
        if pul>=0:
            self.__pul += pul
        else:
            print("Talabaning pulini o'g'irlamang")

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def fanga_yozil(self, fan):
        """Talabani fanga yozish"""
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        """Talabaning fanlari ro'yxatidan fanni o'chirish"""
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"

talaba1 = Talaba('Anvar','Anvarov','TN123467894',2001, 'id458715', 2000)
talaba2 = Talaba('Anvar','Anvarov','TN123467894',2001, 'id458715', 2000)
talaba3 = Talaba('Anvar','Anvarov','TN123467894',2001, 'id458715', 2000)
print(Talaba.get_info(talaba1))