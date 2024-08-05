list1 = [31,32,7,43,34,56,74,68,9]
numbers = range(0,10)
numbers = list(range(0,len(list1)))
print(numbers)
for i in range(0,len(list1)):
    list1[i] *= 10
print(list1)

