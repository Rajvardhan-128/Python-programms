# WAP to print even numbers upto n ?

maximum = int(input(" Please Enter the Value : "))
total = 0

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))