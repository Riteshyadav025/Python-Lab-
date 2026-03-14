def combinationSum3(k, n):
    result = []

    def backtrack(start, k, target, path):
        # If k numbers chosen and sum becomes 0 → valid combination
        if k == 0 and target == 0:
            result.append(path[:])
            return
        
        if k == 0 or target < 0:
            return
        
        for i in range(start, 10):
            path.append(i)
            backtrack(i + 1, k - 1, target - i, path)
            path.pop()  # backtrack

    backtrack(1, k, n, [])
    return result


# Example
n = 9
k = 3
print(combinationSum3(k, n))
