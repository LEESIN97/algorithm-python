n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a.sort(reverse=True)
b.sort()
for i in range(n-1, n-1-k, -1):
  b[i], a[i] = a[i], b[i]

print(sum(a))
