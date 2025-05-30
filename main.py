from random import choice #capitalize karna hai

value = ["Rock", "Paper", "Scissor"]
computer = choice(value)

value1 = input("Choice one from Rock, Paper, Scissor: ")
player = value1.capitalize()

if(computer == player):
    print(f"Match was draw both are same choices: {player}")

else:
    if(computer == "Rock" and player == "Scissor"):
        print("Opps! You lose")

    elif(computer == "Scissor" and player == "Rock"):
        print("Congratulation! You win")

    elif(computer == "Paper" and player == "Rock"):
        print("Oops! You lose")

    elif(computer == "Rock" and player == "Paper"):
        print("Congratulation! You win")

    elif(computer == "Paper" and player == "Scissor"):
        print("Congratulation! You win")

    elif(computer == "Scissor" and player == "Paper"):
        print("Oops! You lose")
