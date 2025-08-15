#Rock-Paper-Scissor 
import random 
user_wins = 0
computer_wins = 0 
options = ['rock','paper','scissor']
while True:
    user_pick = input("Choose Rock/Paper/Scissor or Q to quit: ").lower()
    if user_pick == 'q':
        break
    if user_pick not in options:
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked:",computer_pick)
    if user_pick == computer_pick:
        print("It was a draw!")
    elif (user_pick == 'rock' and computer_pick == 'scissor') or \
         (user_pick == 'paper' and computer_pick == 'rock') or \
         (user_pick == 'scissor' and computer_pick == 'paper'):
        print("You win!")
        user_wins += 1
    else:
        print("You lost!!")
        computer_wins += 1

print("You won",user_wins,"times.")
print("Computer won",computer_wins,"times")
print("Goodbye!")
            

   
    



