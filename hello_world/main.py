# ! Critical note
# TODO: Add feature
# ? Question here
# * Highlight this
# // Deprecated code

# * -----------------------------------------------------
# this is the start 

# ? How to print an output 
print("this is python ")

# ? How to take an input 
user_input = input("Enter something: ")
print("The input is:", user_input)

# * -----------------------------------------------------
print("\n")
# * -----------------------------------------------------

# ? What are the data types 
print(type(1))                        # ! int
print(type("hh"))                     # ! str
print(type(True))                     # ! bool
print(type(6.537777))                 # ! float
print(type([1, 2, 3, 4]))             # ! list
print(type((1, 2, 3, 4)))             # ! tuple
print(type({"one": 1, "two": 2}))     # ! dict
print(type(1 == 1))                   # ! bool

# * -----------------------------------------------------
print("\n")
# * -----------------------------------------------------

# ? How to print a variable
my_name = "abdirhman"
print(my_name)

a, b, c = 1, 2, 3
print(a, b, c)

# * -----------------------------------------------------
print("\n")
# * -----------------------------------------------------

# ? What are the reserved words in Python 
# (opens the keywords help menu in Python shell)
import keyword
print(keyword.kwlist)   # cleaner way instead of help("keywords")


# * -----------------------------------------------------
print("\n")
# * -----------------------------------------------------

# ? How can we connect strings 
a = "hi"
b = "Ahmed"
print(a + " " + b)

# ! Better way: store in a variable
full = a + " " + b
print(full)

# * -----------------------------------------------------
print("\n")
# * -----------------------------------------------------

# ? Let's learn about strings 
my_string1 = 'in this way'
my_string2 = "in this way"

print(my_string1)
print(my_string2)

# * -----------------------------------------------------
print("\n")
# * -----------------------------------------------------

# ? how to do a String manipulation  
string = "hi there i love to learn python"

# Accessing characters by index
print(string[0])   # h
print(string[1])   # i
print(string[2])   # space
print(string[6])   # e
print(string[-1])  # the last character (n)
print(string[-12]) # (l) from left 

# Slicing
# [start:end:steps]

print(string[0:2:])     # hi
print(string[3::])      # there
print(string[-1::])     # last character
print(string[3:-25:2])   # teei 

# Getting length
# function is [len]

first_tray  = "i love python"
second_tray = "       i love python       "

print("the  length of the string is :" ,len(first_tray),"\n")

print("the  length of the string is :" ,len(second_tray),"\n")

# how to remove space
#**.strip()** Removes whitespace from both ends (left & right)

#**.rstrip()** Removes whitespace only from the right side (end)

#**.lstrip()** Removes whitespace only from the left side (start)

print(string.strip())
print(string.rstrip())
print(string.lstrip())

# title 
#** .title() ** string method makes the first letter of each word uppercase and the rest lowercase
print(string.title())

# * -----------------------------------------------------
print("\n")
# * -----------------------------------------------------

a = "I love python and c++"

# split() → breaks string into list by spaces (default)
print(a.split())         # ['I', 'love', 'python', 'and', 'c++']

# rsplit() → same as split but from the right (can limit number of splits)
print(a.rsplit(" ", 2))  # ['I love python', 'and', 'c++']

# Checking the type
print(type(a))           # <class 'str'>

# Correct way to find length
print(len(a),"\n")            # length of string = 20
print(len(a.split()))    # length of list after split = 5
