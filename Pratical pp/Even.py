# python  program to print sum of Even numbers upto n in for loop 

# num = int(input("  Enter the  Value : "))
# total = 0

# for number in range(1, num+1):
#     if(number % 2 == 0):
#         print("{0}".format(number))
#         total = total + number

# print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, total))


# Python Program to  Sum of Even Numbers upto n 
 
num = int(input("  Enter the num Value : "))
total = 0
number = 1
 
while number <= num:
    if(number % 2 == 0):
        print("{0}".format(number))
        total = total + number    # 0=0+1=1  1=1+1=2  
    number = number + 1            #2+1=3 3=3+1=4

print("The Sum of Even Numbers from uto n = {0}".format(total))