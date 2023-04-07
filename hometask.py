
import random

n = int(input("input amount of num: "))

numbers = []
for i in range(n):
    numbers.append(random.randint(1, 12)) 

print("list:", numbers)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("even nums:", even_count)
print("odd nums:", odd_count)
