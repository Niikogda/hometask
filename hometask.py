
numbers = [int(num) for num in input("input nums: ").split()]

k = int(input("input  k: "))

if len(numbers) < k:
    print(" there are less than K")
else:
    numbers.sort(reverse=True)

    result = numbers[k - 1]
    print(int(k), " is the larest:", int(result))
