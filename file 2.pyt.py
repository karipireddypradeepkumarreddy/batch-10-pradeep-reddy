a, b=c=7,8
print(a)
print(b)
print(c)

a=b,c, = 4,2
print(a,b,c)

#--->swapping of variables
a=7
b=5
print(a,b)

# Eg:1
# temp=a #temp=7
#a=b   #a=5
#b=temp#b=7

##a=5,b=7
#print(a,b)

#Eg:2
#a=a+b #a=12
#b=a-b #b=12-7=5
#a=a-b #a=12-5=7

#print(a,b)

# a, b=b, a # only in python
# print(a,b)

a=a*b #a=35
b=a/b #b=35/7=5.0
a=a/b #a=35/5=7.0
print(int(a),int(b))

# id()-->used to find the memory address of the variable
# a = 7
# b = 8
# print(id(a))
# print(id(b))

#--->keywords
# keywords are reserved words which provides special meaning to
# compiler or interpretor

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))


# To check if the string is keyword or not
print(keyword.iskeyword("isd")) # false

# if = 8
# print(if) # error coz if is a keyword

# !---> literals
# literal is the constant value assigned to a variable
# A variable is considers to be constant when it is defines
# in caps

#a= 78 # a is variable
# A=78 # A is constant

# hash()---> it creates a hash value for constant datatypes and
# provides error for non constant datatypes
n1 = 89+7j
print(hash(n1))

f1 = [7,8,9]
print(hash(f1)) # error --> list is non-constant or mutable datatype

# a = 9
# b = 9
# b = 90
# print(id(a))
# print(id(b))

# !--->operators
# ? operators are symbols which is used to perform various opearions
# ? between 2 or more operands

# arithmatic
# assignment
# logical
# relational or comparison
# bitwise
# identity
# membership

# todo--->arthmatic-->+,-,*,/,%,//,**
# Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c)

# input()-->used to get the runtime input
# eval()--->used to get the runtime values of all data type

n1 =input("enter the value:")
print(type(n1))

a = 4
b = 2
# print(a/b) # is used to get the quotient value
# print(a%b) # is to get the remainder value

# ! // ---> floor devision

# a = 765433
# b = 19
# print(a/b) # --> the output will be inn integer and the output will be
# based on floor value

#! **-->used for power of a number
# print (2**4) # -->16
# ! assignment -->+-=,-=,*=,/=,//=,**=,&=,|=

# a = 8
# a+= 2
# print(a)

# a=30
# a-=5
# print(a)

# ! comparsion -->==,>,<,!=,<=,>=
# a = 8
# b = 7
#print(a>b) # true

# a = 9
# b = 5
# print(a==b)

# ! bitwise operator---> &,|,^,~,<<,>>
a = 7
b = 4
print(a&b)

# 2^4 2^3 2^2 2^1 2^0
# 8   4   2   1

# 0   1   1   1   #--->7
# 0   1   0   0   #--->4&
#----------------------
# 0   1   0   0

# 256 128 64 32 16 8 4 2 1
#  0   0   0  0  0 1 0 0
# ! bitwise operator --> &, |, ^, ~, <<, >>
a = 7
b = 4
print(a&b)

# and
# a b a&b
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

# or
# a b a|b
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1


# 2^4 2^3 2^2 2^1 2^0
# 8    4    2    1

# 0    1    1    1     # --> 7
# 0    1    0    0     # --> 4 &
# -----------------------
# 0     1    0    0

#  ~ --->
# a = 9876
# print(~a)

# a = 9

# 128 64 32 16 8 4 2 1
#  0   0  0  0 1 0 0 1 # -->  9

# 1     1  1  1 0 1 1 0 # --> -10

# 0  0  0  0  1  0 1 0 --> 10

# 1 1 1 1 0 1 0 1  -> 1s compliment of 10
              # 1  -> 2s compli,ent
# ---------------------------
# 1  1  1  1  0  1  1  0 --> -10

# 256 128 64 32 16 8 4 2 1
#  0   0   0  0  0 0 1 0 1   3<<
#  0   0   0  0  0 1 0 0 0 --> 40
# 107

# <<, >>
# print(5>>1)
# 16>4

# ! logical --> used to compare the expressions
# and, or, not
a = 6
# print(a>3 and a<10)
# print (a>7 or a<30)
print(not(a>8 and aaaaaa,10))

#! Identity operator
# is, is not
a = 8
b = 8
print(a is b)
print(a==b)

# a = [1,2,3]
# b = [1,2,3]
# print(a is  not b)

# ! membership operator
# in, not in

# |1 =[7,8,9,0,6,5]
# num = 55
# print(num in |1)
# print(num not in |1)

# num  = 678
# print(8 in num) # error

#! conditional statement
# if ,else,elif

#eg:1
# --->csyntex
# if (condition){
     #stament;
     #stament;
     #stament;
#}
# python syntex
# if condition:
     #stament;
     #stament;
     #stament;
#stament
    
# eg:1
# a= 6
# if a:
#     print("hello")

# eg:2
a = 6
if a>3:
    print("hey")
 elseprint("no")
#eg:3
     if 7>8:
         print("hello")
 else:
     print("no")

 # eg:4
 # a =0
 # a = none
 # a= false
 # a =""
 # if a:
 #    print("yes")
 #else:
      print("no")
      
 # a number is even or odd
 # n=int(input(enter the number:))
 # if n% 2==0:
 #sum: 2
 # name, age,nationality
 # 18 above, indian

 
name = input("enter the name: ")
age = int(input("enter the age:"))
nationality=input("enter the nation")

if age>=18 and nationality=="indian":
    print("eligible for vote")
else:
    print("not eligible")














































