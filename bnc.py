from random import randint


print("Get ready to play Bear, Ninja, Cowboy!")

# Define roles for the game
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role and assign it as the computer's choice
computer = roles[randint(0,2)]

# Loop through the game until the user declines to play again
player = False
while player == False:
   
      
   
    # Continue to ask player for their choice of role until they provide a valid choice.
    while True:
        # Get player input for their choice of role.
        player = input("Bear, Ninja, or Cowboy? > ")
        # Check if their choice was valid. If not, continue the loop and re-prompt the player. 
        if player not in ["Bear", "Ninja", "Cowboy"]:
            print(f"{player} is not Bear, Ninja, or Cowboy.")
            continue
        else:
            break

    # Compare computer and player roles and print results
    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
      if player == "Bear":
        print(f"You lose! {computer} shoots {player}")
      else: # computer is cowboy, player is ninja
        print(f"You win! {player} defeats {computer}") 
    elif computer == "Bear":
      if player == "Cowboy":
        print(f"You win! {player} shoots {computer}")
      else: # computer is bear, player is ninja
        print(f"You lose! {computer} eats {player}")
    elif computer == "Ninja":
      if player == "Cowboy":
        print(f"You lose! {computer} defeats {player}")
      else: # computer is ninja, player is bear
        print(f"You win! {player} eats {computer}")

    # Ask if player wants to play again. If yes, set condition to repeat loop, else break out of loop
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break