words = input("enter wwords through ,")
words_sorted = " , ".join(sorted([word for word in words.split(",")]))
print(words_sorted)

sent = input("enter sentence: ")
sent_new = sent.split()
long_word = sent_new[0]
for wordik in sent_new[1:]:
    for word_sec in sent:
        if len(wordik) > len(long_word):
            long_word = wordik
print(long_word)
        