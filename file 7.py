# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

d1={'Ten':10,'Twenty':20,'Thirty':30}
# d2={'Thirty':30,'fourty':40,'fifty':50}
# d1.update(d2)
# print(d1)

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag=0
for val in range(3):
    c=c+1
    if c==1:
       for val in set1:
           if val in set2 or val in set3:
             flag=1
             break
    if c==2:
       for val in set2:
           if val in set1 or val in set3:
             flag=1
             break
    if c==3:
       for val in set3:
           if val in set2 or val in set1:
              flag=1
              break
#if flag==0:
    print("disjoint")
#else:
    print("joint")

# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
l3 = []
for val in range(len(list1)):
    ans = list1[val]+list2[val]
    l3.append(ans)
#print(13)

# ? or

# i=0
# while i<len(list):
#     13.append(list[i]+list[i])
#     i+=1
#     print(13)
# hacker renk---> caesar cipher

# ! functions
#? DEF
# function is a block of code which is used to perform a specific fumvtionality
# function can be created using def keyword

# ? function has 3 parts
# function declaration
# function defanition
# function call

def greet():
    print("greetings user! !")
    
greet()
greet()
greet()
greet()
greet()
greet()
greet()# function calling
      


# O/P --> ['My', 'name', 'is', 'Kelly']a


7
