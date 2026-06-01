import random

choice = ["rock","paper","scissors"]
user_score = 0
computer_score = 0

print("=====STONE PAPER SCISSORS GAME=====")
while True:
    print("Choose one\n1.Rock\n2.Paper\n3.Scissors")
    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choice:
        print("Invalid Choice")
        continue

    computer_choice = random.choice(choice)

    print(f"your choice is {user_choice}")
    print(f"computer choice is {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie")

    elif (
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "rock" and computer_choice == "scissors")
    ):
        print("You Win")
        user_score += 1

    else:
        print("You Lose")
        computer_score += 1

    print("====SCORE BOARD=====")
    print(f"your score : {user_score}")
    print(f"computer : {computer_score}")

    play_again = input("Do you want to play again?(y/n)").lower()

    if play_again != "y":
        print("Thank you for playing")
        break


