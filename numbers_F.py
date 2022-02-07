#fibonachi 1 1 2 3 5 8 13 21 34 55 89...

def number_fib(n):
    if n == 1 or n == 2:
        return 1
    return number_fib(n-1)+number_fib(n-2)

n = int(input())
print(number_fib(n))


