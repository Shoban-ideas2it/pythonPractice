from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name)
        print(age)

    @classmethod
    def get_age(cls,name,year):
        return cls(name, date.today().year - year)

    @staticmethod
    def get_name(age):
        return age

obj = Person("Ravi",22)
print(obj.get_name(22))
obj.get_age("Ravi",1996)