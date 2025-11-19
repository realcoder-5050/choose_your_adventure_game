name = input("Enter your name: ")
print(f"\nWelcome {name} to the fairytale game, where you write your own story!")

answer = input("You are on a dirty road, it has come to an end you can go 'left/right': ").lower()

if answer.lower() == "left":
    answer_1 = input("You come to a river you can either 'swim/ walk: '")
    if answer_1 == "swim":
        print("Then you can proceed on the journey and lose the game.")
    elif answer_1 == "walk":
        print("Sorry you drowned!")
    else:
        print("Do well to select a valid option!  ")
elif answer.lower() == "right":
    answer = input("You proceeded to the next level and qualify to move but you have a choice to " \
    " 'walk/fly': ")

    if answer == "walk":
        print("Sorry, this is the end of the road for you!")
    elif answer == "fly":
        max = input("You suceeded to the final stage, here is the catch you either 'take-profit/stop-loss: '\n ")
        if max == "take-profit":
            print("You really did well , but unfortunately you loss!")
        elif max == "stop-loss":
            print("\n You qualified for the final rounds and stand a chnace to earn millions.")
        else:
            print("Invalid option, selected!")
  
else:
    print("Not a valid option, You lose.")

print("Thank you for trying this  with us, see you the next series!")





