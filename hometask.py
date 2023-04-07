
numbers = [int(num) for num in input("input nums: ").split()]

average = sum(numbers) / len(numbers)

count = 0

for num in numbers:
    if num > average:
        count += 1

print(" amount of nums, mor than the average:", count)
