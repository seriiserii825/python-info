l1 = [1, 2, 3, 4, 5]
l2 = l1
l1.append(6)
print(l1) # [1, 2, 3, 4, 5, 6]
print(l2) # [1, 2, 3, 4, 5, 6]


l1 = ['1', 3, ['a', 'b', 'c']]
print(l1)

# list from string
# just iterable type can be converted to list
s = 'hello world'
l2 = list(s)
print(l2) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# don't work
# l3 = list(1,2,3)

# range
l4 = list(range(10))
print(l4) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

## odd
l5 = list(range(1, 10, 2))
print(l5) # [1, 3, 5, 7, 9]

## list generator
# i - first i is a result
# for i in range(1, 100) - loop
# if i % 2 == 0 - condition
# and i % 3 == 0 - condition
sp = [i for i in range(1, 100) if i % 2 == 0 and i % 3 == 0]
print(sp) # [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]

# list generator with math operation
sp = [i ** 2 for i in range(1, 100) if i % 2 == 0 and i % 3 == 0]
print(sp) # [36, 144, 324, 576, 900, 1296, 1764, 2304, 2916, 3600, 4356, 5184, 6084, 7056, 8100, 9216]

# list generator with if else
sp = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(1, 100) if i % 2 == 0 and i % 3 == 0]
print(sp) # [216, 144, 324, 576, 900, 1296, 1764, 2304, 2916, 3600, 4356, 5184, 6084, 7056, 8100, 9216]


