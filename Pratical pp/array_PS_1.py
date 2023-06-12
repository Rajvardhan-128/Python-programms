# WAP to take input from the user by using funtions catergories them as even number or odd number separate in array?
# (Whether the catergoried even , odd number can generate 
#                        even or odd array as well)

# from array import *
# def evena(even,n):
#     if(n%2==0):
#         even.insert(n)
#         print("Number is even")
# def odda(odd,n):
#      if(n%2==0):
#         odd.insert(n)
#         print("Number is odd")
        
# n=input("Enter the value :")
# even=array('i',[])
# odd=array('i',[])
# evena=(even,n)
# odda=(odd,n)

# from array import *
# def evena(even,n):
#     if(n % 2 == 0):
#         even.append(n)
#         print("Even number is:",n)
# def odda(odd,n):
#      if(n%2 != 0):
#         odd.append(n)
#         print("odd number is",n)
        
# even = array('i',[])
# odd = array('i',[])
# # for i in range(5):
# # while()
# m=1
# while(m is 1):
#     n = input("Enter the number to check it it Even or odd:")
#     evena(even,n)
#     odda(odd,n)
#     m=input("Enter the value :")
# print("Even numbers are :")
# for i in even :
#     print(i)
# print("odd numbers are :")
# for j in odd :
#     print(j)

from array import *

def evena(even, n):
   if(n%2 ==0):
     even.append(n)
     print(n,"is even number")
def odda(odd,n):
   if(n%2 != 0):
     odd.append(n)
     print(n,"is odd number")
odd = array('i',[])
even = array('i',[])
m =1
while(m == 1 ):
 n = input("enter the number to check it is even or odd")

 evena(even,n)
 odda(odd,n)
 m = input("enter 1 to try another number")
print("even list:")
for i in even:
  print(i)
print("odd list:")
for j in odd:
  print(j)