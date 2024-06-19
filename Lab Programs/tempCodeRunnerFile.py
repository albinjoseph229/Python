def factorial(n):
    """
    Calculates the factorial of a number and stores the calculated factorials in a dictionary.
    """
    factorials = {}

    def _factorial(x):
        if x in factorials:
            return factorials[x]
        elif x == 0:
            return 1
        else:
            result = x * _factorial(x-1)
            factorials[x] = result
            return result

    return _factorial(n)

print(factorial(5))  
print(factorial(10)) 