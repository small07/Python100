def Fib(i):
    return 1 if i<=2 else Fib(i-1)+Fib(i-2)
print(Fib(int(raw_input('Please enter a number:'))))
