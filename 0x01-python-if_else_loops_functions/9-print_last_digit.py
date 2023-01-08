#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        lastdigit = number % -10
    elif number == 0:
        lastdigit = 0
    else:
        lastdigit = number % 10

    print("{}".format(lastdigit))
