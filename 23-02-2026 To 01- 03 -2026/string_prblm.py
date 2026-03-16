s = input()

open_count = 0
add = 0

for ch in s:
    if ch == '(':
        open_count += 1
    else:   # ch == ')'
        if open_count > 0:
            open_count -= 1
        else:
            add += 1

result = add + open_count
print(result)
