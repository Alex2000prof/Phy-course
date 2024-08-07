def so_it():
    print("Hello")
so_it()
def pur_lang(lang, name):
    if lang == "en":
        return f"hi, {name}"
    elif lang == "fr":
        return f"baton, {name}"
    elif lang == "ru":
        return f"privet, {name}"
    else:
        return "unknown lang"
print(pur_lang("en", "vasya"))
def calculation(a, b):
    ad  = a + b
    min = a - b
    return f"this is add: {ad},this is minus: {min}"
print(calculation(40, 10))

print('hello')#print is a function

def say_hello():
    print('hello world')

say_hello()

#with arguments
def adv_say_hello(name):
    return f'Hello {name}'
print(adv_say_hello("Ezra"))

#arguments: positional and keyword
def adv_say_hello(name, language='EN'):#default arg = 'EN'
    if language == 'HE':
        return f'Shalom {name}'
    if language == 'EN':
        return f'Hello {name}'
    elif language == 'RU':
        return f'Privet {name}'
    else:
        return "unknown"
print(adv_say_hello(language= 'HE', name='Ezra'))#keyword arguments
print(adv_say_hello('Ezra', language='RU'))#mixed keyword and positional arguments
print(adv_say_hello('Ezra', 'RU'))#positional arguments
print(adv_say_hello('Ezra'))#default argument use




students = ['Harry', 'Hermione', 'Ron', 'Luna']

def wizard(names_list: list):
    greetings = []
    for name in names_list:
        greetings.append(f'{name}, welcome to Hogwarts!')
    return greetings

print(wizard(students))
print(students)# it doesnt change the original list

def selector_hat():
    for i, name in enumerate(students):

        students[i] = f"{name}, you are Griffyndor"
selector_hat()
print(students)

name = 'Avner'
def say_hi():
    name = 'Juliana'
    return name
print(say_hi())
print(name)

#global scope
count = 10
def calculation(a,b):
    global count
    result = a + b
    result += count 
    return result
print(calculation(5,15))

#знаем сколько аргументов передаем в функцию 
def check_arguments(*args):
    print(f"These are the arguments {args}")

check_arguments(1 , 3, "heeey")
def check_tuple(a, b):
    return sum((a,b))
print(check_tuple(10, 30))