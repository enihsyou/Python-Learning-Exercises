# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock": return 0
    if name == "Spock": return 1
    if name == "paper": return 2
    if name == "lizard": return 3
    if name == "scissors": return 4
    else: print("Something Worng!!!")

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0: return "rock"
    if number == 1: return "Spock" 
    if number == 2: return "paper" 
    if number == 3: return "lizard"
    if number == 4: return "scissors"
    else: print('Something Worng!!!')
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    # print a blank line to separate consecutive games

    # print out the message for the player's choice
    print("Player chooses", player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    player_choice_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print("Computer chooses", comp_choice)
    # compute difference of comp_number and player_number modulo five
    c_p_number_mod = (comp_number - player_choice_number) % 5
    # use if/elif/else to determine winner, print winner message
    if (c_p_number_mod == 1 or c_p_number_mod == 2): print("Computer wins!")
    if (c_p_number_mod == 3 or c_p_number_mod == 4): print("Player wins!")
    if (c_p_number_mod == 0): print("Player and computer tie!")
    print()
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
