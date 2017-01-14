#encoding=UTF-8
"""
費式數列Fibonacci練習
"""
def fib_recursive(n):
    if n <= 0:
        return 'input number must greater than 0'
    if n == 1 or n ==2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def list_fib(n):
    if n <= 0:
        return 'input number must greater than 0'
            
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(b)
        a, b = b, a+b
    return result

