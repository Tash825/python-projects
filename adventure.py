name = input("Type your name: ")
print("Welcome "+ name +" to this adventure")

answer = input("You are on a abandoned road and have come to fork in the road, Choose whether you will go left or right").lower()

if answer == "left":
    answer = input("You see a river along the path. Will you swim or walk across? ").lower()
    if answer == "swim":
        print("You are eaten by a crocodile. You lose")
    elif answer == "walk":
        print("You have come across a bridge over the river")
        answer = input("Will you cross the bridge or turn around?").lower()
        if answer == "cross":
            print("You have come to a old hut.")
            answer = input("Will you enter or leave?").lower()
            if answer == "enter":
                print("You found lost treasure inside, you win!")
            elif answer == "leave":
                print("You got stranded in forest. You lose")
            else:
                print("Not a valid option. You lose.") 
    else:
       print("Not a valid option. You lose.") 
elif answer == "right":
    print("You are met by a ferocious tiger and it eats you. You lose")
else:
    print("Not a valid option. You lose.")
