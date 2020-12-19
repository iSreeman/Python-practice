#python relies on indentation. Be careful with the indentation

#1
a = 20
b = 30
if a<b:
    print("a is smaller than b")

#elif
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#else
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("a is smaller than b")

#Short Hand If
if a < b: print("a is not greater than b")

#short hand if-else
print(a) if a>b else print(b)

#Ternary Operator or Conditional expressions
print(a) if a > b else print("=") if a==b else print(b)

#And keyword
a = 3
b = 6
c = 34

if a<b and c>b:
    print("true")

#nested if
p = 54
if p > 10:
    print("above 10")
if p > 60:
    print("and Above 60")
else:
    print("above than 30")

#pass statement
a = 2
b = 8

if a>b:
    pass