n = 5

fact = 1
for i in range(1, n + 1):
    fact *= i
result = [int(digit) for digit in str(fact)]

print(result)
