def equalPartition(arr):
    n = len(arr)
    total = sum(arr)
    target = total // 2
    
    if total % 2 != 0:
        return []

    size1 = n // 2
    size2 = n - size1
    result = []

    def backtrack(start, path, curr_sum, size):
        if curr_sum == target and len(path) == size:
            result.append(path[:])
            return True
        
        if curr_sum > target or len(path) > size:
            return False
        
        for i in range(start, n):
            path.append(arr[i])
            if backtrack(i + 1, path, curr_sum + arr[i], size):
                return True
            path.pop()
        return False

    if backtrack(0, [], 0, size1):
        subset1 = result[0]
    else:
        result.clear()
        backtrack(0, [], 0, size2)
        subset1 = result[0]

    subset2 = arr[:]
    for x in subset1:
        subset2.remove(x)

    return [subset1, subset2]


# Example
arr = [1, 2, 3, 4]
print(equalPartition(arr))
