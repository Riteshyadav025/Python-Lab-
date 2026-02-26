a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

from collections import Counter

count_a = Counter(a)
count_b = Counter(b)

is_subset = True

for key in count_b:
    if count_b[key] > count_a.get(key, 0):
        is_subset = False
        break

print(is_subset)
