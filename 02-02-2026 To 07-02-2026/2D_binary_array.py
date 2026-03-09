def rowWithMax1s(arr):
    n = len(arr)
    m = len(arr[0])

    row = 0
    col = m - 1
    max_row = -1

    while row < n and col >= 0:
        if arr[row][col] == 1:
            max_row = row
            col -= 1
        else:
            row += 1

    return max_row


# Input
arr = [
    [0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]
]

print(rowWithMax1s(arr))
