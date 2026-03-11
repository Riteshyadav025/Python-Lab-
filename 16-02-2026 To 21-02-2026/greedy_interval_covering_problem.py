arr = [1, 2, 1, 0]
n = len(arr)

intervals = []

for i in range(n):
    if arr[i] != -1:
        left = max(0, i - arr[i])
        right = min(n - 1, i + arr[i])
        intervals.append((left, right))

intervals.sort()

count = 0
i = 0
current_end = 0
far = 0

while current_end < n:
    found = False
    
    while i < len(intervals) and intervals[i][0] <= current_end:
        far = max(far, intervals[i][1] + 1)
        i += 1
        found = True
    
    if not found:
        print(-1)
        break
    
    count += 1
    current_end = far

if current_end >= n:
    print(count)
