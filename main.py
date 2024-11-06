from random import randint
from art import logo


EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def game():
    answer = randint(1, 100)


    def check_answer(user_guess, actual_answer):
        if user_guess > actual_answer:
            print("Too high")
        else:
            print("Too low")


    def set_difficulty():
        game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\t").lower()
        print()
        while game_difficulty != "easy" and game_difficulty != "hard":
            print("You entered a wrong value!")
            game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\t").lower()
            print()

        if game_difficulty == "easy":
            return EASY_LEVEL_TURN
        elif game_difficulty == "hard":
            return HARD_LEVEL_TURN

    print(f"\n" * 42)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()
    guess = 0
    while attempts > 0 and guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\t"))
        print()
        if guess != answer:
            check_answer(guess, answer)
            attempts -= 1

        if attempts > 0 and guess != answer:
            print("Guess again\n")

    if guess == answer:
        print(f"You got it! The answer was {answer}.\n")
    else:
        print(f"You have {attempts} attempts. GAME OVER! (The answer was {answer})\n")

    want_new_game = input("Would you like to start a new game? (Y)es or (N)o\t").lower()
    while want_new_game != "y" and want_new_game != "yes" and want_new_game != "n" and want_new_game != "no":
        print("You entered a wrong value!")
        want_new_game = input("Would you like to start a new game? (Y)es or (N)o\t").lower()

    if want_new_game == "y" or want_new_game == "yes":
        game()
    else:
        print("Good bye!")
        return

game()

