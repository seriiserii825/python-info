#!/bin/python3

s = input('Write a string: ').strip()
symbol = input('Input a symbol in string: ').strip()
count = 0
symbol_count = s.count(symbol)

if symbol_count == 0:
    print(f"Symbol '{symbol}' is not in the string")
else:
    print(f"Symbol '{symbol}' occurs {symbol_count} times in the string")

# result = ''
# for i in range(len(s)):
#     if i % 2 == 0:
#         result += s[i]
# print(result)


