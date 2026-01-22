# Find the difference between the largest and smallest number in a list

numbers = [10, 3, 25, 7, 1]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

difference = largest - smallest
print("Difference:", difference)
