print("Welcome to my general knowledge quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who is known as the Father of the Nation in India? ")
if answer.lower() == "mahatma gandhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("When did India gain independence from British rule? ").lower().strip()
correct_answers = ["15th august,1947","August 15 ,1947"]

if answer in correct_answers:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of India's national anthem? ")
if answer.lower() == "jana gana mana":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who wrote the Indian national anthem?")
if answer.lower() == "rabindranath tagore":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who was the first Prime Minister of India?")
if answer.lower() == "jawalharlal neheru":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of India?")
if answer.lower() == "new delhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who was the first woman Prime Minister of India?")
if answer.lower() == "indira gandhi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the current President of India?")
if answer.lower() == "droupadi murmu":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which day is celebrated as Republic Day in India?").lower().strip()
correct_answers = ["january 26","26th january"]
if answer in correct_answers:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which Indian city is known as the City of Joy?")
if answer.lower() == "kolkata":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")