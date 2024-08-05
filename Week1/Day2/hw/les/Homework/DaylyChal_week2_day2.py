a = int(input("nu: "))
b = int(input("len: "))
ar = []
for i in range(1,b + 1):
    ar.append(i * a)
print(ar)    
    













sent = input("enter word")
sent = list(sent)
new_sent = ""
for i in range(len(sent)):
    if i == 0 or sent[i] != sent[i - 1]:
        new_sent += sent[i]
print(new_sent)




