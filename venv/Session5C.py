def showList(numbers):
    s = numbers.__len__()
    for i in range(0, s):
        numbers[i] = numbers[i] * numbers[i]

    print(numbers)


nums = [1, 2, 3, 4, 5]
showList(nums)

print(nums)