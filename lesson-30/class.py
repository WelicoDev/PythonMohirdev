# author : welico_developer

class Shaxs():
    """Shaxslar haqida ma'lumot"""
    def __init__(self, first_name , last_name , passport , birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.passport = passport
        self.birtday = birthday

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.first_name} {self.last_name}"
        info+= f" Passport : {self.passport} , Birthday : {self.birtday}-yilda tig'ulgan !"
        return info
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi method"""
        return yil-self.birtday

class Student(Shaxs):
    """Talaba classi"""
    def __init__(self , first_name , last_name , passport , birthday , idnumber , course , adress):
        """Talabaning xususiyatlari"""
        super().__init__(first_name , last_name , passport , birthday)
        self.idnumber = idnumber
        self.course = course
        self.adress = adress

    def get_id(self):
        """Talabaning ID raqami """
        return  self.idnumber
    def get_course(self):
        """Talabaning bosqich tartibi"""
        return  self.course
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.first_name} {self.last_name} >> Idnumbers : {self.idnumber}"
        info += f" Passport : {self.passport} , Birthday : {self.birtday}-yilda tig'ulgan ! , Course : {self.course}"
        return info

class Adress:
    """Manzilni saqlash uchun class"""
    def __init__(self , uy , kocha , tuman , viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_adress(self):
        """Manzilni ko'rish"""
        adress = f"{self.viloyat} viloyati , {self.tuman} tumani"
        adress+= f" {self.kocha} ko'chasi , {self.uy}-uy ."

        return adress



student = Student('Javohir' , 'Namazov' , 'AC1239876' , 2003 , 545693560503 , 2 , 'Termiz')
print(student.get_course())
people = Shaxs('Otabek' , 'Xurramov' , 'AD0037390' , 2004)
print(people.get_info())
print(people.get_age(2023))
print(student.get_age(2023))
print(student.get_info())

student_adress = Adress(66 , 'Mustaqillik' , 'Angor' , 'Surxondaryo')
student = Student('Javohir' , 'Namazov' , 'AC1239876' , 2003 , 545693560503 , 2 , student_adress)
print(student.adress.get_adress())

