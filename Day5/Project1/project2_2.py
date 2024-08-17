from Project2 import Game

def get_user_menu_choice():
    print("menu:")
    print("play a new game (p)")
    print("show scores (s)")

    choice = input("please choose an option: p or s ").strip().lower()
    return choice

def print_results(results):
    print("\nGame Results:")
    print(f"Wins: {results['wins']}")
    print(f"Losses: {results['losses']}")
    print(f"Draws: {results['draws']}")
    print("thank you for playing! :)")

def main():
    game = Game()
    results = {"wins": 0, "losses": 0, "draws": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "quit":
            print("hmm okay bye!")
            break
        elif choice == "p":
            result = game.play()
            if result == "draw":
                results["draws"] += 1
            elif result == "win":
                results["wins"] += 1
            else:
                results["losses"] += 1
        elif choice == "s":
            print_results(results)
        else:
            print("try again")
if __name__ == "__main__":
    main()


                
                


    
    