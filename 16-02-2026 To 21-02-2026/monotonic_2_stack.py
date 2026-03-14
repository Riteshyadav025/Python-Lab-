def max_people_visible(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    stack = []

    for i in range(n):
        count = 0
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
            count += 1
        if stack:
            count += 1
        left[i] = count
        stack.append(i)

    stack = []

    for i in range(n - 1, -1, -1):
        count = 0
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
            count += 1
        if stack:
            count += 1
        right[i] = count
        stack.append(i)

    max_visible = 0
    for i in range(n):
        max_visible = max(max_visible, left[i] + right[i] + 1)

    return max_visible


# Example
arr = [10, 6, 8, 5, 11, 9]
print(max_people_visible(arr))
