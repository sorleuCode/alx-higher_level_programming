#!/usr/bin/python3

def uniq_add(my_list=[]):
    num = 0
    return map(lambda elm: num += elm, set(my_list) for elm in set(my_list))
