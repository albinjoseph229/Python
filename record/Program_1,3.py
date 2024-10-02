# Function to print the pyramid of numbers
def print_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end="")
        # Print numbers in reverse order
        for l in range(i - 1, 0, -1):
            print(l, end="")
        # Move to the next line
        print()

# Number of levels in the pyramid
n = int(input("Enter the number of levels in the pyramid: "))
print_pyramid(n)