# ---->while loop
#-----> break using while loop

# eg:1
#1.) iterate form 20 to 30 and break the loop in 27
i = 20
while i<31:
    if i== 27:
        break
    print(i)
    i+=1
# 2.)
i = 20
while i<31:
    print(i)
    
    if i == 27:
        break
    i+=1

# 3.)
i =20
while i<31:
    print(i)
    if i==27:
        break
    i+=1

# !--->continue
#--->eg:1
# i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1
# 1eg:5
#while to iterate from 12 to 22
#3find the sum of all numbers

i = 12
while i<23:
    sum=0
    sum=sum+i
    print(sum)
    i+=1
    print(sum)

# eg:6
# find the average of value from 20 to 25

i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
    print(sum/count)

    
for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row, col)
        
# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *

for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()

#i=int(input("Enter the number of rows: ")
#j=int(input("Enter the number of cols: ")


for row in range(rows):
      for col in range(col):
      #print("*", end=" ")
   # print()

#sum = 0
#for row in range(5):
      #for col in range(5):
      #sum=sum+1
      #print("row", end=" ")
    #print()    
        
# ! to print stars in right angled triangle

#for row in range(0, 6):
#for col in range(0, row+1):
#print("*", end=" ")
#print()

# * * * * * *
# * * * * *
# * * * * 
# * * *
# * *
# *
      
rows = 6

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\n")

#*****
#*   *
#*   *
#*   *
#*****

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()
    
    
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#      *
#    * * *
#   * * * *
#  * * * * *

rows = 9

for i in range(rows):
    print(" " * (rows - i - 1), end='')  
    print("*" * (2 * i + 1), end='')    
    print(" " * (rows - i - 1))


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *

for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
# ?--> list

# 1.) if the collection of elements are surrouneded by square brackers, it is considerd
# to be list
# ! eg:
# 11=[4,7,9,"hello",7+9j,[8,9,0]]

# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# to access the elements in  list
lst1=[1,4,1,7,89.7,7.5,"p","i"]
# print(lst1)

#--->indexing
#the colllection datatypes like list, tuple, string, the elements will be alloted
# with peredefines unique value called index value

# we have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# negative indexing -- starts with -1 from right hand side

# positive indexing
# lst1 =[1,4,7,7.5,"p","i"]
print(ist1[0])
print(ist1[4])
print(ist1[20])--> error

# ? ---> Negative indexing
#lst1 = [1,4,1,7,89.7,7.5,"p","i"]
#print(lst[-1])
#print(lst[-5])

# ? ------> slicing
lst1 = [1, 4, 7, 8, 7.5, "p","i"]
# lst1[start_index:end_index:step]

# print(lst1[0:4])
# print(lst1[6:8])
# print(lst1[3:6])
#print(lst1[:5])
#print(lst1[:3])
#print(lst[:])

#print(lst[0:7:1])# lst[0.7]-->both are same
#print(lst1[0:7:2])

# trail = int(input())


lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1[-4:-1])       
print(lst1[-1:-4]) --> []
print(lst1[-7:-1])
print(lst1[-7:1:2])

'''
