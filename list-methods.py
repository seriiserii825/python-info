l = [1, 'a', [4, 8, 9, 10, 11, 12, 13], 14, 15, 16, 17]

l[:2] = [0, 0]
print(l)

#append
l.append(18) #append 18 to the end of the list
print(l)

#extend
l.extend([19, 20, 21]) #extend the list by adding 19, 20, 21
print(l)

#insert
l.insert(1, 9) #insert 9 at index 1
print(l)

#remove
l.remove(14) #remove the first occurrence of 14
print(l)

#pop
l.pop() #remove the last element
l.pop(1) #remove the element at index 1
print(l)

#index
print(l.index(15)) #return the index of the first occurrence of 15

#count
print(l.count(0)) #return the number of times 0 appears in the list

#sort
# l.sort() #sort the list just numebers
# print(l)

#reverse
l.reverse() #reverse the list
print(l)

#copy
l2 = l.copy() #return a copy of the list
print(l2)

#clear
l.clear() #remove all elements from the list
print(l)
