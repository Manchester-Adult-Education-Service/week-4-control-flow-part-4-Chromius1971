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
print("Step 1")
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
print("Step 2")
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
print("Step 3")
print()
user_Num = int(input("Choose a whole number "))
if user_Num %2 ==0:
    print("The number is even")
elif user_Num <0:
        print("The number is negative")
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
print("Extension Activity 1")
print()
attempts = 0
max_attempts = 5
stored_word = "Lion"
while attempts < max_attempts:
    user_word = (input("I'm an animal that lives in a 'pride' What animal am I? "))
    user_Num = int(input("Guess my number between 1 and 100  "))
    attempts += 1
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

# Extension 3 (more challenging):
# Create a small quiz:
# - Ask the user a multiple-choice question.
# - Check their answer and print "Correct!" or "Try again!".
# - Add another condition to give a special message if the answer is partially correct.

# Write your extension code below:


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
