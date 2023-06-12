#write a python program to print sum of odd numbers upto n?
 
maximum = int(input(" Please Enter the Maximum Value : "))
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 1):
        print("{0}".format(number))
        total = total + number

print("The Sum of odd Numbers from 1 to {0} = {1}".format(number, total))