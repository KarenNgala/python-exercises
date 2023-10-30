def fib(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9)) #print nth fibonacci number

print([fib(x) for x in range(10)]) #print fibonacci series upto n-1th number