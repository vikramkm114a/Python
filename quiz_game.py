print("Welcome to my quiz!")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What is the Capital of Germany? ")
if answer.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the Capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many states are there in the USA? ")
if answer.lower() == "50":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What country is the Taj Mahal in? ")
if answer.lower() == "india":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/ 4) * 100) + "%!")