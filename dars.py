# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#
#     def __init__(self, make, model, rang, yil, narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
#
#     def __repr__(self):
#         return f"Avto: {self.make} {self.model}"
#
#     def __eq__(self, y):
#         return self.narh == y.narh
#
#     def __lt__(self,y):
#         return self.narh < y.narh
#
#     def __le__(self,y):
#         return self.narh <= y.narh
#
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
#
#
# class AvtoSalon:
#     """Avtosalon klassi"""
#
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []
#
#     def __repr__(self):
#         return f"{self.name} avtosaloni"
#
#     def __len__(self):
#         return len(self.avtolar)
#
#     def __getitem__(self, index):
#         return self.avtolar[index]
#
#     def __setitem__(self, index, value):
#         if isinstance(value, Avto):
#             self.avtolar[index] = value
#
#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyketini kiriting")
#
#     def __add__(self, qiymat):
#         if isinstance(qiymat, AvtoSalon):
#             yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
#         elif isinstance(qiymat, Avto):
#             self.add_avto(qiymat)
#         else:
#             print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")
#
#     def __call__(self, *param):
#         if param:  # agar parametr bo'lsa
#             for avto in param:
#                 self.add_avto(avto)
#         else:  # agar parametr bo'lmasa
#             return [avto for avto in self.avtolar]
#
# salon1 = AvtoSalon("MaxAvto")
# salon2 = AvtoSalon("Avto Lider")
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)
# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)



class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, yosh):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.yosh = yosh


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, yosh, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, yosh)
        self.idraqam = idraqam
        self.bosqich = 1


    def __repr__(self):
        return (f"\n\nIsmi {self.ism}, Familiya {self.familiya},"
                f"\nPassporti {self.passport}, Yoshi {self.yosh}, \nID raqami {self.idraqam}")

    def __eq__(self,y):
        return self.bosqich == y.bosqich

    def __lt__(self,y):
        return self.bosqich < y.bosqich

    def __le__(self, y):
        return self.bosqich <= y.bosqich

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

class Fan:
    talabalar = []
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalari = []

    @classmethod
    def add_student(cls,talaba):
        return cls.talabalar.append(talaba)

    def get_nom(self):
        return self.nomi

    def __getitem__(self, item):
        return self.talabalar[item]

    def __setitem__(self, key, value):
        if isinstance(value,Talaba):
            self.talabalar[key]=value

    def __len__(self):
        return len(self.talabalar)

    def __add__(self, other):
        if isinstance(other, Fan):
            yangi_talabalar = Fan(f"{self.nomi} {other.nomi}")
            yangi_talabalar.talabalar = self.talabalari + other.talabalar
            return yangi_talabalar
        elif isinstance(other, Talaba):
            self.add_student(other)
        else:
            print(f"guruhga {type(other)} qo`shib bo`lmaydi")
    @classmethod
    def remove_student(cls, identifier):
        cls.talabalar = [student for student in cls.talabalar if student.id != identifier and student.passport != identifier]

    @classmethod
    def __repr__(cls):
        return f"Talaba({cls.talabalar})"

fan1 = Fan('Tarix')
fan2 = Fan('Algebra')
fan3 = Fan('informatika')

talaba1 = Talaba("Ibrohim","Avazov","TN2146685",15,"ID:15498515588")
talaba2 = Talaba("Abdumalik","Samikjanov","TN2588549",16,"ID:15498525588")
talaba3 = Talaba("Hojiakbar","Mansurov","TN2145685",15,"ID:15498515898")
talaba4 = Talaba("Suxrob","Xudoyberdiyev","TN2146689",15,"ID:15898515588")
talaba5 = Talaba("Asilbek","Nasriddinov","TN2147785",16,"ID:15488515588")
talaba6 = Talaba("Bobur","Asadullayev","TN2186685",16,"ID:25498515588")
talabalar_g = [talaba1,talaba2,talaba3]
talabalar_g2 = [talaba4,talaba5,talaba6]
Fan.add_student(talaba1)
Fan.add_student(talaba2)
Fan.add_student(talaba3)

index = Fan.__getitem__(fan3,1)
set = Fan.__setitem__(fan1,0,talaba1)
uzun = Fan.__len__(fan3)
students = Fan.__add__(fan2, talaba2)


print(Fan.talabalar)
print(Fan.get_nom(fan3))
print(set)
print(uzun)
print(students)



