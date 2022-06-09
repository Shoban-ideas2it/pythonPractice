from abc import ABC, abstractmethod, abstractproperty

class AbstractSample(ABC):
    @abstractmethod
    def show(self):
        pass

    


class SubClass(AbstractSample):
    def show(self):
        print("abstract method")



# obj = SubClass()
# obj.show()

# class A:
#     def do_thing(self):
#         print('From A')

# class B(A):
#     def do_thing(self):
#         print('From B')

# class C(A):
#     def do_thing(self):
#         super().do_thing()
#         print('From C')

# class D(B, C):
#     pass

# d = D()
# d.do_thing()

# c = C()
# c.do_thing()