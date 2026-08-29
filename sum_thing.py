# Title: Sum Thing
# Author: _hofner
# Date: 29th August 2026

# Import Packages
import random
import time

# Initialise Variables
op: int = 0				# Operation (1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide)
num1: int = 0
num2: int = 0
user_ans: float = 0.0	# The Answer Given By The User
answer: float = 0.0		# Correct Answer
min_val: int = 0		# Minimum Value For Num1 & Num2
max_val: int = 0		# Maximum Value For Num1 & Num2
conf: str = ""			# User Confirmation of Min and Max
conf2: str = ""			# User Confirmation of Their Answer
again: str = ""

total: int = 0			# Total Questions Asked
correct: int = 0		# Questions The User Got Correct
wrong: int = 0			# Questions The User Got Wrong
acc: float = 0.0		# Percentage Of Questions The User Got Correct
score: int = 0
streak: int = 0
max_streak: int = 0		# The User's Longest Streak

# Display Title Screen
print("WELCOME TO SUM THING!")
time.sleep(1.5)
print()
print("_hofner")
time.sleep(1.5)
print()
print("PRESS ENTER TO BEGIN")
input()
print()

# Request Min & Max Values From User
while True:
    min_val = int(input("Minimum Value? (Must Be An Integer) "))
    max_val = int(input("Maximum Value? (Must Be An Integer) "))

# Confirm Min & Max From User
    print()
    conf = input("Are You Happy With Your Choices? [" + str(min_val) + ", " + str(max_val) + "] (y/n) ")
    
    if conf == "n":
        print('\n' * 2)
        continue  # Return To Line 29
    
    break # Continue With Program


        
print('\n' * 2)

# Generate Random Equation
while True: # For When The Game Is Repeated
    op = random.randint(1, 4)
    num1 = random.randint(min_val, max_val)
    num2 = random.randint(min_val, max_val)

    if op == 4 and num2 == 0: # Failsafe To Avoid Division By 0
        op = random.randint(1, 3)

# Calculate Correct Answer
    if op == 1: # Addition
        answer = num1 + num2

    elif op == 2: # Subtraction
        answer = num1 - num2
    
    elif op == 3: # Multiplication
        answer = num1 * num2
    
    elif op == 4: # Division
        answer = round(num1 / num2, 2)
    
# Display Calculation
    print("What is:")

    if op == 1: # Addition
        print(str(num1) + " + " + str(num2) + "?")

    elif op == 2: # Subtraction
        print(str(num1) + " - " + str(num2) + "?")
    
    elif op == 3: # Multiplication
        print(str(num1) + " * " + str(num2) + "?")
    
    elif op == 4: # Divison
        print(str(num1) + " / " + str(num2) + "? (2 d.p.)")

# Get User's Answer
    user_ans = float(input())
    print()

# Confirm User's Answer
    while True:
        conf2 = input("Are You Happy With This Answer? [" + str(user_ans) + "] (y/n) ")

        if conf2 == "n":
            print()
            user_ans = float(input("New Answer: "))
            print()
            continue # Return To Line 84
    
        break # Continue With Program
    print('\n' * 3)

# Compare To Correct Answer & Give Feedback
    if user_ans == answer:
        print("Correct! The Correct Answer Is " + str(answer) + ".")
        total = total + 1
        correct = correct + 1
        score = score + 1
        streak = streak + 1
    
    else:
        print("Wrong! The Correct Answer Is " + str(answer) + ".")
        total = total + 1
        wrong = wrong + 1
        score = score - 1
        streak = 0
        
    if streak > max_streak:
        max_streak = streak
    print()
    
# End Game Or Play Again
    again = input("Would You Like To Play Again? (y/n) ")
    
    if again == "y":
        print('\n' * 3)
        continue # Return To Line 54
    
    break # End Game

print()

# Calculate Accuracy
acc = round(correct / total, 2)

# Display Statistics
print("FINAL SCORE: " + str(score))
print()
print("Correct: " + str(correct))
print("Incorrect: " + str(wrong))
print("Total: " + str(total))
print("Accuracy: " + str(acc) + "%")
print("Longest Streak: " + str(max_streak))

# End of Game