def min_time_difference(arr):
    times = []
    for t in arr:
        h, m, s = map(int, t.split(":"))
        total_seconds = h * 3600 + m * 60 + s
        times.append(total_seconds)
    

    times.sort()
    
    min_diff = float('inf')
    
    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i - 1])
    
    wrap_diff = 24 * 3600 - times[-1] + times[0]
    min_diff = min(min_diff, wrap_diff)
    
    return min_diff


# Given Input
arr = ["12:30:15", "12:30:45"]

print(min_time_difference(arr))
