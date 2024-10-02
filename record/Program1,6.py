def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    return int(str(n)[::-1])

def reverse_and_add(n):
    while not is_palindrome(n):
        reversed_n = reverse_number(n)
        n += reversed_n
        print(f"Reversed: {reversed_n}, Sum: {n}")
    return n

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = reverse_and_add(number)
    print(f"The palindrome is: {result}")