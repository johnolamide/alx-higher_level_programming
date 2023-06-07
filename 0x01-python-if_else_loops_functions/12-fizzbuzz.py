#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if ((number % 3 == 0) and (number % 5 == 0)):
            print("{:s}".format("FizzBuzz"), end=" ")
        elif (number % 3 == 0):
            print("{:s}".format("Fizz"), end=" ")
        elif (number % 5 == 0):
            print("{:s}".format("Buzz"), end=" ")
        else:
            print("{:d}".format(number), end=" ")
