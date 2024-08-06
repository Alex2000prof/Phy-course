my_dog = {
  'name': 'Rufus',
  'age': 4
}

print(my_dog['name'])


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print(a_dict.items())
# output : 


# The items() method returns a view object that displays 
# a list of dictionary's (key, value) tuple pairs.


for key, value in a_dict.items():
    print(key, '->', value)