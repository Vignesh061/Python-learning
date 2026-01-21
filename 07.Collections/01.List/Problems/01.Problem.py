# Count how many even and odd numbers are in a list. give the ans

numbers = [1, 2, 3, 4, 5, 6, 7]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
