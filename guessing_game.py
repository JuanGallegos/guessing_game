import random


def message(message):
    print("\n" + "-" * 30)
    print(message)
    print("-" * 30)


def start_game():
    solution = random.randint(1, 10)
    counter = 0

    while True:
        try:
            guess = int(input("\nPick a number between 1 and 10: "))
            if guess not in range(1, 11):
                raise ValueError("The selected number is out of range")
        except ValueError as err:
            print(f"We ran into an issue: '{err}'. Please try again.")
        else:
            counter += 1

            if guess == solution:
                print(f"\n You got it! The solution was {solution}. "
                      + f"It took you {counter} tries. \n")
                break
            elif guess > solution:
                print("It is lower!")
            elif guess < solution:
                print("It is higher!")

    return counter


def main():
    scores = []
    message(" Welcome to the Number Guessing Game!")
    scores.append(start_game())

    while True:

        play = input("Would you like to play again? [y]es/[n]no:")
        if play == 'y':
            print(f"The current High Score is {min(scores)}")
            scores.append(start_game())
        elif play == 'n':
            break
        else:
            print("\nYou did not enter a response of 'y' or 'n'.")

    message(f" Thank you for playing the Guessing Game! Your High Score was {min(scores)} tries!")


if __name__ == '__main__':
    main()
