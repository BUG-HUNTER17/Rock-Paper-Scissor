import random

item_list = ["Rock", "Paper", "Scissor"]
score = 0

while True:
    user_choice = input("Enter your move (Rock, Paper, Scissor) or 'quit' to end: ").capitalize()

    if user_choice == 'Quit':
        print("Final score:", score)
        break

    comp_choice = random.choice(item_list)

    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Both choose the same: Match Tie")
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock: Computer Wins")
            score -= 1
        else:
            print("Rock smashes Scissor: You win")
            score += 1
    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts Paper: Computer Wins")
            score -= 1
        else:
            print("Paper covers Rock: You win")
            score += 1
    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            print("Rock smashes Scissor: Computer Wins")
            score -= 1
        else:
            print("Scissor cuts Paper: You win")
            score += 1

    print("Current score:", score)
