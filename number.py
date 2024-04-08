number = int(input("Enter a number: "))
sum = 0

while number:
    # remove last digit from number
    sum += number % 10 # sum = sum + number % 10
    # get the remaining number
    number //= 10

print("Sum of digits: ", sum)

