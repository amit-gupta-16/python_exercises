# Game Development: Snake water gun
print("\t\t\t\t::Snake Water Gun Game:: \n\n   ")
print("Rule of playing game:\nYou have 10 chance\nchoose 'S','W','G' to play game\n")
import random
name = input("Type Your name to play game: \n")
player_score = 0
computer_score = 0
num_of_play = 0
print("\nSTART\n")
while num_of_play < 10:
    swg = ['s','w','g']
    computer_choice = random.choice(swg)
    player_choice = input("Please, select 's','w','g': ")
    if player_choice == computer_choice:
        player_score = player_score + 1
        print("You got +1 point")
    elif player_choice != computer_choice:
        computer_score = computer_score + 1
        print("You lose -1 point\nComputer got +1 point")
    num_of_play = num_of_play + 1

if player_score > 4:
    print(f"\n{name} ,You have Won! \n Your Score is: {player_score}\n Computer score is: {computer_score} ")
else:
    print(f"\n{name},You lose! \n Your Score is: {player_score}\n Computer score is: {computer_score} ")