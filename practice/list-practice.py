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

checkForLuckyBilet()
