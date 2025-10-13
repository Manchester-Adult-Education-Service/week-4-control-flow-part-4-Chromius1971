# -------------------------------------------
# Exercise 4: Decision-Making Program
# -------------------------------------------
# In this exercise, you will write a program that makes decisions based on user input.
# You will practice combining Boolean logic with conditional statements.
#
# Goals:
# - Ask the user for input
# - Use conditions to decide what to do
# - Print messages based on the conditions
# - Test your program with different inputs
#
# -------------------------------------------

# Step 1: Simple decision
# -----------------------
# Ask the user to enter a number.
# Decide something about the number using an if statement.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message for True condition")

# TODO:
# 1. Ask the user to type a number and store it in a variable.
# 2. Use an if statement to check something about the number.
# 3. Print a message if the condition is True.

# Write your code below:
print()
print("Step 1: Checking if a number is even using if.")
print()
user_Num = int(input("Choose a whole number "))
if user_Num %2 ==0:
    print("The number is even")

# Step 2: Add else
# ----------------
# Sometimes we need to print a different message if the condition is False.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message if True")
# else:
#     print("Message if False")

# TODO:
# 1. Add an else statement to your code from Step 1.
# 2. Print a different message if the number does not meet your condition.

# Write your code below:
print()
print("Step 2: Checking if a number is odd or even using if & else.")
print()
user_Num = int(input("Choose a whole number "))
if user_Num %2 ==0:
    print("The number is even")
else:
    print("The number is odd")    
print()

# Step 3: Multiple conditions
# ---------------------------
# You can check more than one condition using elif or Boolean operators.

# Example of syntax (no answer given):
# if condition1:
#     print("Message 1")
# elif condition2:
#     print("Message 2")
# else:
#     print("Message 3")

# TODO:
# 1. Extend your program to check multiple conditions.
# 2. Print different messages for each case.
# 3. Test your program with different inputs to see all possible messages.

# Write your code below:
print()
print("Step 3: Checking multiple conditions using if, elif & else")
print()
user_Num = int(input("Choose a whole number "))
if user_Num %2 ==0:
    print("The number is even")
elif user_Num <0:
    print("The number is negative")
elif user_Num ==0:
    print("The number is 0")
else:
    print("The number is odd")    
print()

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed decision-making program exercise"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1:
# Ask the user for a number and a word.
# Use conditions to print a message only if the number is greater than a value
# AND the word matches a stored word.
# Write your extension code below:
print("Extension Activity 1 - Guess the word and number with an attempt counter.")
print()
attempts = 0
max_attempts = 5
stored_word = "Lion"
while attempts < max_attempts:
    user_word = (input("I'm an animal that lives in a 'pride' What animal am I? "))
    print()
    user_Num = int(input("Guess my number between 1 and 100  "))
    print()
    attempts += 1
    print(f"Attempts left: {max_attempts - attempts}")
    if attempts == max_attempts:
        print("Too bad the answer was Lion and the number was over 50!")
    if user_word == stored_word and user_Num >50:
        print("Correct it is a lion and the number was over 50!")
        break
print()

# Extension 2:
# Ask the user for a number.
# Print different messages depending on:
# - number is positive
# - number is zero
# - number is negative
# Write your extension code below:
print("Extension 2 - Printing messages using several conditions.")
print()
user_Num = int(input("Choose a whole number between 0 and 100 "))
if user_Num %2 ==0:
    print("The number is even.")
    print()
elif user_Num ==0:
    print("The number is 0.")
    print()
else:
    print("The number is odd.")
    print()
# Extension 3 (more challenging):
# Create a small quiz:
# - Ask the user a multiple-choice question.
# - Check their answer and print "Correct!" or "Try again!".
# - Add another condition to give a special message if the answer is partially correct.

# Write your extension code below:
score = 0
print()
print("Capital Cities Quiz")
print()
ans_1 = int(input("Question 1: Ankara is the capital of? 1. Turkey 2. Morocco. 3. Moldova: "))
while ans_1 !=1:
    print("Incorrect and you've lost point too! Try again")
    score -= 1
    print(f"SCORE: {score}")
    ans_1 = int(input("Ankara is the capital of? 1. Turkey 2. Morocco. 3. Moldova: ")) 
else:
    print("Correct! Well done! Have a point!")
    score += 1
    print(f"SCORE: {score}")
    print()
ans_2 = int(input("Question 2: Majuro is the capital of? 1. Maldives 2. Lesotho 3. Marshall Islands:  "))
while ans_2 !=3:
    print("Incorrect. Unlucky you've lost a point! Try again")
    score -= 1
    print(f"SCORE: {score}")
    ans_2 = int(input("Majuro is the capital of? 1. Maldives 2. Lesotho 3. Marshall Islands:  "))
else:
    print("Correct! You did well to get that one! Have another point!")
    score += 1
    print(f"SCORE: {score}")
    print()
ans_3 = int(input("Question 3: Georgetown is the capital of? 1. Honduras 2. Guyana. 3. Ghana: "))
while ans_3 !=2:
    print("Incorrect. Unlucky you've lost a point! Try again")
    score -= 1
    print(f"SCORE: {score}")
    ans_2 = int(input("Georgetown is the capital of? 1. Honduras 2. Guyana. 3. Ghana: "))
else:
    print("Correct! That was tough one! Have another point!")
    score += 1
    print(f"SCORE: {score}")
    print()
ans_4 = int(input("Question 4: Vaduz is the capital of? 1. Liechtenstein 2. San Marino. 3. Mauritius: "))
while ans_4 !=1:
    print("Incorrect. Unlucky you've lost a point! Try again")
    score -= 1
    print(f"SCORE: {score}")
    ans_4 = int(input("Vaduz is the capital of? 1. Liechtenstein 2. San Marino. 3. Mauritius: "))
else:
    print("Correct! Are you cheating?! Have another point!")
    score += 1
    print(f"SCORE: {score}")
    print()
ans_5 = int(input("Question 5: Bamako is the capital of? 1. Maldives 2. Mali. 3. Myanmar: "))
while ans_5 !=2:
    print("Incorrect and you've lost point too! Try again")
    score -= 1
    print(f"SCORE: {score}")
    ans_5 = int(input("Bamako is the capital of? 1. Maldives 2. Mali. 3. Myanmar: ")) 
else:
    print("Correct! Well done! Have a point!")
    score += 1
    print(f"SCORE: {score}")
    print()
print(f"You scored {score} out of 5!")
print()
if score <=0:
    print("I'm surprised you can find your front door!")
elif score ==1:
    print("You really need a map on any journey!")
elif score ==2:
    print("Have you been out of this country yet?!")
elif score ==3:
    print("You probably have a passport but only use it for ID purposes!")
elif score ==4:
    print("You are probably a seasoned traveller!")
else:
    print("Globetrotter! I bet you're always travelling!")
# 
# I'm really proud of myself for producing this! I know it's very, very basic but I've tried to
# incorporate everything we've learned so far and some things I discovered on my own! I know it's
# hardly AI but it works so that's something!

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed extension activities"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------
