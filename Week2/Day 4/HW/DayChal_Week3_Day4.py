class Text():
    def __init__(self,text):
        self.text = text
    def frequency(self, word):
        count = 0
        for w in self.text.split():
            if w == word:
                count += 1
        return count 
    def most_frequent_word(self):
        words = self.text.split()
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_frequent = max(word_count, key=word_count.get, default=None)
        return most_frequent
    def unique_words(self):
        words = self.text.split()
        unique_words_set = set(words)
        return list(unique_words_set)
text_given = "A good book would sometimes cost as much as a good house ."
sentence = Text(text_given)
print(sentence.text)
print("text: ", sentence.text)
print("frequency of the word house: ", sentence.frequency("house"))
print("most frequent word: ", sentence.most_frequent_word())
print("list of unique words: ", sentence.unique_words())
