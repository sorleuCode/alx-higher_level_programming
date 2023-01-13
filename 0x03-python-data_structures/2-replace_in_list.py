#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx != i:
            return my_list
        else:
            my_list.insert(idx, element)

            return my_list
