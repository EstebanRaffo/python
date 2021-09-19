numA = float(input("First: "))
numB = float(input("Second: "))
sub = numA - numB
print("Result: " + str(sub))

if sub < 0:
    print("Negative number")
else:
    print("Positive number")


isTrue = 5 == 4
print(isTrue)

carSpeed = 50

if carSpeed > 100:
    print("Too Fast")
elif carSpeed < 20:
    print("Too slow")
else:
    print("Good")
print("Ready")

degree = input("Enter degree: ")
experience = input("Years of experience: ")

if degree == "master" or degree == "phd":
    if int(experience) >= 2:
        print("accepted")
    else:
        print("you don't")
else:
    print("you don't have required degree")