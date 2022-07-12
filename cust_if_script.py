#!/usr/bin/env python3

# """Alta3 Research | RZFeeser
#    if, elif, else - A simple program using conditionals to make a decision."""

# A program that prompts a user for a numeric score, then returns the letter grade associated with that score.
# A (100 to 90)
# B (89 to 80)
# C (79 to 70)
# D (69 to 60)
# F (59 and below)

message = 'Your letter grade for test score'

# wrap score in a float() to accept decimals as numbers
score = int(input("What is your test score?"))

# if input value was higher or equal to 25
if score >= 90:
    grade = 'A'
elif score <= 89 & score >= 80:
    grade = 'B'
elif score <= 79 & score >= 70:
    grade = 'C'
elif score <= 69 & score >= 60:
    grade = 'D'
elif score <= 59:
    grade = 'F'    
else:
    message = f'{message} {score} is {grade}.'
print(f'{message} {score} is {grade}.')
