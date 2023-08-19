#!/usr/bin/env python3

import ipdb

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i = i -1
        if i == 0:
            print("Happy New Year!")
    pass

num = [1, 2, 3, 4, 5]

def square_integers(int_list):
    # code goes here!
    new_list = list()
    for item in int_list:
        new_item = item * item
        new_list.append(new_item)
    return new_list         
   

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
            sum = i/3
            fum = i/5
            if sum.is_integer() and fum.is_integer():
                print("FizzBuzz")
            elif sum.is_integer():
                print("Fizz")
            elif fum.is_integer():
                print("Buzz")
            else:
                print(f"{i}")



#ipdb.set_trace()