import random

MAX_ROUNDS = 7
CURRENT_ROUND = 0
RANDOM_NUMBER = 0
selection = ""

def MENU_DISPLAY():
    global selection

    print("\nGUESS THE MYSTERY NUMBER!")
    print("-" * 25)
    print("1) Play Game")
    print("2) See Rules")
    print("3) Quit")

    selection = input("SELECTION: ")
    menuInput()

def SHOW_RULES():
    print("\nRULES:")
    print("* Selected number must be between 1-100")
    print("* You get 7 chances to guess the mystery number")

def getGuess(min, max):
    guess = int(input("\nEnter guess: "))
    if guess >= min and guess <= max:
        return guess

def guessWin(number,guess):
    global CURRENT_ROUND
    CURRENT_ROUND += 1
    if number < guess:
        print("Too High...")
        return False
    if number > guess:
        print("Too Low...")
        return False
    if number == guess:
        print("Congratulations! You guessed the random number!")
        return True

def playGame():
    global CURRENT_ROUND
    RANDOM_NUMBER = random.randint(1,100)
    while CURRENT_ROUND < MAX_ROUNDS:
        guess = getGuess(1,100)
        gameOver = guessWin(RANDOM_NUMBER, guess)
        if gameOver:
            break

    print("\nGAME OVER!")
    print(f"Score: {CURRENT_ROUND}")

    CURRENT_ROUND = 0

def menuInput():
    if selection == "1":
        playGame()
    elif selection == "2":
        SHOW_RULES()
    elif selection == "3":
        print("\nThank you for playing!")
        exit()
    else:
        print("\nInvalid input. Try again")

while True:
    MENU_DISPLAY()
