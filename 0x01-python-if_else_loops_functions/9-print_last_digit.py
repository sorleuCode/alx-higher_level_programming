#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        lastdigit = number % -10
    else:
        lastdigit = number % 10

    print("{}".format(lastdigit, end=''))
