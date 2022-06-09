def show(text):
    return text.upper()


def display(func):
    text = func("hii, i am awesome")
    print(text)

print(show("hii"))

# displayvar = show
# print(displayvar("hello"))
display(show)


def helloDecorators(func):
    print("b4 execution")
    def inner(*args,**kwargs):
        value = func(*args,**kwargs)
        print("after exection")
        return value
    return inner

@helloDecorators
def sum_two_num(a,b):
    print(a+b)

sum_two_num(10,20)