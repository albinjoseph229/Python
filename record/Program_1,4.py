def find_numbers_and_sum():
    count = 0
    total_sum = 0
    for number in range(101, 200):
        if number % 7 == 0:
            count += 1
            total_sum += number
    return count, total_sum

count, total_sum = find_numbers_and_sum()
print(f"Count of numbers: {count}")
print(f"Sum of numbers: {total_sum}")