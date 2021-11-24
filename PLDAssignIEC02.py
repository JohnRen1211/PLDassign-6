# The addition trainer create a program that automatically generate two random numbers to add 0 to 99 value. 
# Let the user evaluate if the user has the correct answer.
# The program will ask 10 addition operation display the result summary of the 10 operations example 10/10 operations.

#Program Introduction
print("Program for additon trainer")
print("Welcome to the system would you want to try addition trainer? Type 1 for yes and 2 for no command.")
answer= int(input("Response: "))
command1 = 1
command2 = 2
if answer == command2:
    print("Okay, then rest.")
    raise SystemExit
elif answer <= -1:
    print("Input the right command.")
    raise SystemExit
elif answer == command1:
    print("Continue to the survey")
elif answer >= command2:
    print("Input the right command.")
    raise SystemExit

# Import random command

import random

ran_num1 = random.randint(0,99)
ran_num2 = random.randint(0,99)
ran_num3 = random.randint(0,99)
ran_num4 = random.randint(0,99)
ran_num5 = random.randint(0,99)
ran_num6 = random.randint(0,99)
ran_num7 = random.randint(0,99)
ran_num8 = random.randint(0,99)
ran_num9 = random.randint(0,99)
ran_num10 = random.randint(0,99)
ran_num11 = random.randint(0,99)
ran_num12 = random.randint(0,99)
ran_num13 = random.randint(0,99)
ran_num14 = random.randint(0,99)
ran_num15 = random.randint(0,99)
ran_num16 = random.randint(0,99)
ran_num17 = random.randint(0,99)
ran_num18 = random.randint(0,99)
ran_num19 = random.randint(0,99)
ran_num20 = random.randint(0,99)
ran_num1 = random.randint(0,99)
ran_num2 = random.randint(0,99)

# Sample program using random command
print("Set#1 of random numbers:")
num1 = ran_num1 + ran_num2 
print("The answer in operation#1 is:",num1)
print("Random number1 is: ",ran_num1)
print("Random number2 is: ",ran_num2)
print("Evaluating if the answer is correct: Type 1 for yes and 2 for no command.")
print("Operation: 1/10")
answer= int(input("Response: "))
command1 = 1
command2 = 2
if answer == command2:
    print("Okay, then rest.")
    raise SystemExit
elif answer <= -1:
    print("Input the right command.")
    raise SystemExit
elif answer == command1:
    print("Continue to the survey")
elif answer >= command2:
    print("Input the right command.")
    raise SystemExit

print("Set#2 of random numbers")
num2 = ran_num3 + ran_num4 
print("The answer in operation#2 is:",num2)
print("Random number1 is: ",ran_num3)
print("Random number2 is: ",ran_num4)
print("Evaluating if the answer is correct: Type 1 for yes and 2 for no command.")
print("Operation number: 2/10")
answer= int(input("Response: "))
command1 = 1
command2 = 2
if answer == command2:
    print("Okay, then rest.")
    raise SystemExit
elif answer <= -1:
    print("Input the right command.")
    raise SystemExit
elif answer == command1:
    print("Continue to the survey")
elif answer >= command2:
    print("Input the right command.")
    raise SystemExit

print("Set#3 of random numbers")
num3 = ran_num5 + ran_num6 
print("The answer in operation#3 is:",num3)
print("Random number1 is: ",ran_num5)
print("Random number2 is: ",ran_num6)
print("Evaluating if the answer is correct: Type 1 for yes and 2 for no command.")
print("Operation: 3/10")
answer= int(input("Response: "))
command1 = 1
command2 = 2
if answer == command2:
    print("Okay, then rest.")
    raise SystemExit
elif answer <= -1:
    print("Input the right command.")
    raise SystemExit
elif answer == command1:
    print("Continue to the survey")
elif answer >= command2:
    print("Input the right command.")
    raise SystemExit
