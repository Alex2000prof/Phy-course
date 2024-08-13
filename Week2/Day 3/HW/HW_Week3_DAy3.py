#1
from typing import Any


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return (f"{self.amount} {self.currency}s")
    def __int__(self):
        return self.amount
    def __repr__(self):
        return (f"{self.amount} {self.currency}s")
    def __add__(self,other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"valid currency")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError(f"valid addition")
    def __iadd__(self,other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"valid currency")
            self.amount + other.amount
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError(f"VAlid syntax")

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1.__str__())
print(c1.__int__())
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
c1 += 5
print(c1)
c1 += 2
print(c1)
try:
    print(c3 + 5)
except TypeError as e:
    print(e)
#3
import random
import string
class Stringi: 
    def __init__(self, letter=""):
        self.letter = letter
    def __str__(self):
        return self.letter
    def generate(self):
        self.letter = "".join(random.choice(string.ascii_uppercase) for _ in range(5))
        return self.letter
lst = Stringi()
random_string = lst.generate()
print(random_string)
#4 

from datetime import datetime

def current_date():
    time = datetime.now()
    print(time.strftime("%Y-%m-%d"))

current_date()
#5
def time_before():
    before = datetime.strptime("2025-01-01", "%Y-%m-%d")
    after = datetime.now()
    result = before - after
    print(f"Time remaining: {result}")

time_before()
#6
def time_alive():
    birthday = input("Enter your birthdate (YYYY-MM-DD): ")
    birthday_new = datetime.strptime(birthday, "%Y-%m-%d")
    time_now = datetime.now()
    time_alive_min = time_now - birthday_new
    min_alive = time_alive_min.total_seconds() / 60
    print(f"{min_alive:.0f} minutes")
time_alive()
        
#
from faker import Faker
# print(fake.name())           
# print(fake.address())        
# print(fake.email())         
# print(fake.text())           
# print(fake.date_of_birth())  
fake = Faker()
users = []
def adduser(user_list):
    user = {
        "name": fake.name(),
        "adress": fake.address(),
        "language_code": fake.language_code()
    }
    user_list.append(user)
for _ in range(5):
    adduser(users)
for user in users:
    print(user)



    




        
    