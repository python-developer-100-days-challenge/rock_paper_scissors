import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Get user's choice
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
while user_choice not in choices:
    user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()

# Computer chooses
computer_choice = random.choice(choices)

# Display choices
print(f"You chose {user_choice}.")
print(f"Computer chose {computer_choice}.")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
