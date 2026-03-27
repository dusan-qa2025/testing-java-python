

def welcome_message(name):
    print("Hello", name)


# zadatak
name = "Veljko"
age = 24
message = f"Hello{name}, you are {age} years old"
print(message)

def addition (a, b):
    print(a+b)
addition(5, 10)

def addition (a, b):
    print(a + b)
addition(a=20, b=25)

def student_info(name, points=0):
    print(f"Name: {name}, points on test: {points}.")
 
student_info("John")
student_info("Peter", 90)

def myltiply(a, b):
    return a * b 
result = myltiply(10, 5)
print(result)

def to_square(x):
    y = x * x
    return y
nbr = 5
result = to_square(nbr)
print('Result of square function is: ', result )

def f_one():
    pass
def f_two():
    pass
def f_three(f):
    print(id(f))

t = (f_one, f_two, f_three)
for i in t:
    print("Function:", i.__name__)
    print("Object is instance of object:", isinstance(i, object))
    print("Id:", id(i))

f_three(f_one)


def addition(*arguments):
    s = 0
    for i in arguments:
        s += i 
    return s 
print("Addition:", addition(2, 1, 3))

def addition(**arguments):
    for i in arguments:
        print("Key:",i, "Value:", arguments[i])
addition(a=2,b=1,c=3)


def func(y):
    y[0] = y[0]**2

x = [5]
func(x)
print ("X now holds the value of: ", x[0])


a = 5 # promenljiva koja se vidi u celoj skripti (globalna)
  
def f(): 
    a = 10
    print(a) 
 
print(a) 

a = 5
  
def f(): 
    global a 
    a = 10
    print(a) 
  
print(a) 
f() 
  
print(a)

def func_example(i):
    print(i)
    i -= 1
    if i > 0:
        func_example(i)
 
func_example(5)