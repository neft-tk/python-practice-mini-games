name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across. ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game.")
    else:
        print("Not a valid option, you lose. :(")
elif answer == "right":
    answer == input("You come to a bridge, it looks wobbly, do you want to cross or go back -cross- -back-? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        input("You cross the bridge and meet a stranger. Do you talk to the stranger or ignore them? -talk- -ignore-").lower()
        
        if answer == "talk":
            print("You talk to the stranger and they give you gold, you win!")
        elif answer == "ignore":
            print("You ignore the stranger and they are offended, you lose.")
        else:
            print("Not a valid option, you lose.")
    else:
        print("Not a valid option, you lose.")
else:
    print("Not a valid option, you lose. :(")