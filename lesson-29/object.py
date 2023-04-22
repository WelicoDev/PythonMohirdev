class Student():
    def __init__(self , first_name , last_name , age , study , course , profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.study = study
        self.course = course
        self.profession = profession

    def name(self):
        return  self.first_name

    def last_name(self):
        return self.last_name

    def age_year(self, year):
        return year - self.age

    def welcome(self):
        return  f"Assalom aleykum {self.first_name} {self.last_name} yoshingiz {self.age} . "

talaba = Student("Otabek" , "Xurramov" , 19 , "" , "TUIT" , 2)


class Fan():
    """Fan nomli class"""
    def __init__(self , name):
        self.name = name
        self.numbers = 0
        self.students = []

    def add_student(self , student):
        """Fanga talabalar qo'shish"""
        self.students.append(student)
        self.numbers+=1
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return  [x.welcome() for x in self.students]

matematika = Fan("Oliy Matematika")
talaba1 = Student("Islom" , "Haydarov" , 20 , "Temiryollar" , 2 , "aviatsiya")
talaba2 = Student("Javohir" , "Namazov" , 20 , "Temiryollar" , 2 , "aviatsiya")
talaba3 = Student("Suxrob" , "Qodirov" , 20 , "Temiryollar" , 2 , "aviatsiya")

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

matem = Fan("Oliy Matematika")
matem.add_student(talaba)
print(matem.students[0].first_name)
print(matematika.get_students())
print(dir(Student))


