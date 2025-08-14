print("welcome to my compter quiz!")
//hanumreddy
playing = input("Do you went to play? ")

if playing.lower() !="yes":
    quit()

print("okay! let's play :)")
score = 0

answer = input("what does CPU stad for?")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU stad for?")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does Ram stand for?")
if answer.lower()== "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does psu stand for?")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("YOU got " + str(score) + "qustion correct!")

print("YOU got " + str((score / 4) * 100) + "%")


