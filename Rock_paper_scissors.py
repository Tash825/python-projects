import random

choices = ('r','p','s')
emojis = {'r':'🪨','s':'✂️','p':'📃'}

while True:
    chosen = random.choice(choices)
    ur_input = input('CHoose your hand: rock, paper or scissors? (r/p/s): ').lower()
    
    if ur_input not in choices:
        print("Invalid Choice")
        continue
    
    print(f"You chose {emojis[ur_input]}")
    print(f"Computer chose{emojis[chosen]}")
    
    if ur_input == chosen:
        print("It's a Tie")
    elif(
        (ur_input == 'r' and chosen == 's') or 
        (ur_input == 's' and chosen == 'p') or 
        (ur_input == 'p' and chosen == 'r')):
            print("You Win!")
    else:
        print("You Lose!")
    Should_continue = input("Would you like to continue? (y/n)").lower()
    if Should_continue == 'n':
        break
