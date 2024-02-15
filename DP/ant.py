n = int(input())
warehouse = list(map(int, input().split()))
d = [0] * 100
for i in range(n):
  d[i] = warehouse[i]

for i in range(2, n):
  d[i] = max(d[i] + d[i - 2], d[i - 1])

print(d[n - 1])
