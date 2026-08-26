import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

running = True
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")


    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("it's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You won!")
    elif player == "paper" and computer == "rock":
        print("You won!")
    elif player == "scissors" and computer == "paper":
        print("You won!")
    else:
        print("You lose!")
    
    if not input("play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")