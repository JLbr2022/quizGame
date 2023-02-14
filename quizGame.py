# Program which do a small quiz, calculate the score percentege and display the result
# NOTE: this program was made to refresh and mantain my basic python's knowledge

# variables declaration
score = 0

# Display the welcome message
print("Welcome to the quiz game!")
print("You will be asked 4 questions, each question is worth 25 points.")

# Question 1
print("Question 1: What is the capital of France?")

answer = input("Enter your answer: ").lower()
if answer == "paris":
    print("Correct!")
    score = 25
else:
    print("Incorrect!")
    print("The correct answer is Paris")

# Question 2
print("Question 2: What is the capital of Spain?")
answer = input("Enter your answer: ").lower()
if answer == "madrid":
    print("Correct!")
    score = score + 25
else:
    print("Incorrect!")
    print("The correct answer is Madrid")

# Question 3
print("Question 3: What is the capital of Italy?")
answer = input("Enter your answer: ").lower()
if answer == "rome":
    print("Correct!")
    score = score + 25
else:
    print("Incorrect!")
    print("The correct answer is Rome")

# Question 4
print("Question 4: What is the capital of Brasil?")
answer = input("Enter your answer: ").lower()
if answer == "brasilia":
    print("Correct!")
    score = score + 25
else:
    print("Incorrect!")
    print("The correct answer is Brasilia")
    score = score - 25

# Display the score
print("Your score is: ", score, "%")

# Display the result
if score == 100:
    print("You are a genius!")
elif score >= 75:
    print("You are good!")
elif score >= 50:
    print("You are average!")
else:
    print("You are bad!")
