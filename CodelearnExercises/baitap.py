#Hello
def say_hello(name):
    print("Hello", name)

#Total
def total(a,b):
    print(a+b)

#Operation
def Operation(a,b):
    print(f"{a} + {b} =",a+b) #f 'str'/"str" với giá trị biến được gán trong {}.
    print(f"{a} - {b} =",a-b)
    print(f"{a} * {b} =",a*b)
    print(f"{a} / {b} =",a/b)

#Variables and type of variables 
def variables():
    a = 5
    b = 3.14
    c = "Hello"
    d = True
    e = [1, 2, 3]
    f = (1, 2, 3)
    g = {1: "one", 2: "two"}
    h = None

    print(type(a)) #int
    print(type(b)) #float
    print(type(c)) #str
    print(type(d)) #bool
    print(type(e)) #list
    print(type(f)) #tuple
    print(type(g)) #dict
    print(type(h)) #NoneType

#input
def greet():
    print(f"Hello {input("Enter your name:" )}")
 
#input2
def Information():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"In 15 years, age of {name} will be {age + 15}")

