# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
#
#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
#
#
# class Talaba(Shaxs):
#     """Talaba klassi"""
#
#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
#
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
#
#
# class Manzil:
#     """Manzil saqlash uchun klass"""
#
#     def __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
#
#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil






class Shaxs:
    """Shaxs klassi"""
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

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

class Fan:
    """Fan klassi"""
    def __init__(self, nomi):
        self.nomi = nomi

matematika = Fan("Matematika")
fizika = Fan("Fizika")
informatika = Fan("Informatika")

talaba1 = Talaba("Ali", "Valiyev", "AA1234567", 2000, "T12345")

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)

talaba1.remove_fan(matematika)
talaba1.remove_fan(informatika)

print(talaba1.get_info())

class Foydalanuvchi(Shaxs):
    def __init__(self,foydalanuvchi,ism,familiya,email):
        self.foydalanuvchi = foydalanuvchi
        self.ism = ism
        self.familiya = familiya
        self.email = email

    def get_info(self):
        return f"{self.foydalanuvchi},{self.ism},{self.familiya},{self.email}"

class Sotuv(Shaxs):
    def __init__(self,meva,kiyim,avto):
        self.meva = meva
        self.kiyim = kiyim
        self.avto = avto

    def get_info(self):
        return f"{self.meva},{self.kiyim},{self.avto}"

sotuv = Sotuv('Olma','shortik','Malibu')

class Admin(Foydalanuvchi):
    def __init__(self, name):
        self.name = name
    def ban_user(self):
        print("Foydalanuvchi bloklandi")

admin = Admin("Admin")
admin.ban_user()