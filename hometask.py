
numbers = [int(num) for num in input("input nums: ").split()]
squared_numbers = [num ** 2 for num in numbers if num > 0]
print(squared_numbers)
