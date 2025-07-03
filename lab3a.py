#!/usr/bin/env python3
# return_text_value() function
# Author ID: 158418228

def hello():
    print('Hello World')
    print('Inside a Function')
    return

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

if __name__ == '__main__':
    hello()
    hello()
    hello()
    my_stuff = hello()
    print('Stuff return from hello():', my_stuff)
    print('the object my_stuff is of type:', type(my_stuff))
    print(return_text_value())
    number = return_number_value()
    print(number)
    print('my number is ' + str(number))
