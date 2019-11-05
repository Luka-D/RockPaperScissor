import random
import time

def main():
    begin()
    opponent()
    game()

def begin():
    print('Welcome to Rock, Paper, Scissors')
    result = input('Choose either rock, paper or scissors (Case sensitive) ')
    choicelist = ['rock', 'paper', 'scissors']
    if result in choicelist:
        global pyresult
        pyresult = result
        #print(pyresult)
    else:
        print ('Invalid Selection')
        begin()

def opponent():
    choice = random.randrange(0,3)
    global opresult
    if choice == 0:
        opresult = 'rock'
    elif choice == 1:
        opresult = 'paper'
    else:
        opresult = 'scissors'
    #print(opresult)

def game():
    print('3')
    time.sleep(0.5)
    print('2')
    time.sleep(0.5)
    print('1')
    time.sleep(0.5)
    print('Go!')
    time.sleep(0.5)
    print('Opponent chooses '+opresult)
    time.sleep(0.5)
    print('You chose '+pyresult)
    if pyresult == 'rock' and opresult == 'scissors':
        print("rock beats scissors. You win!")
    elif pyresult == 'rock' and opresult == 'paper':
        print('paper beats rock. You lose.')
    elif pyresult == 'paper' and opresult == 'rock':
        print("paper beats rock. You win!")
    elif pyresult == 'paper' and opresult == 'scissors':
        print('scissors beat paper. You lose.')
    elif pyresult == 'scissors' and opresult == 'paper':
        print("scissors beat paper. You win!")
    elif pyresult == 'scissors' and opresult == 'rock':
        print('rock beats scissors. You lose.')
    elif pyresult == 'rock' and opresult == 'rock':
        print('Same result. Try again.')
    elif pyresult == 'paper' and opresult == 'paper':
        print('Same result. Try again.')
    elif pyresult == 'scissors' and opresult == 'scissors':
        print('Same result. Try again.')
    play = input("Play again? (y = Yes, n = No) ")
    if play == 'y':
        main()
    else:
        print("Goodbye!")
        
if __name__=='__main__':
    main()