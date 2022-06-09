# Global Variables
glbvariable = 10

def func():
    global glbvariable
    glbvariable = 20
    print(glbvariable)

func()
print(glbvariable)


# Local Variables
x = 'global'

def fun():
    x =20 # local Variable
    print(x)

fun()
print(x)

# NonLocal
def outer():
    j = 10
    def inner():
        nonlocal j
        j = 20
    inner()
    print(j)

outer()