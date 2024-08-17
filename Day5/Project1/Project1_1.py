from Project1 import AnagramCheckerCheck
def main():
    anagram_checker = AnagramCheckerCheck("AnagramChecker.txt")
    while True:
        print("\nmenu:")
        print("1. enter a word")
        print("2. exit")
        choice = input("choose an option (1 or 2): ").strip()
        if choice == '2':
            print("exiting...")
            break
        elif choice == '1':
            word = input("enter a word: ").strip().lower()
            if not word.isalpha() or ' ' in word:
                print("error: please enter a single word containing only letters.")
                continue
            if anagram_checker.is_valid(word):
                print(f"\nYOUR WORD: \"{word.upper()}\"")
                print("this is a valid English word.")
                anagrams = anagram_checker.get_anagrams(word)
                if anagrams:
                    print("anagrams for your word:", ', '.join(anagrams).lower())
                else:
                    print("no anagrams found.")
            else:
                print(f"'{word}' is not a valid English word.")
        else:
            print("invalid choice.please try again.")
if __name__ == "__main__":
    main()

