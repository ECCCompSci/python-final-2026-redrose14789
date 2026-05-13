# ============================================================
# Python Final Project 2026
# Name: Emily
# Date: May 9, 2026, 04:59
# Project Title: escape?
# Description: (Write 1-2 sentences explaining what your program does)
# can yo escape?
# ============================================================


cName = input("What is your name: ")
aName = input("Name a pet: ")
tName = input("Name a fantasy town: ")
mName = input("Name a monster species: ")
nmName = int(input("How many monsters are there: "))

# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.



print("Hello " + cName)
print("You and your pet "+ aName + " were walking through the woods of " + tName + " when " + (str(nmName) +" "+ mName + " come out of no where and start attacking you and " + aName))
runFight = input("Would you like to Run or Fight: ")






# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

if runFight == "Run":
    if nmName <= 5:
        print ("Because they are in a small pack you you can't run fast enough and they get you. :( )")
    else:
        print ("The pack was to big for all of them to catch up. YOU ESCAPED! ")
elif runFight == "Fight":
    if nmName <=5: 
        print("Because their were only " + (str(nmName) + " mosters you were able to fight them off YOU ESCAPED!"))
    else:
        print("you got over powered you didn't make it. They got you :( )")
else: print("Invailed answer play again")


print("----------------------------")
print("Thanks for using my program!")
