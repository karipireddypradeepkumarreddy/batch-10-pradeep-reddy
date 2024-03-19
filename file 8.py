# ! Eg:3
def profile(name, age, place):
    txt ="My name is {}. Iam {} years old.Iam from {}."
    print(txt.format(name, age, place))
profile("k.pradeep kumar reddy",22, "KSRM")

# ! Eg:4
# ? Function with return statement

# ! return
# 1.)a variable declared inside the function can be accessed outside of the function
# using return
# 2.)return does not print anything
# 3.)we cannot write any code below return statement

def f1():
    z = 8
f1()
print(z) # error --> cannot use outside the function

def f1(a, b):
    c = a*b
    return c
# print(f1(6, 8)
obj = f1(6, 8)
obj1 = f1(4, 6)

def gracemark(object):
    print(object+4)    
gracemark(obj)
gracemark(obj1)

# ? problem:1
def palindrome(n):
    string = sttr(n);
    rev =str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a = int(input("enter the value"))
palindrome(a)

# ? based on the declaration of parameter and args
# ? functions are divided into 5 catagories

# positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# * positional args
#eg:1
def profile(name,phone,mark):
    txt = "my name is {},my phone number is {},i got {} marks."
    print(txt.format(name,phone,mark))

profile(9182355711,"k.pradeep kumar reddy",99) # unexpected output

# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "k.pradeep kumar reddy", mark=99, phone(9182355711)# Error--->positional arg follow keywords

# profile(9876543210,name= "k.pradeep kumar reddy", mark=99) # error---->name has muliple values

profile("k.pradeep kumar reddy",mark=99,phone=9182355711)

# * default args
# the method of assigning the argument to the parameter while declaring the
# function
# ! eg:2
def profile(name, phone, place):
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))

# profile("k.pradeep kumar reddy",9182355711,kothanellore))

# Problem statement  Given a string S(input consisting) of ,* and #’. 
# The length of the string is variable. The task is to find the minimum number of * 
or #’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and #’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of * 
and # in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   # number of * and # are equal

profile(name, phone, place="kadapa"):
    if place |="kadapa" or place |= "kadapa" or place=="kadapa":
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))
else:
    print("you are not eligible to signup")
profile("k.pradeep kumar reddy",9182355711)

def profile(name, place="kadapa",phone): # error --> coz default args should not follow
                                         # positional param
    if place |="kadapa" or place |= "kadapa" or place=="kadapa":
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))
else:
    print("you are not eligible to signup")
profile("k.pradeep kumar reddy",9182355711)

# * variable length prams
# ! eg:1
# to pass more then 1 argto a paremeter means we use variable length args
# to convert normal parameter to variable length params add * to their prefix of param
# name = "pradeep"

def profile(*name):
    print(:my name is ,name)
profile("k.pradeep kumar reddy",'name2','name3')

name ="k.pradeep kumar reddy,'name1','name2')

def profile(*name):
    print("My name is ",name)
profile("k.pradeep", 'name2', 'name3')


# ! Eg:2
# n = 12`
# ! Eg:2

def profile (*name, age):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile("pradeep", 'name2', 'name3', 22) # error --> age has no args


'''
        
def profile (age,*name):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile(22, "pradeep", 'name2', 'name3')

# *keyword variable lengh args
# kwargs --> which is used to provide the args in the form of key value pair.
# ! Eg:1
# def price(price_list):
#     print(price_list)

print(shirt=1000, iphone=80000)

# n=5
# {1:1,2:4,3:9,4:16,5:25}

n =int(input("enter the number:"))
d1 ={}
for val in range(1, n+1)
     d1[val] =val**2
print(d1)
def dict(n):
dict(5)

# !------->object oriented programming
# the paradigms of objects oriented programming are
# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# ? eg:1
# class c1:
#     name = "k.pradeep"
#     print(name1)

# ?eg:2
# class person:
#    name = "k.pradeep"

# c=person() # c as object
# the process of creation of an object is called as instantaiation
print(c.name)

# ? Eg:3
# create of amethod
# when the function is created with aclass is called as method

class person:
    def display(person):# it is a method
    print("hello welcome to classes")

p = person()
p.display()

# ? eg:4
# ! method with parameter
#class person:
#  def display(person,name,age):
#       print(name,age)

#p = person()
#p.display("k.pradeep",22)

# ! eg:5
class person:
   name = "pradeep" #attribute or static variable
   lname = "T"

   def first_name(self):
        print(self.fname3)
        
   def full_name(self):
       print(self.fname+" "+self.lname)
       
p = person()
p.display()
p.full_name()

# ? eg:6
# constructors --->_init_()
# this is a special method which has the ability to exccute it'self without
# calling it manually through the process of instantiation


class profile:
   def _init_(self):# constructor method
       print("hey")

p = profile()
p.d1()
       
# d1 = {"a":100, "b":200, "c":300}
# d1 = dict{a=100, b=200, c=300}
# print(d1)



