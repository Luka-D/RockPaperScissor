import random, time, os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def player_chooses():
    print("Welcome to Rock, Paper, Scissors")
    print("=" * 50)
    result = input("Choose either rock, paper or scissors: ").casefold()
    choicelist = ["rock", "paper", "scissors"]
    if result in choicelist:
        players_choice = result
        return players_choice
    else:
        print("Invalid Selection")
        player_chooses()


def opponent_chooses():
    choice = random.randrange(0, 3)
    if choice == 0:
        opponents_choice = "rock"
    elif choice == 1:
        opponents_choice = "paper"
    else:
        opponents_choice = "scissors"
    return opponents_choice


def game(players_choice, opponents_choice):
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("Go!")
    time.sleep(0.5)
    print(f"Opponent chooses {opponents_choice}.")
    time.sleep(0.5)
    print(f"You chose {players_choice}.")
    if players_choice == "rock" and opponents_choice == "scissors":
        print("rock beats scissors. You win!")
    elif players_choice == "rock" and opponents_choice == "paper":
        print("paper beats rock. You lose.")
    elif players_choice == "paper" and opponents_choice == "rock":
        print("paper beats rock. You win!")
    elif players_choice == "paper" and opponents_choice == "scissors":
        print("scissors beat paper. You lose.")
    elif players_choice == "scissors" and opponents_choice == "paper":
        print("scissors beat paper. You win!")
    elif players_choice == "scissors" and opponents_choice == "rock":
        print("rock beats scissors. You lose.")
    elif players_choice == "rock" and opponents_choice == "rock":
        print("Same result. Try again.")
    elif players_choice == "paper" and opponents_choice == "paper":
        print("Same result. Try again.")
    elif players_choice == "scissors" and opponents_choice == "scissors":
        print("Same result. Try again.")
    play = input("Play again? (y = Yes, n = No) ")
    if play == "y":
        main()
    else:
        print("Goodbye!")


def main():
    clear_screen()
    players_choice = player_chooses()
    opponents_choice = opponent_chooses()
    game(players_choice, opponents_choice)


if __name__ == "__main__":
    main()
