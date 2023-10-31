def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


my_list = [2, 7, 15, 29, 75]
target = 75

result = binary_search(my_list, target)
print(result)
