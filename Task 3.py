# Name: Task 3.py
# Author: Rylan
# Date created: October 4th, 2022
# Date last modified: October 4th, 2022
# Purpose: This program will take a users input for username and make sure it meets requirements.

while True:
    username = str(input("Please type a username. Username must have the following: more than 1 character but less than 20, an uppercase and a number "))
    username = str(username)

    length = len(username)
    if (length >20):
        print("Username must be less than 20 characters")
    elif (length <2):
        print("Username must be more than 1 character")
    elif (length >=2 <=20):
        break

print("Your username is", username,)
input("Press enter to exit")
quit()


