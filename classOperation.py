class Base:
    def func(self):
        print("Pubic Method")

    def __func(self):
        print("Private Method")

class Child(Base):
    def funct(self):
        super().func()

    def call_private(self):
        super().__func()


obj = Child()
obj.funct()
# obj.call_private()


# Name mangling
obj1 = Base()
obj1._Base__func()