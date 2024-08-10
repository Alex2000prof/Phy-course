#lambda

#not effective
fruits = ["apple","banana","pear","apricot",]
new_fruis = []
for fruit in fruits:
    new_fruis.append(fruit.upper())
print(new_fruis)

#using method map
def upper_string(s):
    return s.upper()
fruits_upper = map(upper_string, fruits)

#using lambda

fruits_upper = map(lambda f: f.upper(),fruits)

