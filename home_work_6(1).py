def rec(n):
    if n <= 1:
        return n
    else:
        return n + rec(n - 1)

num = int(input("Enter number: "))

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", rec(num))