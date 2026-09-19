import random

first_die = [2,3,4,5,6]
die = [1,2,3,4,5,6]
die_result = random.choice(first_die)
print("You rolled " + str(die_result))
score = 0
if die_result == 1:
    print("Game over!")
else:
    score = score + die_result
    print("You scored: " + str(score))

want_to_roll = input("Roll the die? answer yes or no")
while want_to_roll == "yes" and die_result != 1:
    die_result = random.choice(die)
    print("You rolled " + str(die_result))
    if die_result == 1:
        print("Game over!")
    else:
        score = score + die_result
        print("You scored: " + str(score))

    if die_result != 1:
        want_to_roll = input("Roll the die? answer yes or no: ")
    else:
        print("Your final score is " + str(score))





