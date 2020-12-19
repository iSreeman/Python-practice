# Immutable data types - (Numbers, Strings, Tuples)
# Mutable Data types - (Lists, Dictionaries, Sets)

#Numeric datatypes - Int, Float, complex, Boolean#

#Strings

a = "Hello Python"
b = "Hi"

print(a," ",b)

#multi-line strings

text = """This is a multi line text where we can add paragraphs"""

print(text)

#Strings as Arrays to access elements of an array
print(a[4])

#String Slicing
print(text[0:7])

#Negative Indexing
print(text[-20:-15])

#length
print(len(text))

#methods
print(a.lower())
print(a.upper())
print(a.strip())
print(b.replace('i','e'))
print(a.split(","))

#Check String is present or not
x = "where" in text
print(x)

y = "where" not in text
print(y)

#Concatenation
p = "Test"
q = "Concatenation"

r = p+" "+q

print(r)
print(format(a+" "+b))

test = "we are about to {}"
print(test.format(r))

#There are many String methods which can be used based on the requirement

# We also have escape character to make the illegal strings to print without any exceptions