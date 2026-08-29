# Title: Sumthing
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
again: str = ""
diff: int = 0			# Difficulty (The Maximum That Op Can Be)

total: int = 0			# Total Questions Asked
correct: int = 0		# Questions The User Got Correct
wrong: int = 0			# Questions The User Got Wrong
acc: float = 0.0		# Percentage Of Questions The User Got Correct
score: int = 0
streak: int = 0
max_streak: int = 0		# The User's Longest Streak

# Display Title Screen
print("WELCOME TO SUMTHING!")
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
    try: # Failsafe Incase User Inputs String
        min_val = int(input("Minimum Value? (Must Be An Integer) "))
        max_val = int(input("Maximum Value? (Must Be An Integer) "))
        break
        
    except: # Failsafe Incase User Inputs String
        print("Please Enter An Integer.")
        print()
        continue # Return To Line 40
    
    if min_val > max_val: # Failsafe To Prevent Value Error When Min > Max
        min_val, max_val = max_val, min_val

# Confirm Min & Max From User
    print()
    conf = input("Are You Happy With Your Choices? [" + str(min_val) + ", " + str(max_val) + "] You cannot change this later. (y/n) ")
    
    if conf == "n":
        print('\n' * 2)
        continue  # Return To Line 40
    
    break # Continue With Program
     
print('\n' * 2)

# Let User Select Difficulty
print("Please type your preferred difficulty:")
while True:
    print("(1) Only Addition")
    print("(2) Addition & Subtraction")
    print("(3) Addition, Subtraction, and Multiplication.")
    print("(4) Addition, Subtraction, Multiplication, and Division.")

    try: # Failsafe Incase User Inputs String
        diff = int(input())
        break
    
    except:
        print("Please Enter An Integer.") # Failsafe Incase User Inputs String
        continue # Return To Line 68
    
if diff > 4: # Failsafe To Prevent Out-Of-Bounds Difficulty Levels
    diff = 4
        
if diff < 1: # Failsafe To Prevent Out-Of-Bounds Difficulty Levels
    diff = 1
        
print('\n' * 2)

# Generate Random Equation
while True: # For When The Game Is Repeated
    op = random.randint(1, diff)
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
    while True:
        try: # Failsafe Incase User Inputs String
            user_ans = float(input())
            break
        
        except: # Failsafe Incase User Inputs String
            print()
            print("Please Enter A Number.")
            print()
            continue # Return To Line 128
        
    print()

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
    again = input("press enter to continue or type & enter to end game")
    
    if again == "":
        print('\n' * 3)
        continue # Return To Line 91
    
    break # End Game

print()

# Calculate Accuracy
acc = round(correct / total * 100, 2)

# Display Statistics
print("FINAL SCORE: " + str(score))
print()
print("Correct: " + str(correct))
print("Incorrect: " + str(wrong))
print("Total: " + str(total))
print("Accuracy: " + str(acc) + "%")
print("Longest Streak: " + str(max_streak))

# End of Game
input()