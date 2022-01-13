#!/usr/bin/env python3

# Created by: Melody Berhane
# Created on: Jan 12, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the factor of that number.

# asks the user if they want to pay the game
def ask_again():
    ask_user = input("Do you what to find the factors of a number?(y/n): ")
    # If yes then it directs the program to man
    if ask_user == "Y" or ask_user == "y":
        main()
    # If no then it ends the program
    elif ask_user == "N" or ask_user == "n":
        print("Thank you for using my app!")
    # If input is not y or n then they are
    # directed to the top of the ask again funtion.
    else:
        print("Please enter either y/n")
        print()
        # returns the ask_again function.
        return ask_again()


# Finds the factors of the input.
def main():
    # initializations
    counter = 0
    factor = []
    # Global varaibles
    global user_number_string
    global user_number
    # Get the user number
    user_number_string = input("Enter a positive number: ")

    # catches any invaild input
    try:
        # Changing string to integer
        user_number = int(user_number_string)
        # Check to see if they inputed a postive number
        if (user_number >= 0):
            # calculate the factors of the input
            for counter in range(1, user_number + 1):
                if user_number % counter == 0:
                    factor.append(counter)
            print("The factors of {} are = {}".format(user_number, factor))
            print()
            # Sends program to ask again function
            ask_again()
        else:
            print("You entered a negative number, please try again.")
            print()
            ask_again()
    except Exception:
        print("This is not an integer, please try again")
        print()
        ask_again()


if __name__ == "__main__":
    ask_again()
