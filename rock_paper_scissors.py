import random, time, os

from ASCII_sprites import ASCII_sprites


def print_result(images):
    strings_by_column = [s.split("\n") for s in images]
    strings_by_line = zip(*strings_by_column)
    max_length_by_column = [
        max([len(s) for s in col_strings]) for col_strings in strings_by_column
    ]
    for parts in strings_by_line:
        # Pad strings in each column so they are the same length
        padded_strings = [
            parts[i].ljust(max_length_by_column[i]) for i in range(len(parts))
        ]
        print("".join(padded_strings))


def player_chooses():
    print("Welcome to Rock, Paper, Scissors")
    print("=" * 50)
    result = input("Choose either rock, paper or scissors ").lower()
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


def ro_sham_bo(num):
    print(num)
    print_result(ASCII_sprites["rock_rotated"])
    time.sleep(0.25)
    os.system("cls")
    print_result(ASCII_sprites["rock_rock"])
    time.sleep(0.25)
    os.system("cls")


def game(players_choice, opponents_choice):
    os.system("cls")
    count = 3
    while count > 0:
        ro_sham_bo(count)
        count -= 1
    print("Go!")
    print_result(ASCII_sprites["rock_rotated"])
    time.sleep(0.25)
    os.system("cls")
    if players_choice == "rock" and opponents_choice == "scissors":
        print_result(ASCII_sprites["rock_scissors"])
        print("rock beats scissors. You win!")
    elif players_choice == "rock" and opponents_choice == "paper":
        print_result(ASCII_sprites["rock_paper"])
        print("paper beats rock. You lose.")
    elif players_choice == "paper" and opponents_choice == "rock":
        print_result(ASCII_sprites["paper_rock"])
        print("paper beats rock. You win!")
    elif players_choice == "paper" and opponents_choice == "scissors":
        print_result(ASCII_sprites["paper_scissors"])
        print("scissors beat paper. You lose.")
    elif players_choice == "scissors" and opponents_choice == "paper":
        print_result(ASCII_sprites["scissors_paper"])
        print("scissors beat paper. You win!")
    elif players_choice == "scissors" and opponents_choice == "rock":
        print_result(ASCII_sprites["scissors_rock"])
        print("rock beats scissors. You lose.")
    elif players_choice == "rock" and opponents_choice == "rock":
        print_result(ASCII_sprites["rock_rock"])
        print("Same result. Try again.")
    elif players_choice == "paper" and opponents_choice == "paper":
        print_result(ASCII_sprites["paper_paper"])
        print("Same result. Try again.")
    elif players_choice == "scissors" and opponents_choice == "scissors":
        print_result(ASCII_sprites["scissors_scissors"])
        print("Same result. Try again.")
    play = input("Play again? (y = Yes, n = No) ").lower()
    if play == "y":
        main()
    else:
        print("Goodbye!")


def main():
    os.system("cls")
    players_choice = player_chooses()
    opponents_choice = opponent_chooses()
    game(players_choice, opponents_choice)


if __name__ == "__main__":
    main()
