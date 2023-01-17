#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in len(new_list):
        if new_list[i] == ord(search):
            new_list[i] = 'replace'
    return new_list
