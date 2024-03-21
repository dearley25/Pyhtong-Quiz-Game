print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play")
score = 0 
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does DNS stand for? ")
if answer.lower() == "domain name server":
    print("Correct!")
    score += 1    
else: 
    print("Incorrect!")

answer = input("What is port 443? ")
if answer.lower() == "https":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 5) * 100) + "%.")
