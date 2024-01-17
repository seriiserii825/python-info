l1 = [1, 2, 3, 4, 5]
l2 = l1
l1.append(6)
print(l1) # [1, 2, 3, 4, 5, 6]
print(l2) # [1, 2, 3, 4, 5, 6]


l1 = ['1', 3, ['a', 'b', 'c']]
print(l1)

# list from string
s = 'hello world'
l2 = list(s)
print(l2)

# don't work
# l3 = list(1,2,3)

# list from tuple
l3 = list((1,2,3))
print(l3)

# list from range
l4 = list(range(5))
print(l4)

# list from generator
s2 = 'hello world'
l5 = list(i for i in s2)
print(l5)

# list comprehension
s3 = 'hello world'
l6 = [i for i in s3 if i != ' '] 
print(l6)

# list comprehension with if else
l7 = [i for i in s3 if i != ' ' and i != 'l']
print(l7)

# list comprehension with if else not
l8 = [i for i in s3 if i not in [' ', 'l', 'w']]
print(l8)

# table of multiplication
for i in range(1, 11):
    for j in range(i, 11):
        print(f'{i} * {j} = {i*j}', end='\t')
