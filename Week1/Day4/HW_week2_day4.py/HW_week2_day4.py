import random
# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
def display_message():
    print("we study")
display_message()



# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.
def favorite_book(title):
    print(f"One of my favorite books is: {title}")
favorite_book("The lord of the rings")



# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.
def describe_city(city, country = "unknown counrty"):
    print(f"{city} is in {country}")
describe_city("Moscow", "Russia")




# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

def rndm(number):
    if number > 100 or number < 1:
        print("enter number 1 and 100")
        return
    number_n = random.randint(1, 100)
    if number == number_n:
        print("success ")
    else:
        print("fail")
rndm(1)


# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.
def make_shirt(text = "I love python",size = "Large"):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirt()
make_shirt(size = "medium")
make_shirt(size="small", text="top")
make_shirt(text="sss",size="small" )

# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(ms):
    for m in ms:
        print(m)
show_magicians(magician_names)
def make_great(ms):
    for i in range(len(ms)):
        ms[i] = f"{ms[i]} the Great"
make_great(magician_names)






# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
def get_random_temp(season):
    if season == 'winter':
        return round(random.uniform(-10, 16), 1)
    elif season == 'spring':
        return round(random.uniform(0, 20), 1)
    elif season == 'summer':
        return round(random.uniform(20, 38), 1)
    elif season == 'autumn':
        return round(random.uniform(5, 19), 1)
    else:
        return round(random.uniform(-10, 40), 1)
def get_random_month(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else: 
        return None
    


def main():
    month = int(input("Please enter the month:  "))
    season = get_random_month(month)
    if season is None:
        print("next")
        return
    temp = get_random_temp(season)
    print(f"temp is {temp}")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temp < 23:
        print("hot")
    elif 24 <= temp < 32:
        print("HOT")
    elif 32 <= temp <= 40: 
        print("HHHHHOOOOOOTTTTT") 
    else: 
        print(temp)
main()



    



# 🌟 Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def ask_que (questions):
    goodans = 0
    badans = 0
    wrong_ans = []
    for i in data:
        answer = input(i["question"]).strip().lower()
        answercor = i["answer"].strip().lower()
        if answer == answercor:
            goodans += 1
        else: 
            badans += 1
            wrong_ans.append(
                {
                "question": i["question"],
                "your_answer": answer,
                "correct_answer": answercor
                }
            )
    return goodans, badans, wrong_ans

def count_answers(goodans, badans):
    print(f"Correct answers: {goodans}")
    print(f"Incorrect answers: {badans}")

def explanations(wrong_ans):
    if wrong_ans:
        print("Explanation for incorrect answers:")
        for i in wrong_ans:
            print(f"Question: {i['question']}")
            print(f"Your answer: {i['your_answer']}")
            print(f"Correct answer: {i['correct_answer']}")

def main():
    goodans, badans, wrong_ans = ask_que(data)
    count_answers(goodans, badans)
    explanations(wrong_ans)
    if badans > 3:
        print("You had more than 3 incorrect answers. Please try again!")
main()


        

    

        
        
    




    
