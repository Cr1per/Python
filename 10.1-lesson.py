# class Talaba:
#     def __init__(self,ism,familiya,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def get_name(self):
#         return self.ism
#
#     def get_lastname(self):
#         return self.familiya
#
#     def get_age(self,yil):
#         return yil - self.tyil
#
#     def tanishtir(self):
#         return f"Ismim  {self.ism} familiyam {self.familiya}, tug'ilgan yilim {self.tyil}"
#
# talaba1 = Talaba("Olim","Olimov",2000)
# talaba2 = Talaba("Hasan","Husanov",2014)
# talaba3 = Talaba("Anvar","Anvarov",2009)

class Foydalanuvchi:
    def __init__(self,foydalanuvchi,ism,familiya,tyil,email,tel):
        self.foydalanuvchi = foydalanuvchi
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.email = email
        self.tel = tel

    def get_name(self):
        return self.ism

    def get_login(self):
        return self.foydalanuvchi

    def get_lastname(self):
        return self.familiya

    def get_age(self,yil):
        return yil - self.tyil

    def get_email(self):
        return self.email

    def get_tel(self):
        return self.tel

    def tanishuv(self):
        return f"Foydalanuvchi {self.foydalanuvchi}, Ismi {self.ism}, Familiyasi {self.familiya}, Tug'ilgan yili {self.tyil}, Email {self.email}, Telefon raqami {self.tel}"

foydalanuvchi1 = Foydalanuvchi('Olim2585','Olim','Olimov',2015,'Olimolimov2585@gmail.com',991243988)
foydalanuvchi2 = Foydalanuvchi('Husan7894','Husan','Hasanov',2010,'Husanhasanov@gmail.com',991244571)
foydalanuvchi3 = Foydalanuvchi('Anvar1654','Anvar','Anvarov',2011,'Anvaranvarov@gmail.com',991243948)