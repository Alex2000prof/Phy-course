#List array
#Can hold any type of 
#Mutable - can be changed

a_list = []

print(type(a_list))

a_list = [1,2,3,4,5,6,7,8]

first_value = a_list[0]
print(first_value)

#Slicing
sub_list = a_list[0:4]
print(sub_list)

sublist_b = a_list[len(a_list)//2:len(a_list)]
print(sublist_b)

b_list = ['a','c',2]
b_list.remove(2)
b_list.pop() #remove last elemet
print(b_list)

