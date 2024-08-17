import requests
from collections import Counter

url = "http://norvig.com/ngrams/sowpods.txt"
response = requests.get(url)
filename = "AnagramChecker.txt"
with open(filename, 'wb') as file:
    file.write(response.content)

class AnagramCheckerCheck:
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.words = {word.strip().upper() for word in file}

    def is_valid(self, word):
        return word.upper() in self.words

    def get_anagrams(self, word):
        word = word.upper()
        if not self.is_valid(word):
            return f"'{word}' is not a valid word."

        anagrams = [w for w in self.words if Counter(w) == Counter(word) and w != word]
        return anagrams









