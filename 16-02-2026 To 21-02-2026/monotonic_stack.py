def max_visible_people(arr):
    n = len(arr)
    max_seen = 0

    for i in range(n):
        count = 1   

        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                count += 1
            else:
                count += 1
                break

        for j in range(i+1, n):
            if arr[j] < arr[i]:
                count += 1
            else:
                count += 1
                break

        max_seen = max(max_seen, count)

    return max_seen


arr = [6, 2, 5, 4, 5, 1, 6]

print(max_visible_people(arr))
