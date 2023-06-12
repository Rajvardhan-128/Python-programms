from array import *
# import array as arr
# 1>
# numbers =arr.array('i',[10,20,30,40])
numbers =array('i',[10,20,30,40]) #---> for  eg 6>

# print(numbers)

# 2> print specific position if array
# print(numbers[3])

# 3> calculate the length of array
# print(len(numbers))

# 4> Display the index of that element
# print(numbers.index(20))

# 5> Array in for loop 
# for i in range(5): 
# # for i in range(len(numbers)):  ---> Also we can written in this type
#     print(numbers[i])

# 6>
newarr =array(numbers.typecode,(a*a for a in numbers))
# for e in newarr:
#      print(e)

# 7> while loop
i=0  #--->initilize
while i<len(newarr): #--->check the condition
    print(newarr[i]) #---> set the increment , decrement
    i+=1

# >---->---->---->---->---->---->---->
# vals = array('i',[3,5,6,8,-10,12])
# vals.reverse();
# print(vals.reverse())
#  buffer_info ---> telling the address & size of array 