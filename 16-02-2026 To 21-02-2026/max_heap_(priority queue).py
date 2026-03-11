import heapq

arr = list(map(float, input().split()))

total = sum(arr)
target = total / 2

heap = [-x for x in arr]
heapq.heapify(heap)

reduced = 0
operations = 0

while reduced < target:
    largest = -heapq.heappop(heap)
    half = largest / 2
    reduced += half
    heapq.heappush(heap, -half)
    operations += 1

print(operations)
