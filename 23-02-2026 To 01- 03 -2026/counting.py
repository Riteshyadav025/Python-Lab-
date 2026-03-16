s1 = input()
s2 = input()

n = len(s1)

total_ones = s1.count('1') + s2.count('1')

if total_ones % 2 != 0:
    print(-1)
else:
    target = total_ones // 2 
    
    ones_s1 = s1.count('1')

    diff = abs(ones_s1 - target)
    
    swaps = diff
    
    print(swaps)
