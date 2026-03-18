def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# calling the function
n = int(input("Enter number of terms: "))
fibonacci(n)
