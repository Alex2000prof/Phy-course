# 🌟 Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
my_fav_numbers = {1,3,4,6,35,46,5}
my_fav_numbers.update([2, 7])
print(my_fav_numbers)
my_fav_numbers.discard(46)
print(my_fav_numbers)
friend_fav_numbers = {2,3,5,67,8}
our_fav_numbers = friend_fav_numbers.union( my_fav_numbers)
print(our_fav_numbers)



# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
#Answer: No

# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
apples = basket.count("Apples")
print(basket)
basket.clear
print(basket)



# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?
#Answer
#float - 1.6, 2.35
#difference is that int - 3,4,5,6,7 float - 1.6, 2.35
a_list = []
for i in range(0,6):
    a_list.append(i / 2 + 0.5)
print(a_list)

b_list = []
a = 1
while a > 0 and a < 10:
    b_list.append(a * 0.5)
    a += 1
print(b_list)



# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
nums = []
for x in range(1,21):
    nums.append(x)
    if x % 2 == 0:
        print(x)
print(nums)


# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = "Alex"
while True:
    your_name = input("enter your name: ")
    if your_name == name:
        print("good")
        break

    

# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
fruit_s = input("several fruits: ")
fruit_s_l = fruit_s.split()
fruit = input("choose your fav")
if fruit in fruit_s_l:
    print("You chose one of your favorite fruits! Enjoy!" )
else:
    print("You chose a new fruit. I hope you enjoy")





# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
count = 0
finish = 0
tops = []
while True:
    topping = input("enter topping")
    if topping == "quit":
        break
    else:
        count += 1
        tops.append(topping)
finish = (count * 2.5) + 10
print("give money 2.5 for everyone",tops,finish)



    

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.
price = 0
while True:
    say_name = input("name or finish")
    if say_name == "finish" :
        print(price)
        break
    age = int(input("age"))
    if age < 3:
        price += 0
    elif 3 <= age < 12:
        price += 10
    elif age >= 12:
        price += 15


names = []
while True:
    username = input("name")
    if username == "finish":
        break
    names.append(username)
n = 0
while n < len(names):
    age_user = int(input(f"How old a u?{names[n]}"))
    if 16 <= age_user <= 21:
        names.pop(n)
    else:
        n += 1
print("list: ", names)
    





# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)  
    finished_sandwiches.append(sandwich) 
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")

