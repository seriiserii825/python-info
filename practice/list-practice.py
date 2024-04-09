#!/bin/python3

from termcolor import colored

def getOddNumbers():
    s = input(colored('Enter a list of numbers not separated by space: ', "green")).strip()
    l = list(s)
    l = [int(i) for i in l]
    s = [i for i in l if i % 2 != 0]
    print(s)

# getOddNumbers()

def getSquareNumbers():
    s = input('Enter a number: ').strip()
    l = list(range(1, int(s) + 1))
    s = [i ** 2 for i in l if i % 5 == 0]
    print(s)
# getSquareNumbers()

def checkForLuckyBilet():
    print(colored('Check for lucky bilet, if sum of first 3 number is equal with sum of last 3 numbers', "green"))
    s = input(colored('Enter a number min length 6: ', "blue")).strip()
    if len(s) < 6:
        print(colored('The number is too short', "red"))
        checkForLuckyBilet()
    else:
        l = list(s)
        l = [int(i) for i in l]
        if sum(l[:3]) == sum(l[-3:]):
            print(colored('Lucky bilet', "green"))
        else:
            print(colored('Not lucky bilet', "red"))

# checkForLuckyBilet()

def reverseArray(array) :
    print (array)
    print(colored(array[::-1], "green"))

# reverseArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def changeFirstWithLast(array):
    if len(array) < 2:
        print(colored('Array is too short', "red"))
        return
    print(array)
    array[0], array[-1] = array[-1], array[0]
    print(colored(array, "green"))

# changeFirstWithLast([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def toList(*args):
    print(list(args))

# toList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def useless(lst):
    result = max(lst) / len(lst)
    print(result)

useless([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
