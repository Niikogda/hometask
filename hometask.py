
numbers = [int(num) for num in input("input nums: ").split()]

min_idx = numbers.index(min(numbers))
max_idx = numbers.index(max(numbers))

numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]

print("list:")
print(numbers)
