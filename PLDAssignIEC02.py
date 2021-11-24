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

