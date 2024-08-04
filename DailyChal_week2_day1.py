#1
import random
sent = input("everything")
if len(sent) < 10:
    print("not enough")
elif len(sent) > 10:
    print("too much")
elif len(sent) == 10:
    print("perfect")
print(sent[0],sent[-1])
word = ""
for i in sent:
    word += i
    print(word)
word = list(word)
random.shuffle(word)
new_word = ""
for x in word:
    new_word += x
print(new_word)


