# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# s1 = s1.split(" ")
# s2 = s2.split(" ")

# for val in s1:
#     if val not in s2:
#        print(val)

# for val in s2:
#     if val not in s1:
#        print(val)


# 3.)Wrire a code print the 8th fibanochi number


#---> or

num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)


#n1 = 1
#n2 = 1
#ans = 1+1==>2

#n1 = 1
#n2 = 2
#ans = 1+2==>3

#n1 = 2
#n2 = 3
#ans = 2+3==>5

# ! find the 8th fibanochi number
# num = 8
# n1 = 0
#n2 = 1

# for val in range (num):
# ans = n1+n2
#  n1 = n2
#  n2 = ans
# print(ans)

# ! constructors
# ? eg:2
# * unparametarised constructor
  #class profile:
      #def _init_(self):
          #print("hello world")

# obj = profile()
# obj _init_()

# ? eg:3
# * parametarised constructor
class profile:
    def_init_(self, id, name, age)
     #'print(id,name,age)

obj = profile(1,"pradeep",22)

# ? eg:4
class c1:
    name = "pradeep"
    place = "kadapa"

    def m1(self):
        print()

object =c1()
object.m1()


# ? eg:5
class c1:
  def m1(self):
    name = "pradeep"
    age = "22"
    return name,age
def display(self):
       # ! print(name,age)
       # ! print (self.name,self.age)
       print(self.m1())
# object = c1()
# object.display()

# ? eg:6
# ? to use the variable inisde the constructor in another methods
class class1:
    def_init_(self)
      name = "pradeep"
      email = "pradeepreddy@gmail.com"
      return name,email # error --->cannot use return with constructor

    def display(self):
        print(self._init_())

c1 = class1()
c1.dispaly()

# ! ---> inheritance
# the process of utilising the methods and attributes of parent class
# throught the object of child class it is called as inheritance

# ? 5 types of inheritance
# single inheritance
# multilevel inheritance
# multiple inheritance
# hybrid inheritance
# heirarichal inheritance

# * single inheritance
# ? it has only one parent class and only ome child class
# ? Eg:1
class parent:
    def m1():
        print("iam child class")        
parent.m1()
class child:
    def m2(self):
        print("iam child class")

obj = child()
obj.m1()

! eg:2
class c1:
    def_ init_(self):
        print("i am constructor from parent class")

    class child(c1)
       pass

object =child1()
   pass

object.child1()
# ! constructors
# ? Eg:2
# * unparamentarised constructor
class profile:
    def__init__(self):
        print("hello world")

obj = Profile()
obj.__init__()

# ! Eg:3
class parent:
    name = "sai"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()

# ! Multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(voice):
    def cat_voice(self):
        print("meow")

class parrot(voice):
    def parrot_voice(self):
        print("speak")


all = parrot()
all.dog voice()
all.cat_voice()
all.sound()
all.parrot_voice()

# ? Eg:2
class honda_city:
    def honda_city_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def honda_city_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class civic(amaze):
    def civic_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def civic_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class amaze(Honda_city):
     def amaze_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def amaze_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

# ? Eg:2
class honda_city:
    def honda_city_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def honda_city_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class civic(amaze):
    def civic_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def civic_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class amaze(Honda_city):
     def amaze_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def amaze_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)


class honda (civic):
    pass

honda = honda()
honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
honda.civic_body_specs("white,2000,5.5,8,"hatchback")

# ! Multiple Inheritance
# ? It has multiple parent and 1 child

class while_petrol:
    print("used to Aeroplane")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")

class petrol(while_petrol, Organic_petrol, premium_petrol):
    def defanition(self):
print("Petrols types")

p=petrol()
p.defanition()
p.function ()

# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)

# ? heirarical inheritance
class catagory:
    def cal_name(self):
        print("vegetables")

class Tomato:
    def tomato_specs(self):
        color="black"
        taste = "neutral taste"
        self.display(color, taste)
        
class carrot(catagory):
    def carrot_specs(self):
        color="green"
        taste = "sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = tomato()
t.tomato_specs()
t.weigth("30gms")

# Hydrid inheritance
# ? the combination of above 4 inheritance is called Hydrid inheritance

class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class 3")

class c4(c3):
    def m4(self):
        print("Iam m3 from c4")

class c5(c4):
    def m5(self):
        print("class 4")

class c6(c3, c5):
    def m6(self):
        print("class 4")

obj = c6()
obj.m3()


# ! --------------> Polymorphism

# ? poly - many, morph-->from
# a function which is has the ability to perform more than 1 functionality
# then it is considered to be as poliymorphism




# * ploymorphism in built in functions
# len()----> which is used to find the length of list, tuple,dict etc..
# index()
# max()
# min()
# count()
# pop)()
# and more...

# *polymorphism in operations
# +
# print(8+8)
# print("k +1")
# print([1,2,3]+[5,6])


# *
print (6*7)
l1 =[1,2,3,4]
# *
# print(6*7)
# l1 = [1,2,3,4]
# print(*l1)
# def f1(*args)
# l1= [1,2,3,4]
# print(l1*10)

# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding
#) Tasks
#Write the code for the belwo tasks using function
#!)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'
#2.) Find then 67, is strong number or not
#3.) 11 [1,2,3,4,5,6]
#n=2> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]




        
