import random
import os


words = ["mango", "rainbow", "playground", "battle"]

def pickword():
    return random.choice(words)

def jumble(word):
    return "".join(random.sample(word, len(word)))

def display_scoreboard(p1score, p2score):
    print("\n------- Current Scoreboard -------")
    print(f"Player 1: {p1score} points.")
    print(f"Player 2: {p2score} points.")
    print("------- ------------------ -------")


def play():
    p1 = input("Enter Player 1 name: ")
    p2 = input("Enter Player 2 name: ")

    p1score = 0
    p2score = 0

    turn = 0
    while True:
        word = pickword()
        ques = jumble(word)

        print(f"\nGuess the word '{ques}'\n")

        if turn % 2 == 0:
            guess = input(f"> {p1}: ").lower()

            if guess == word:
                print(f"Yay! you guessed the word '{word}'")
                p1score += 1
            else:
                print("\nBetter luck next time.")
        else:
            guess = input(f"> {p2}: ")

            if guess == word:
                print(f"Yay! you guessed the word '{word}'")
                p2score += 1
            else:
                print("\nBetter luck next time.")

        os.system('cls' if os.name == 'nt' else 'clear')
        display_scoreboard(p1score, p2score)
        turn += 1



play()