#Functions contains set of statements of code in a block. we can use same set of functions statements anywhere by just calling the function

#defining and calling a function

#defining#
def function():
    print("hi")

#calling
function()

#Add 2 numbers using functions
def fun(a,b):
    print(a+b)

#a,b are parameters or arguments and we are giving values while calling the function
fun(2,3)

#add and sub two numbers
def fun1(a,b):
    return a+b,a-b
result = fun1(4,5)
print(result)

#Function arguments >> Immutable object as arg >> Immmutable obj will create a new variable and memory address to store them instead of updating original value
def update(a):
    print(a)
    print(id(a))
    a = 10
    print("value of a after update",a)
    print(id(a))
update(8)

#Mutable obj as arg >> Mutable obj will update the original value and won't create new variables
def update1(spam):
    print(spam)
    print(id(spam))
    spam[1] = -3
    print(spam)
    print(id(spam))

spam = [1,2,4]
print(spam)
print(id(spam))
update1(spam)
print(spam)
print(id(spam))

#Types of arguments in python
#Formal and Actual arguments

def add(a,b):#formal arguments
    print(a+b)
add(5,7)#actual arguments

#position, keyword, default and variable length are different types of Actual arguments
def person(name,age):
    print(name)
    print(age)
person('sree',22)#position arguments in which the arg value will be inserted

person(age=23,name='man')#keyword(age,name) is used