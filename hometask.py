

numbers = input("input numbers: ").split()


numbers = list(map(int, numbers))

positive_numbers = []


for num in numbers:
    if num > 0:
        positive_numbers.append(num)

print("list:", positive_numbers)
