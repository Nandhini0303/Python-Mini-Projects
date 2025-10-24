#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Rock Papper Scissor game


# In[12]:


import random

def play_round():
    """Plays a single round of Rock-Paper-Scissors."""
    choices = ['r', 'p', 's']

    # Computer makes a random choice
    computer_choice = random.choice(choices)

    # User input (strip whitespace and make lowercase)
    user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()

    print("You chose: ",user_choice, "\ncomputer chose: ",computer_choice)

    # Determine outcome
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        print("You win!")
    else:
        print("You lose!")


def main():
    """Runs the Rock-Paper-Scissors game loop."""
    print("Welcome to Rock-Paper-Scissors!")
    
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()


# In[13]:


#second method


# In[ ]:


import random
''' Rock Paper scissors game - Mini game project!'''
print("Welcome to Rock-Paper-Scissors!")
while(1<2):
    user_choice = input("Enter your choice: ")
    user_choice = str.upper(user_choice)
    #print(len(user_choice));
    # validating the user input

    if (user_choice == 'E'):
        print("Exit the game!")
        break;
    if(len(user_choice) == 1):
        if((user_choice == "R") or (user_choice == "S") or (user_choice == "P")):
            print("You_choose : ",user_choice)
        else:
            print("Invalid choice. Please enter a correct choise")
            continue;
        
    #Get computer value
    choice = ['R','P','S']
    computer_choice = random.choice(choice)
    print("Computer_choose: ",computer_choice)
    
    if (computer_choice == str.upper(user_choice)):
        print("Tie!")
    elif( (user_choice == 'r' and computer_choice.upper() == 's') or 
    (user_choice == 's' and computer_choice.upper() == 'p') or 
    (user_choice == 'p' and computer_choice.upper() == 'r')):
        print("You Win!")
    
    else: 
        print("You Lose!")



    

    


# In[ ]:





# In[ ]:




