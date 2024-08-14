#1
import requests
import random
url = "https://norvig.com/ngrams/sowpods.txt"
open_file = requests.get(url)
with open ("sowpods.txt", "wb") as file:
    file.write(open_file.content)
def get_words_from_file(filename):
    with open (filename, "r") as file:
        words = file.read().split()
    return words
def get_random_sentence(lenght):
    word = get_words_from_file("sowpods.txt")
    sentence = [random.choice(word) for _ in range(lenght)]
    return " ".join(sentence)

def main():
    print("The programm uses modules import and random. First of all we make file readable and after that we are splitting textfile into words and after that make from them collections. Next step we do sentence from random words using module random. ")
    lenght = int(input(f"please enter lenght of sentence that u want:"))
    if lenght >= 2 and lenght <= 20:
        sentence = get_random_sentence(lenght)
        print(sentence)
    else:
        raise TypeError("Valid number")
main()
#json.dump(object_to_save, destination_file)
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
slovar = json.loads(sampleJson)
json_file = "my_file.json"
salary = slovar["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")
slovar["company"]["employee"]["birth_date"] = "1990-01-01"
with open (json_file, 'w') as file_obj:
    json.dump(slovar,file_obj)