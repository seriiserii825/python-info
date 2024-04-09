from copy import deepcopy

boys = ['John', 'David', 'Nick', 'Martin', 'Tom']
print(boys[0]) # John
print(boys[0:2]) # ['John', 'David']

# inverse list
print(boys[::-1]) # ['Tom', 'Martin', 'Nick', 'David', 'John']

# copy list
s1 = boys[:]

# join lists
boys = ['John', 'David', 'Nick', 'Martin', 'Tom']
girls = ['Alice', 'Eva', 'Linda', 'Mary', 'Sara']
print(boys + girls) # ['John', 'David', 'Nick', 'Martin', 'Tom', 'Alice', 'Eva', 'Linda', 'Mary', 'Sara']

# append
progs = ['Python', 'Java', 'C++', 'C#', 'Ruby']
progs.append('PHP')
print(progs) # ['Python', 'Java', 'C++', 'C#', 'Ruby', 'PHP']

# insert
progs.insert(2, 'JavaScript')
print(progs) # ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'PHP']

# extend
numbs = ['1', '2', '3', '4', '5']
progs.extend(numbs)
print(progs) # ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'PHP', '1', '2', '3', '4', '5']

# remove elements
progs.remove('Java')
print(progs) # ['Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'PHP', '1', '2', '3', '4', '5']
elem_by_index = progs.pop(2)
print(elem_by_index) # C++
print(progs) # ['Python', 'JavaScript', 'C#', 'Ruby', 'PHP', '1', '2', '3', '4', '5']

del progs[0]
print(progs) # ['JavaScript', 'C#', 'Ruby', 'PHP', '1', '2', '3', '4', '5']

# clear
progs.clear()
print(progs) # []

# search
progs = ['Python', 'Java', 'C++', 'C#', 'Ruby', ['JavaScript', 'PHP']]
print(progs.index('Java')) # 1

# count
print(progs.count('Java')) # 1

# copy
# copy first level
progs_copy = progs.copy()
progs_copy[-1][1] = 'JavaScript'
print(progs_copy) # ['Python', 'Java', 'C++', 'C#', 'Ruby', ['JavaScript', 'JavaScript']]
print(progs) # ['Python', 'Java', 'C++', 'C#', 'Ruby', ['JavaScript', 'JavaScript']]

# deep copy
progs_one = deepcopy(progs)
progs_one[-1][1] = 'PHP'
print(progs_one) # ['Python', 'Java', 'C++', 'C#', 'Ruby', ['JavaScript', 'PHP']]

# sort
nums = [1, 4, 2, 3, 5]
nums.sort()
print(nums) # [1, 2, 3, 4, 5]

# sort key
# change this array
progs = ['Python', 'Java', 'C++', 'C#', 'Ruby']
progs.sort(key=len)
print(progs) # ['Java', 'C++', 'C#', 'Ruby', 'Python']

# sorted
# sorted create new array
progs = ['Python', 'Java', 'C++', 'C#', 'Ruby']
sorted_progs = sorted(progs)
print(sorted_progs) # ['C#', 'C++', 'Java', 'Python', 'Ruby']

#sum
nums = [1, 2, 3, 4, 5]
print(sum(nums)) # 15
print(sum(nums, start=1000)) # 1015

#max
print(max(nums)) # 5

#min
print(min(nums)) # 1


