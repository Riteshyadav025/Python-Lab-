a = [2, 4, 7, 10]
b = [2, 3]

n = len(a)
m = len(b)

for i in range(n):
    if a[i] > b[0]:
        # swap
        a[i], b[0] = b[0], a[i]
        b.sort()

print("a[] =", a)
print("b[] =", b)
