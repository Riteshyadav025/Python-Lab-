arr = [111, 222, 333, 444, 555]

result = True

for num in arr:
    if str(num) != str(num)[::-1]:
        result = False
        break

print(result)
