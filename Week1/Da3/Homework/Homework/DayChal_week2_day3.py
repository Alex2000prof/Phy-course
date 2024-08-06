word = input()
dic = {}
for i in range(len(word)):
    word_d = word[i]
    if word_d not in dic:
        dic[word_d] = []
dic[word_d].append(i)
print(dic)


items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

#sorry couldn-t do it:()