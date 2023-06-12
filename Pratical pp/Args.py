# Date - 3-10-22

from this import *


# Q1- Arbitary arguments funtion 

def display(*n):
    print("Name is:",n[2])
display("DYP","DYPCET","CSE")


# Q2- Keyword Arguments :

def display(n1,n2,n3):
    print("Name is:",n2)
display(n1="DYP",n2="DYPCET",n3="CSE")

# Q3- Keywords Arbitary Arguments (**Kargs)

def display(**n):
    print("Name is:",n["lname"])
display(fname="DYP",lname="DYPCET",branch="CSE")
  