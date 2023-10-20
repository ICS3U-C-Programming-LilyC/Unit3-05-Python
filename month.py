#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/20/2023
# This program tells the user the month based on the number they input from 1-12.


def main():
    # Explaining my program to the user.
    print(
        "My program will tell you what month it would be based on the number inputted."
    )

    # Getting user input.
    user_number = int(input("Enter a number between 1 and 12: "))

    # Initiating the switch case operation.
    match user_number:
        # Month of January.
        case 1:
            print("{} is the month of January.".format(user_number))

        # Month of February.
        case 2:
            print("{} is the month of February.".format(user_number))

        # Month of March.
        case 3:
            print("{} is the month of March.".format(user_number))

        # Month of April.
        case 4:
            print("{} is the month of April.".format(user_number))

        # Month of May.
        case 5:
            print("{} is the month of May.".format(user_number))

        # Month of June.
        case 6:
            print("{} is the month of June.".format(user_number))

        # Month of July.
        case 7:
            print("{} is the month of July.".format(user_number))

        # Month of August.
        case 8:
            print("{} is the month of August.".format(user_number))

        # Month of September.
        case 9:
            print("{} is the month of September.".format(user_number))

        # Month of October.
        case 10:
            print("{} is the month of October.".format(user_number))

        # Month of November.
        case 11:
            print("{} is the month of November.".format(user_number))

        # Month of December.
        case 12:
            print("{} is the month of December.".format(user_number))

        # Error message for input that is not between 1 and 12.
        case _:
            print("Invalid number.Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()
