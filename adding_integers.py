#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if a number is negative or positive

def main():
    # input
    print("\n", end="")
    positive_integer = print("Enter any postitve integer ")
    positive_integer_as_string = input("Enter integer here:")
    loop_counter = 0
# process and output
    try:
        print("\n", end="")
        positive_integer = int(positive_integer_as_string)
        while loop_counter < positive_integer:
            print("{0}, time through the loop.".format(loop_counter))
            loop_counter = loop_counter + 1

    except Exception:
        print("This is not a positive_integer")


if __name__ == "__main__":
    main()
