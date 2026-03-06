arr = [1, 2, 3, 3, 4]
a = 1
b = 2

low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] < a:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif a <= arr[mid] <= b:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)
print(True)
