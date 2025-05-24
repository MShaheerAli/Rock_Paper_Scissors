import random
import pyjokes

def cpu_move():
    choice = random.randint(1, 3)
    if choice == 1:
        cpu_role = "rock"
    elif choice == 2:
        cpu_role = "paper"
    elif choice == 3:
        cpu_role = "scissor"
    return cpu_role

def human_move():
    character = input("Choose between rock, paper and scissor: ").lower()
    while character != "rock" and character != "paper" and character != "scissor":
        character = input("INVALID INPUT! Choose between rock, paper and scissor: ").lower()
    return character

def print_result(h_wins, cpu_wins,rounds):
    if cpu_wins > h_wins:
        print(f"YOU LOST! BETTER LUCK NEXT TIME! You won {h_wins} out of {rounds}")
    elif h_wins > cpu_wins:
        print(f"YOU WON!!!! You won {h_wins} out of {rounds}. You get to hear a joke: {pyjokes.get_joke()}")
    else:
        print("Game ended in a draw! Boringgggg")


def Number_Rounds():
    rounds = input("How many rounds do you wanna play?: ")
    t_value = rounds.isdigit()

    while t_value != True or int(rounds)<=0:

        rounds = input("INVALID INPUT! Enter a positive non-zero number: ")
        t_value = rounds.isdigit()

    Rounds = int(rounds)


    return Rounds



print("Welcome to Rock Paper Scissors!")
Rounds=Number_Rounds()

replay = True

while replay == True:
    Hwins = 0
    CPUwins = 0

    for i in range(Rounds):
        move = cpu_move()
        character = human_move()

        if character == "rock":
            if move == "rock":
                print("The CPU chose rock. Draw")
            elif move == "paper":
                CPUwins += 1
                print("CPU won this round as it chose paper")
            elif move == "scissor":
                Hwins += 1
                print("You won this round as the CPU chose scissor")
            print(f"Your Wins: {Hwins}\nCPU Wins: {CPUwins}")

        elif character == "paper":
            if move == "paper":
                print("Draw as the CPU chose paper")
            elif move == "scissor":
                CPUwins += 1
                print("CPU won this round as it chose scissor")
            elif move == "rock":
                Hwins += 1
                print("You won this round as the CPU chose rock")
            print(f"Your Wins: {Hwins}\nCPU Wins: {CPUwins}")

        elif character == "scissor":
            if move == "scissor":
                print("Draw as the CPU also chose scissors")
            elif move == "rock":
                CPUwins += 1
                print("CPU won this round as it chose rock")
            elif move == "paper":
                Hwins += 1
                print("You won this round as the CPU chose paper")
            print(f"Your Wins: {Hwins}\nCPU Wins: {CPUwins}")

    else:
        print_result(Hwins, CPUwins,Rounds)

        response = input("Do you wanna play again? ").lower()
        while response != "yes" and response != "no":
            response = input("Answer only in yes or no. Do you wanna play again? ").lower()

        if response == "yes":
            Rounds=Number_Rounds()
            replay = True
        elif response == "no":
            print("Thank you for playing")
            replay = False
