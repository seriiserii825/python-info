#!/bin/python3
from termcolor import colored
def findSubstr(string, substring):
    if substring.lower() in string.lower():
        return True
    return False

# print(findSubstr('hello', 'ts'))

def firstLastIndex(string, symbol):
    first = string.find(symbol)
    if first == -1:
        return (None, None)
    last = string.rfind(symbol)
    if last == first:
        return (first, None)
    return (first, last)

# print("hello", 'll', firstLastIndex('hello', 'll'))
# print("hello", 'l',firstLastIndex('hello', 'l'))
# print("hello", 'o',firstLastIndex('hello', 'o'))
# print("hello", 't',firstLastIndex('hello', 't'))

def top3Str(text):
    count_res = []
    words = text.split()
    if len(words) < 3:
        print(colored("Not enough words in text, need at least 3 words.", "red"))
        return
    words = set(words)
    words = list(words)
    for word in words:
        count_res.append([word, text.count(word)])
    count_res.sort(key=lambda x: x[1], reverse=True)
    print(f"""Top 3 words in text: 
          {count_res[0][0]} - {count_res[0][1]},
          {count_res[1][0]} - {count_res[1][1]},
          {count_res[2][0]} - {count_res[2][1]}""")

# top3Str('hello my world')





