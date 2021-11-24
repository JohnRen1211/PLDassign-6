# The application of if else in giving input then evaluating the value.
# The steps to do.
#1 Ask for 3 numbers value.
#2 Show the lowest value showing the highest is optional.
# Using list,min,max,raise commands for the program.

print("Welcome to the system can you input 4 numbers? Type 1 for yes and 2 for no command.")
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
  
# The intro code