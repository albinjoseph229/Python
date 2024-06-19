count = 0
total_sum = 0

for num in range(101, 200):
    if num % 7 == 0:
        count += 1
        total_sum += num

print("The number of integers greater than 100 and less than 200 that are divisible by 7 is:", count)
print("The sum of these integers is:", total_sum)