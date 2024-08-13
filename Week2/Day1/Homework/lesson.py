# class Dog():
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

# shelter_dog = Dog(name_of_the_dog="Rex")
# other_shelter_dog = Dog("Jimmy")

# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# first_person = Person("john", 25)

# print(first_person.name)
# print(first_person.age)

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)

# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print("{} barks ! WAF".format(self.name))


class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)