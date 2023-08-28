import random

# ASCII art for each choice
rock_img = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_img = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_img = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of ASCII art images for each choice
game_imgs = [rock_img, paper_img, scissors_img]

# List of available choices
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

# Display ASCII art for user's choice
print("\nYour choice:")
print(game_imgs[choices.index(user_choice)])

# Display ASCII art for computer's choice
print("\nComputer's choice:")
print(game_imgs[choices.index(computer_choice)])

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
