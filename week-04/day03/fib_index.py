def fibonacci(n):
    if isinstance(n, int):
        if n < 2:
            return n
        else:
            return (fibonacci(n-2) + fibonacci(n-1))
    else:
        return n