# QUIZ GAME
# Ask the user a couple of questions, and at the end show the final result

print('Welcome to my food quiz game!')

# create the score variable
score = 0
play = input('Do you want to play? y/n: ')

# check the player input to start the game

if play.lower() != 'y':
    quit()

answer = input("Which is the most important ingredient on the pizza? ")

if answer.lower() == "mozzarella":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Which is the most common food are you eating during Easter? ")

if answer.lower() == "lamb":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# or can be done also with the .lower() at the end of the input
answer = input(
    "Which is the ingredient you never add to a carbonara? ").lower()

if answer == "cream":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("The national Belgian dish? ").lower()

if answer == "chips":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You answered at ' + str(score) + ' correct questions!')
