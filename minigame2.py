import random

strikes = 0
score = 0
number = random.randint(1,100)
print("The computer generates " + str(number))

while strikes < 3:
    my_answer = input("Is the next one larger or smaller? answer larger or smaller: ")
    previous_number = number
    number  = random.randint(1,100)
    print("The computer generates " + str(number))
    if my_answer == "larger" and number > previous_number:
        print("You're right!")
        score = score + 1
    elif my_answer == "smaller" and number < previous_number:
        print("You're right!")
        score = score + 1
    else:
        print("You're wrong")
        strikes = strikes + 1

    print("Current score is " + str(score))
    print("Current strikes is " + str(strikes))

print("Game over")





