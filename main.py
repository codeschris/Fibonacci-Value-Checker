n = int(input("Enter a positive value: "))

def fib(n):
    x = 0
    y = 1
    z = 0
    a = 0

    while a < n:
        z = x + y
        x = y
        y = z
        a += 1

        if n == y:
            print(f"{n} is in the sequence")

fib(n)
